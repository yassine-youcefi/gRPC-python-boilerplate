# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cart.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import product_pb2 as product__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncart.proto\x12\x04\x63\x61rt\x1a\x1bgoogle/protobuf/empty.proto\x1a\rproduct.proto\"S\n\x08\x63\x61rtItem\x12\x12\n\ncartItemId\x18\x01 \x01(\t\x12!\n\x07product\x18\x02 \x01(\x0b\x32\x10.product.product\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"Y\n\x04\x63\x61rt\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x1d\n\x05items\x18\x02 \x03(\x0b\x32\x0e.cart.cartItem\x12\x12\n\ntotalPrice\x18\x03 \x01(\x02\x12\x0e\n\x06status\x18\x04 \x01(\t\"\x18\n\x06\x63\x61rtId\x12\x0e\n\x06\x63\x61rtId\x18\x01 \x01(\t\"\x18\n\x06userId\x12\x0e\n\x06userId\x18\x01 \x01(\t\" \n\ncartItemId\x12\x12\n\ncartItemId\x18\x01 \x01(\t2\xc9\x02\n\x0b\x63\x61rtService\x12\x32\n\x0e\x63reateCartItem\x12\x0e.cart.cartItem\x1a\x10.cart.cartItemId\x12\x32\n\x0eupdateCartItem\x12\x0e.cart.cartItem\x1a\x10.cart.cartItemId\x12+\n\x0fgetCartByUserId\x12\x0c.cart.userId\x1a\n.cart.cart\x12&\n\ncreateCart\x12\n.cart.cart\x1a\x0c.cart.cartId\x12#\n\x07getCart\x12\x0c.cart.cartId\x1a\n.cart.cart\x12$\n\nupdateCart\x12\n.cart.cart\x1a\n.cart.cart\x12\x32\n\ndeleteCart\x12\x0c.cart.cartId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CARTITEM']._serialized_start=64
  _globals['_CARTITEM']._serialized_end=147
  _globals['_CART']._serialized_start=149
  _globals['_CART']._serialized_end=238
  _globals['_CARTID']._serialized_start=240
  _globals['_CARTID']._serialized_end=264
  _globals['_USERID']._serialized_start=266
  _globals['_USERID']._serialized_end=290
  _globals['_CARTITEMID']._serialized_start=292
  _globals['_CARTITEMID']._serialized_end=324
  _globals['_CARTSERVICE']._serialized_start=327
  _globals['_CARTSERVICE']._serialized_end=656
# @@protoc_insertion_point(module_scope)
