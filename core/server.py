import threading
import socket
import time

EOM = "\n"

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketes = []

    def recv_send_handler(self):
        while True:
            try:
                conn, addr = self.s.accept()
                self.socketes.append(conn)
                threading.Thread(target=self.recv_send, args=(conn, addr,)).start()
            except:
                print("server socket EXIT!")
                break

    def recv_send(self, conn: socket.socket, addr):
        while True:
            content: str = ""
            while True:
                try:
                    content += conn.recv(1024).decode("utf-8")
                except:
                    break
                if content == "" or content.endswith(EOM):
                    break
            if content == "":
                break
            if content != "":
                print(content)
                # TODO other operation
                for os in self.socketes:
                    os.send(content.encode("utf-8"))
        if conn in self.socketes:
            self.socketes.remove(conn)
        conn.close()

    def exit(self):
        print("online user:" + str(len(self.socketes)))
        for s in self.socketes:
            if s in self.socketes:
                self.socketes.remove(s)
            s.close()
        self.s.close()

    def start(self):
        self.s.bind(("127.0.0.1", 8888))
        self.s.listen(20)
        threading.Thread(target=self.recv_send_handler, args=()).start()


# test
if __name__ == "__main__":
    s = Server()
    s.start()
    time.sleep(25)
    s.exit()
