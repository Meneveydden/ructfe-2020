# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: office.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='office.proto',
  package='officepb',
  syntax='proto3',
  serialized_options=b'Z\005proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0coffice.proto\x12\x08officepb\"3\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0b\n\x03\x62io\x18\x03 \x01(\t\"d\n\x08\x44ocument\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05token\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1e\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\r.officepb.Ctx\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\"x\n\x03\x43tx\x12%\n\x04vars\x18\x01 \x03(\x0b\x32\x17.officepb.Ctx.VarsEntry\x12\x1d\n\x05\x65xprs\x18\x02 \x03(\x0b\x32\x0e.officepb.Expr\x1a+\n\tVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\"\n\x04\x45xpr\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x65xpr\x18\x02 \x01(\t\">\n\x0fRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0b\n\x03\x62io\x18\x03 \x01(\t\"#\n\x10RegisterResponse\x12\x0f\n\x07session\x18\x01 \x01(\t\".\n\x0cLoginRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\" \n\rLoginResponse\x12\x0f\n\x07session\x18\x01 \x01(\t\",\n\x0bListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"!\n\x0cListResponse\x12\x11\n\tusernames\x18\x01 \x03(\t\"2\n\x15\x43reateDocumentRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x64oc\x18\x02 \x01(\t\"3\n\x16\x43reateDocumentResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05token\x18\x02 \x01(\t\"5\n\x14ListDocumentsRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\")\n\rShortDocument\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\">\n\x15ListDocumentsResponse\x12%\n\x04\x64ocs\x18\x01 \x03(\x0b\x32\x17.officepb.ShortDocument\"@\n\x0e\x45xecuteRequest\x12\x0f\n\x07session\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x0e\n\x06\x64oc_id\x18\x03 \x01(\x03\"#\n\x0f\x45xecuteResponse\x12\x10\n\x08\x65xecuted\x18\x01 \x01(\t\"2\n\x0eTestDocRequest\x12\x0f\n\x07session\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"#\n\x0fTestDocResponse\x12\x10\n\x08\x65xecuted\x18\x01 \x01(\t2\x85\x01\n\x05Users\x12\x43\n\x08Register\x12\x19.officepb.RegisterRequest\x1a\x1a.officepb.RegisterResponse\"\x00\x12\x37\n\x04List\x12\x15.officepb.ListRequest\x1a\x16.officepb.ListResponse\"\x00\x32\xa9\x02\n\tDocuments\x12I\n\x04List\x12\x1e.officepb.ListDocumentsRequest\x1a\x1f.officepb.ListDocumentsResponse\"\x00\x12M\n\x06\x43reate\x12\x1f.officepb.CreateDocumentRequest\x1a .officepb.CreateDocumentResponse\"\x00\x12@\n\x07\x45xecute\x12\x18.officepb.ExecuteRequest\x1a\x19.officepb.ExecuteResponse\"\x00\x12@\n\x07TestDoc\x12\x18.officepb.TestDocRequest\x1a\x19.officepb.TestDocResponse\"\x00\x42\x07Z\x05protob\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='officepb.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='officepb.User.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bio', full_name='officepb.User.bio', index=2,
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
  serialized_start=26,
  serialized_end=77,
)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='officepb.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='officepb.Document.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='officepb.Document.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.Document.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='officepb.Document.context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='officepb.Document.content', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=79,
  serialized_end=179,
)


_CTX_VARSENTRY = _descriptor.Descriptor(
  name='VarsEntry',
  full_name='officepb.Ctx.VarsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='officepb.Ctx.VarsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='officepb.Ctx.VarsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=301,
)

_CTX = _descriptor.Descriptor(
  name='Ctx',
  full_name='officepb.Ctx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vars', full_name='officepb.Ctx.vars', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exprs', full_name='officepb.Ctx.exprs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CTX_VARSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=301,
)


_EXPR = _descriptor.Descriptor(
  name='Expr',
  full_name='officepb.Expr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.Expr.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expr', full_name='officepb.Expr.expr', index=1,
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
  serialized_start=303,
  serialized_end=337,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='officepb.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.RegisterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='officepb.RegisterRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bio', full_name='officepb.RegisterRequest.bio', index=2,
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
  serialized_start=339,
  serialized_end=401,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='officepb.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='officepb.RegisterResponse.session', index=0,
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
  serialized_start=403,
  serialized_end=438,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='officepb.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.LoginRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='officepb.LoginRequest.password', index=1,
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
  serialized_start=440,
  serialized_end=486,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='officepb.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='officepb.LoginResponse.session', index=0,
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
  serialized_start=488,
  serialized_end=520,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='officepb.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='officepb.ListRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='officepb.ListRequest.limit', index=1,
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
  serialized_start=522,
  serialized_end=566,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='officepb.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='usernames', full_name='officepb.ListResponse.usernames', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=568,
  serialized_end=601,
)


_CREATEDOCUMENTREQUEST = _descriptor.Descriptor(
  name='CreateDocumentRequest',
  full_name='officepb.CreateDocumentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.CreateDocumentRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc', full_name='officepb.CreateDocumentRequest.doc', index=1,
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
  serialized_start=603,
  serialized_end=653,
)


_CREATEDOCUMENTRESPONSE = _descriptor.Descriptor(
  name='CreateDocumentResponse',
  full_name='officepb.CreateDocumentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='officepb.CreateDocumentResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='officepb.CreateDocumentResponse.token', index=1,
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
  serialized_start=655,
  serialized_end=706,
)


_LISTDOCUMENTSREQUEST = _descriptor.Descriptor(
  name='ListDocumentsRequest',
  full_name='officepb.ListDocumentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='officepb.ListDocumentsRequest.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='officepb.ListDocumentsRequest.limit', index=1,
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
  serialized_start=708,
  serialized_end=761,
)


_SHORTDOCUMENT = _descriptor.Descriptor(
  name='ShortDocument',
  full_name='officepb.ShortDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='officepb.ShortDocument.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='officepb.ShortDocument.name', index=1,
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
  serialized_start=763,
  serialized_end=804,
)


_LISTDOCUMENTSRESPONSE = _descriptor.Descriptor(
  name='ListDocumentsResponse',
  full_name='officepb.ListDocumentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docs', full_name='officepb.ListDocumentsResponse.docs', index=0,
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
  serialized_start=806,
  serialized_end=868,
)


_EXECUTEREQUEST = _descriptor.Descriptor(
  name='ExecuteRequest',
  full_name='officepb.ExecuteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='officepb.ExecuteRequest.session', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='officepb.ExecuteRequest.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doc_id', full_name='officepb.ExecuteRequest.doc_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=870,
  serialized_end=934,
)


_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='officepb.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='executed', full_name='officepb.ExecuteResponse.executed', index=0,
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
  serialized_start=936,
  serialized_end=971,
)


_TESTDOCREQUEST = _descriptor.Descriptor(
  name='TestDocRequest',
  full_name='officepb.TestDocRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='officepb.TestDocRequest.session', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='officepb.TestDocRequest.content', index=1,
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
  serialized_start=973,
  serialized_end=1023,
)


_TESTDOCRESPONSE = _descriptor.Descriptor(
  name='TestDocResponse',
  full_name='officepb.TestDocResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='executed', full_name='officepb.TestDocResponse.executed', index=0,
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
  serialized_start=1025,
  serialized_end=1060,
)

_DOCUMENT.fields_by_name['context'].message_type = _CTX
_CTX_VARSENTRY.containing_type = _CTX
_CTX.fields_by_name['vars'].message_type = _CTX_VARSENTRY
_CTX.fields_by_name['exprs'].message_type = _EXPR
_LISTDOCUMENTSRESPONSE.fields_by_name['docs'].message_type = _SHORTDOCUMENT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['Ctx'] = _CTX
DESCRIPTOR.message_types_by_name['Expr'] = _EXPR
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['CreateDocumentRequest'] = _CREATEDOCUMENTREQUEST
DESCRIPTOR.message_types_by_name['CreateDocumentResponse'] = _CREATEDOCUMENTRESPONSE
DESCRIPTOR.message_types_by_name['ListDocumentsRequest'] = _LISTDOCUMENTSREQUEST
DESCRIPTOR.message_types_by_name['ShortDocument'] = _SHORTDOCUMENT
DESCRIPTOR.message_types_by_name['ListDocumentsResponse'] = _LISTDOCUMENTSRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteRequest'] = _EXECUTEREQUEST
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
DESCRIPTOR.message_types_by_name['TestDocRequest'] = _TESTDOCREQUEST
DESCRIPTOR.message_types_by_name['TestDocResponse'] = _TESTDOCRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.User)
  })
_sym_db.RegisterMessage(User)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.Document)
  })
_sym_db.RegisterMessage(Document)

Ctx = _reflection.GeneratedProtocolMessageType('Ctx', (_message.Message,), {

  'VarsEntry' : _reflection.GeneratedProtocolMessageType('VarsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CTX_VARSENTRY,
    '__module__' : 'office_pb2'
    # @@protoc_insertion_point(class_scope:officepb.Ctx.VarsEntry)
    })
  ,
  'DESCRIPTOR' : _CTX,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.Ctx)
  })
_sym_db.RegisterMessage(Ctx)
_sym_db.RegisterMessage(Ctx.VarsEntry)

Expr = _reflection.GeneratedProtocolMessageType('Expr', (_message.Message,), {
  'DESCRIPTOR' : _EXPR,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.Expr)
  })
_sym_db.RegisterMessage(Expr)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

CreateDocumentRequest = _reflection.GeneratedProtocolMessageType('CreateDocumentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOCUMENTREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.CreateDocumentRequest)
  })
_sym_db.RegisterMessage(CreateDocumentRequest)

CreateDocumentResponse = _reflection.GeneratedProtocolMessageType('CreateDocumentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOCUMENTRESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.CreateDocumentResponse)
  })
_sym_db.RegisterMessage(CreateDocumentResponse)

ListDocumentsRequest = _reflection.GeneratedProtocolMessageType('ListDocumentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOCUMENTSREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ListDocumentsRequest)
  })
_sym_db.RegisterMessage(ListDocumentsRequest)

ShortDocument = _reflection.GeneratedProtocolMessageType('ShortDocument', (_message.Message,), {
  'DESCRIPTOR' : _SHORTDOCUMENT,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ShortDocument)
  })
_sym_db.RegisterMessage(ShortDocument)

ListDocumentsResponse = _reflection.GeneratedProtocolMessageType('ListDocumentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDOCUMENTSRESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ListDocumentsResponse)
  })
_sym_db.RegisterMessage(ListDocumentsResponse)

ExecuteRequest = _reflection.GeneratedProtocolMessageType('ExecuteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ExecuteRequest)
  })
_sym_db.RegisterMessage(ExecuteRequest)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTERESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.ExecuteResponse)
  })
_sym_db.RegisterMessage(ExecuteResponse)

TestDocRequest = _reflection.GeneratedProtocolMessageType('TestDocRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTDOCREQUEST,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.TestDocRequest)
  })
_sym_db.RegisterMessage(TestDocRequest)

TestDocResponse = _reflection.GeneratedProtocolMessageType('TestDocResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTDOCRESPONSE,
  '__module__' : 'office_pb2'
  # @@protoc_insertion_point(class_scope:officepb.TestDocResponse)
  })
_sym_db.RegisterMessage(TestDocResponse)


DESCRIPTOR._options = None
_CTX_VARSENTRY._options = None

_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='officepb.Users',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1063,
  serialized_end=1196,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='officepb.Users.Register',
    index=0,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='officepb.Users.List',
    index=1,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS


_DOCUMENTS = _descriptor.ServiceDescriptor(
  name='Documents',
  full_name='officepb.Documents',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1199,
  serialized_end=1496,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='officepb.Documents.List',
    index=0,
    containing_service=None,
    input_type=_LISTDOCUMENTSREQUEST,
    output_type=_LISTDOCUMENTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='officepb.Documents.Create',
    index=1,
    containing_service=None,
    input_type=_CREATEDOCUMENTREQUEST,
    output_type=_CREATEDOCUMENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='officepb.Documents.Execute',
    index=2,
    containing_service=None,
    input_type=_EXECUTEREQUEST,
    output_type=_EXECUTERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestDoc',
    full_name='officepb.Documents.TestDoc',
    index=3,
    containing_service=None,
    input_type=_TESTDOCREQUEST,
    output_type=_TESTDOCRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOCUMENTS)

DESCRIPTOR.services_by_name['Documents'] = _DOCUMENTS

# @@protoc_insertion_point(module_scope)
