# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='room.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nroom.proto\"\x13\n\x11\x43reateRoomRequest\"7\n\x12\x43reateRoomResponse\x12\x0f\n\x07roomnum\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"8\n\x13ValidateRoomRequest\x12\x0f\n\x07roomnum\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"J\n\x14ValidateRoomResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x0f\n\x07\x65rrcode\x18\x02 \x01(\t\x12\x0e\n\x06mssage\x18\x03 \x01(\t\"F\n\x10JoinRoomResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x0f\n\x07\x65rrcode\x18\x02 \x01(\t\x12\x0e\n\x06mssage\x18\x03 \x01(\t\"T\n\x0fJoinRoomRequest\x12\x0e\n\x06userIp\x18\x01 \x01(\t\x12\x10\n\x08userPort\x18\x02 \x01(\x05\x12\x0f\n\x07roomnum\x18\x03 \x01(\t\x12\x0e\n\x06passwd\x18\x04 \x01(\t\"%\n\x12GetRoomAddrRequest\x12\x0f\n\x07roomnum\x18\x01 \x01(\t\"$\n\x08UserAddr\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\".\n\x13GetRoomAddrResponse\x12\x17\n\x04\x61\x64\x64r\x18\x01 \x03(\x0b\x32\t.UserAddr\"0\n\x10LeaveRoomRequest\x12\x0e\n\x06userIp\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"G\n\x11LeaveRoomResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x0f\n\x07\x65rrcode\x18\x02 \x01(\t\x12\x0e\n\x06mssage\x18\x03 \x01(\t\"7\n\x17GetRoomNumByAddrRequest\x12\x0e\n\x06userIp\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"+\n\x18GetRoomNumByAddrResponse\x12\x0f\n\x07roomnum\x18\x01 \x01(\t2\xde\x02\n\x04Room\x12\x33\n\x06\x43reate\x12\x12.CreateRoomRequest\x1a\x13.CreateRoomResponse\"\x00\x12\x39\n\x08Validate\x12\x14.ValidateRoomRequest\x1a\x15.ValidateRoomResponse\"\x00\x12-\n\x04Join\x12\x10.JoinRoomRequest\x1a\x11.JoinRoomResponse\"\x00\x12:\n\x0bGetRoomAddr\x12\x13.GetRoomAddrRequest\x1a\x14.GetRoomAddrResponse\"\x00\x12\x30\n\x05Leave\x12\x11.LeaveRoomRequest\x1a\x12.LeaveRoomResponse\"\x00\x12I\n\x10GetRoomNumByAddr\x12\x18.GetRoomNumByAddrRequest\x1a\x19.GetRoomNumByAddrResponse\"\x00\x62\x06proto3'
)




_CREATEROOMREQUEST = _descriptor.Descriptor(
  name='CreateRoomRequest',
  full_name='CreateRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=33,
)


_CREATEROOMRESPONSE = _descriptor.Descriptor(
  name='CreateRoomResponse',
  full_name='CreateRoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomnum', full_name='CreateRoomResponse.roomnum', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='CreateRoomResponse.password', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=90,
)


_VALIDATEROOMREQUEST = _descriptor.Descriptor(
  name='ValidateRoomRequest',
  full_name='ValidateRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomnum', full_name='ValidateRoomRequest.roomnum', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='ValidateRoomRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=148,
)


_VALIDATEROOMRESPONSE = _descriptor.Descriptor(
  name='ValidateRoomResponse',
  full_name='ValidateRoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='ValidateRoomResponse.isSuccess', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errcode', full_name='ValidateRoomResponse.errcode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mssage', full_name='ValidateRoomResponse.mssage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=224,
)


_JOINROOMRESPONSE = _descriptor.Descriptor(
  name='JoinRoomResponse',
  full_name='JoinRoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='JoinRoomResponse.isSuccess', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errcode', full_name='JoinRoomResponse.errcode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mssage', full_name='JoinRoomResponse.mssage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=296,
)


_JOINROOMREQUEST = _descriptor.Descriptor(
  name='JoinRoomRequest',
  full_name='JoinRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userIp', full_name='JoinRoomRequest.userIp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userPort', full_name='JoinRoomRequest.userPort', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roomnum', full_name='JoinRoomRequest.roomnum', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='JoinRoomRequest.passwd', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=382,
)


_GETROOMADDRREQUEST = _descriptor.Descriptor(
  name='GetRoomAddrRequest',
  full_name='GetRoomAddrRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomnum', full_name='GetRoomAddrRequest.roomnum', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=421,
)


_USERADDR = _descriptor.Descriptor(
  name='UserAddr',
  full_name='UserAddr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='UserAddr.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='UserAddr.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=459,
)


_GETROOMADDRRESPONSE = _descriptor.Descriptor(
  name='GetRoomAddrResponse',
  full_name='GetRoomAddrResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='GetRoomAddrResponse.addr', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=507,
)


_LEAVEROOMREQUEST = _descriptor.Descriptor(
  name='LeaveRoomRequest',
  full_name='LeaveRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userIp', full_name='LeaveRoomRequest.userIp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='LeaveRoomRequest.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=557,
)


_LEAVEROOMRESPONSE = _descriptor.Descriptor(
  name='LeaveRoomResponse',
  full_name='LeaveRoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='LeaveRoomResponse.isSuccess', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errcode', full_name='LeaveRoomResponse.errcode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mssage', full_name='LeaveRoomResponse.mssage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=630,
)


_GETROOMNUMBYADDRREQUEST = _descriptor.Descriptor(
  name='GetRoomNumByAddrRequest',
  full_name='GetRoomNumByAddrRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userIp', full_name='GetRoomNumByAddrRequest.userIp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='GetRoomNumByAddrRequest.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=687,
)


_GETROOMNUMBYADDRRESPONSE = _descriptor.Descriptor(
  name='GetRoomNumByAddrResponse',
  full_name='GetRoomNumByAddrResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roomnum', full_name='GetRoomNumByAddrResponse.roomnum', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=732,
)

_GETROOMADDRRESPONSE.fields_by_name['addr'].message_type = _USERADDR
DESCRIPTOR.message_types_by_name['CreateRoomRequest'] = _CREATEROOMREQUEST
DESCRIPTOR.message_types_by_name['CreateRoomResponse'] = _CREATEROOMRESPONSE
DESCRIPTOR.message_types_by_name['ValidateRoomRequest'] = _VALIDATEROOMREQUEST
DESCRIPTOR.message_types_by_name['ValidateRoomResponse'] = _VALIDATEROOMRESPONSE
DESCRIPTOR.message_types_by_name['JoinRoomResponse'] = _JOINROOMRESPONSE
DESCRIPTOR.message_types_by_name['JoinRoomRequest'] = _JOINROOMREQUEST
DESCRIPTOR.message_types_by_name['GetRoomAddrRequest'] = _GETROOMADDRREQUEST
DESCRIPTOR.message_types_by_name['UserAddr'] = _USERADDR
DESCRIPTOR.message_types_by_name['GetRoomAddrResponse'] = _GETROOMADDRRESPONSE
DESCRIPTOR.message_types_by_name['LeaveRoomRequest'] = _LEAVEROOMREQUEST
DESCRIPTOR.message_types_by_name['LeaveRoomResponse'] = _LEAVEROOMRESPONSE
DESCRIPTOR.message_types_by_name['GetRoomNumByAddrRequest'] = _GETROOMNUMBYADDRREQUEST
DESCRIPTOR.message_types_by_name['GetRoomNumByAddrResponse'] = _GETROOMNUMBYADDRRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRoomRequest = _reflection.GeneratedProtocolMessageType('CreateRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROOMREQUEST,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:CreateRoomRequest)
  })
_sym_db.RegisterMessage(CreateRoomRequest)

CreateRoomResponse = _reflection.GeneratedProtocolMessageType('CreateRoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROOMRESPONSE,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:CreateRoomResponse)
  })
_sym_db.RegisterMessage(CreateRoomResponse)

ValidateRoomRequest = _reflection.GeneratedProtocolMessageType('ValidateRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEROOMREQUEST,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:ValidateRoomRequest)
  })
_sym_db.RegisterMessage(ValidateRoomRequest)

ValidateRoomResponse = _reflection.GeneratedProtocolMessageType('ValidateRoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATEROOMRESPONSE,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:ValidateRoomResponse)
  })
_sym_db.RegisterMessage(ValidateRoomResponse)

JoinRoomResponse = _reflection.GeneratedProtocolMessageType('JoinRoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOINROOMRESPONSE,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:JoinRoomResponse)
  })
_sym_db.RegisterMessage(JoinRoomResponse)

JoinRoomRequest = _reflection.GeneratedProtocolMessageType('JoinRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOINROOMREQUEST,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:JoinRoomRequest)
  })
_sym_db.RegisterMessage(JoinRoomRequest)

GetRoomAddrRequest = _reflection.GeneratedProtocolMessageType('GetRoomAddrRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETROOMADDRREQUEST,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:GetRoomAddrRequest)
  })
_sym_db.RegisterMessage(GetRoomAddrRequest)

UserAddr = _reflection.GeneratedProtocolMessageType('UserAddr', (_message.Message,), {
  'DESCRIPTOR' : _USERADDR,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:UserAddr)
  })
_sym_db.RegisterMessage(UserAddr)

GetRoomAddrResponse = _reflection.GeneratedProtocolMessageType('GetRoomAddrResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETROOMADDRRESPONSE,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:GetRoomAddrResponse)
  })
_sym_db.RegisterMessage(GetRoomAddrResponse)

LeaveRoomRequest = _reflection.GeneratedProtocolMessageType('LeaveRoomRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEAVEROOMREQUEST,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:LeaveRoomRequest)
  })
_sym_db.RegisterMessage(LeaveRoomRequest)

LeaveRoomResponse = _reflection.GeneratedProtocolMessageType('LeaveRoomResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEAVEROOMRESPONSE,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:LeaveRoomResponse)
  })
_sym_db.RegisterMessage(LeaveRoomResponse)

GetRoomNumByAddrRequest = _reflection.GeneratedProtocolMessageType('GetRoomNumByAddrRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETROOMNUMBYADDRREQUEST,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:GetRoomNumByAddrRequest)
  })
_sym_db.RegisterMessage(GetRoomNumByAddrRequest)

GetRoomNumByAddrResponse = _reflection.GeneratedProtocolMessageType('GetRoomNumByAddrResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETROOMNUMBYADDRRESPONSE,
  '__module__' : 'room_pb2'
  # @@protoc_insertion_point(class_scope:GetRoomNumByAddrResponse)
  })
_sym_db.RegisterMessage(GetRoomNumByAddrResponse)



_ROOM = _descriptor.ServiceDescriptor(
  name='Room',
  full_name='Room',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=735,
  serialized_end=1085,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='Room.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEROOMREQUEST,
    output_type=_CREATEROOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Validate',
    full_name='Room.Validate',
    index=1,
    containing_service=None,
    input_type=_VALIDATEROOMREQUEST,
    output_type=_VALIDATEROOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Join',
    full_name='Room.Join',
    index=2,
    containing_service=None,
    input_type=_JOINROOMREQUEST,
    output_type=_JOINROOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRoomAddr',
    full_name='Room.GetRoomAddr',
    index=3,
    containing_service=None,
    input_type=_GETROOMADDRREQUEST,
    output_type=_GETROOMADDRRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Leave',
    full_name='Room.Leave',
    index=4,
    containing_service=None,
    input_type=_LEAVEROOMREQUEST,
    output_type=_LEAVEROOMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRoomNumByAddr',
    full_name='Room.GetRoomNumByAddr',
    index=5,
    containing_service=None,
    input_type=_GETROOMNUMBYADDRREQUEST,
    output_type=_GETROOMNUMBYADDRRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROOM)

DESCRIPTOR.services_by_name['Room'] = _ROOM

# @@protoc_insertion_point(module_scope)
