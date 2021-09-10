import argparse
import threading
import grpc
import json

from protobuf import room_pb2,room_pb2_grpc
# from flask import Flask
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource, WebSocketError
from collections import OrderedDict

class Config:
    def __init__(self):
        self.rooms = {} # key：房间号 value：client_array
        self.members = {} # key:addr_tuple value：房间号

def callRpcMethod(handlefunc):
    with grpc.insecure_channel(f"{args.roomip}:{args.roomport}") as chan:
        roomStub = room_pb2_grpc.RoomStub(chan)
        return handlefunc(roomStub)

ADDR_CLIENT = {}

class EchoApplication(WebSocketApplication):
    def __init__(self,ws):
        super().__init__(ws)
        self.ip = str(self.ws.handler.active_client.address[0])
        self.port = int(self.ws.handler.active_client.address[1])

    def addToRoom(self):
        path_arr = self.ws.path.split("/")
        room_number = path_arr[len(path_arr) - 2]
        password = path_arr[len(path_arr) - 1]
        # if room_number not in config.rooms:
        #     config.rooms[room_number] = []
        # config.rooms[room_number].append(self.ws.handler.active_client)
        # config.members[self.ws.handler.active_client.address] = room_number
        def join(roomStub):
            response = roomStub.Join(room_pb2.JoinRoomRequest(
                userIp=self.ip,
                userPort=self.port,
                roomnum=room_number,
                passwd=password
            ))
            if response.isSuccess == True:
                ADDR_CLIENT[(self.ip, self.port)] = self.ws.handler.active_client
            return response
        response = callRpcMethod(join)


    def on_open(self):
        self.addToRoom()
        print("Connection opened")

    # def getRoomNumByAddr(self):
    #     return config.members[self.ws.handler.active_client.address]

    def on_message(self, message):
        if message == None or message == "":
            return
        message_obj = json.loads(message.decode("utf-8"))
        nickname = message_obj["nickname"]
        mes_type = message_obj["type"]
        content = message_obj["content"]
        def handleFunc(roomstub):
            getRoomNumByAddrResponse = roomstub.GetRoomNumByAddr(room_pb2.GetRoomNumByAddrRequest(userIp=self.ip, port=self.port))
            getRoomAddrResponse=roomstub.GetRoomAddr(room_pb2.GetRoomAddrRequest(roomnum=getRoomNumByAddrResponse.roomnum))
            userAddrs = getRoomAddrResponse.addr
            return userAddrs
        userAddrs = callRpcMethod(handleFunc)
        for client in userAddrs:
            if ((client.ip, client.port) in ADDR_CLIENT):
                ADDR_CLIENT[(client.ip, client.port)].ws.send(json.dumps({
                    'msg_type': mes_type,
                    'nickname': nickname,
                    "content": content
                }))

        # roomNum = self.getRoomNumByAddr()
        # for client in config.rooms[roomNum]:
        #     if client and client.ws and message:
        #         client.ws.send(json.dumps({
        #             'msg_type': mes_type,
        #             'nickname': nickname,
        #             "content" : content
        #         }))


    def on_close(self, reason):
        def handleFunc(roomstub):
            print(self.ip)
            print(self.port)
            resp = roomstub.Leave(room_pb2.LeaveRoomRequest(
                userIp=self.ip,
                port=self.port
            ))
            if resp.isSuccess:
                del ADDR_CLIENT[(self.ip, self.port)]
        callRpcMethod(handleFunc)
        print("close")

# flask_app = Flask(__name__)
# @flask_app.route("/personcount/<roomnum>")
# def personCount(roomnum):
#     if roomnum not in config.rooms:
#         return "0"
#     else:
#         return str(len(config.rooms[roomnum]))

# def flask_server_run():
#     flask_app.run(host="0.0.0.0",port="5556")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5555)
    parser.add_argument("--roomip", type=str, default="127.0.0.1")
    parser.add_argument("--roomport", type=int, default=9000)
    args = parser.parse_args()

    config = Config()
    # threading.Thread(target=flask_server_run,args="").start()
    WebSocketServer(
        ('0.0.0.0', args.port),
        Resource(OrderedDict([
            ('/echo/.*', EchoApplication)
        ]))
    ).serve_forever()