import random
from concurrent import futures

import grpc

from protobuf import room_pb2,room_pb2_grpc

class Room(room_pb2_grpc.RoomServicer):
    def __init__(self):
        self.rooms_pw: dict[str, str] = {} #key:房间号 value：密码
        self.rooms: dict[str, tuple] = {} # key：房间号 value：addr_tuple_array
        self.members: dict[tuple, str] = {} # key:addr_tuple value：房间号


    def print_count(func):
        def inner(self, *args, **kwargs):
            print(self)
            result = func(self, *args, **kwargs)
            print(result)
            print(self.rooms)
            print(self.members)
            print(self.rooms_pw)
            return result
        return inner

    @print_count
    def Create(self, request, context):
        roomnum = self.createRandomNum()
        pw = self.createRandomNum()
        print(pw)
        self.rooms_pw[roomnum] = pw
        return room_pb2.CreateRoomResponse(
            roomnum = roomnum,
            password = pw
        )

    def validateLogin(self, roomnum, password):
        if roomnum not in self.rooms_pw:
            return False
        if password != self.rooms_pw[roomnum]:
            return False
        else:
            return True

    @print_count
    def Validate(self, request, context):
        r = self.validateLogin(request.roomnum, request.password)
        return room_pb2.ValidateRoomResponse(isSuccess=r)

    def addToRoom(self, room_number, ip, port):
        if room_number not in self.rooms:
            self.rooms[room_number] = []
        self.rooms[room_number].append((ip, port))
        self.members[(ip, port)] = room_number

    @print_count
    def Join(self, request, context):
        self.addToRoom(request.roomnum, request.userIp, request.userPort)
        return room_pb2.JoinRoomResponse(isSuccess=True)

    @print_count
    def GetRoomAddr(self, request, context):
        addrs = [room_pb2.UserAddr(ip=k, port=v) for k, v in self.rooms[request.roomnum]]
        return room_pb2.GetRoomAddrResponse(addr = addrs)

    def getRoomNumByAddr(self,ip ,port):
        return self.members[(ip, port)]

    def GetRoomNumByAddr(self, request, context):
        roomnum = self.getRoomNumByAddr(userIp=request.userIp,port=request.port)
        return room_pb2.GetRoomAddrRequest(roomnum=roomnum)


    @print_count
    def Leave(self, request, context):
        print("leave")
        ip,port = request.userIp,request.port
        roomNum = self.getRoomNumByAddr()
        self.members.pop((ip, port))
        self.rooms[roomNum].remove((ip, port))

        if len(self.rooms[roomNum]) == 0:
            self.rooms.pop(roomNum)
            self.rooms_pw.pop(roomNum)


    ALL_FONTS = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def createRandomNum(self):
        result = ""
        for i in range(8):
            result += str(Room.ALL_FONTS[random.randint(0, len(Room.ALL_FONTS) - 1)])
        return result

    def run(self):
        s = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
        room_pb2_grpc.add_RoomServicer_to_server(Room(), s)
        s.add_insecure_port("0.0.0.0:9000")
        s.start()
        s.wait_for_termination()



if __name__ == "__main__":
    Room().run()

