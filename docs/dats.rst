########## 
DATS Model
##########  

.. list-table:: DATS specifications
   :header-rows: 1
   :widths: 15 15 30 15 15 15 15 15  

   * - Entity
     - Property
     - Definition
     - Value(s)
     - Cardinality
     - Requirement Level
     - Relevant Competency Question(s)
     - Notes or Example(s)

   * - ``dataset``
     - ``identifier``
     - Primary identifiers for the dataset.
     - IdentifiersInformation
     - 0..n
     - SHOULD
     - BGUC5
     -

   * - 
     - ``relatedIdentifiers``
     - Related identifiers for the dataset.
     - IdentifiersInformation
     - 0..n
     - SHOULD
     - BGUC5
     - 

   * - 
     - ``alternateIdentifiers``
     - Alternate identifiers for the dataset.
     - AlternateIdentifiersInformation
     - 0..n
     - MAY
     -
     -

   * - 
     - ``title``
     - The name of the dataset, usually one sentence or short description of the dataset.
     - string
     - 1
     - MUST
     - BGUC5
     - DataCite[/resource/titles];DataCite[/resource/titles/title];Schema.org[https://schema.org/headline];HCLS[(dct:title,rdf:langString)]  

   * - 
     - ``types``
     - A term, ideally from a controlled terminology, identifying the dataset type or nature of the data, placing it in a typology.
     - DataType
     - ``1..n``
     - ``MUST``
     - BGUC1-1;BGUC1-2;BGUC3-2;BGUC3-3;BGUC5;BGUC5-1;WPUC1;WPUC2;WPUC3;WPUC9-p7;UC1       
     - For example: microscopy imaging, gene expression profile, genomic sequence, fMRI, pathway simulation.

   * - 
     - ``creators``
     - The person(s) or organization(s) which contributed to the creation of the dataset.
     - Person or Organization
     - 1..n
     - MUST
     - UC2       
     - 

   * - 
     - ``dates``
     - Relevant dates for the dataset, a date must be added, e.g. creation date or last modification date should be added.
     - Date
     - 0..n
     - MAY
     -       
     -     

   * - 
     - ``distributions``
     - The distribution(s) by which datasets are made available (for example: mySQL dump).
     - DataSet Distribution
     - ``0..n``
     - ``SHOULD``
     -       
     - 

   * - 
     - ``dimensions``
     - The different dimensions (granular components)  making up a dataset.
     - Dimension
     - ``0..n``
     - ``MAY``
     - BGUC2;BGUC5-4     
     -  

   * - 
     - ``isCitedBy``
     - The relevant publication(s) describing how the dataset was produced or used.
     - Publication
     - ``0..n``
     - ``MAY``
     - BGUC5-2      
     -  

   * - 
     - ``producedBy``
     - A study process which generated a given dataset, if any.
     - Study
     - ``0..1``
     - ``SHOULD``
     -      
     -  

   * - 
     - ``isAbout``
     - Different entiies (biological entity, taxonomic information, disease, molecular entity, anatomical part, treatment) associated with this dataset.
     - BiologicalEntity or TaxonomicInformation or Disease or MolecularEntity or AnatomicalPart or Treatment
     - ``0..n``
     - ``SHOULD``
     -       
     -       

   * - 
     - ``hasPart``
     - A Dataset that is a subset of this Dataset; Datasets declaring the 'hasPart' relationship are considered a collection of Datasets, the aggregation criteria could be included in the 'description' field.
     - Dataset
     - ``0..n``
     - ``MAY``
     -     
     -   

   * - 
     - ``keywords``
     - Tags associated with the dataset, which will help in its discovery.
     - Annotation
     - ``0..n``
     - ``MAY``
     -     
     -


    * - ````
      - ``acknowledges``
      - The grant(s) which funded and supported the work reported by the dataset.
      - Grant
      - 0..n
      - MAY
      - 
      - 

    * - ````
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``DatasetDistribution``
      - ``identifiers``
      - Primary identifiers for the dataset distribution.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``DatasetDistribution``
      - ``alternateIdentifiers``
      - Alternate identifiers for the dataset distribution.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``DatasetDistribution``
      - ``relatedIdentifiers``
      - Related identifiers for the dataset distribution.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``DatasetDistribution``
      - ``title``
      - "The name of the dataset distribution, usually one sentece or short description of the dataset."
      - string
      - 0..1
      - MAY
      - 
      - 

    * - ``DatasetDistribution``
      - ``description``
      - A textual narrative comprised of one or more statements describing the dataset distribution.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``DatasetDistribution``
      - ``dates``
      - "Relevant dates for the datasets, a date must be added, e.g. creation date or last modification date should be added."
      - Date
      - 1..n
      - MUST
      - 
      - 

    * - ``DatasetDistribution``
      - ``storedIn ``
      - The data repository(ies) hosting the dataset.
      - DataRepository
      - 0..n
      - MAY
      - BGUC1-1;UC2
      - "While from the DDI perspective, every dataset may be coming from a data repository, we put a less strict requirement allowing for datasets available online and not in a repository."

    * - ``DatasetDistribution``
      - ``version``
      - A release point for the dataset when applicable.
      - string
      - 0..1
      - SHOULD
      - WPUC5-p7
      - 

    * - ``DatasetDistribution``
      - ``accessModalities``
      - The information about access modality for the dataset.
      - Access
      - 1..n
      - MUST
      - 
      - 

    * - ``DatasetDistribution``
      - ``licenses``
      - The terms of use of the data standard.
      - License
      - 0..n
      - SHOULD
      - BGUC5-4
      - 

    * - ``DatasetDistribution``
      - ``curationStatus``
      - The level of curation of the dataset distribution.
      - Annotation
      - 0..n
      - MAY
      - 
      - "E.g. manually or authomatic or both, other values such as https://wiki.nci.nih.gov/display/CTRPdoc/Curation+Status+Definitions+-+Include+v4.3.1"

    * - ``DatasetDistribution``
      - ``conformsTo``
      - A data standard whose requirements and constraints are met by the dataset.
      - DataStandard
      - 0..n
      - MAY
      - BGUC5-7;WPUC9-p7
      - 

    * - ``DatasetDistribution``
      - ``format``
      - The technical format of the dataset distribution. Use the file extension or MIME type when possible. (Definition adapted from DataCite)
      - string
      - 0..n
      - MAY
      - 
      - "e.g. PDF, XML, MPG or application/pdf, text/xml, video/mpeg"

    * - ``DatasetDistribution``
      - ``qualifiers``
      - "One or more characteristics of the dataset distribution (e.g. how it relates to other distributions, if the data is raw or processed, compressed or encrypted). "
      - Annotation or CategoryValuesPair
      - 0..n
      - MAY
      - 
      - "e.g. indicate if the distribution is isomorphic (corresponds completely with the dataset), a derivative from the dataset, or is a partial distribution of the dataset. These qualifiers can also indicate if the distribution refers to raw, processed or summarised data. It could also refer to the data being encrypted or compressed."

    * - ``DatasetDistribution``
      - ``size ``
      - The size of the dataset.
      - number
      - 0..1
      - MAY
      - BGUC5-1
      - 

    * - ``DatasetDistribution``
      - ``unit``
      - "The unit of measurement used to estimate the size of the dataset (e.g, petabyte). Ideally, the unit should be coming from a reference controlled terminology."
      - Annotation
      - "1, if size is reported"
      - (MUST)
      - 
      - 

    * - ``DatasetDistribution``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``DataStandard``
      - ````
      - "A format, reporting guideline, terminology. It is used to indicate whether the dataset conforms to a particular community norm or specification."
      - 
      - 
      - 
      - BGUC5-7;UC15;WPUC9-p7
      - 

    * - ``DataStandard``
      - ``identifiers``
      - Primary identifiers for the standard.
      - IdentifiersInformation
      - 0..n
      - SHOULD
      - BGUC5
      - 

    * - ``DataStandard``
      - ``alternateIdentifiers``
      - Alternate identifiers for the standard.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``DataStandard``
      - ``relatedIdentifiers``
      - Related identifiers for the standard.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``DataStandard``
      - ``name``
      - "The name of the standard (e.g. FASTQ, CDISC STDM, ISO8601)"
      - string
      - 1
      - MUST
      - 
      - 

    * - ``DataStandard``
      - ``type``
      - "The nature of the information resource, ideally specified with a controlled vocabulary or ontology (.e.g model or format, vocabulary, reporting guideline)."
      - Annotation
      - 1
      - MUST
      - WPUC9-p7
      - 

    * - ``DataStandard``
      - ``description``
      - A textual narrative comprised of one or more statements describing the data standard.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``DataStandard``
      - ``licenses``
      - The terms of use of the data standard.
      - License
      - 0..n
      - SHOULD
      - BGUC5-4
      - 

    * - ``DataStandard``
      - ``version``
      - A release point for the repository when applicable.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``DataStandard``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``DataRepository``
      - ````
      - A repository or catalog of datasets. It could be a primary repository or a repository that aggregates data existing in other repositories.
      - 
      - 
      - 
      - BGUC1-1;UC2;UC15
      - 

    * - ``DataRepository``
      - ``identifiers``
      - Primary identifiers for the data repository.
      - IdentifiersInformation
      - 0..n
      - SHOULD
      - BGUC5
      - 

    * - ``DataRepository``
      - ``alternateIdentifiers``
      - Alternate identifiers for the data repository.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``DataRepository``
      - ``relatedIdentifiers``
      - Related identifiers for the data repository.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``DataRepository``
      - ``name``
      - The name of the data repository.
      - string
      - 1
      - MUST
      - BGUC1-1;UC2
      - 

    * - ``DataRepository``
      - ``description``
      - A textual narrative comprised of one or more statements describing the data repository.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``DataRepository``
      - ``dates``
      - Relevant dates for the data repository.
      - Date
      - 0..n
      - MAY
      - 
      - 

    * - ``DataRepository``
      - ``scopes``
      - "Information about the nature of the datasets in the repository, ideally from a controlled vocabulary or ontology (e.g. transcription profile, sequence reads, molecular structure, image, DNA sequence, NMR spectra)."
      - Annotation
      - 0..n
      - 1..n
      - SPUC1;SPUC7-2
      - 

    * - ``DataRepository``
      - ``types``
      - "A descriptor (ideally from a controlled vocabulary) providing information about the type of repository, such as primary resource or aggregator."
      - Annotation
      - 0..n
      - SHOULD
      - 
      - 

    * - ``DataRepository``
      - ``licenses``
      - The terms of use of the data repository.
      - License
      - 0..n
      - SHOULD
      - BGUC5-4
      - 

    * - ``DataRepository``
      - ``version``
      - "A release point for the repository, when applicable."
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``DataRepository``
      - ``publishers``
      - The person(s) or organization(s) responsible for the repository and its availability.
      - Person or Organization
      - 0..n
      - SHOULD
      - 
      - 

    * - ``DataRepository``
      - ``aggregatorOf``
      - The DataRepositories aggregated by this repository. This property will be empty for primary repositories.
      - DataRepository
      - 0..n
      - MAY
      - 
      - 

    * - ``DataRepository``
      - ``accessModalities``
      - The information about access modality for the data repository.
      - Access
      - 1..n
      - MAY
      - 
      - 

    * - ``DataRepository``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Software``
      - ````
      - "A digital entity containing sets of instructions and operation, which allows computation and operation of and by computer."
      - 
      - 
      - 
      - SPUC11;SPUC10
      - 

    * - ``Software``
      - ``identifiers``
      - Primary identifiers for the software.
      - IdentifiersInformation
      - 0..n
      - SHOULD
      - BGUC5
      - 

    * - ``Software``
      - ``alternateIdentifiers``
      - Alternate identifiers for the software.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Software``
      - ``relatedIdentifiers``
      - Related identifiers for the software.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Software``
      - ``name``
      - The name of the software.
      - string
      - 1
      - MUST
      - 
      - 

    * - ``Software``
      - ``licenses``
      - The terms of use of the software.
      - License
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Software``
      - ``isUsedBy``
      - The data acquisition activity that makes use of this software.
      - DataAcquisition or DataAnalysis
      - 0..n
      - MAY
      - 
      - 

    * - ``Software``
      - ``manufacturer``
      - The person or organisation that produced the software.
      - Person or Organization
      - 0..1
      - MAY
      - 
      - e.g. Adobe

    * - ``Software``
      - ``version``
      - A release point for the software.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``Software``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Publication``
      - ````
      - A (digital) document made available by a publisher.
      - 
      - 
      - 
      - BGUC5-2;WPUC5-p7;WPUC10-p7;UC2
      - 

    * - ``Publication``
      - ``identifiers``
      - Primary identifiers for the publication.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``Publication``
      - ``alternateIdentifiers``
      - Alternate identifiers for the publication.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Publication``
      - ``relatedIdentifiers``
      - Related identifiers for the publication.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Publication``
      - ``title``
      - "The name of the publication, usually one sentece or short description of the publication."
      - string
      - 1
      - SHOULD
      - 
      - 

    * - ``Publication``
      - ``dates ``
      - "Relevant dates, the date of the publication must be provided. "
      - Date
      - 1..n
      - SHOULD
      - 
      - 

    * - ``Publication``
      - ``type``
      - "Publication type, ideally delegated to an external vocabulary/resource."
      - Annotation
      - 0..1
      - SHOULD
      - 
      - "e.g. book, article, weblog, chapter, review, correspondence"

    * - ``Publication``
      - ``publicationVenue``
      - The name of the publication venue where the document is published if applicable.
      - string
      - 0..1
      - MAY
      - 
      - 

    * - ``Publication``
      - ``authorsList``
      - The list of authors made available as a string (does not allow disambiguation).
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``Publication``
      - ``authors``
      - The person(s) and/or organisation(s) responsible for the publication.
      - Person or Organization
      - 1..n
      - SHOULD
      - BGUC5-6
      - 

    * - ``Publication``
      - ``acknowledges``
      - The grant(s) which funded and supported the work reported by the publication.
      - Grant
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Publication``
      - ``licenses``
      - The terms of use of the publication.
      - License
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Publication``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``IdentifiersInformation``
      - ``identifier``
      - A code uniquely identifying an entity locally to a system or globally.
      - string or IRI
      - 0..n
      - SHOULD
      - BGUC5
      - 

    * - ``IdentifiersInformation``
      - ``identifierSource``
      - The identifier source represents information about the organisation/namespace responsible for minting the identifiers. It must be provided if the identifier is provided.
      - string
      - "1, if identifier is available"
      - (MUST)
      - 
      - 

    * - ``AlternateIdentifiersInformation``
      - ``alternateIdentifier``
      - An identifier or identifiers other than the primary Identifier applied to the resource being registered. (definition from DataCite)
      - string or IRI
      - 0..n
      - MAY
      - 
      - 

    * - ``AlternateIdentifiersInformation``
      - ``alternateIdentifierSource``
      - The identifier source represents information about the organisation/namespace responsible for minting the identifiers. It must be provided if the identifier is provided.
      - string
      - 0..n
      - MAY
      - 
      - 

    * - ``RelatedIdentifiersInformation``
      - ``relatedIdentifier``
      - An identifier of a related resource.
      - string or IRI
      - 
      - MUST
      - 
      - 

    * - ``RelatedIdentifiersInformation``
      - ``relatedIdentifierSource``
      - The identifier source represents information about the organisation/namespace responsible for minting the identifiers. It must be provided if the identifier is provided.
      - string
      - 
      - (MUST)
      - 
      - 

    * - ``RelatedIdentifiersInformation``
      - ``relationType``
      - The type of the relationship corresponding to this identifier.
      - string or IRI
      - 
      - SHOULD
      - 
      - 

    * - ``Annotation``
      - ``value ``
      - A label or value (string or numeric) that might be associated with an ontology term.
      - string or number
      - 1
      - MUST
      - 
      - 

    * - ``Annotation``
      - ``ontologyTermIRI /suggested renaming = ValueIRI``
      - The IRI of an ontology term that corresponds to value.
      - IRI
      - 0..1
      - MAY
      - 
      - 

    * - ``Date``
      - ``date``
      - A date following the ISO8601 standard.
      - date
      - 1
      - MUST 
      - 
      - "The type of date is specified in the dateType field, following the DataCite practice. (change cardinality from 1..n to 1)"

    * - ``Access``
      - ``identifiers``
      - Primary identifiers for the access information.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - 
      - 

    * - ``Access``
      - ``alternateIdentifiers``
      - Alternate identifiers for the access information.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Access``
      - ``relatedIdentifiers``
      - Related identifiers for the access information.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Access``
      - ``landingPage``
      - A web page that contains information about the associated dataset or other research object and a direct link to the object itself.
      - IRI
      - 1
      - MUST
      - 
      - 

    * - ``Access``
      - ``accessURL``
      - "A URL from which the resource (dataset or other research object) can be retrieved, i.e. a direct link to the object itself."
      - IRI
      - 0..1
      - SHOULD
      - 
      - 

    * - ``Access``
      - ``types``
      - "Method to obtain the resource, ideally specified from a controlled vocabulary or ontology."
      - Annotation (see worksheet 'Access Types' for CV defined by WG7)
      - 0..n
      - SHOULD
      - 
      - "download, remote access, remote service, enclave, not available"

    * - ``Access``
      - ``authorizations``
      - Types of verification that accessing the resource is allowed. Authorization occurs before successful authentication and refers to the process of obtaining approval to use a data set. Ideally specified from a controlled vocabulary or ontology.
      - Annotation (see worksheet 'Access Types' for CV defined by WG7)
      - 0..n
      - SHOULD
      - 
      - "none, click license, registration, dual individual, dual institution"

    * - ``Access``
      - ``authentications``
      - "Types of verification of the credentials for accessing the resource, it is the identification process at the time of access. ideally specified from a controlled vocabulary or ontology."
      - Annotation (see worksheet 'Access Types' for CV defined by WG7)
      - 0..n
      - SHOULD
      - 
      - "none, simple login, multiple login"

    * - ``Access``
      - ``licenses``
      - Terms of usage as specified on a license or data use agreement.
      - License
      - 0..n
      - MAY
      - BGUC5-1;BGUC5-4;BGUC5-8
      - 

    * - ``Access``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Grant``
      - ````
      - An allocated sum of funds given by a government or other organization for a particular purpose
      - 
      - 
      - 
      - BGUC5-6
      - 

    * - ``Grant``
      - ``identifiers``
      - Primary identifiers for the grant.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - (change to MUST?)

    * - ``Grant``
      - ``alternateIdentifiers``
      - Alternate identifiers for the grant.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Grant``
      - ``relatedIdentifiers``
      - Related identifiers for the grant.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Grant``
      - ``name``
      - The name of the grant and its funding program.
      - string
      - 1
      - MUST
      - 
      - 

    * - ``Grant``
      - ``funds``
      - The study or dataset supported by the grant.
      - Study or Dataset
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Grant``
      - ``funders``
      - The person(s) or organization(s) which has awarded the funds supporting the project.
      - (Person or Organization) and role funder
      - 1..n
      - MUST
      - BGUC5-6;WPUC7-p7;WPUC8-p7;WPUC10-p7;UC1
      - 

    * - ``Grant``
      - ``awardees``
      - The person(s) or organization(s) which received the funds supporting the project. 
      - Person or Organization
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Grant``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - ExtraProperty
      - 0..n
      - MAY
      - 
      - 

    * - ``License``
      - ````
      - "A legal document giving official permission to do something with a Resource. It is assumed that an external vocabulary will describe with sufficient granularity the permission for redistribution, modification, derivation, reuse, etc. and conditions for citation/acknowledgment."
      - 
      - 
      - 
      - "BGUC5-4,BGUC5-8"
      - 

    * - ``License``
      - ``identifiers``
      - Primary identifiers for the license.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``License``
      - ``alternateIdentifiers``
      - Alternate identifiers for the license.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``License``
      - ``relatedIdentifiers``
      - Related identifiers for the license.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``License``
      - ``name``
      - The name of the license.
      - string
      - 1
      - MUST
      - 
      - 

    * - ``License``
      - ``version``
      - The version of the license.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``License``
      - ``creators``
      - The person(s) or organization(s) responsible for writing the license.
      - Person or Organization
      - 0..n
      - SHOULD
      - 
      - 

    * - ``License``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Dimension``
      - ````
      - "A feature of an entity, i.e. an individual measurable property (both quantitative or qualitative) of the entity being observed"
      - 
      - 
      - 
      - BGUC2;BGUC4;BGUC5-1;BGUC5-4;PB1
      - "e.g. demographic characteristics, quality indicator, access statistics"

    * - ``Dimension``
      - ``identifiers``
      - Primary identifiers for the dimension.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``Dimension``
      - ``alternateIdentifiers``
      - Alternate identifiers for the dimension.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Dimension``
      - ``relatedIdentifiers``
      - Related identifiers for the dimension.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Dimension``
      - ``name``
      - "The name of the dimension measured or observed during the data acquisition process, ideally from a controlled terminology."
      - Annotation
      - 1
      - MUST
      - "BGUC5-10,WPUC3, SPUC6,SPUC1"
      - "e.g. signal intensity, standard deviation"

    * - ``Dimension``
      - ``types``
      - "A term, ideally from a controlled terminology, identifying the nature of the dimension, placing it in a typology."
      - Annotation
      - 1..n
      - MUST
      - 
      - "e.g. continuous, discrete, scalar, ordinal "

    * - ``Dimension``
      - ``partOf``
      - The dataset(s) this dimension belongs to.
      - Dataset
      - 1..n
      - MUST
      - 
      - 

    * - ``Dimension``
      - ``description``
      - A textual narrative comprised of one or more statements describing the dimension.
      - string
      - 0..1
      - SHOULD
      - 
      - 

    * - ``Dimension``
      - ``values``
      - The actual collections of values collected for that dimension.
      - array
      - 0..n
      - SHOULD
      - BGUC2
      - 

    * - ``Dimension``
      - ``unit``
      - "A reference measurement unit associated with scalar dimensions, ideally from a reference controlled terminology."
      - Annotation
      - 0..1
      - MAY
      - 
      - 

    * - ``Dimension``
      - ``isAbout ``
      - "A material or a dataset, which is the object of this dimension (this dimension is about the material - e.g. the heights of the patients - or the dataset - e.g. the standard deviation or the set of outliers or a quality indicator of a dataset)."
      - Dataset or Material
      - 0..n
      - MAY
      - BGUC5-4;WPUC9-p7;PB1
      - 

    * - ``Dimension``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``DataType``
      - ``information``
      - The measurements or facts that the data is about.
      - Annotation
      - 0..1
      - MAY
      - 
      - "e.g. gene expression, protein structure, proteomics, phenotyping."

    * - ``DataType``
      - ``method``
      - The procedure or technology used to generate the information. 
      - Annotation
      - 0..1
      - MAY
      - 
      - "e.g. imaging, microarray, clinical trial."

    * - ``DataType``
      - ``platform``
      - "The set of instruments, software and reagents that are needed to generated the data."
      - Annotation
      - 0..1
      - MAY
      - 
      - "e.g. Affymetrix, NGS, mass spectrometer type"

    * - ``DataType``
      - ``instrument``
      - The specific device used to generate the data.
      - Annotation
      - 0..1
      - MAY
      - 
      - 

    * - ``DataType``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Material``
      - ````
      - "A physical entity, part of collection or used in a study (e.g. patient)"
      - 
      - 
      - 
      - BGUC3-3;BGUC3-5;BGUC5;BGUC5-1;BGUC5-9;BGUC5-11;PB1;SPUC13;WPUC6-p7
      - 

    * - ``Material``
      - ``identifiers``
      - Primary identifiers for the material.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``Material``
      - ``alternateIdentifiers``
      - Alternate identifiers for the material.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Material``
      - ``relatedIdentifiers``
      - Related identifiers for the material.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Material``
      - ``name``
      - The name of the material.
      - string
      - 1
      - MUST
      - 
      - 

    * - ``Material``
      - ``derivesFrom``
      - A material from which this material originated.
      - Material or AnatomicalPart
      - 0..n
      - MAY
      - BGUC2
      - 

    * - ``Material``
      - ``bearerOfDisease``
      - The pathology affecting the material used in the study or refered to in the dataset (ideally from a controlled vocabulary/ontology).
      - Disease
      - 0..n
      - MAY
      - "BGUC1-1;BGUC1-2;BGUC1-3;BGUC5,BGUC5-4,BGUC5-6,BGUC5-8,BGUC-5-9,SPUC7-3,WPUC1"
      - 

    * - ``Material``
      - ``taxonomicInformation``
      - The taxonomic information for this material (ideally specified from a controlled vocabulary/ontology).
      - TaxonomicInformation
      - 0..n
      - MAY
      - BGUC2
      - 

    * - ``Material``
      - ``involvedInBiologicalEntity``
      - A biological process (ideally specified from a controlled vocabulary/ontology) in which the material is involved.
      - BiologicalEntity
      - 0..n
      - MAY
      - BGUC2;BGUC3-1;BGUC3-2;BGUC4;SPUC18
      - 

    * - ``Material``
      - ``characteristics``
      - The characteristic information or attributes denoting the material.
      - Dimension or Material
      - 0..n
      - MAY
      - BGUC2
      - 

    * - ``Material``
      - ``roles``
      - The roles played by a material.
      - Annotation
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Material``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Person``
      - ````
      - A human being.
      - 
      - 
      - 
      - UC2
      - 

    * - ``Person``
      - ``identifiers``
      - Primary identifiers for the person.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``Person``
      - ``alternateIdentifiers``
      - Alternate identifiers for the person.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Person``
      - ``relatedIdentifiers``
      - Related identifiers for the person.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Person``
      - ``fullName``
      - "The first name, any middle names, and surname of a person."
      - string
      - 1
      - SHOULD
      - 
      - 

    * - ``Person``
      - ``firstName``
      - The given name of the person.
      - string
      - 1
      - MAY
      - 
      - 

    * - ``Person``
      - ``middleInitial``
      - The first letter of the person's middle name.
      - string
      - 0..n
      - MAY
      - 
      - 

    * - ``Person``
      - ``lastName``
      - The person's family name.
      - string
      - 1
      - SHOULD
      - 
      - 

    * - ``Person``
      - ``email``
      - An electronic mail address for the person.
      - string (format=email)
      - 0..1
      - SHOULD
      - 
      - 

    * - ``Person``
      - ``affiliations``
      - The organizations to which the person is associated with. 
      - Organization
      - 0..n
      - SHOULD
      - 
      - 

    * - ``Person``
      - ``roles``
      - "The roles assumed by a person, ideally from a controlled vocabulary/ontology."
      - Annotation
      - 0..n
      - MAY
      - "(has_role author) BGUC5-6, UC2"
      - "e.g. author, creator, contributor, awardee, submitter, researcher, patient"

    * - ``Person``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

    * - ``Organization``
      - ``identifiers``
      - Primary identifiers for the organization.
      - IdentifiersInformation
      - 1..n
      - SHOULD
      - BGUC5
      - 

    * - ``Organization``
      - ``alternateIdentifiers``
      - Alternate identifiers for the organization.
      - AlternateIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Organization``
      - ``relatedIdentifiers``
      - Related identifiers for the organization.
      - RelatedIdentifiersInformation
      - 0..n
      - MAY
      - 
      - 

    * - ``Organization``
      - ``name``
      - The name of the organization.
      - string
      - 1
      - MUST
      - 
      - 

    * - ``Organization``
      - ``abbreviation``
      - "The shortname, abbreviation associated to the organization."
      - string
      - 0..1
      - MAY
      - 
      - 

    * - ``Organization``
      - ``postalAddress``
      - "The postal, street address associated to the organization."
      - string
      - 0..1
      - MAY
      - 
      - 

    * - ``Organization``
      - ``roles``
      - "The roles of the organization, ideally from a controlled vocabulary/ontology."
      - Annotation
      - 0..n
      - MAY
      - UC1; SPUC5 
      - "e.g. author, creator, contributor, awardee, submitter, researcher, patient"

    * - ``Organization``
      - ``extraProperties``
      - Extra properties that do not fit in the previous specified attributes. 
      - CategoryValuesPair
      - 0..n
      - MAY
      - 
      - 

