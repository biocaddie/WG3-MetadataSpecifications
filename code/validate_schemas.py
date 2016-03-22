__author__ = 'agbeltran'

import json, os
from os import listdir
from os.path import isfile, join
from jsonschema import Draft4Validator

path = os.path.abspath("../json-schemas")
files = [ f for f in listdir(path) if isfile(join(path,f)) ]

#schema = json.load(open(join("../json-schemas","study_schema.json")))
#Draft4Validator.check_schema(schema)

for schemaFile in files:
    print("Validating schema ", schemaFile, "...")
    schema = json.load(open(join(path,schemaFile)))
    Draft4Validator.check_schema(schema)
    print("done.")

