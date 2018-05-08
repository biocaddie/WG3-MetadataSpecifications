#####################
First Steps with DATS
#####################

This document offers an overview of the DATS model from a practical perspective, detailing how DATS may be used to document a specific dataset. 

The DATS model is centered around the *`Dataset <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/dataset_schema.json>`_.* entity, which supports most of the relevant information about the data being observed.

The main building blocks of the DATS model are defined as "entities", which and for convenience purposes, may be compared to the different "sections" of information in a flat document.
Each entity has a number of properties that are instantiated either as other entities or as direct entries. For the latter, information may may be structured (e.g., integer, date, URI) or unstructured (string, or free text entries). 
 
First and foremost, *Dataset* entity aims to cater for essential provenance information: who, when, what, why, where, and how. 
By answering these questions, each dataset source will define its own view on what a dataset is. 
The *Dataset* entity is also designed to declare which variables were measured and what type of data was collected. 


*What* is the dataset about?
----------------------------

The nature of the information available in a dataset is recorded in the *DataType* entity.

The DATS *DataType* covers four aspects of a dataset's nature: type of information (what the data is about), method (how the data was generated), platform (the instrumentation, software and reagents used to generate the data), and instrument (the specific device used to generate the data).

The DATS *`Dimension <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/dimension_schema.json>`_.* entity is the object to use for reporting variables measured and for which data have been collected.


*Why* was the data produced?
----------------------------

As a *Dataset* property, the "description" is a textual narrative that typically indicates the dataset's purpose and why it was produced.

In addition, in the extended DATS it is possible to describe the *Study* that produced one, or several related datasets, including
the purpose, objective, or hypothesis that gave origin to the dataset(s) defined as belonging to a study.

Related studies may also be grouped to constitute a series.


Tracking dataset spatial and temporal properties

*Where* was the dataset collected and where was it produced?
------------------------------------------------------------

The DATS Dataset property *spatialCoverage* includes a description of the geography covered by the dataset and/or measured by the dataset's dimensions or variables.

*spatialCoverage* is instantiated within a *`Place <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/place_schema.json>`_.* entity, which maps to the entity bearing the same name in schema.org (http://schema.org/Place), to "geoLocation" in the DataCite schema (http://schema.datacite.org/meta/kernel-4.0/) and to "Feature" in GeoJSON (https://tools.ietf.org/html/rfc7946).


*When* was the dataset produced?
-------------------------------

DATS model provides a *`Date <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/date_info_schema.json>`_.* object to records key *Date(s)* associated with the description of a *Dataset*.

For each *Date*, users have to identify its type, in relation to a specific event (e.g. creation, update, validation, verification, deprecation...).

Such generic mechanism of providing *Date* and temporal information offers flexibility and extensibility. Dates may be repeated and differentiated by type. This allows for extensions to new types of dates that may be required in specific scenarios. The actual definition of the types is delegated to existing ontologies.


*Who* produced the dataset?
-----------------------------

Using the Dataset's "creators" property, DATS records the *`Person <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/person_schema.json>`_.* and/or *`Organization <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/organization_schema.json>`_.* associated with the dataset, and supports documenting their roles (e.g., creator, curator, developer, funder, principal investigator).


*Where* and *How* can the dataset be accessed?
----------------------------------------------

DATS provides for a comprehensive description of the ways to access a Dataset. 
This information can be reported in the *`Access <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/access_schema.json>`_.* entity, that is part of *`DatasetDistribution <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/dataset_distribution_schema.json>`_.* as well as part of the description of a *`DataRepository <https://github.com/biocaddie/WG3-MetadataSpecifications/blob/master/json-schemas/data_repository_schema.json>`_. *.
It covers information such as the dataset landing page and/or access URL if available, a description of the type of access (such as download, remote access, remote service, enclave or not available) as well as any authorization or authentication needed to access the dataset. 


