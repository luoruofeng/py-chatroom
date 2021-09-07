import threading
import socket
import time
import json
import random

from core.server import EOM
from core.common import *

class Client:
    def __init__(self,name="匿名用户"):
        self.s = socket.create_connection(("127.0.0.1", 8888,))
        self.name = name

    def send(self,content: str):
        self.s.send(content.encode("utf-8"))

    def start(self):
         threading.Thread(target=self.recv,args=()).start()

    def recv(self):
        while True:
            content = ""
            while True:
                try:
                    content += self.s.recv(1024).decode("utf-8")
                except:
                    break
                if content == "" or content.endswith(EOM):
                    break
            if content == "":
                break
            # print(content)
            #TODO other operation
            c_dict = json.loads(content)
            print("name:"+c_dict['name']+" type:"+str(c_dict['mt'])+" content:"+c_dict['content'])
        self.s.close()

    def end(self):
        self.s.close()


def random_name() -> str:
    ALL_FONT = "abcdefghijklmnopqrstuvwxyz1234567890"
    name = ""
    for i in range(3):
        name += ALL_FONT[random.randint(0,len(ALL_FONT)-1)]
    return name

if __name__ == "__main__":
    name = random_name()
    c = Client(name=name)
    c.start()

    time.sleep(3)
    c.send(create_message(name=name,type=MessageType.TXT,content="hello!")+EOM)

    time.sleep(3)
    c.end()