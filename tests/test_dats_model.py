from unittest import TestCase

from dats import dats_model


class DatasetValidation(TestCase):

    def setUp(self):
        self.path = "../json-instances"

    def test_validate_dataset_1(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "SBGrid-179.json", 0))

    def test_validate_dataset_2(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "ClinicalTrials.gov-NCT00001372.json", 2))

    def test_validate_dataset_3(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "PDB-5AEM.json", 2))

    def test_validate_dataset_4(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "Uniprot-P77967.json", 2))

    def test_validate_dataset_5(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "DBgap-phs000979.v1.p1.json", 2))

    def test_validate_dataset_6(self):
        self.assertTrue(dats_model.validate_dataset(self.path, "PDB-5AEM.jsonld", 2))

