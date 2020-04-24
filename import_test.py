from ReqIF import *

pyxb.RequireValidWhenParsing(False)

try:
    reqif_doc = CreateFromDocument(open('RMF_CustomerRequirementsSpecification.reqif').read())
except Exception as e:
    print(e.details())

print(reqif_doc)