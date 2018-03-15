import os
from unittest import TestCase

from dats import dats_model


class DatasetValidation(TestCase):

    def setUp(self):
        self.path = os.path.join(os.path.dirname(__file__), "../json-instances")

    def tearDown(self):
        pass

    def test_validate_dats_schemas(self):
        self.assertTrue(dats_model.validate_dats_schemas())

    def test_validate_dats_contexts(self):
        self.assertTrue(dats_model.validate_dats_contexts())

    def test_validate_dataset_1(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "SBGrid-179.json", 0))

    def test_validate_dataset_2(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "ClinicalTrials.gov-NCT00001372.json", 1))

    def test_validate_dataset_3(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "PDB-5AEM.json", 1))

    def test_validate_dataset_4(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "Uniprot-P77967.json", 1))

    def test_validate_dataset_5(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "DBgap-phs000979.v1.p1.json", 1))

    def test_validate_dataset_6(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "PDB-5AEM.jsonld", 1))

    def test_validate_dataset_7(self):
        folder_path = os.path.join(self.path, "index-json")
        self.assertTrue(dats_model.validate_dataset(folder_path, "PRJNA97269-dats.json", 1))

    def test_validate_dataset_8(self):
        folder_path = os.path.join(self.path, "index-json")
        self.assertTrue(dats_model.validate_dataset(folder_path, "output.json", 1))

    def test_validate_dataset_9(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "NYU-10040-dats.json", 1))

    def test_validate_instance(self):
        folder_path = os.path.join(self.path, "ICPSR-Dimensions")
        self.assertTrue(dats_model.validate_instance(folder_path, "Dimension-33581-0001-AQ5.json", "dimension_schema.json", 0) )


   


   

