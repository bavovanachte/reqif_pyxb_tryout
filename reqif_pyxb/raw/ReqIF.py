# ./pyxb/bundles/reqif/raw/ReqIF.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7d260e1204a98742c478d4bbddd9fcc89ef5ca5b
# Generated 2020-04-19 18:31:53.478204 by PyXB version 1.2.6 using Python 3.6.10.final.0
# Namespace http://www.omg.org/spec/ReqIF/20110401/reqif.xsd

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:46b87c24-825b-11ea-973b-185e0f0f4bc8')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from . import _nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.omg.org/spec/ReqIF/20110401/reqif.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)

from ._nsgroup import REQ_IF # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}REQ-IF
from ._nsgroup import LOCAL_REF # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}LOCAL-REF
from ._nsgroup import GLOBAL_REF # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}GLOBAL-REF
from ._nsgroup import ALTERNATIVE_ID # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ALTERNATIVE-ID
from ._nsgroup import ATTRIBUTE_DEFINITION_BOOLEAN # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-BOOLEAN
from ._nsgroup import CTD_ANON # None
from ._nsgroup import CTD_ANON_ # None
from ._nsgroup import CTD_ANON_2 # None
from ._nsgroup import ATTRIBUTE_DEFINITION_DATE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-DATE
from ._nsgroup import CTD_ANON_3 # None
from ._nsgroup import CTD_ANON_4 # None
from ._nsgroup import CTD_ANON_5 # None
from ._nsgroup import ATTRIBUTE_DEFINITION_ENUMERATION # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-ENUMERATION
from ._nsgroup import CTD_ANON_6 # None
from ._nsgroup import CTD_ANON_7 # None
from ._nsgroup import CTD_ANON_8 # None
from ._nsgroup import ATTRIBUTE_DEFINITION_INTEGER # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-INTEGER
from ._nsgroup import CTD_ANON_9 # None
from ._nsgroup import CTD_ANON_10 # None
from ._nsgroup import CTD_ANON_11 # None
from ._nsgroup import ATTRIBUTE_DEFINITION_REAL # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-REAL
from ._nsgroup import CTD_ANON_12 # None
from ._nsgroup import CTD_ANON_13 # None
from ._nsgroup import CTD_ANON_14 # None
from ._nsgroup import ATTRIBUTE_DEFINITION_STRING # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-STRING
from ._nsgroup import CTD_ANON_15 # None
from ._nsgroup import CTD_ANON_16 # None
from ._nsgroup import CTD_ANON_17 # None
from ._nsgroup import ATTRIBUTE_DEFINITION_XHTML # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-DEFINITION-XHTML
from ._nsgroup import CTD_ANON_18 # None
from ._nsgroup import CTD_ANON_19 # None
from ._nsgroup import CTD_ANON_20 # None
from ._nsgroup import ATTRIBUTE_VALUE_BOOLEAN # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-BOOLEAN
from ._nsgroup import CTD_ANON_21 # None
from ._nsgroup import ATTRIBUTE_VALUE_DATE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-DATE
from ._nsgroup import CTD_ANON_22 # None
from ._nsgroup import ATTRIBUTE_VALUE_ENUMERATION # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-ENUMERATION
from ._nsgroup import CTD_ANON_23 # None
from ._nsgroup import CTD_ANON_24 # None
from ._nsgroup import ATTRIBUTE_VALUE_INTEGER # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-INTEGER
from ._nsgroup import CTD_ANON_25 # None
from ._nsgroup import ATTRIBUTE_VALUE_REAL # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-REAL
from ._nsgroup import CTD_ANON_26 # None
from ._nsgroup import ATTRIBUTE_VALUE_STRING # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-STRING
from ._nsgroup import CTD_ANON_27 # None
from ._nsgroup import ATTRIBUTE_VALUE_XHTML # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ATTRIBUTE-VALUE-XHTML
from ._nsgroup import CTD_ANON_28 # None
from ._nsgroup import DATATYPE_DEFINITION_BOOLEAN # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-BOOLEAN
from ._nsgroup import CTD_ANON_29 # None
from ._nsgroup import DATATYPE_DEFINITION_DATE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-DATE
from ._nsgroup import CTD_ANON_30 # None
from ._nsgroup import DATATYPE_DEFINITION_ENUMERATION # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-ENUMERATION
from ._nsgroup import CTD_ANON_31 # None
from ._nsgroup import CTD_ANON_32 # None
from ._nsgroup import DATATYPE_DEFINITION_INTEGER # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-INTEGER
from ._nsgroup import CTD_ANON_33 # None
from ._nsgroup import DATATYPE_DEFINITION_REAL # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-REAL
from ._nsgroup import CTD_ANON_34 # None
from ._nsgroup import DATATYPE_DEFINITION_STRING # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-STRING
from ._nsgroup import CTD_ANON_35 # None
from ._nsgroup import DATATYPE_DEFINITION_XHTML # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}DATATYPE-DEFINITION-XHTML
from ._nsgroup import CTD_ANON_36 # None
from ._nsgroup import EMBEDDED_VALUE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}EMBEDDED-VALUE
from ._nsgroup import ENUM_VALUE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}ENUM-VALUE
from ._nsgroup import CTD_ANON_37 # None
from ._nsgroup import CTD_ANON_38 # None
from ._nsgroup import RELATION_GROUP # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}RELATION-GROUP
from ._nsgroup import CTD_ANON_39 # None
from ._nsgroup import CTD_ANON_40 # None
from ._nsgroup import CTD_ANON_41 # None
from ._nsgroup import CTD_ANON_42 # None
from ._nsgroup import CTD_ANON_43 # None
from ._nsgroup import RELATION_GROUP_TYPE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}RELATION-GROUP-TYPE
from ._nsgroup import CTD_ANON_44 # None
from ._nsgroup import CTD_ANON_45 # None
from ._nsgroup import REQ_IF_ # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}REQ-IF
from ._nsgroup import CTD_ANON_46 # None
from ._nsgroup import CTD_ANON_47 # None
from ._nsgroup import CTD_ANON_48 # None
from ._nsgroup import REQ_IF_CONTENT # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}REQ-IF-CONTENT
from ._nsgroup import CTD_ANON_49 # None
from ._nsgroup import CTD_ANON_50 # None
from ._nsgroup import CTD_ANON_51 # None
from ._nsgroup import CTD_ANON_52 # None
from ._nsgroup import CTD_ANON_53 # None
from ._nsgroup import CTD_ANON_54 # None
from ._nsgroup import REQ_IF_HEADER # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}REQ-IF-HEADER
from ._nsgroup import SPEC_HIERARCHY # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPEC-HIERARCHY
from ._nsgroup import CTD_ANON_55 # None
from ._nsgroup import CTD_ANON_56 # None
from ._nsgroup import CTD_ANON_57 # None
from ._nsgroup import CTD_ANON_58 # None
from ._nsgroup import SPEC_OBJECT # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPEC-OBJECT
from ._nsgroup import CTD_ANON_59 # None
from ._nsgroup import CTD_ANON_60 # None
from ._nsgroup import CTD_ANON_61 # None
from ._nsgroup import SPEC_OBJECT_TYPE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPEC-OBJECT-TYPE
from ._nsgroup import CTD_ANON_62 # None
from ._nsgroup import CTD_ANON_63 # None
from ._nsgroup import SPEC_RELATION # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPEC-RELATION
from ._nsgroup import CTD_ANON_64 # None
from ._nsgroup import CTD_ANON_65 # None
from ._nsgroup import CTD_ANON_66 # None
from ._nsgroup import CTD_ANON_67 # None
from ._nsgroup import CTD_ANON_68 # None
from ._nsgroup import SPEC_RELATION_TYPE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPEC-RELATION-TYPE
from ._nsgroup import CTD_ANON_69 # None
from ._nsgroup import CTD_ANON_70 # None
from ._nsgroup import SPECIFICATION # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPECIFICATION
from ._nsgroup import CTD_ANON_71 # None
from ._nsgroup import CTD_ANON_72 # None
from ._nsgroup import CTD_ANON_73 # None
from ._nsgroup import CTD_ANON_74 # None
from ._nsgroup import SPECIFICATION_TYPE # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}SPECIFICATION-TYPE
from ._nsgroup import CTD_ANON_75 # None
from ._nsgroup import CTD_ANON_76 # None
from ._nsgroup import REQ_IF_TOOL_EXTENSION # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}REQ-IF-TOOL-EXTENSION
from ._nsgroup import XHTML_CONTENT # {http://www.omg.org/spec/ReqIF/20110401/reqif.xsd}XHTML-CONTENT