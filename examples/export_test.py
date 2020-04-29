from reqif_pyxb.ReqIF import *
import reqif_pyxb._xh11d as _xh11d
import reqif_pyxb.driver as driver
import uuid
import pyxb.binding.datatypes as datatypes
from pyxb.utils import six
import xml
from datetime import datetime

from reqif_pyxb.raw._nsgroup import xhtml_div_type # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-ENUMERATION

# Construct the header
a = REQ_IF(
    THE_HEADER=pyxb.BIND(),
    CORE_CONTENT=pyxb.BIND(),
    TOOL_EXTENSIONS=pyxb.BIND(),
)
a.THE_HEADER.REQ_IF_HEADER=REQ_IF_HEADER()

content = REQ_IF_CONTENT()


gen_id = ('x' + str(uuid.uuid1()))
datatype_xhtml = DATATYPE_DEFINITION_XHTML(LONG_NAME="xhtml")
content.add_datatype(datatype_xhtml)
datatype_string = DATATYPE_DEFINITION_STRING(LONG_NAME="String")
content.add_datatype(datatype_string)
datatype_date = DATATYPE_DEFINITION_DATE(LONG_NAME="Date")
content.add_datatype(datatype_date)
datatype_boolean = DATATYPE_DEFINITION_BOOLEAN(LONG_NAME="Boolean")
content.add_datatype(datatype_boolean)
datatype_real = DATATYPE_DEFINITION_REAL(LONG_NAME="Real", MIN=0.0, MAX=100.0, ACCURACY=2)
content.add_datatype(datatype_real)
datatype_unsigned_integer = DATATYPE_DEFINITION_INTEGER(LONG_NAME="Unsigned int", MIN=0, MAX=65535)
content.add_datatype(datatype_unsigned_integer)

# The specification types
text_attribute = ATTRIBUTE_DEFINITION_XHTML(LONG_NAME="Text", datatype=datatype_xhtml)
min_value_attribute = ATTRIBUTE_DEFINITION_REAL(LONG_NAME="Minimum Value", datatype=datatype_real)
max_value_attribute = ATTRIBUTE_DEFINITION_REAL(LONG_NAME="Maximum Value", datatype=datatype_real)
author_attribute = ATTRIBUTE_DEFINITION_STRING(LONG_NAME="Author", datatype=datatype_string)
last_executed_attribute = ATTRIBUTE_DEFINITION_DATE(LONG_NAME="Last executed", datatype=datatype_date)
approved_attribute = ATTRIBUTE_DEFINITION_BOOLEAN(LONG_NAME="Approved", datatype=datatype_boolean)
number_of_subtestcases_attribute = ATTRIBUTE_DEFINITION_INTEGER(LONG_NAME="No. of subtestcases", datatype=datatype_unsigned_integer)

requirement_object_type = SPEC_OBJECT_TYPE(LONG_NAME= "Requirement")
requirement_object_type.add_attribute(text_attribute)
requirement_object_type.add_attribute(author_attribute)
requirement_object_type.add_attribute(approved_attribute)

test_object_type = SPEC_OBJECT_TYPE(LONG_NAME= "Test Case")
test_object_type.add_attribute(text_attribute)
test_object_type.add_attribute(author_attribute)
test_object_type.add_attribute(last_executed_attribute)
test_object_type.add_attribute(number_of_subtestcases_attribute)

configuration_object_type = SPEC_OBJECT_TYPE(LONG_NAME= "Configuration item")
configuration_object_type.add_attribute(text_attribute)
configuration_object_type.add_attribute(min_value_attribute)
configuration_object_type.add_attribute(max_value_attribute)

spec_relation_type = SPEC_RELATION_TYPE(LONG_NAME="selflink")
specification_type = SPECIFICATION_TYPE(LONG_NAME="doc_type")

# a.CORE_CONTENT.REQ_IF_CONTENT.SPEC_TYPES = pyxb.BIND()
content.add_spectype(requirement_object_type)
content.add_spectype(test_object_type)
content.add_spectype(configuration_object_type)
content.add_spectype(spec_relation_type)
content.add_spectype(specification_type)

# The actual requirements
requirement_1 = SPEC_OBJECT(IDENTIFIER="SWRQT-ANGLE_CALCUL", spectype=requirement_object_type)
requirement_1.VALUES.append(ATTRIBUTE_VALUE_XHTML(definition=text_attribute, value="The SW shall calculate an angle"))
requirement_1.VALUES.append(ATTRIBUTE_VALUE_STRING(definition=author_attribute, value="John Doe"))
requirement_1.VALUES.append(ATTRIBUTE_VALUE_BOOLEAN(definition=approved_attribute, value=False))
content.add_specobject(requirement_1)

requirement_2 = SPEC_OBJECT(IDENTIFIER="SWRQT-FIELD_CALCUL", spectype=requirement_object_type)
xml_string = '<div>XY Block Adapter shall translate the Communication to TMN-Block in a bidirectional manner and support all functionalities of a TMN-Block.<br/> <object data="files/rmf-6d04fefa-8350-4870-b2bf-f4923148d064_diagram_20190628-1304.42265.mxg.png" name="diagram_20190628-1304.42265.mxg.png" type="image/png"/></div>'
requirement_2.VALUES.append(ATTRIBUTE_VALUE_XHTML(definition=text_attribute, value=xml_string))
requirement_2.VALUES.append(ATTRIBUTE_VALUE_STRING(definition=author_attribute, value="John Doe"))
requirement_2.VALUES.append(ATTRIBUTE_VALUE_BOOLEAN(definition=approved_attribute, value=True))
content.add_specobject(requirement_2)

# Test cases
utest_1 = SPEC_OBJECT(IDENTIFIER="UTEST-ANGLE_CALCUL", spectype=test_object_type)
utest_1.VALUES.append(ATTRIBUTE_VALUE_XHTML(definition=text_attribute, value="The SW shall test the correct functioning of the angle calculation"))
utest_1.VALUES.append(ATTRIBUTE_VALUE_STRING(definition=author_attribute, value="Jane \n Doe"))
utest_1.VALUES.append(ATTRIBUTE_VALUE_DATE(definition=last_executed_attribute, value=datetime.today()))
utest_1.VALUES.append(ATTRIBUTE_VALUE_INTEGER(definition=number_of_subtestcases_attribute, value=3))
content.add_specobject(utest_1)

utest_2 = SPEC_OBJECT(IDENTIFIER="UTEST-FIELD_CALCUL", spectype=test_object_type)
utest_2.VALUES.append(ATTRIBUTE_VALUE_XHTML(definition=text_attribute, value="The SW shall test the correct functioning of the magnetic field calculation"))
utest_2.VALUES.append(ATTRIBUTE_VALUE_STRING(definition=author_attribute, value="Jane \n Doe"))
utest_2.VALUES.append(ATTRIBUTE_VALUE_DATE(definition=last_executed_attribute, value=datetime.today()))
utest_2.VALUES.append(ATTRIBUTE_VALUE_INTEGER(definition=number_of_subtestcases_attribute, value=0))
content.add_specobject(utest_2)

# Configuration items

config_clockspeed = SPEC_OBJECT(IDENTIFIER="CONFIG-CLOCKSPEED", spectype=configuration_object_type)
config_clockspeed.VALUES.append(ATTRIBUTE_VALUE_XHTML(definition=text_attribute, value="A configuration parameter for configuring the clock speed shall be available"))
config_clockspeed.VALUES.append(ATTRIBUTE_VALUE_REAL(definition=min_value_attribute, value=12.0))
config_clockspeed.VALUES.append(ATTRIBUTE_VALUE_REAL(definition=max_value_attribute, value=36.0))
content.add_specobject(config_clockspeed)

config_pwm_accuracy = SPEC_OBJECT(IDENTIFIER="CONFIG-PWM_ACCURACY", spectype=configuration_object_type)
config_pwm_accuracy.VALUES.append(ATTRIBUTE_VALUE_XHTML(definition=text_attribute, value="A configuration parameter for setting the PWM accuracy (number of bits)"))
config_pwm_accuracy.VALUES.append(ATTRIBUTE_VALUE_REAL(definition=min_value_attribute, value=0.0))
config_pwm_accuracy.VALUES.append(ATTRIBUTE_VALUE_REAL(definition=max_value_attribute, value=16.0))
content.add_specobject(config_pwm_accuracy)

spec = SPECIFICATION(IDENTIFIER="SW_specification", spectype=specification_type, LONG_NAME="SW specification")
spec.add_spec_hierarchy(SPEC_HIERARCHY(spec_object=requirement_1))
spec.add_spec_hierarchy(SPEC_HIERARCHY(spec_object=requirement_2))
content.add_specification(spec)

utp = SPECIFICATION(IDENTIFIER="SW_UTEST_PLAN", spectype=specification_type, LONG_NAME="SW Unit test plan")
utp.add_spec_hierarchy(SPEC_HIERARCHY(spec_object=utest_1))
utp.add_spec_hierarchy(SPEC_HIERARCHY(spec_object=utest_2))
content.add_specification(utp)

config_params = SPECIFICATION(IDENTIFIER="CONFIGURATION_PARAMS", spectype=specification_type, LONG_NAME="Configuration parameters")
config_params.add_spec_hierarchy(SPEC_HIERARCHY(spec_object=config_clockspeed))
config_params.add_spec_hierarchy(SPEC_HIERARCHY(spec_object=config_pwm_accuracy))
content.add_specification(config_params)

# Relationships between requirements
content.add_spec_relation(
    SPEC_RELATION(
        source_spec_object=requirement_1,
        target_spec_object=requirement_2,
        link_type=spec_relation_type))

content.add_spec_relation(
    SPEC_RELATION(
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