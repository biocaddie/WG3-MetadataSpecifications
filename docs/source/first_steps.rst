#####################
First Steps with DATS
#####################

This document gives an overview of the DATS components from a practical perspective, detailing how DATS may be used to document a specific dataset. 

The main building blocks of the DATS model are defined as "entities", and for convenience purposes they may be compared to "sections" of information in a flat documentation. Each entity has a number of properties that are instantiated either as other entities or as direct entries for documentation that may be structured (e.g., integer, date, URI) or unstructured (string, or free text entries). The DATS model is centered around the *Dataset* entity, which supports most of the relevant information about the data being observed. 

The *Dataset* entity is designed to describe a "set of dimensions" or a "collection of data" that are produced and/or distributed as a whole. First and foremost, it addresses a set of questions that determine the dataset provenance: who, when, what, why, where, and how. By answering these questions each repository will define its own view on what a dataset is, and will represent it as the central piece in the DATS documentation.

*Who* produced the dataset?
-----------------------------

In the Dataset "creators" property, DATS records the *Person* (s) and/or *Organization* (s) associated with the dataset, and supports documenting their roles (e.g., creator, curator, developer, funder, principal investigator).


*When* was the dataset produced?
-------------------------------

DATS records key *Date(s)* in connection with the *Dataset*.

For each *Date* users can identify its type, in relation to a specific event (e.g. creation, update, validation, verification, deprecation of the dataset).

This mechanism of providing a generic *Date* that may be repeated and differentiated by type allows for creating extensions to new types of dates that may be required in specific scenarios but may not be readily available in existing ontologies.


*What* is the dataset about?
----------------------------

The nature of the information available in a dataset is recorded in the DataType entity.

A *DataType* reflects four axes of a dataset's nature: information (what the data is about), method (how the data was generated), platform (the instrumentation, software and reagents used to generate the data), and instrument (the specific device used to generate the data).


*Why* was the data produced?
----------------------------

As a *Dataset* property, the "description" is a textual narrative that usually indicates the dataset's purpose and why it was produced.

In addition, in the extended DATS it is possible to describe the *Study* that produced one, or several related datasets, including
the purpose, objective, or hypothesis that gave origin to the dataset(s) defined as belonging to a study.

Related studies may also be grouped to constitute a series.


*Where* was the dataset produced?
---------------------------------

The Dataset property *spatialCoverage* includes a description of the geography covered by the dataset and/or measured by the dataset's dimensions or variables.

Spatial coverage is instantiated within a *Place* entity, which maps to the entity bearing the same name in schema.org (http://schema.org/Place), to "geoLocation" in the DataCite schema (http://schema.datacite.org/meta/kernel-4.0/) and to "Feature" in GeoJSON (https://tools.ietf.org/html/rfc7946).


*Where* and *How* can the dataset be accessed?
----------------------------------------------

DATS also provides for a comprehensive description of the ways to access a Dataset, including the dataset landing page and/or access URL if available, a description of the type of access (such as download, remote access, remote service, enclave or not available) as well as  any authorization or authetication needed to access the dataset. This information can be entered in the *Access* entity, that is part of *DatasetDistribution* as well as the description of a *DataRepository*.


