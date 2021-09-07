import random
import threading
import time

import grpc
import requests
from flask import Flask,render_template,request,redirect

from manage.protobuf import room_pb2_grpc
from manage.protobuf.room_pb2 import *


#Flask will look for templates in the templates folder.
flask_app = Flask(import_name=__name__,
            static_url_path='/static', # 配置静态文件的访问 url 前缀
            static_folder='ui',    # 配置静态文件的文件夹
            template_folder='ui/html') # 配置模板文件的文件夹

@flask_app.route("/")
def home():
    return render_template("home.html")

@flask_app.route("/index/<roomnum>/<password>")
def index(roomnum,password):
    return render_template("index.html",roomnum=roomnum,password=password)

@flask_app.route("/test")
def test():
    return render_template("test.html")

ALL_FONTS="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def createRandomNum():
#     result = ""
#     for i in range(8):
#         result += str(ALL_FONTS[random.randint(0,len(ALL_FONTS)-1)])
#     return result

RPC_ADDR = "localhost:9000"

def callRpcMethod(handleFunc):
    with grpc.insecure_channel(RPC_ADDR) as chan:
        stub = room_pb2_grpc.RoomStub(chan)
        return handleFunc(stub)


@flask_app.route("/initroom")
def initRoom():
    def handleFunc(roomStub):
        resp = roomStub.Create(CreateRoomRequest())
        return resp.roomnum, resp.password
    roomnum, password = callRpcMethod(handleFunc)
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
    if validateLogin(rn,pw):
        return redirect("/index/%s/%s"%(rn,pw))
    else:
        return redirect("/")

@flask_app.route("/vallogin")
def validateLogin(roomnum, password):
    def handleFunc(serverStub):
        resp = serverStub.Validate(ValidateRoomRequest(
            roomnum=roomnum,
            password=password
        ))
        return resp.isSuccess
    return callRpcMethod(handleFunc)

if __name__ == '__main__':
    # allRoomsPW = {}
    # threading.Thread(target=cleanDisableRoom,args=()).start()
    flask_app.run("0.0.0.0", 8888)