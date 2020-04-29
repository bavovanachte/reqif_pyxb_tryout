# ./pyxb/bundles/reqif/raw/driver.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5d6f8cadd22252ff307715949ba136120f3c1ac5
# Generated 2020-04-19 18:31:53.478431 by PyXB version 1.2.7-DEV using Python 3.6.10.final.0
# Namespace http://www.w3.org/1999/xhtml

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
_PyXBVersion = '1.2.7-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from . import _nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/1999/xhtml', create_if_missing=True)
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

from ._nsgroup import xhtml_br_type # {http://www.w3.org/1999/xhtml}xhtml.br.type
from ._nsgroup import STD_ANON # None
from ._nsgroup import STD_ANON_ # None
from ._nsgroup import STD_ANON_2 # None
from ._nsgroup import STD_ANON_3 # None
from ._nsgroup import STD_ANON_4 # None
from ._nsgroup import STD_ANON_5 # None
from ._nsgroup import STD_ANON_6 # None
from ._nsgroup import xhtml_address_type # {http://www.w3.org/1999/xhtml}xhtml.address.type
from ._nsgroup import xhtml_blockquote_type # {http://www.w3.org/1999/xhtml}xhtml.blockquote.type
from ._nsgroup import xhtml_pre_type # {http://www.w3.org/1999/xhtml}xhtml.pre.type
from ._nsgroup import xhtml_heading_type # {http://www.w3.org/1999/xhtml}xhtml.heading.type
from ._nsgroup import xhtml_h1_type # {http://www.w3.org/1999/xhtml}xhtml.h1.type
from ._nsgroup import xhtml_h2_type # {http://www.w3.org/1999/xhtml}xhtml.h2.type
from ._nsgroup import xhtml_h3_type # {http://www.w3.org/1999/xhtml}xhtml.h3.type
from ._nsgroup import xhtml_h4_type # {http://www.w3.org/1999/xhtml}xhtml.h4.type
from ._nsgroup import xhtml_h5_type # {http://www.w3.org/1999/xhtml}xhtml.h5.type
from ._nsgroup import xhtml_h6_type # {http://www.w3.org/1999/xhtml}xhtml.h6.type
from ._nsgroup import xhtml_hr_type # {http://www.w3.org/1999/xhtml}xhtml.hr.type
from ._nsgroup import xhtml_div_type # {http://www.w3.org/1999/xhtml}xhtml.div.type
from ._nsgroup import xhtml_p_type # {http://www.w3.org/1999/xhtml}xhtml.p.type
from ._nsgroup import xhtml_edit_type # {http://www.w3.org/1999/xhtml}xhtml.edit.type
from ._nsgroup import xhtml_a_type # {http://www.w3.org/1999/xhtml}xhtml.a.type
from ._nsgroup import xhtml_abbr_type # {http://www.w3.org/1999/xhtml}xhtml.abbr.type
from ._nsgroup import xhtml_acronym_type # {http://www.w3.org/1999/xhtml}xhtml.acronym.type
from ._nsgroup import xhtml_cite_type # {http://www.w3.org/1999/xhtml}xhtml.cite.type
from ._nsgroup import xhtml_code_type # {http://www.w3.org/1999/xhtml}xhtml.code.type
from ._nsgroup import xhtml_dfn_type # {http://www.w3.org/1999/xhtml}xhtml.dfn.type
from ._nsgroup import xhtml_em_type # {http://www.w3.org/1999/xhtml}xhtml.em.type
from ._nsgroup import xhtml_kbd_type # {http://www.w3.org/1999/xhtml}xhtml.kbd.type
from ._nsgroup import xhtml_samp_type # {http://www.w3.org/1999/xhtml}xhtml.samp.type
from ._nsgroup import xhtml_strong_type # {http://www.w3.org/1999/xhtml}xhtml.strong.type
from ._nsgroup import xhtml_var_type # {http://www.w3.org/1999/xhtml}xhtml.var.type
from ._nsgroup import xhtml_q_type # {http://www.w3.org/1999/xhtml}xhtml.q.type
from ._nsgroup import xhtml_InlPres_type # {http://www.w3.org/1999/xhtml}xhtml.InlPres.type
from ._nsgroup import xhtml_span_type # {http://www.w3.org/1999/xhtml}xhtml.span.type
from ._nsgroup import xhtml_dt_type # {http://www.w3.org/1999/xhtml}xhtml.dt.type
from ._nsgroup import xhtml_dd_type # {http://www.w3.org/1999/xhtml}xhtml.dd.type
from ._nsgroup import xhtml_dl_type # {http://www.w3.org/1999/xhtml}xhtml.dl.type
from ._nsgroup import xhtml_li_type # {http://www.w3.org/1999/xhtml}xhtml.li.type
from ._nsgroup import xhtml_ol_type # {http://www.w3.org/1999/xhtml}xhtml.ol.type
from ._nsgroup import xhtml_ul_type # {http://www.w3.org/1999/xhtml}xhtml.ul.type
from ._nsgroup import xhtml_param_type # {http://www.w3.org/1999/xhtml}xhtml.param.type
from ._nsgroup import xhtml_caption_type # {http://www.w3.org/1999/xhtml}xhtml.caption.type
from ._nsgroup import xhtml_object_type # {http://www.w3.org/1999/xhtml}xhtml.object.type
from ._nsgroup import xhtml_td_type # {http://www.w3.org/1999/xhtml}xhtml.td.type
from ._nsgroup import xhtml_th_type # {http://www.w3.org/1999/xhtml}xhtml.th.type
from ._nsgroup import xhtml_tr_type # {http://www.w3.org/1999/xhtml}xhtml.tr.type
from ._nsgroup import xhtml_col_type # {http://www.w3.org/1999/xhtml}xhtml.col.type
from ._nsgroup import xhtml_colgroup_type # {http://www.w3.org/1999/xhtml}xhtml.colgroup.type
from ._nsgroup import xhtml_tbody_type # {http://www.w3.org/1999/xhtml}xhtml.tbody.type
from ._nsgroup import xhtml_tfoot_type # {http://www.w3.org/1999/xhtml}xhtml.tfoot.type
from ._nsgroup import xhtml_thead_type # {http://www.w3.org/1999/xhtml}xhtml.thead.type
from ._nsgroup import xhtml_table_type # {http://www.w3.org/1999/xhtml}xhtml.table.type
