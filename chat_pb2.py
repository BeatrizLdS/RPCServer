# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\"\x07\n\x05\x45mpty\"+\n\x0b\x43hatMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t2v\n\x0b\x43hatService\x12\x35\n\x0bSendMessage\x12\x11.chat.ChatMessage\x1a\x11.chat.ChatMessage\"\x00\x12\x30\n\nChatStream\x12\x0b.chat.Empty\x1a\x11.chat.ChatMessage\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=20
  _globals['_EMPTY']._serialized_end=27
  _globals['_CHATMESSAGE']._serialized_start=29
  _globals['_CHATMESSAGE']._serialized_end=72
  _globals['_CHATSERVICE']._serialized_start=74
  _globals['_CHATSERVICE']._serialized_end=192
# @@protoc_insertion_point(module_scope)
