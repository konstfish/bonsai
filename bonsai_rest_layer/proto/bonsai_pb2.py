# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bonsai.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x62onsai.proto\x12\x06\x62onsai\"V\n\x13RegistrationRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03job\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x10\n\x03key\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_key\"+\n\x18RegistrationConfirmation\x12\x0f\n\x07message\x18\x01 \x01(\t\"X\n\x0eMetricsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03job\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0f\n\x07metrics\x18\x04 \x01(\x0c\x12\x0e\n\x06labels\x18\x05 \x03(\t\"4\n\x13MetricsConfirmation\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07\x63onfirm\x18\x02 \x01(\t2\xa1\x01\n\x06Server\x12Q\n\x0eRegisterClient\x12\x1b.bonsai.RegistrationRequest\x1a .bonsai.RegistrationConfirmation\"\x00\x12\x44\n\x0bPushMetrics\x12\x16.bonsai.MetricsRequest\x1a\x1b.bonsai.MetricsConfirmation\"\x00\x42/\n\x18io.grpc.konstfish.bonsaiB\x0b\x42onsaiProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bonsai_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030io.grpc.konstfish.bonsaiB\013BonsaiProtoP\001\242\002\003HLW'
  _REGISTRATIONREQUEST._serialized_start=24
  _REGISTRATIONREQUEST._serialized_end=110
  _REGISTRATIONCONFIRMATION._serialized_start=112
  _REGISTRATIONCONFIRMATION._serialized_end=155
  _METRICSREQUEST._serialized_start=157
  _METRICSREQUEST._serialized_end=245
  _METRICSCONFIRMATION._serialized_start=247
  _METRICSCONFIRMATION._serialized_end=299
  _SERVER._serialized_start=302
  _SERVER._serialized_end=463
# @@protoc_insertion_point(module_scope)