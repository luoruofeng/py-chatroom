import socket
import time

class Explorer():
    def __init__(self,url: str):
        self.url = url
        # self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # self.socket.connect((url,80))
        self.socket = socket.create_connection((url,80))
        self.send()
        self.recv()

    def send(self):
        i = self.socket.send(("GET / HTTP/1.1\r\nHost:%s\r\nConnection:close\r\n\r\n"%self.url).encode("utf-8"))

    def recv(self):
        content = ""
        while True:
            buf = self.socket.recv(1024).decode()
            content += buf
            if buf == None or buf == "":
                break
        print(content)
        self.socket.close()


if __name__ == "__main__":
    Explorer("www.baidu.com")
    time.sleep(3)