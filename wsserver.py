import threading

from flask import Flask
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource, WebSocketError
from collections import OrderedDict
import json

class Config:
    def __init__(self):
        self.rooms = {} # key：房间号 value：client_array
        self.members = {} # key:addr_tuple value：房间号

class EchoApplication(WebSocketApplication):
    def __init__(self,ws):
        super().__init__(ws)

    def addToRoom(self):
        path_arr = self.ws.path.split("/")
        room_number = path_arr[len(path_arr) - 1]
        if room_number not in config.rooms:
            config.rooms[room_number] = []
        config.rooms[room_number].append(self.ws.handler.active_client)
        config.members[self.ws.handler.active_client.address] = room_number


    def on_open(self):
        self.addToRoom()
        print("Connection opened")

    def getRoomNumByAddr(self):
        return config.members[self.ws.handler.active_client.address]

    def on_message(self, message):
        if message == None or message == "":
            return
        message_obj = json.loads(message.decode("utf-8"))
        nickname = message_obj["nickname"]
        mes_type = message_obj["type"]
        content = message_obj["content"]
        roomNum = self.getRoomNumByAddr()
        for client in config.rooms[roomNum]:
            if client and client.ws and message:
                client.ws.send(json.dumps({
                    'msg_type': mes_type,
                    'nickname': nickname,
                    "content" : content
                }))


    def on_close(self, reason):
        roomNum = self.getRoomNumByAddr()
        config.members.pop(self.ws.handler.active_client.address)
        config.rooms[roomNum].remove(self.ws.handler.active_client)

        if len(config.rooms[roomNum]) == 0:
            config.rooms.pop(roomNum)

        print("close")

flask_app = Flask(__name__)

@flask_app.route("/personcount/<roomnum>")
def personCount(roomnum):
    if roomnum not in config.rooms:
        return "0"
    else:
        return str(len(config.rooms[roomnum]))

def flask_server_run():
    flask_app.run(host="0.0.0.0",port="5556")

if __name__ == '__main__':
    config = Config()
    threading.Thread(target=flask_server_run,args="").start()
    WebSocketServer(
        ('0.0.0.0', 5555),
        Resource(OrderedDict([
            ('/echo/.*', EchoApplication)
        ]))
    ).serve_forever()