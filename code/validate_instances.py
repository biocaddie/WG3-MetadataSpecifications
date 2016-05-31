__author__ = 'agbeltran'

import json,os
from jsonschema import RefResolver, Draft4Validator
from os.path import join


def validate_instance(filename, error_printing):
    schemasPath = os.path.abspath("../json-schemas")
    path = "../examples"
    datasetSchema = json.load(open(join(schemasPath,"dataset_schema.json")))
    instrumentSchema = json.load(open(join(schemasPath,"instrument_schema.json")))
    resolver = RefResolver('file://'+schemasPath+'/'+"dataset_schema.json", datasetSchema) #, base_uri=schemasPath)
    validator = Draft4Validator(datasetSchema, resolver=resolver)
    print("Validating ", filename)
    instance = json.load(open(join(path,filename)))

    if (error_printing == 0):
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        for error in errors:
             print(error.message)
    elif (error_printing == 1):
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        for error in errors:
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                print(list(suberror.schema_path), suberror.message, sep=", ")
    else:
        validator.validate(instance, datasetSchema)

    print("...done")


validate_instance("GEO-GSE46964.json", 1)
validate_instance("ClinicalTrials.gov-NCT00001372.json", 1)
validate_instance("PDB-5AEM.json", 2)
validate_instance("Uniprot-P77967.json", 2)