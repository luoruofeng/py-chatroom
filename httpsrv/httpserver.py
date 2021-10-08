import random
import threading
import time
import argparse

import grpc
# import requests
from flask import Flask,render_template,request,redirect
from gevent import pywsgi
from loguru import logger

from protobuf import room_pb2_grpc
from protobuf.room_pb2 import *


#Flask will look for templates in the templates folder.
flask_app = Flask(import_name=__name__,
            static_url_path='/static', # 配置静态文件的访问 url 前缀
            static_folder='ui',    # 配置静态文件的文件夹
            template_folder='ui/html') # 配置模板文件的文件夹

@flask_app.route("/")
def home():
    logger.info("home page")
    return render_template("home.html")

@flask_app.route("/index/<roomnum>/<password>")
def index(roomnum,password):
    logger.info(f"index page: roomnum={roomnum} password={password} roomnum={roomnum}, password={password}")
    return render_template("index.html", roomnum=roomnum, password=password, wsip=wsip, wsport=wsport)

@flask_app.route("/test")
def test():
    return render_template("test.html")

ALL_FONTS="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def createRandomNum():
#     result = ""
#     for i in range(8):
#         result += str(ALL_FONTS[random.randint(0,len(ALL_FONTS)-1)])
#     return result

def callRpcMethod(handleFunc):
    with grpc.insecure_channel(f"{roomip}:{roomport}") as chan:
        stub = room_pb2_grpc.RoomStub(chan)
        return handleFunc(stub)


@flask_app.route("/initroom")
def initRoom():
    logger.info("initroom page")
    def handleFunc(roomStub):
        resp = roomStub.Create(CreateRoomRequest())
        return resp.roomnum, resp.password
    roomnum, password = callRpcMethod(handleFunc)
    logger.info(f"initroom page done: roomnum={roomnum} password={password}")
    return redirect("/index/"+roomnum+"/"+password)


# def cleanDisableRoom():
#     #test
#     # allRoomsPW[111111] = 234
#     while True:
#         for roomnum in allRoomsPW:
#             data = requests.get("http://localhost:5556/personcount/%s" % str(roomnum))
#             if data.status_code == 200 and data.content != None:
#                 if data.content.decode("utf-8") == "0":
#                     allRoomsPW.pop(roomnum)
#         time.sleep(60)

@flask_app.route("/login",methods=["POST"])
def login():
    rn = request.form.get("roomnum")
    pw = request.form.get("password")
    logger.info(f"login page:rn={rn} pw={pw}")
    if validateLogin(rn,pw):
        return redirect("/index/%s/%s"%(rn,pw))
    else:
        return redirect("/")

@flask_app.route("/vallogin")
def validateLogin(roomnum, password):
    def handleFunc(serverStub):
        logger.info(f"validateLogin page:roomnum={roomnum} password={password}")
        resp = serverStub.Validate(ValidateRoomRequest(
            roomnum=roomnum,
            password=password
        ))
        return resp.isSuccess
    return callRpcMethod(handleFunc)

if __name__ == '__main__':
    logger.add("logs/http_{time}.log")
    # allRoomsPW = {}
    # threading.Thread(target=cleanDisableRoom,args=()).start()
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=80)
    parser.add_argument("--roomip", type=str, default="127.0.0.1")
    parser.add_argument("--roomport", type=int, default=9000)
    parser.add_argument("--wsip", type=str, default="127.0.0.1")
    parser.add_argument("--wsport", type=int, default=5555)
    args = parser.parse_args()
    roomip = args.roomip
    roomport = args.roomport
    wsip = args.wsip
    wsport = args.wsport
    logger.info(f"http server start.args={args}")
    server = pywsgi.WSGIServer(('0.0.0.0', args.port), flask_app)
    server.serve_forever()
    # flask_app.run("0.0.0.0", args.port)
