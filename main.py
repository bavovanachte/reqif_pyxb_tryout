from ReqIF import *
import uuid
import pyxb.binding.datatypes as datatypes

# Construct the header
a = REQ_IF(
    THE_HEADER=pyxb.BIND(),
    CORE_CONTENT=pyxb.BIND(),
    TOOL_EXTENSIONS=pyxb.BIND(),
)
a.THE_HEADER.REQ_IF_HEADER=REQ_IF_HEADER(identifier = "abcd")

content = REQ_IF_CONTENT()


gen_id = ('x' + str(uuid.uuid1()))
datatype_xhtml = DATATYPE_DEFINITION_XHTML(IDENTIFIER=gen_id, LAST_CHANGE=dateTime.today(), LONG_NAME="xhtml")
content.add_datatype(datatype_xhtml)

# The specification types
col1_attribute = ATTRIBUTE_DEFINITION_XHTML(long_name= "Text", datatype=datatype_xhtml)
col2_attribute = ATTRIBUTE_DEFINITION_XHTML(long_name= "Author", datatype=datatype_xhtml)
requirement_object_type = SPEC_OBJECT_TYPE(
    IDENTIFIER = "REQUIREMENT_TYPE",
    LAST_CHANGE = dateTime.today(),
    LONG_NAME= "Requirement",
    SPEC_ATTRIBUTES = pyxb.BIND(col1_attribute, col2_attribute)
)
test_object_type = SPEC_OBJECT_TYPE(
    IDENTIFIER = "TEST_TYPE",
    LAST_CHANGE = dateTime.today(),
    LONG_NAME= "Test Case",
    SPEC_ATTRIBUTES = pyxb.BIND(col1_attribute, col2_attribute)
)
spec_relation_type = SPEC_RELATION_TYPE(IDENTIFIER="_1link_type", LAST_CHANGE=dateTime.today(), LONG_NAME="selflink")
specification_type = SPECIFICATION_TYPE(IDENTIFIER="_doc_type_ref", LAST_CHANGE=dateTime.today(), LONG_NAME="doc_type")

# a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES = pyxb.BIND()
content.add_spectype(requirement_object_type)
content.add_spectype(test_object_type)
content.add_spectype(spec_relation_type)
content.add_spectype(specification_type)


# The actual requirements
requirement_1 = SPEC_OBJECT(identifier="SWRQT-ANGLE_CALCUL", spectype=requirement_object_type)
requirement_1.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_4", THE_VALUE=pyxb.BIND(div="Hallo")))
requirement_1.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_5", THE_VALUE=pyxb.BIND(div="Hallo2")))
content.add_specobject(requirement_1)

requirement_2 = SPEC_OBJECT(identifier="SWRQT-FIELD_CALCUL", spectype=requirement_object_type)
requirement_2.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_4", THE_VALUE=pyxb.BIND(div="Hallo3")))
requirement_2.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_5", THE_VALUE=pyxb.BIND(div="Hallo4")))
content.add_specobject(requirement_2)

# The actual requirements
utest_1 = SPEC_OBJECT(identifier="UTEST-ANGLE_CALCUL", spectype=test_object_type)
utest_1.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_4", THE_VALUE=pyxb.BIND(div="Utest_1")))
utest_1.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_5", THE_VALUE=pyxb.BIND(div="utest_2")))
content.add_specobject(utest_1)

utest_2 = SPEC_OBJECT(identifier="UTEST-FIELD_CALCUL", spectype=test_object_type)
utest_2.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_4", THE_VALUE=pyxb.BIND(div="Utest_3")))
utest_2.VALUES.append(ATTRIBUTE_VALUE_XHTML(DEFINITION="_5", THE_VALUE=pyxb.BIND(div="Utest_4")))
content.add_specobject(utest_2)


spec = SPECIFICATION(identifier="SW_SPEC", spectype=specification_type, long_name="SW specification")
spec.add_spec_hierarchy(SPEC_HIERARCHY(identifier="RANDOM_ID1", spec_object=requirement_1))
spec.add_spec_hierarchy(SPEC_HIERARCHY(identifier="RANDOM_ID2", spec_object=requirement_2))
content.add_specification(spec)

utp = SPECIFICATION(identifier="SW_UTP", spectype=specification_type, long_name="SW Unit test plan")
utp.add_spec_hierarchy(SPEC_HIERARCHY(identifier="RANDOM_ID3", spec_object=utest_1))
utp.add_spec_hierarchy(SPEC_HIERARCHY(identifier="RANDOM_ID4", spec_object=utest_2))
content.add_specification(utp)


# Relationships between requirements
content.add_spec_relation(
    SPEC_RELATION(
        identifier="_self_link",
        source_spec_object=requirement_1,
        target_spec_object=requirement_2,
        link_type=spec_relation_type))

content.add_spec_relation(
    SPEC_RELATION(
        identifier="_self_link",
        source_spec_object=utest_1,
        target_spec_object=utest_2,
        link_type=spec_relation_type))

a.CORE_CONTENT.REQ_IF_CONTENT = content

# print(a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES)
a.TOOL_EXTENSIONS.REQ_IF_TOOL_EXTENSION.append(REQ_IF_TOOL_EXTENSION())

try:
    print(a.toxml());
except Exception as e:
    print(e.details())