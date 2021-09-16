import argparse
import threading
import grpc
import json

from protobuf import room_pb2,room_pb2_grpc
# from flask import Flask
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource, WebSocketError
from collections import OrderedDict
from loguru import logger

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
        logger.info(f"init echo app.addr={self.ws.handler.active_client.address}")
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
        logger.info(f"start ws.addr={self.ip} {self.port}")
        self.addToRoom()

    # def getRoomNumByAddr(self):
    #     return config.members[self.ws.handler.active_client.address]

    def on_message(self, message):
        if message == None or message == "":
            return
        message_obj = json.loads(message.decode("utf-8"))
        nickname = message_obj["nickname"]
        mes_type = message_obj["type"]
        content = message_obj["content"]
        logger.info(f"init echo app.addr={self.ws.handler.active_client.address} message={message_obj}")
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

    def on_close(self, reason):
        def handleFunc(roomstub):
            logger.info(f"close ws.addr={self.ip} {self.port}")
            resp = roomstub.Leave(room_pb2.LeaveRoomRequest(
                userIp=self.ip,
                port=self.port
            ))
            if resp.isSuccess:
                del ADDR_CLIENT[(self.ip, self.port)]
        callRpcMethod(handleFunc)
        print("close")

if __name__ == '__main__':
    logger.add("logs/ws_{time}.log",encoding='utf-8',level='INFO')
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5555)
    parser.add_argument("--roomip", type=str, default="127.0.0.1")
    parser.add_argument("--roomport", type=int, default=9000)
    args = parser.parse_args()
    logger.info(f"ws server start.args={args}")
    config = Config()
    WebSocketServer(
        ('0.0.0.0', args.port),
        Resource(OrderedDict([
            ('/echo/.*', EchoApplication)
        ]))
    ).serve_forever()