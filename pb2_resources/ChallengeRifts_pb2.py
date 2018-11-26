# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChallengeRifts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from pb2_resources import HeroCommon_pb2 as HeroCommon__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='ChallengeRifts.proto',
  package='D3.ChallengeRifts',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x43hallengeRifts.proto\x12\x11\x44\x33.ChallengeRifts\x1a\x10HeroCommon.proto\"\xe7\x01\n\rChallengeData\x12\x18\n\x10\x63hallenge_number\x18\x01 \x01(\r\x12!\n\x19\x63hallenge_start_unix_time\x18\x02 \x01(\x03\x12*\n\"challenge_last_broadcast_unix_time\x18\x03 \x01(\x03\x12\'\n\x1f\x63hallenge_end_unix_time_console\x18\x04 \x01(\x03\x12\x16\n\x0e\x63hallenge_hash\x18\x05 \x01(\x04\x12,\n!challenge_nephalem_orb_multiplier\x18\x06 \x01(\x02:\x01\x31\"\x8b\x01\n\x0b\x41\x63\x63ountData\x12$\n\x1clast_challenge_reward_earned\x18\x01 \x01(\r\x12\x1c\n\x14last_challenge_tried\x18\x02 \x01(\r\x12\x38\n\x13saved_conversations\x18\x03 \x01(\x0b\x32\x1b.D3.Hero.SavedConversations')
  ,
  dependencies=[HeroCommon__pb2.DESCRIPTOR,])




_CHALLENGEDATA = _descriptor.Descriptor(
  name='ChallengeData',
  full_name='D3.ChallengeRifts.ChallengeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='challenge_number', full_name='D3.ChallengeRifts.ChallengeData.challenge_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_start_unix_time', full_name='D3.ChallengeRifts.ChallengeData.challenge_start_unix_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_last_broadcast_unix_time', full_name='D3.ChallengeRifts.ChallengeData.challenge_last_broadcast_unix_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_end_unix_time_console', full_name='D3.ChallengeRifts.ChallengeData.challenge_end_unix_time_console', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_hash', full_name='D3.ChallengeRifts.ChallengeData.challenge_hash', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge_nephalem_orb_multiplier', full_name='D3.ChallengeRifts.ChallengeData.challenge_nephalem_orb_multiplier', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=293,
)


_ACCOUNTDATA = _descriptor.Descriptor(
  name='AccountData',
  full_name='D3.ChallengeRifts.AccountData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_challenge_reward_earned', full_name='D3.ChallengeRifts.AccountData.last_challenge_reward_earned', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_challenge_tried', full_name='D3.ChallengeRifts.AccountData.last_challenge_tried', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saved_conversations', full_name='D3.ChallengeRifts.AccountData.saved_conversations', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=435,
)

_ACCOUNTDATA.fields_by_name['saved_conversations'].message_type = HeroCommon__pb2._SAVEDCONVERSATIONS
DESCRIPTOR.message_types_by_name['ChallengeData'] = _CHALLENGEDATA
DESCRIPTOR.message_types_by_name['AccountData'] = _ACCOUNTDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChallengeData = _reflection.GeneratedProtocolMessageType('ChallengeData', (_message.Message,), dict(
  DESCRIPTOR = _CHALLENGEDATA,
  __module__ = 'ChallengeRifts_pb2'
  # @@protoc_insertion_point(class_scope:D3.ChallengeRifts.ChallengeData)
  ))
_sym_db.RegisterMessage(ChallengeData)

AccountData = _reflection.GeneratedProtocolMessageType('AccountData', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTDATA,
  __module__ = 'ChallengeRifts_pb2'
  # @@protoc_insertion_point(class_scope:D3.ChallengeRifts.AccountData)
  ))
_sym_db.RegisterMessage(AccountData)


# @@protoc_insertion_point(module_scope)