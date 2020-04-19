# -*- coding: utf-8 -*-
from raw.ReqIF import *


from pyxb.binding.datatypes import dateTime

a = REQ_IF();
a.THE_HEADER = pyxb.BIND(REQ_IF_HEADER=REQ_IF_HEADER())
a.THE_HEADER.REQ_IF_HEADER.IDENTIFIER = "abcd"
a.THE_HEADER.REQ_IF_HEADER.COMMENT = "abcd"
a.THE_HEADER.REQ_IF_HEADER.CREATION_TIME = dateTime.today()
a.THE_HEADER.REQ_IF_HEADER.REPOSITORY_ID = ""
a.THE_HEADER.REQ_IF_HEADER.REQ_IF_TOOL_ID = ""
a.THE_HEADER.REQ_IF_HEADER.REQ_IF_VERSION = "1.0"
a.THE_HEADER.REQ_IF_HEADER.SOURCE_TOOL_ID = ""
a.THE_HEADER.REQ_IF_HEADER.TITLE = ""
a.CORE_CONTENT = pyxb.BIND(REQ_IF_CONTENT())
a.TOOL_EXTENSIONS = pyxb.BIND(REQ_IF_TOOL_EXTENSION())

try:
    print(a.toxml());
except Exception as e:
    print(e.details())