from ReqIF import *

# Construct the header
a = REQ_IF(
    THE_HEADER=pyxb.BIND(),
    CORE_CONTENT=pyxb.BIND(),
    TOOL_EXTENSIONS=pyxb.BIND(),
)
a.THE_HEADER.REQ_IF_HEADER=REQ_IF_HEADER(identifier = "abcd")

content = REQ_IF_CONTENT()

content.add_datatype(DATATYPE_DEFINITION_XHTML(IDENTIFIER="_2", LAST_CHANGE=dateTime.today(), LONG_NAME="xhtml"))

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
content.add_spectype(requirement_object_type)
content.add_spectype(spec_relation_type)
content.add_spectype(specification_type)


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

content.add_specobject(requirement_6)
content.add_specobject(requirement_7)

spec = SPECIFICATION(
    IDENTIFIER="_ea4773d4-80a0-11ea-851b-185e0f0f4bc8",
    LAST_CHANGE=dateTime.today(),
    TYPE="_doc_type_ref",
    CHILDREN=pyxb.BIND())
spec.CHILDREN.append(SPEC_HIERARCHY(IDENTIFIER="_ea4773d5-80a0-11ea-851b-185e0f0f4bc8", LAST_CHANGE=dateTime.today(), OBJECT="_6"))
spec.CHILDREN.append(SPEC_HIERARCHY(IDENTIFIER="_ea4773d6-80a0-11ea-851b-185e0f0f4bc8", LAST_CHANGE=dateTime.today(), OBJECT="_7"))
content.add_specification(spec)


# Relationships between requirements
content.add_spec_relation(SPEC_RELATION(IDENTIFIER="_self_link", LAST_CHANGE=dateTime.today(), SOURCE="_6", TARGET="_7", TYPE="_1link_type"))

a.CORE_CONTENT.REQ_IF_CONTENT = content

# print(a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES)
a.TOOL_EXTENSIONS.REQ_IF_TOOL_EXTENSION.append(REQ_IF_TOOL_EXTENSION())

try:
    print(a.toxml());
except Exception as e:
    print(e.details())