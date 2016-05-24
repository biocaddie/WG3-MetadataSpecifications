__author__ = 'agbeltran'

import json,os
from jsonschema import validate, FormatChecker, RefResolver, Draft4Validator
from os.path import join


schemasPath = os.path.abspath("../json-schemas")

path = "../examples"

datasetSchema = json.load(open(join(schemasPath,"dataset_schema.json")))
instrumentSchema = json.load(open(join(schemasPath,"instrument_schema.json")))

resolver = RefResolver('file://'+schemasPath+'/'+"dataset_schema.json", datasetSchema) #, base_uri=schemasPath)

validator = Draft4Validator(datasetSchema, resolver=resolver)

#validator.validate(json.load(open(join(path,"PDB-5AEM.json"))), datasetSchema) #, format_checker=FormatChecker())

validator.validate(json.load(open(join(path,"GEO-GSE46964.json"))), datasetSchema) #, format_checker=FormatChecker())

#validator.validate(json.load(open(join(path,"Uniprot-P77967.json"))), datasetSchema) #, format_checker=FormatChecker())


