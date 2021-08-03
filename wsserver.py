
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource, WebSocketError
from collections import OrderedDict
import json

class EchoApplication(WebSocketApplication):
    def on_open(self):
        print("Connection opened")

    def on_message(self, message):
        for addr,client in self.ws.handler.server.clients.items():
            if client and client.ws and message:
                client.ws.send(json.dumps({
                    'msg_type': 'message',
                    'nickname': message.decode("utf-8")
                }))


    def on_close(self, reason):
        print(reason)

if __name__ == '__main__':
    WebSocketServer(
        ('0.0.0.0', 5555),
        Resource(OrderedDict([('/echo', EchoApplication)]))
    ).serve_forever()