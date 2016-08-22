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

   * - ``dataset``
     - ``title``
     - The name of the dataset, usually one sentence or short description of the dataset.
     - string
     - 1
     - MUST
     - BGUC5
     - DataCite[/resource/titles];DataCite[/resource/titles/title];Schema.org[https://schema.org/headline];HCLS[(dct:title,rdf:langString)]  

   * - ``dataset``
     - ``types``
     - A term, ideally from a controlled terminology, identifying the dataset type or nature of the data, placing it in a typology.
     - DataType
     - ``1..n``
     - ``MUST``
     - BGUC1-1;BGUC1-2;BGUC3-2;BGUC3-3;BGUC5;BGUC5-1;WPUC1;WPUC2;WPUC3;WPUC9-p7;UC1       
     - For example: microscopy imaging, gene expression profile, genomic sequence, fMRI, pathway simulation.

   * - ``dataset``
     - ``creators``
     - The person(s) or organization(s) which contributed to the creation of the dataset.
     - Person or Organization
     - 1..n
     - MUST
     - UC2       
     - 

   * - ``dataset``
     - ``dates``
     - Relevant dates for the dataset, a date must be added, e.g. creation date or last modification date should be added.
     - Date
     - 0..n
     - MAY
     -       
     -     

   * - ``dataset``
     - ``distributions``
     - The distribution(s) by which datasets are made available (for example: mySQL dump).
     - DataSet Distribution
     - ``0..n``
     - ``SHOULD``
     -       
     - 

   * - ``dataset``
     - ``dimensions``
     - The different dimensions (granular components)  making up a dataset.
     - Dimension
     - ``0..n``
     - ``MAY``
     - BGUC2;BGUC5-4     
     -  

   * - ``dataset``
     - ``isCitedBy``
     - The relevant publication(s) describing how the dataset was produced or used.
     - Publication
     - ``0..n``
     - ``MAY``
     - BGUC5-2      
     -  

   * - ``dataset``
     - ``producedBy``
     - A study process which generated a given dataset, if any.
     - Study
     - ``0..1``
     - ``SHOULD``
     -      
     -  

   * - ``dataset``
     - ``isAbout``
     - Different entiies (biological entity, taxonomic information, disease, molecular entity, anatomical part, treatment) associated with this dataset.
     - BiologicalEntity or TaxonomicInformation or Disease or MolecularEntity or AnatomicalPart or Treatment
     - ``0..n``
     - ``SHOULD``
     -       
     -       
