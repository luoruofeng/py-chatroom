import random
from concurrent import futures
import argparse

import grpc
from loguru import logger

from protobuf import room_pb2,room_pb2_grpc

class Room(room_pb2_grpc.RoomServicer):
    def __init__(self):
        self.rooms_pw: dict[str, str] = {} #key:房间号 value：密码
        self.rooms: dict[str, tuple] = {} # key：房间号 value：addr_tuple_array
        self.members: dict[tuple, str] = {} # key:addr_tuple value：房间号


    def print_count(func):
        def inner(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            logger.info(f"rooms:{self.rooms}")
            logger.info(f"members:{self.members}")
            logger.info(f"rooms_pw:{self.rooms_pw}")
            return result
        return inner

    @print_count
    def Create(self, request, context):
        logger.info(f"create request:{request}")
        roomnum = self.createRandomNum()
        pw = self.createRandomNum()
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
        logger.info(f"validate request:{request}")
        r = self.validateLogin(request.roomnum, request.password)
        return room_pb2.ValidateRoomResponse(isSuccess=r)

    def addToRoom(self, room_number, ip, port):
        if room_number not in self.rooms:
            self.rooms[room_number] = []
        self.rooms[room_number].append((ip, port))
        self.members[(ip, port)] = room_number

    @print_count
    def Join(self, request, context):
        logger.info(f"join request:{request}")
        self.addToRoom(request.roomnum, request.userIp, request.userPort)
        return room_pb2.JoinRoomResponse(isSuccess=True)

    @print_count
    def GetRoomAddr(self, request, context):
        logger.info(f"GetRoomAddr request:{request}")
        addrs = [room_pb2.UserAddr(ip=k, port=v) for k, v in self.rooms[request.roomnum]]
        return room_pb2.GetRoomAddrResponse(addr = addrs)


    def getRoomNumByAddr(self,ip ,port):
        return self.members[(ip, port)]

    @print_count
    def GetRoomNumByAddr(self, request, context):
        logger.info(f"GetRoomNumByAddr request:{request}")
        roomnum = self.getRoomNumByAddr(ip=request.userIp,port=request.port)
        return room_pb2.GetRoomAddrRequest(roomnum=roomnum)


    @print_count
    def Leave(self, request, context):
        logger.info(f"Leave request:{request}")
        ip,port = request.userIp,request.port
        roomNum = self.getRoomNumByAddr(ip, port)
        self.members.pop((ip, port))
        self.rooms[roomNum].remove((ip, port))
        if len(self.rooms[roomNum]) == 0:
            self.rooms.pop(roomNum)
            self.rooms_pw.pop(roomNum)
        return room_pb2.LeaveRoomResponse(isSuccess=True)

    ALL_FONTS = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def createRandomNum(self):
        result = ""
        for i in range(8):
            result += str(Room.ALL_FONTS[random.randint(0, len(Room.ALL_FONTS) - 1)])
        return result

    @logger.catch
    def run(self):
        s = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
        room_pb2_grpc.add_RoomServicer_to_server(Room(), s)
        s.add_insecure_port(f"0.0.0.0:{args.port}")
        logger.info(f"start room grpc servicer. addr:0.0.0.0:{args.port}")
        s.start()
        s.wait_for_termination()
        logger.info(f"end room grpc servicer. addr:0.0.0.0:{args.port}")




if __name__ == "__main__":
    logger.add("logs/room_{time}.log",encoding='utf-8',level='INFO')
    logger.add("logs/room_error_{time}.log",encoding='utf-8',level='ERROR')
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=9000)
    args = parser.parse_args()
    Room().run()

