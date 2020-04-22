# -*- coding: utf-8 -*-
from raw.ReqIF import *
import raw.ReqIF as raw_reqif


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
    def __init__(self):
        super().__init__(
            SPEC_TYPES = pyxb.BIND(),
            DATATYPES=pyxb.BIND(),
            SPEC_OBJECTS=pyxb.BIND(),
            SPEC_RELATIONS=pyxb.BIND(),
            SPECIFICATIONS=pyxb.BIND(),
            SPEC_RELATION_GROUPS=pyxb.BIND()
        )
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
    def __init__(self, identifier):
        super().__init__(
            IDENTIFIER = identifier,
            COMMENT = "",
            CREATION_TIME = dateTime.today(),
            REPOSITORY_ID = "",
            REQ_IF_TOOL_ID = "",
            REQ_IF_VERSION = "1.0",
            SOURCE_TOOL_ID = "",
            TITLE = ""
        )
raw_reqif.REQ_IF_HEADER._SetSupersedingClass(REQ_IF_HEADER)

