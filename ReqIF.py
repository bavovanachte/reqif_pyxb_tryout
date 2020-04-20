# -*- coding: utf-8 -*-
from raw.ReqIF import *


from pyxb.binding.datatypes import dateTime

# Construct the header
a = REQ_IF();
header = REQ_IF_HEADER(
    IDENTIFIER = "abcd",
    COMMENT = "abcd",
    CREATION_TIME = dateTime.today(),
    REPOSITORY_ID = "",
    REQ_IF_TOOL_ID = "",
    REQ_IF_VERSION = "1.0",
    SOURCE_TOOL_ID = "",
    TITLE = "")
a.THE_HEADER = pyxb.BIND(REQ_IF_HEADER=header)

content = REQ_IF_CONTENT(
    SPEC_TYPES = pyxb.BIND(),
    DATATYPES=pyxb.BIND(),
    SPEC_OBJECTS=pyxb.BIND(),
    SPEC_RELATIONS=pyxb.BIND(),
    SPECIFICATIONS=pyxb.BIND(),
    SPEC_RELATION_GROUPS=pyxb.BIND())
a.CORE_CONTENT = pyxb.BIND(REQ_IF_CONTENT=content)

# The specification types
col1_attribute = ATTRIBUTE_DEFINITION_XHTML(IDENTIFIER = "_4", LAST_CHANGE = dateTime.today(), LONG_NAME= "Col1", TYPE="_2")
col2_attribute = ATTRIBUTE_DEFINITION_XHTML(IDENTIFIER = "_5", LAST_CHANGE = dateTime.today(), LONG_NAME= "Col2", TYPE="_2")
requirement_object_type = SPEC_OBJECT_TYPE(
    IDENTIFIER = "_3",
    LAST_CHANGE = dateTime.today(),
    LONG_NAME= "requirement Type",
    SPEC_ATTRIBUTES = pyxb.BIND(col1_attribute, col2_attribute)
)
spec_relation_type = SPEC_RELATION_TYPE(IDENTIFIER="_1link_type", LAST_CHANGE=dateTime.today(), LONG_NAME="selflink")
specification_type = SPECIFICATION_TYPE(IDENTIFIER="_doc_type_ref", LAST_CHANGE=dateTime.today(), LONG_NAME="doc_type")

# a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES = pyxb.BIND()
a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES.append(requirement_object_type)
a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES.append(spec_relation_type)
a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES.append(specification_type)


# The actual requirements
requirement_6 = SPEC_OBJECT(
    IDENTIFIER="_6",
    LAST_CHANGE=dateTime.today(),
    TYPE="_3",
    VALUES=pyxb.BIND())
requirement_6.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_4", THE_VALUE=pyxb.BIND(div="Hallo")))
requirement_6.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_5", THE_VALUE=pyxb.BIND(div="Hallo2")))

requirement_7 = SPEC_OBJECT(
    IDENTIFIER="_7",
    LAST_CHANGE=dateTime.today(),
    TYPE="_3",
    VALUES=pyxb.BIND())
requirement_7.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_4", THE_VALUE=pyxb.BIND(div="Hallo3")))
requirement_7.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_5", THE_VALUE=pyxb.BIND(div="Hallo4")))
a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_OBJECTS.append(requirement_6)
a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_OBJECTS.append(requirement_7)

# Relationships between requirements
a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_RELATIONS.append(SPEC_RELATION(IDENTIFIER="_self_link", LAST_CHANGE=dateTime.today(), SOURCE="_6", TARGET="_7", TYPE="_1link_type"))

# print(a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES)
a.TOOL_EXTENSIONS = pyxb.BIND(REQ_IF_TOOL_EXTENSION())

try:
    print(a.toxml());
except Exception as e:
    print(e.details())