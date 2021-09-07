import queue
import socket
import select
from core.server import EOM
class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.inputs = [self.s,]
        self.outputs = []
        self.messageQ = {}

    def end(self,s: socket.socket):
        print("--")
        self.inputs.remove(s)
        if s in self.outputs:
            self.outputs.remove(s)
        del self.messageQ[s]
        s.close()

    def start(self):
        self.s.bind(("0.0.0.0",8888))
        self.s.listen(20)
        while True:
            reads, writes, exceptions = select.select(self.inputs,self.outputs,self.inputs)
            for r in reads:
                if r is self.s:
                    socket, addr = self.s.accept()
                    self.inputs.append(socket)
                    self.messageQ[socket] = queue.Queue()
                else:
                    content = ""
                    while True:
                        try:
                            buf = r.recv(1024)
                            if buf:
                                content += buf.decode("utf-8")
                            else:
                                # self.end(r)
                                break
                        except:
                            break
                        if content == "" or content.endswith(EOM):
                            break
                    if content == "":
                        self.end(r)
                        continue
                    print(content)
                    self.messageQ[r].put(content)
                    if r not in self.outputs:
                        self.outputs.append(r)
            for w in writes:
                try:
                    mes = self.messageQ[w].get_nowait()
                except queue.Empty:
                    if w in self.outputs:
                        self.outputs.remove(w)
                else:
                    w.send(mes.encode("utf-8"))

            for e in exceptions:
                self.end(e)


if __name__ == "__main__":
    Server().start()
