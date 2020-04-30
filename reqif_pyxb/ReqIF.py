""" ReqIf wrapper classes and function for QoL improvements over the PyXB-generated classes

The classes you find in this module provide improvements such as:

- Initialization of anonymous members:
  PyXB is not able to find sensible names for all elements in the xml schema, as some don't have a type defined for them.
  PyXB provides solutions for this through the "pyxb.BIND()" method, but this makes coding with the classes awkward to use.
  Therefore, these pyxb.BIND() statements are hidden as much as possible in these wrapper classes.
  More info on these anonymous types here: http://pyxb.sourceforge.net/userref_usebind.html#creating-instances-of-anonymous-types
- Adding of convenience functions:
  For some of the classes, some convenience functions are added, such as REQ_IF_CONTENT.add_datatype.
- Constructor tweaks:

    + Default values:
      Most of the classes expect an identifier and a timestamp of some sort (required in the XML schema)
      As the user might want to always generate a random ID and and the current timestamp, these are applied as
      default values (but can still be supplied explicitly through the constructor)
    + Allow passing references as objects:
      Many instances have references to other instances (i.e. a specification has a spec_type).
      This linking is done by passing the IDENTIFIER of the instance that needs to be included/linked.
      When using the classes, it's a bit nicer to be able to pass the instance directly as a reference
      instead of extracting the ID and passing that.

  Implementation note: the code around the constructors might look a bit weird at times
  (popping items out of the kwargs, applying default values in the constructor body instead of directly in the arguments,...).
  Main reason for this is that these classes need to be initializable in the same way as their superclasses in order to benefit
  from the CreateFromDocument and CreateFromDOM functions (allowing importing and accessing ReqIf files)
"""

# -*- coding: utf-8 -*-
from .raw.ReqIF import *
from .raw import ReqIF as raw_reqif
import uuid


from pyxb.binding.datatypes import dateTime


def generate_unique_id():
    return ('x' + str(uuid.uuid1()))

# class REQ_IF_x(REQ_IF_):
#     def __init__(self):
#         super().__init__(
#             THE_HEADER=pyxb.BIND(),
#             CORE_CONTENT=pyxb.BIND(),
#             TOOL_EXTENSIONS=pyxb.BIND(),
#         )

# REQ_IF_._SetSupersedingClass(REQ_IF_x)

class REQ_IF_CONTENT(raw_reqif.REQ_IF_CONTENT):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.SPEC_TYPES: self.SPEC_TYPES= pyxb.BIND()
        if not self.DATATYPES: self.DATATYPES=pyxb.BIND()
        if not self.SPEC_OBJECTS: self.SPEC_OBJECTS=pyxb.BIND()
        if not self.SPEC_RELATIONS: self.SPEC_RELATIONS=pyxb.BIND()
        if not self.SPECIFICATIONS: self.SPECIFICATIONS=pyxb.BIND()
        if not self.SPEC_RELATION_GROUPS: self.SPEC_RELATION_GROUPS=pyxb.BIND()

    def add_datatype(self, datatype):
        self.DATATYPES.append(datatype)
    def add_spectype(self, spectype):
        self.SPEC_TYPES.append(spectype)
    def add_specobject(self, specobject):
        self.SPEC_OBJECTS.append(specobject)
    def add_specification(self, specification):
        self.SPECIFICATIONS.append(specification)
    def add_spec_relation(self, spec_relation):
        self.SPEC_RELATIONS.append(spec_relation)
    def add_spec_relation_group(self, spec_relation_group):
        self.SPEC_RELATION_GROUPS.append(spec_relation_group)
raw_reqif.REQ_IF_CONTENT._SetSupersedingClass(REQ_IF_CONTENT)


class REQ_IF_HEADER(raw_reqif.REQ_IF_HEADER):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.CREATION_TIME: self.CREATION_TIME = dateTime.today()
        if not self.REQ_IF_VERSION: self.REQ_IF_VERSION = "1.0"
        if not self.TITLE: self.TITLE = ""
        if not self.REPOSITORY_ID: self.REPOSITORY_ID = ""
        if not self.REQ_IF_TOOL_ID: self.REQ_IF_TOOL_ID = ""
        if not self.SOURCE_TOOL_ID: self.SOURCE_TOOL_ID = ""
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.REQ_IF_HEADER._SetSupersedingClass(REQ_IF_HEADER)

class SPEC_OBJECT(raw_reqif.SPEC_OBJECT):
    def __init__ (self, *args, **kw):
        try:
            spectype = kw.pop('spectype')
            if isinstance(spectype, str):
                spectype_local = spectype
            else:
                spectype_local = str(spectype.IDENTIFIER)
        except KeyError:
            spectype_local = None
            pass
        super().__init__(*args, **kw)
        if spectype_local: self.TYPE=spectype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.VALUES: self.VALUES = pyxb.BIND()

raw_reqif.SPEC_OBJECT._SetSupersedingClass(SPEC_OBJECT)


class SPECIFICATION(raw_reqif.SPECIFICATION):
    def __init__ (self, *args, **kw):
        try:
            spectype = kw.pop('spectype')
            if isinstance(spectype, str):
                spectype_local = spectype
            else:
                spectype_local = str(spectype.IDENTIFIER)
        except KeyError:
            spectype_local = None
            pass
        super().__init__(*args, **kw)
        if spectype_local: self.TYPE=spectype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()
        if not self.CHILDREN: self.CHILDREN = pyxb.BIND()

    def add_spec_hierarchy(self, spec_hierarchy):
        self.CHILDREN.append(spec_hierarchy)

raw_reqif.SPECIFICATION._SetSupersedingClass(SPECIFICATION)


class SPEC_HIERARCHY(raw_reqif.SPEC_HIERARCHY):
    def __init__ (self, *args, **kw):
        try:
            spec_object = kw.pop('spec_object')
            if isinstance(spec_object, str):
                spec_object_local = spec_object
            else:
                spec_object_local = str(spec_object.IDENTIFIER)
        except KeyError:
            spec_object_local = None
            pass
        super().__init__(*args, **kw)
        if spec_object_local: self.OBJECT=spec_object_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.SPEC_HIERARCHY._SetSupersedingClass(SPEC_HIERARCHY)


class SPEC_RELATION(raw_reqif.SPEC_RELATION):
    def __init__ (self, *args, **kw):
        try:
            source_spec_object = kw.pop('source_spec_object')
            if isinstance(source_spec_object, str):
                source_spec_object_local = source_spec_object
            else:
                source_spec_object_local = str(source_spec_object.IDENTIFIER)
        except KeyError:
            source_spec_object_local = None
            pass
        try:
            target_spec_object = kw.pop('target_spec_object')
            if isinstance(target_spec_object, str):
                target_spec_object_local = target_spec_object
            else:
                target_spec_object_local = str(target_spec_object.IDENTIFIER)
        except KeyError:
            target_spec_object_local = None
            pass
        try:
            link_type = kw.pop('link_type')
            if isinstance(link_type, str):
                link_type_local = link_type
            else:
                link_type_local = str(link_type.IDENTIFIER)
        except KeyError:
            link_type_local = None
            pass
        super().__init__(*args, **kw)
        if source_spec_object_local: self.SOURCE=source_spec_object_local
        if target_spec_object_local: self.TARGET=target_spec_object_local
        if link_type_local: self.TYPE=link_type_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.SPEC_RELATION._SetSupersedingClass(SPEC_RELATION)

class SPEC_OBJECT_TYPE(raw_reqif.SPEC_OBJECT_TYPE):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()
        if not self.SPEC_ATTRIBUTES: self.SPEC_ATTRIBUTES = pyxb.BIND()

    def add_attribute(self, attribute):
        self.SPEC_ATTRIBUTES.append(attribute)

raw_reqif.SPEC_OBJECT_TYPE._SetSupersedingClass(SPEC_OBJECT_TYPE)


class SPEC_RELATION_TYPE(raw_reqif.SPEC_RELATION_TYPE):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.SPEC_RELATION_TYPE._SetSupersedingClass(SPEC_RELATION_TYPE)

class SPECIFICATION_TYPE(raw_reqif.SPECIFICATION_TYPE):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.SPECIFICATION_TYPE._SetSupersedingClass(SPECIFICATION_TYPE)

# XHTML values

class DATATYPE_DEFINITION_XHTML(raw_reqif.DATATYPE_DEFINITION_XHTML):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.DATATYPE_DEFINITION_XHTML._SetSupersedingClass(DATATYPE_DEFINITION_XHTML)

class ATTRIBUTE_VALUE_XHTML(raw_reqif.ATTRIBUTE_VALUE_XHTML):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local:
            self.THE_VALUE=pyxb.BIND(div=value_local)
        elif self.THE_VALUE is None:
            self.THE_VALUE=pyxb.BIND()

raw_reqif.ATTRIBUTE_VALUE_XHTML._SetSupersedingClass(ATTRIBUTE_VALUE_XHTML)

class ATTRIBUTE_DEFINITION_XHTML(raw_reqif.ATTRIBUTE_DEFINITION_XHTML):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_XHTML._SetSupersedingClass(ATTRIBUTE_DEFINITION_XHTML)


# String values

class DATATYPE_DEFINITION_STRING(raw_reqif.DATATYPE_DEFINITION_STRING):
    ''' Default MAX_LENGTH=1000 '''
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()
        if not self.MAX_LENGTH: self.MAX_LENGTH = 1000

raw_reqif.DATATYPE_DEFINITION_STRING._SetSupersedingClass(DATATYPE_DEFINITION_STRING)

class ATTRIBUTE_VALUE_STRING(raw_reqif.ATTRIBUTE_VALUE_STRING):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local: self.THE_VALUE=value_local

raw_reqif.ATTRIBUTE_VALUE_STRING._SetSupersedingClass(ATTRIBUTE_VALUE_STRING)

class ATTRIBUTE_DEFINITION_STRING(raw_reqif.ATTRIBUTE_DEFINITION_STRING):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_STRING._SetSupersedingClass(ATTRIBUTE_DEFINITION_STRING)


# Date values

class DATATYPE_DEFINITION_DATE(raw_reqif.DATATYPE_DEFINITION_DATE):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.DATATYPE_DEFINITION_DATE._SetSupersedingClass(DATATYPE_DEFINITION_DATE)

class ATTRIBUTE_VALUE_DATE(raw_reqif.ATTRIBUTE_VALUE_DATE):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local: self.THE_VALUE=value_local

raw_reqif.ATTRIBUTE_VALUE_DATE._SetSupersedingClass(ATTRIBUTE_VALUE_DATE)

class ATTRIBUTE_DEFINITION_DATE(raw_reqif.ATTRIBUTE_DEFINITION_DATE):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_DATE._SetSupersedingClass(ATTRIBUTE_DEFINITION_DATE)

# Boolean values

class DATATYPE_DEFINITION_BOOLEAN(raw_reqif.DATATYPE_DEFINITION_BOOLEAN):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.DATATYPE_DEFINITION_BOOLEAN._SetSupersedingClass(DATATYPE_DEFINITION_BOOLEAN)

class ATTRIBUTE_VALUE_BOOLEAN(raw_reqif.ATTRIBUTE_VALUE_BOOLEAN):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local is not None: self.THE_VALUE=value_local

raw_reqif.ATTRIBUTE_VALUE_BOOLEAN._SetSupersedingClass(ATTRIBUTE_VALUE_BOOLEAN)

class ATTRIBUTE_DEFINITION_BOOLEAN(raw_reqif.ATTRIBUTE_DEFINITION_BOOLEAN):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_BOOLEAN._SetSupersedingClass(ATTRIBUTE_DEFINITION_BOOLEAN)

# REAL values

class DATATYPE_DEFINITION_REAL(raw_reqif.DATATYPE_DEFINITION_REAL):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.DATATYPE_DEFINITION_REAL._SetSupersedingClass(DATATYPE_DEFINITION_REAL)

class ATTRIBUTE_VALUE_REAL(raw_reqif.ATTRIBUTE_VALUE_REAL):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local is not None: self.THE_VALUE=value_local

raw_reqif.ATTRIBUTE_VALUE_REAL._SetSupersedingClass(ATTRIBUTE_VALUE_REAL)

class ATTRIBUTE_DEFINITION_REAL(raw_reqif.ATTRIBUTE_DEFINITION_REAL):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_REAL._SetSupersedingClass(ATTRIBUTE_DEFINITION_REAL)

# Integer values

class DATATYPE_DEFINITION_INTEGER(raw_reqif.DATATYPE_DEFINITION_INTEGER):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.DATATYPE_DEFINITION_INTEGER._SetSupersedingClass(DATATYPE_DEFINITION_INTEGER)

class ATTRIBUTE_VALUE_INTEGER(raw_reqif.ATTRIBUTE_VALUE_INTEGER):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local is not None: self.THE_VALUE=value_local

raw_reqif.ATTRIBUTE_VALUE_INTEGER._SetSupersedingClass(ATTRIBUTE_VALUE_INTEGER)

class ATTRIBUTE_DEFINITION_INTEGER(raw_reqif.ATTRIBUTE_DEFINITION_INTEGER):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_INTEGER._SetSupersedingClass(ATTRIBUTE_DEFINITION_INTEGER)


# Enum values

class ENUM_VALUE(raw_reqif.ENUM_VALUE):
    def __init__ (self, *args, **kw):
        try:
            value_local = kw.pop('value')
        except KeyError:
            value_local = None
            pass
        try:
            key_local = kw.pop('key')
        except KeyError:
            key_local = None
            pass
        super().__init__(*args, **kw)
        if value_local is not None and key_local is not None:
            self.PROPERTIES=pyxb.BIND(EMBEDDED_VALUE(KEY=key_local, OTHER_CONTENT=value_local))
        else:
            self.PROPERTIES=pyxb.BIND()
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()
raw_reqif.ENUM_VALUE._SetSupersedingClass(ENUM_VALUE)

class DATATYPE_DEFINITION_ENUMERATION(raw_reqif.DATATYPE_DEFINITION_ENUMERATION):
    def __init__ (self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()
        if not self.SPECIFIED_VALUES: self.SPECIFIED_VALUES = pyxb.BIND()

    def add_enum_value(self, enum_value):
        self.SPECIFIED_VALUES.append(enum_value)

raw_reqif.DATATYPE_DEFINITION_ENUMERATION._SetSupersedingClass(DATATYPE_DEFINITION_ENUMERATION)

class ATTRIBUTE_VALUE_ENUMERATION(raw_reqif.ATTRIBUTE_VALUE_ENUMERATION):
    def __init__ (self, *args, **kw):
        try:
            definition = kw.pop('definition')
            if isinstance(definition, str):
                definition_local = definition
            else:
                definition_local = str(definition.IDENTIFIER)
        except KeyError:
            definition_local = None
            pass
        try:
            value_local = kw.pop('value')
            if not isinstance(value_local, str):
                value_local = str(value_local.IDENTIFIER)
        except KeyError:
            value_local = None
            pass
        super().__init__(*args, **kw)
        if definition_local: self.DEFINITION=definition_local
        if value_local is not None:
            self.VALUES=pyxb.BIND(value_local)
        else:
            self.VALUES=pyxb.BIND()

raw_reqif.ATTRIBUTE_VALUE_ENUMERATION._SetSupersedingClass(ATTRIBUTE_VALUE_ENUMERATION)

class ATTRIBUTE_DEFINITION_ENUMERATION(raw_reqif.ATTRIBUTE_DEFINITION_ENUMERATION):
    def __init__ (self, *args, **kw):
        try:
            datatype = kw.pop('datatype')
            if isinstance(datatype, str):
                datatype_local = datatype
            else:
                datatype_local = str(datatype.IDENTIFIER)
        except KeyError:
            datatype_local = None
            pass
        super().__init__(*args, **kw)
        if datatype_local: self.TYPE=datatype_local
        if not self.LAST_CHANGE: self.LAST_CHANGE = dateTime.today()
        if not self.IDENTIFIER: self.IDENTIFIER = generate_unique_id()

raw_reqif.ATTRIBUTE_DEFINITION_ENUMERATION._SetSupersedingClass(ATTRIBUTE_DEFINITION_ENUMERATION)

# Classes not overridden (yet):
# - RELATION_GROUP
# - RELATION_GROUP_TYPE
# - ALTERNATIVE_ID
# - XHTML_CONTENT


# Classes that won't be overridden:
# - LOCAL_REF
# - GLOBAL_REF
# - REQ_IF_ --> Not sure how.
# - REQ_IF_TOOL_EXTENSION
