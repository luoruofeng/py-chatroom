import random
import threading
import time

import requests


from flask import Flask,render_template,request,redirect

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

def createRandomNum():
    result = ""
    for i in range(8):
        result += str(ALL_FONTS[random.randint(0,len(ALL_FONTS)-1)])
    return result

@flask_app.route("/initroom")
def initRoom():
    roomnum = createRandomNum()
    password = createRandomNum()
    allRoomsPW[roomnum] = password
    return redirect("/index/"+roomnum+"/"+password)


def cleanDisableRoom():
    #test
    # allRoomsPW[111111] = 234
    while True:
        for roomnum in allRoomsPW:
            data = requests.get("http://localhost:5556/personcount/%d" % str(roomnum))
            if data.status_code == 200 and data.content != None:
                if data.content.decode("utf-8") == "0":
                    allRoomsPW.pop(roomnum)
        time.sleep(60)


if __name__ == '__main__':
    allRoomsPW = {}
    threading.Thread(target=cleanDisableRoom,args=()).start()
    flask_app.run("0.0.0.0", 8888)