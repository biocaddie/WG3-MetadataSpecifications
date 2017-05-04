#####################
First Steps with DATS
#####################

This document gives an overview of the DATS components from a practical perspective, i.e. considering how DATS is used to describe a specific dataset considering a set of questions that determine the dataset provenance. These questions identify descriptions of the dataset related to who, when, what, why and where. Each repository will define its own view on what a dataset is and DATS represents such dataset as the main entity.

*Who* produced the dataset:
-----------------------------

DATS records the *Person* (s) and *Organization* (s) associated with the dataset.

In addition, it supports documenting their roles (e.g. creator, curator, developer, funder, principal investigator)


*When* was the data produced:
-------------------------------

DATS records key *Date*(s) about the *Dataset*.

Each *Date* can specify its type, related to the event related to the key date (e.g. creation, update, validation, verification, deprecation of the dataset).

This mechanism of providing a generic *Date* indicating its type allows for extensions to new types of dates, which may be required in specific scenarios.


*What* is the dataset about:
----------------------------

DATS records the nature of information available in a dataset using the *types* property through the data type object.

A *DataType* reflects four axes of the dataset nature: information, method, platform and instrument.


*Why* was the data produced:
----------------------------

DATS supports to document a description of the dataset, which would usually indicate its purpose and why it was produced.

In addition, in the extended DATS it is possible to describe the the *Study* that yielded the datasets, including
the purpose, objective or hypothesis that gave origin to the dataset.


*Where* the dataset was produced:
---------------------------------

The Dataset property *spatialCoverage* allows to describe the geographical extension and span covered by the dataset and/or measured by the dimension or variables.

The spatial coverage is represented with a *Place* entity. *Place* corresponds to the entity with the same name in schema.org (http://schema.org/Place), to geoLocation in DataCite schema (http://schema.datacite.org/meta/kernel-4.0/) and to Feature in GeoJSON (https://tools.ietf.org/html/rfc7946).


*Where* and *How* the dataset can be accessed:
----------------------------------------------

DATS also supports to give a comprehensive description on the ways of accessing a Dataset, including the dataset landing page and/or access URL if available, a description of the type of access (such as download, remote access, remote service, enclave or not available) as well as  any authorization or authetication information to access the dataset.


