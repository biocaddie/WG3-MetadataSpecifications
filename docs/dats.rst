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


    * - 
      - ``acknowledges``
      - The grant(s) which funded and supported the work reported by the dataset.
      - Grant
      - 0..n
      - MAY
      - 
      - 

    * - 
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

