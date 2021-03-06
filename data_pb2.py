# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='DATA2410_Portfolio2',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ndata.proto\x12\x13\x44\x41TA2410_Portfolio2\"\x0e\n\x0cNo_parameter\"!\n\tConfirmed\x12\x14\n\x0c\x63onfirmation\x18\x01 \x01(\x08\" \n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"i\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x03(\x05\x12\x11\n\tgame_over\x18\x03 \x01(\x08\x12/\n\x08position\x18\x04 \x03(\x0b\x32\x1d.DATA2410_Portfolio2.Position\")\n\nHigh_score\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"B\n\x0bLeaderboard\x12\x33\n\nhigh_score\x18\x01 \x03(\x0b\x32\x1f.DATA2410_Portfolio2.High_score\"h\n\x0bInformation\x12+\n\x06player\x18\x01 \x01(\x0b\x32\x1b.DATA2410_Portfolio2.Player\x12,\n\x05\x66ruit\x18\x02 \x01(\x0b\x32\x1d.DATA2410_Portfolio2.Position2\xf7\x03\n\x05Snake\x12T\n\x0fsend_high_score\x12\x1f.DATA2410_Portfolio2.High_score\x1a\x1e.DATA2410_Portfolio2.Confirmed\"\x00\x12M\n\nsend_fruit\x12\x1d.DATA2410_Portfolio2.Position\x1a\x1e.DATA2410_Portfolio2.Confirmed\"\x00\x12I\n\x0bsend_player\x12\x1b.DATA2410_Portfolio2.Player\x1a\x1b.DATA2410_Portfolio2.Player\"\x00\x12X\n\x0fget_leaderboard\x12!.DATA2410_Portfolio2.No_parameter\x1a .DATA2410_Portfolio2.Leaderboard\"\x00\x12N\n\x08get_size\x12!.DATA2410_Portfolio2.No_parameter\x1a\x1d.DATA2410_Portfolio2.Position\"\x00\x12T\n\x0fget_information\x12\x1b.DATA2410_Portfolio2.Player\x1a .DATA2410_Portfolio2.Information\"\x00\x30\x01\x62\x06proto3'
)




_NO_PARAMETER = _descriptor.Descriptor(
  name='No_parameter',
  full_name='DATA2410_Portfolio2.No_parameter',
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
  serialized_start=35,
  serialized_end=49,
)


_CONFIRMED = _descriptor.Descriptor(
  name='Confirmed',
  full_name='DATA2410_Portfolio2.Confirmed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='confirmation', full_name='DATA2410_Portfolio2.Confirmed.confirmation', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=51,
  serialized_end=84,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='DATA2410_Portfolio2.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='DATA2410_Portfolio2.Position.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='DATA2410_Portfolio2.Position.y', index=1,
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
  serialized_start=86,
  serialized_end=118,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='DATA2410_Portfolio2.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DATA2410_Portfolio2.Player.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='DATA2410_Portfolio2.Player.color', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='game_over', full_name='DATA2410_Portfolio2.Player.game_over', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='DATA2410_Portfolio2.Player.position', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=120,
  serialized_end=225,
)


_HIGH_SCORE = _descriptor.Descriptor(
  name='High_score',
  full_name='DATA2410_Portfolio2.High_score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DATA2410_Portfolio2.High_score.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='DATA2410_Portfolio2.High_score.score', index=1,
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
  serialized_start=227,
  serialized_end=268,
)


_LEADERBOARD = _descriptor.Descriptor(
  name='Leaderboard',
  full_name='DATA2410_Portfolio2.Leaderboard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='high_score', full_name='DATA2410_Portfolio2.Leaderboard.high_score', index=0,
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
  serialized_start=270,
  serialized_end=336,
)


_INFORMATION = _descriptor.Descriptor(
  name='Information',
  full_name='DATA2410_Portfolio2.Information',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='DATA2410_Portfolio2.Information.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fruit', full_name='DATA2410_Portfolio2.Information.fruit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=338,
  serialized_end=442,
)

_PLAYER.fields_by_name['position'].message_type = _POSITION
_LEADERBOARD.fields_by_name['high_score'].message_type = _HIGH_SCORE
_INFORMATION.fields_by_name['player'].message_type = _PLAYER
_INFORMATION.fields_by_name['fruit'].message_type = _POSITION
DESCRIPTOR.message_types_by_name['No_parameter'] = _NO_PARAMETER
DESCRIPTOR.message_types_by_name['Confirmed'] = _CONFIRMED
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['High_score'] = _HIGH_SCORE
DESCRIPTOR.message_types_by_name['Leaderboard'] = _LEADERBOARD
DESCRIPTOR.message_types_by_name['Information'] = _INFORMATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

No_parameter = _reflection.GeneratedProtocolMessageType('No_parameter', (_message.Message,), {
  'DESCRIPTOR' : _NO_PARAMETER,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.No_parameter)
  })
_sym_db.RegisterMessage(No_parameter)

Confirmed = _reflection.GeneratedProtocolMessageType('Confirmed', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMED,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.Confirmed)
  })
_sym_db.RegisterMessage(Confirmed)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.Position)
  })
_sym_db.RegisterMessage(Position)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.Player)
  })
_sym_db.RegisterMessage(Player)

High_score = _reflection.GeneratedProtocolMessageType('High_score', (_message.Message,), {
  'DESCRIPTOR' : _HIGH_SCORE,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.High_score)
  })
_sym_db.RegisterMessage(High_score)

Leaderboard = _reflection.GeneratedProtocolMessageType('Leaderboard', (_message.Message,), {
  'DESCRIPTOR' : _LEADERBOARD,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.Leaderboard)
  })
_sym_db.RegisterMessage(Leaderboard)

Information = _reflection.GeneratedProtocolMessageType('Information', (_message.Message,), {
  'DESCRIPTOR' : _INFORMATION,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:DATA2410_Portfolio2.Information)
  })
_sym_db.RegisterMessage(Information)



_SNAKE = _descriptor.ServiceDescriptor(
  name='Snake',
  full_name='DATA2410_Portfolio2.Snake',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=445,
  serialized_end=948,
  methods=[
  _descriptor.MethodDescriptor(
    name='send_high_score',
    full_name='DATA2410_Portfolio2.Snake.send_high_score',
    index=0,
    containing_service=None,
    input_type=_HIGH_SCORE,
    output_type=_CONFIRMED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='send_fruit',
    full_name='DATA2410_Portfolio2.Snake.send_fruit',
    index=1,
    containing_service=None,
    input_type=_POSITION,
    output_type=_CONFIRMED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='send_player',
    full_name='DATA2410_Portfolio2.Snake.send_player',
    index=2,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_PLAYER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_leaderboard',
    full_name='DATA2410_Portfolio2.Snake.get_leaderboard',
    index=3,
    containing_service=None,
    input_type=_NO_PARAMETER,
    output_type=_LEADERBOARD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_size',
    full_name='DATA2410_Portfolio2.Snake.get_size',
    index=4,
    containing_service=None,
    input_type=_NO_PARAMETER,
    output_type=_POSITION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_information',
    full_name='DATA2410_Portfolio2.Snake.get_information',
    index=5,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_INFORMATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SNAKE)

DESCRIPTOR.services_by_name['Snake'] = _SNAKE

# @@protoc_insertion_point(module_scope)
