__author__ = 'agbeltran'

import json,os
from jsonschema import RefResolver, Draft4Validator
from os import listdir
from os.path import isfile, join
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

DATS_schemasPath = os.path.abspath("../json-schemas")

def validate_dataset(path, filename, error_printing):
    datasetSchema = json.load(open(join(DATS_schemasPath,"dataset_schema.json")))
    resolver = RefResolver('file://'+DATS_schemasPath+'/'+"dataset_schema.json", datasetSchema) #, base_uri=schemasPath)
    validator = Draft4Validator(datasetSchema, resolver=resolver)
    logger.info("Validating ", filename)
    instance = json.load(open(join(path,filename)))

    if (error_printing == 0):
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        for error in errors:
             print(error.message)

        if (len(errors)==0):
            return True
        else:
            return False

    elif (error_printing == 1):
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        for error in errors:
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                print(list(suberror.schema_path), suberror.message, sep=", ")

        if (len(errors)==0):
            return True
        else:
            return False
    else:
        try:
            validator.validate(instance, datasetSchema)
            return True
        except Exception as e:
            logger.error(e)
            return False

    logger.info("...done")


def validate_schema(path, schemaFile):
    logger.info("Validating schema ", schemaFile, "...")
    schema = json.load(open(join(path, schemaFile)))
    Draft4Validator.check_schema(schema)
    logger.info("done.")

def validate_dats_schemas():
    files = [f for f in listdir(DATS_schemasPath) if isfile(join(DATS_schemasPath, f))]
    for schemaFile in files:
        logger.info("Validating schema ", schemaFile, "...")
        schema = json.load(open(join(DATS_schemasPath, schemaFile)))
        try:
            Draft4Validator.check_schema(schema)
            return True
        except Exception as e:
            logger.error(e)
            return False
        logger.info("done.")
