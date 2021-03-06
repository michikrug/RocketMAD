# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/buddy/buddy_history_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.data.buddy import buddy_stats_pb2 as pogoprotos_dot_data_dot_buddy_dot_buddy__stats__pb2
from pogoprotos.data import souvenir_pb2 as pogoprotos_dot_data_dot_souvenir__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/buddy/buddy_history_data.proto',
  package='pogoprotos.data.buddy',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.pogoprotos/data/buddy/buddy_history_data.proto\x12\x15pogoprotos.data.buddy\x1a!pogoprotos/enums/pokemon_id.proto\x1a%pogoprotos/data/pokemon_display.proto\x1a\'pogoprotos/inventory/item/item_id.proto\x1a\'pogoprotos/data/buddy/buddy_stats.proto\x1a\x1epogoprotos/data/souvenir.proto\"\x81\x06\n\x10\x42uddyHistoryData\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12/\n\npokedex_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x38\n\x0fpokemon_display\x18\x03 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x18\n\x10hatched_from_egg\x18\x04 \x01(\x08\x12\x10\n\x08nickname\x18\x05 \x01(\t\x12\x1b\n\x13\x63\x61ptured_s2_cell_id\x18\x06 \x01(\x03\x12\x1d\n\x15\x63reation_timestamp_ms\x18\x07 \x01(\x03\x12\x33\n\x08pokeball\x18\x08 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x36\n\x0btotal_stats\x18\t \x01(\x0b\x32!.pogoprotos.data.buddy.BuddyStats\x12\x1d\n\x15\x63urrent_points_earned\x18\n \x01(\x05\x12\x1d\n\x15last_set_timestamp_ms\x18\x0b \x01(\x03\x12\x1f\n\x17last_unset_timestamp_ms\x18\x0c \x01(\x03\x12!\n\x19num_days_spent_with_buddy\x18\r \x01(\x05\x12\x0f\n\x07\x64itched\x18\x0e \x01(\x08\x12\x1f\n\x17original_owner_nickname\x18\x0f \x01(\t\x12\x16\n\x0etraded_time_ms\x18\x10 \x01(\x03\x12\\\n\x13souvenirs_collected\x18\x11 \x03(\x0b\x32?.pogoprotos.data.buddy.BuddyHistoryData.SouvenirsCollectedEntry\x12\x19\n\x11km_candy_progress\x18\x12 \x01(\x02\x1aT\n\x17SouvenirsCollectedEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.pogoprotos.data.Souvenir:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_buddy_dot_buddy__stats__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_souvenir__pb2.DESCRIPTOR,])




_BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY = _descriptor.Descriptor(
  name='SouvenirsCollectedEntry',
  full_name='pogoprotos.data.buddy.BuddyHistoryData.SouvenirsCollectedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.data.buddy.BuddyHistoryData.SouvenirsCollectedEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pogoprotos.data.buddy.BuddyHistoryData.SouvenirsCollectedEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=947,
  serialized_end=1031,
)

_BUDDYHISTORYDATA = _descriptor.Descriptor(
  name='BuddyHistoryData',
  full_name='pogoprotos.data.buddy.BuddyHistoryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.buddy.BuddyHistoryData.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokedex_id', full_name='pogoprotos.data.buddy.BuddyHistoryData.pokedex_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.buddy.BuddyHistoryData.pokemon_display', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hatched_from_egg', full_name='pogoprotos.data.buddy.BuddyHistoryData.hatched_from_egg', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='pogoprotos.data.buddy.BuddyHistoryData.nickname', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='captured_s2_cell_id', full_name='pogoprotos.data.buddy.BuddyHistoryData.captured_s2_cell_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_timestamp_ms', full_name='pogoprotos.data.buddy.BuddyHistoryData.creation_timestamp_ms', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='pogoprotos.data.buddy.BuddyHistoryData.pokeball', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_stats', full_name='pogoprotos.data.buddy.BuddyHistoryData.total_stats', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_points_earned', full_name='pogoprotos.data.buddy.BuddyHistoryData.current_points_earned', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_set_timestamp_ms', full_name='pogoprotos.data.buddy.BuddyHistoryData.last_set_timestamp_ms', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_unset_timestamp_ms', full_name='pogoprotos.data.buddy.BuddyHistoryData.last_unset_timestamp_ms', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_days_spent_with_buddy', full_name='pogoprotos.data.buddy.BuddyHistoryData.num_days_spent_with_buddy', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ditched', full_name='pogoprotos.data.buddy.BuddyHistoryData.ditched', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_owner_nickname', full_name='pogoprotos.data.buddy.BuddyHistoryData.original_owner_nickname', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traded_time_ms', full_name='pogoprotos.data.buddy.BuddyHistoryData.traded_time_ms', index=15,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='souvenirs_collected', full_name='pogoprotos.data.buddy.BuddyHistoryData.souvenirs_collected', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='km_candy_progress', full_name='pogoprotos.data.buddy.BuddyHistoryData.km_candy_progress', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=1031,
)

_BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY.fields_by_name['value'].message_type = pogoprotos_dot_data_dot_souvenir__pb2._SOUVENIR
_BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY.containing_type = _BUDDYHISTORYDATA
_BUDDYHISTORYDATA.fields_by_name['pokedex_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_BUDDYHISTORYDATA.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_BUDDYHISTORYDATA.fields_by_name['pokeball'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_BUDDYHISTORYDATA.fields_by_name['total_stats'].message_type = pogoprotos_dot_data_dot_buddy_dot_buddy__stats__pb2._BUDDYSTATS
_BUDDYHISTORYDATA.fields_by_name['souvenirs_collected'].message_type = _BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY
DESCRIPTOR.message_types_by_name['BuddyHistoryData'] = _BUDDYHISTORYDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyHistoryData = _reflection.GeneratedProtocolMessageType('BuddyHistoryData', (_message.Message,), dict(

  SouvenirsCollectedEntry = _reflection.GeneratedProtocolMessageType('SouvenirsCollectedEntry', (_message.Message,), dict(
    DESCRIPTOR = _BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY,
    __module__ = 'pogoprotos.data.buddy.buddy_history_data_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.buddy.BuddyHistoryData.SouvenirsCollectedEntry)
    ))
  ,
  DESCRIPTOR = _BUDDYHISTORYDATA,
  __module__ = 'pogoprotos.data.buddy.buddy_history_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.buddy.BuddyHistoryData)
  ))
_sym_db.RegisterMessage(BuddyHistoryData)
_sym_db.RegisterMessage(BuddyHistoryData.SouvenirsCollectedEntry)


_BUDDYHISTORYDATA_SOUVENIRSCOLLECTEDENTRY._options = None
# @@protoc_insertion_point(module_scope)
