# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngame.proto\x12\x04game\"\x14\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\tGameState\x12\r\n\x05state\x18\x01 \x01(\t\"_\n\x04Move\x12\x10\n\x08moveFrom\x18\x01 \x01(\x05\x12\x0e\n\x06moveTo\x18\x02 \x01(\x05\x12\x0f\n\x07removed\x18\x03 \x01(\x05\x12\x0f\n\x07\x65ndGame\x18\x04 \x01(\x08\x12\x13\n\x0brestartGame\x18\x05 \x01(\x08\"\x07\n\x05\x45mpty2\x88\x01\n\x0bGameService\x12(\n\x07\x43onnect\x12\n.game.User\x1a\x0f.game.GameState\"\x00\x12$\n\x08SendMove\x12\n.game.Move\x1a\n.game.Move\"\x00\x12)\n\nGameStream\x12\x0b.game.Empty\x1a\n.game.Move\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=20
  _globals['_USER']._serialized_end=40
  _globals['_GAMESTATE']._serialized_start=42
  _globals['_GAMESTATE']._serialized_end=68
  _globals['_MOVE']._serialized_start=70
  _globals['_MOVE']._serialized_end=165
  _globals['_EMPTY']._serialized_start=167
  _globals['_EMPTY']._serialized_end=174
  _globals['_GAMESERVICE']._serialized_start=177
  _globals['_GAMESERVICE']._serialized_end=313
# @@protoc_insertion_point(module_scope)
