import grpc

from protobuf import room_pb2,room_pb2_grpc

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:9000") as chan:
        s = room_pb2_grpc.RoomStub(chan)
        response = s.Validate(room_pb2.ValidateRoomRequest(roomnum="rn", password="pw"))
    print(response.isSuccess)