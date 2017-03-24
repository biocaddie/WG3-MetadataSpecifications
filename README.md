[![Build Status](https://travis-ci.org/biocaddie/WG3-MetadataSpecifications.svg?branch=master)](https://travis-ci.org/biocaddie/WG3-MetadataSpecifications/)

# WG3- DATS Model - Metadata Specifications
This repository contains the output of [bioCADDIE WG3 Descriptive Metadata for Datasets](https://biocaddie.org/group/working-group/working-group-3-descriptive-metadata-datasets)., defining the DatA Tag Suite (DATs) model.
The presentations and notes from the WG3 activities can be found at [this website](https://biocaddie.org/workgroup-3-group-links). This repository contains the different versions of the DATS specification.

The (work in progress) documentation about DATS can be found at [readthedocs](http://wg3-metadataspecifications.readthedocs.io).

The material in this repository is distributed under [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

## DATS Pre-print

A preprint on "DATS: the data tag suite to enable discoverability of datasets" can be found at [bioRxiv DOI: 10.1101/103143 ](https://doi.org/10.1101/103143).

## Version 2.1 - [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.62024.svg)](http://dx.doi.org/10.5281/zenodo.62024)

The document provides links to the different appendices files.

* [DATS model version 2.1 (Google Document)](https://docs.google.com/document/d/1hVcYRleE6-dFfn7qbF9Bv1Ohs1kTF6a8OwWUvoZlDto/edit?usp=sharing)
* [DATS model version 2.1 (pdf)](https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/doc/v2.1/DataMedDATSspecificationv2.1-NIH-BD2KbioCADDIE.pdf)



## Version 2.0 - [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.54010.svg)](http://dx.doi.org/10.5281/zenodo.54010)

The document provides links to the different appendices files.

* [DATS model version 2.0 (pdf)](https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/doc/v2.0/DataMedDATSspecificationv2-NIHDB2KbioCADDIE.pdf)

## Version 1.1 - [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.53078.svg)](http://dx.doi.org/10.5281/zenodo.53078)


* [Metadata Specification - version 1.1 - Draft open for comments (doc)] (https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/doc/v1.1/NIH-BS2K-bioCADDIE-WG3-MetadataElements-Specification-v1.1.docx) 

## Version 1.0 - [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.28019.svg)](http://dx.doi.org/10.5281/zenodo.28019)


* [Metadata Specification - version 1.0 (PDF file)](https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/doc/v1.0/WG3MetadataSpecificationv1-NIH-BD2K-bioCADDIE-DataDiscoveryIndex.pdf)
* [Appendix 1 - Metadata Mapping File v1 (Spreadsheet)](https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/doc/v1.0/AppendixI-WG3MetadataMappingFilev1-NIH-BD2K-bioCADDIE-DataDiscoveryIndex.xlsx)
* [Appendix 2 - Metadata Elements File v1 (Spreadsheet)](https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/doc/v1.0/AppendixII-WG3MetadataElementsFilev1-NIH-BD2K-bioCADDIE-DataDiscoveryIndex.xlsx)

## Instructions to execute code

The python code included in the repository validates the DATS JSON schemas and the DATS JSON instances against the schemas.
To execute the code, it is recommended to use a virtual environment, following these steps:

1. If not already installed in your system, first install the virtual environment via `pip`:
   `pip install virtualenv`
2. Create a virtual environment:
   `virtualenv venv`
3. Then, activate the virtual environment:
  `source venv/bin/activate`
4. Install the requirements:
  `pip install -r requirements.txt`
5. Finally, you can inspect and run the tests to validate the DATS schemas and JSON instances against the schemas.
   `python setup.py test`








