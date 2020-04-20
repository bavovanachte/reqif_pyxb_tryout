# -*- coding: utf-8 -*-
from raw.ReqIF import *


from pyxb.binding.datatypes import dateTime

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
a.CORE_CONTENT = pyxb.BIND(REQ_IF_CONTENT())
a.TOOL_EXTENSIONS = pyxb.BIND(REQ_IF_TOOL_EXTENSION())

try:
    print(a.toxml());
except Exception as e:
    print(e.details())