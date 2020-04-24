from ReqIF import *

pyxb.RequireValidWhenParsing(False)

try:
    reqif_doc = CreateFromDocument(open('RMF_CustomerRequirementsSpecification.reqif').read())
except Exception as e:
    print(e.details())

for spec in reqif_doc.CORE_CONTENT.REQ_IF_CONTENT.SPECIFICATIONS.SPECIFICATION:
    print(spec.LONG_NAME)