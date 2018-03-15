__author__ = 'agbeltran'

import json, os
from jsonschema import RefResolver, Draft4Validator
from os import listdir
from os.path import isfile, join
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATS_schemasPath = os.path.join(os.path.dirname(__file__), "../json-schemas")
DATS_contextsPath = os.path.join(os.path.dirname(__file__), "../json-schemas/contexts")

def validate_instance(path, filename, schema_filename, error_printing):
    try:
        schema_file = open(join(DATS_schemasPath, schema_filename))
        schema = json.load(schema_file)
        resolver = RefResolver('file://' + DATS_schemasPath + '/' + schema_filename, schema)  # , base_uri=schemasPath)
        validator = Draft4Validator(schema, resolver=resolver)
        logger.info("Validating %s against %s ", filename,  schema_filename)

        try:
            instance_file = open(join(path, filename))
            instance = json.load(instance_file)

            if (error_printing == 0):
                errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
                for error in errors:
                    print(error.message)

                if (len(errors) == 0):
                    return True
                else:
                    return False

            elif (error_printing == 1):
                errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
                for error in errors:
                    for suberror in sorted(error.context, key=lambda e: e.schema_path):
                        print(list(suberror.schema_path), suberror.message, sep=", ")

                if (len(errors) == 0):
                    logger.info("...done")
                    return True
                else:
                    return False
            else:
                try:
                    validator.validate(instance, schema)
                    logger.info("...done")
                    return True
                except Exception as e:
                    logger.error(e)
                    return False
        finally:
            instance_file.close()
    finally:
        schema_file.close()


def validate_dataset(path, filename, error_printing):
   return validate_instance(path, filename, "dataset_schema.json", error_printing)


def validate_schema(path, schemaFile):
    try:
        logger.info("Validating schema %s", schemaFile)
        schema_file = open(join(path, schemaFile))
        schema = json.load(schema_file)
        try:
            Draft4Validator.check_schema(schema)
            return True
        except Exception as e:
            logger.error(e)
            return False
        logger.info("done.")
    finally:
        schema_file.close()


def validate_schemas(path):
    result = True
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for schemaFile in files:
        result = result and  validate_schema(path, schemaFile)
    return result

def validate_dats_schemas():
    return validate_schemas(DATS_schemasPath)

def validate_dats_contexts():
    return validate_schemas(DATS_contextsPath)