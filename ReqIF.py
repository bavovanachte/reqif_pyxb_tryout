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
from raw.ReqIF import *
import raw.ReqIF as raw_reqif
import uuid


from pyxb.binding.datatypes import dateTime


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
        if self.CREATION_TIME == None:
            self.CREATION_TIME = dateTime.today()
        if self.REQ_IF_VERSION == None:
            self.REQ_IF_VERSION = "1.0"
        if self.TITLE == None:
            self.TITLE = ""
        if self.REPOSITORY_ID == None:
            self.REPOSITORY_ID = ""
        if self.REQ_IF_TOOL_ID == None:
            self.REQ_IF_TOOL_ID = ""
        if self.SOURCE_TOOL_ID == None:
            self.SOURCE_TOOL_ID = ""

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
        if spectype_local:
            self.TYPE=spectype_local
        if self.LAST_CHANGE == None:
            self.LAST_CHANGE = dateTime.today()
        if self.VALUES == None:
            self.VALUES = pyxb.BIND()

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
        if spectype_local:
            self.TYPE=spectype_local
        if self.LAST_CHANGE == None:
            self.LAST_CHANGE = dateTime.today()
        if self.CHILDREN == None:
            self.CHILDREN = pyxb.BIND()

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
        if spec_object_local:
            self.OBJECT=spec_object_local
        if self.LAST_CHANGE == None:
            self.LAST_CHANGE = dateTime.today()

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
        if source_spec_object_local:
            self.SOURCE=source_spec_object_local
        if target_spec_object_local:
            self.TARGET=target_spec_object_local
        if link_type_local:
            self.TYPE=link_type_local
        if self.LAST_CHANGE == None:
            self.LAST_CHANGE = dateTime.today()

raw_reqif.SPEC_RELATION._SetSupersedingClass(SPEC_RELATION)


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
        if datatype_local:
            self.TYPE=datatype_local
        if self.LAST_CHANGE == None:
            self.LAST_CHANGE = dateTime.today()
        if self.IDENTIFIER == None:
            self.IDENTIFIER = ('x' + str(uuid.uuid1()))

raw_reqif.ATTRIBUTE_DEFINITION_XHTML._SetSupersedingClass(ATTRIBUTE_DEFINITION_XHTML)

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
        if definition_local:
            self.DEFINITION=definition_local
        if value_local:
            self.THE_VALUE=pyxb.BIND(div=value)
        else:
            self.THE_VALUE=pyxb.BIND()



    def __init__(self, definition, value):
        if isinstance(definition, str):
            definition_local = definition
        else:
            definition_local = str(definition.IDENTIFIER)
        super().__init__(
            DEFINITION=definition_local,
            THE_VALUE=pyxb.BIND(div=value))

raw_reqif.ATTRIBUTE_VALUE_XHTML._SetSupersedingClass(ATTRIBUTE_VALUE_XHTML)

class SPEC_OBJECT_TYPE(raw_reqif.SPEC_OBJECT_TYPE):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        if self.LAST_CHANGE == None:
            self.LAST_CHANGE = dateTime.today()
        if self.IDENTIFIER == None:
            self.IDENTIFIER = ('x' + str(uuid.uuid1()))
        if self.SPEC_ATTRIBUTES == None:
            self.SPEC_ATTRIBUTES = pyxb.BIND()

    def add_attribute(self, attribute):
        self.SPEC_ATTRIBUTES.append(attribute)

raw_reqif.SPEC_OBJECT_TYPE._SetSupersedingClass(SPEC_OBJECT_TYPE)



# Classes not overridden (yet):
# - RELATION_GROUP
# - RELATION_GROUP_TYPE
# - SPEC_RELATION_TYPE
# - SPECIFICATION_TYPE
# - LOCAL_REF
# - GLOBAL_REF
# - ALTERNATIVE_ID
# - ATTRIBUTE_DEFINITION_BOOLEAN
# - ATTRIBUTE_DEFINITION_DATE
# - ATTRIBUTE_DEFINITION_ENUMERATION
# - ATTRIBUTE_DEFINITION_INTEGER
# - ATTRIBUTE_DEFINITION_REAL
# - ATTRIBUTE_DEFINITION_STRING
# - ATTRIBUTE_VALUE_BOOLEAN
# - ATTRIBUTE_VALUE_DATE
# - ATTRIBUTE_VALUE_ENUMERATION
# - ATTRIBUTE_VALUE_INTEGER
# - ATTRIBUTE_VALUE_REAL
# - ATTRIBUTE_VALUE_STRING
# - DATATYPE_DEFINITION_BOOLEAN
# - DATATYPE_DEFINITION_DATE
# - DATATYPE_DEFINITION_ENUMERATION
# - DATATYPE_DEFINITION_INTEGER
# - DATATYPE_DEFINITION_REAL
# - DATATYPE_DEFINITION_STRING
# - DATATYPE_DEFINITION_XHTML
# - EMBEDDED_VALUE
# - ENUM_VALUE
# - REQ_IF_
# - REQ_IF_TOOL_EXTENSION
# - XHTML_CONTENT
