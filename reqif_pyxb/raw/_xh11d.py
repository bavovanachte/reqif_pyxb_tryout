# ./pyxb/bundles/reqif/raw/_xh11d.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0708ac24d1213a8a80348fd6086bedf80db34d5c
# Generated 2020-04-19 18:31:53.477932 by PyXB version 1.2.6 using Python 3.6.10.final.0
# Namespace http://www.w3.org/1999/xhtml/datatypes/ [xmlns:xh11d]

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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/1999/xhtml/datatypes/', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 26, 12)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='\\d+[%]|\\d*\\.\\d+[%]')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)
_module_typeBindings.STD_ANON = STD_ANON

# List simple type: {http://www.w3.org/1999/xhtml/datatypes/}LinkTypes
# superclasses pyxb.binding.datatypes.anySimpleType
class LinkTypes (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.NMTOKEN."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinkTypes')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 34, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.NMTOKEN
LinkTypes._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LinkTypes', LinkTypes)
_module_typeBindings.LinkTypes = LinkTypes

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}MediaDesc
class MediaDesc (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MediaDesc')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 38, 4)
    _Documentation = None
MediaDesc._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MediaDesc', MediaDesc)
_module_typeBindings.MediaDesc = MediaDesc

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 44, 12)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='\\d*\\*')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Number
class Number (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Number')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 52, 4)
    _Documentation = None
Number._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Number', Number)
_module_typeBindings.Number = Number

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Pixels
class Pixels (pyxb.binding.datatypes.nonNegativeInteger):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Pixels')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 56, 4)
    _Documentation = None
Pixels._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Pixels', Pixels)
_module_typeBindings.Pixels = Pixels

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Script
class Script (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Script')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 60, 4)
    _Documentation = None
Script._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Script', Script)
_module_typeBindings.Script = Script

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 66, 12)
    _Documentation = None
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2._CF_pattern.addPattern(pattern='#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_pattern)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Text
class Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 74, 4)
    _Documentation = None
Text._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Text', Text)
_module_typeBindings.Text = Text

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Character
class Character (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Character')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 79, 4)
    _Documentation = None
Character._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Character._InitializeFacetMap(Character._CF_length)
Namespace.addCategoryObject('typeBinding', 'Character', Character)
_module_typeBindings.Character = Character

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Charset
class Charset (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Charset')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 85, 4)
    _Documentation = None
Charset._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Charset', Charset)
_module_typeBindings.Charset = Charset

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}ContentType
class ContentType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 93, 4)
    _Documentation = None
ContentType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ContentType', ContentType)
_module_typeBindings.ContentType = ContentType

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}ContentTypes
class ContentTypes (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContentTypes')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 97, 4)
    _Documentation = None
ContentTypes._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ContentTypes', ContentTypes)
_module_typeBindings.ContentTypes = ContentTypes

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}Datetime
class Datetime (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Datetime')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 101, 4)
    _Documentation = None
Datetime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Datetime', Datetime)
_module_typeBindings.Datetime = Datetime

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}FPI
class FPI (pyxb.binding.datatypes.normalizedString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FPI')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 105, 4)
    _Documentation = None
FPI._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'FPI', FPI)
_module_typeBindings.FPI = FPI

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 112, 8)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.blank = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='_blank', tag='blank')
STD_ANON_3.self = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='_self', tag='self')
STD_ANON_3.parent = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='_parent', tag='parent')
STD_ANON_3.top = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='_top', tag='top')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 120, 8)
    _Documentation = None
STD_ANON_4._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_4._CF_pattern.addPattern(pattern='[a-zA-Z].*')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_pattern)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}LanguageCode
class LanguageCode (pyxb.binding.datatypes.language):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 129, 4)
    _Documentation = None
LanguageCode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LanguageCode', LanguageCode)
_module_typeBindings.LanguageCode = LanguageCode

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}LanguageCodes
class LanguageCodes (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageCodes')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 133, 4)
    _Documentation = None
LanguageCodes._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'LanguageCodes', LanguageCodes)
_module_typeBindings.LanguageCodes = LanguageCodes

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}URI
class URI (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URI')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 137, 4)
    _Documentation = None
URI._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'URI', URI)
_module_typeBindings.URI = URI

# List simple type: {http://www.w3.org/1999/xhtml/datatypes/}URIs
# superclasses pyxb.binding.datatypes.anySimpleType
class URIs (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.anyURI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URIs')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 141, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.anyURI
URIs._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'URIs', URIs)
_module_typeBindings.URIs = URIs

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}URIREF
class URIREF (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URIREF')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 145, 4)
    _Documentation = None
URIREF._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
URIREF._CF_pattern = pyxb.binding.facets.CF_pattern()
URIREF._CF_pattern.addPattern(pattern='#\\c*')
URIREF._InitializeFacetMap(URIREF._CF_minLength,
   URIREF._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'URIREF', URIREF)
_module_typeBindings.URIREF = URIREF

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}MultiLengths
class MultiLengths (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiLengths')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 152, 4)
    _Documentation = None
MultiLengths._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MultiLengths', MultiLengths)
_module_typeBindings.MultiLengths = MultiLengths

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}CDATA
class CDATA (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CDATA')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 156, 4)
    _Documentation = None
CDATA._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'CDATA', CDATA)
_module_typeBindings.CDATA = CDATA

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}CURIE
class CURIE (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CURIE')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 160, 4)
    _Documentation = None
CURIE._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
CURIE._CF_pattern = pyxb.binding.facets.CF_pattern()
CURIE._CF_pattern.addPattern(pattern='(([\\i-[:]][\\c-[:]]*)?:)?.+')
CURIE._InitializeFacetMap(CURIE._CF_minLength,
   CURIE._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CURIE', CURIE)
_module_typeBindings.CURIE = CURIE

# Atomic simple type: {http://www.w3.org/1999/xhtml/datatypes/}SafeCURIE
class SafeCURIE (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SafeCURIE')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 169, 4)
    _Documentation = None
SafeCURIE._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
SafeCURIE._CF_pattern = pyxb.binding.facets.CF_pattern()
SafeCURIE._CF_pattern.addPattern(pattern='\\[(([\\i-[:]][\\c-[:]]*)?:)?.+\\]')
SafeCURIE._InitializeFacetMap(SafeCURIE._CF_minLength,
   SafeCURIE._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SafeCURIE', SafeCURIE)
_module_typeBindings.SafeCURIE = SafeCURIE

# Union simple type: {http://www.w3.org/1999/xhtml/datatypes/}Length
# superclasses pyxb.binding.datatypes.anySimpleType
class Length (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.nonNegativeInteger, STD_ANON."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Length')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 24, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.nonNegativeInteger, STD_ANON, )
Length._CF_pattern = pyxb.binding.facets.CF_pattern()
Length._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Length)
Length._InitializeFacetMap(Length._CF_pattern,
   Length._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Length', Length)
_module_typeBindings.Length = Length

# Union simple type: {http://www.w3.org/1999/xhtml/datatypes/}MultiLength
# superclasses pyxb.binding.datatypes.anySimpleType
class MultiLength (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.nonNegativeInteger, STD_ANON, STD_ANON_."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiLength')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 42, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.nonNegativeInteger, STD_ANON, STD_ANON_, )
MultiLength._CF_pattern = pyxb.binding.facets.CF_pattern()
MultiLength._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MultiLength)
MultiLength._InitializeFacetMap(MultiLength._CF_pattern,
   MultiLength._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MultiLength', MultiLength)
_module_typeBindings.MultiLength = MultiLength

# Union simple type: {http://www.w3.org/1999/xhtml/datatypes/}Color
# superclasses pyxb.binding.datatypes.anySimpleType
class Color (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.NMTOKEN, STD_ANON_2."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Color')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 64, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.NMTOKEN, STD_ANON_2, )
Color._CF_pattern = pyxb.binding.facets.CF_pattern()
Color._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Color)
Color._InitializeFacetMap(Color._CF_pattern,
   Color._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Color', Color)
_module_typeBindings.Color = Color

# List simple type: {http://www.w3.org/1999/xhtml/datatypes/}Charsets
# superclasses pyxb.binding.datatypes.anySimpleType
class Charsets (pyxb.binding.basis.STD_list):

    """Simple type that is a list of Charset."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Charsets')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 89, 4)
    _Documentation = None

    _ItemType = Charset
Charsets._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Charsets', Charsets)
_module_typeBindings.Charsets = Charsets

# Union simple type: {http://www.w3.org/1999/xhtml/datatypes/}FrameTarget
# superclasses pyxb.binding.datatypes.anySimpleType
class FrameTarget (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_3, STD_ANON_4."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FrameTarget')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 110, 4)
    _Documentation = None

    _MemberTypes = ( STD_ANON_3, STD_ANON_4, )
FrameTarget._CF_pattern = pyxb.binding.facets.CF_pattern()
FrameTarget._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FrameTarget)
FrameTarget.blank = '_blank'                      # originally STD_ANON_3.blank
FrameTarget.self = '_self'                        # originally STD_ANON_3.self
FrameTarget.parent = '_parent'                    # originally STD_ANON_3.parent
FrameTarget.top = '_top'                          # originally STD_ANON_3.top
FrameTarget._InitializeFacetMap(FrameTarget._CF_pattern,
   FrameTarget._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FrameTarget', FrameTarget)
_module_typeBindings.FrameTarget = FrameTarget

# List simple type: {http://www.w3.org/1999/xhtml/datatypes/}CURIEs
# superclasses pyxb.binding.datatypes.anySimpleType
class CURIEs (pyxb.binding.basis.STD_list):

    """Simple type that is a list of CURIE."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CURIEs')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 166, 4)
    _Documentation = None

    _ItemType = CURIE
CURIEs._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'CURIEs', CURIEs)
_module_typeBindings.CURIEs = CURIEs

# List simple type: {http://www.w3.org/1999/xhtml/datatypes/}SafeCURIEs
# superclasses pyxb.binding.datatypes.anySimpleType
class SafeCURIEs (pyxb.binding.basis.STD_list):

    """Simple type that is a list of SafeCURIE."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SafeCURIEs')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 175, 4)
    _Documentation = None

    _ItemType = SafeCURIE
SafeCURIEs._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SafeCURIEs', SafeCURIEs)
_module_typeBindings.SafeCURIEs = SafeCURIEs

# Union simple type: {http://www.w3.org/1999/xhtml/datatypes/}URIorSafeCURIE
# superclasses pyxb.binding.datatypes.anySimpleType
class URIorSafeCURIE (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.anyURI, SafeCURIE."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URIorSafeCURIE')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 178, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.anyURI, SafeCURIE, )
URIorSafeCURIE._CF_pattern = pyxb.binding.facets.CF_pattern()
URIorSafeCURIE._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=URIorSafeCURIE)
URIorSafeCURIE._InitializeFacetMap(URIorSafeCURIE._CF_pattern,
   URIorSafeCURIE._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'URIorSafeCURIE', URIorSafeCURIE)
_module_typeBindings.URIorSafeCURIE = URIorSafeCURIE

# List simple type: {http://www.w3.org/1999/xhtml/datatypes/}URIorSafeCURIEs
# superclasses pyxb.binding.datatypes.anySimpleType
class URIorSafeCURIEs (pyxb.binding.basis.STD_list):

    """Simple type that is a list of URIorSafeCURIE."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URIorSafeCURIEs')
    _XSDLocation = pyxb.utils.utility.Location('/home/bvn/Projects/git/pyxb/pyxb/bundles/reqif/schemas/xhtml-datatypes-1.xsd', 181, 4)
    _Documentation = None

    _ItemType = URIorSafeCURIE
URIorSafeCURIEs._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'URIorSafeCURIEs', URIorSafeCURIEs)
_module_typeBindings.URIorSafeCURIEs = URIorSafeCURIEs
