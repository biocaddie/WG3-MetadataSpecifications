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
     -
     - DataCite[/resource/titles];DataCite[/resource/titles/title];Schema.org[https://schema.org/headline];HCLS[(dct:title,rdf:langString)]  

   * - ``dataset``
     - ``types``
     - A term, ideally from a controlled terminology, identifying the dataset type or nature of the data, placing it in a typology.
     - DataType
     - ``1..n``
     - ``MUST``
     - BGUC1-1;BGUC1-2;BGUC3-2;BGUC3-3;BGUC5;BGUC5-1;WPUC1;WPUC2;WPUC3;WPUC9-p7;UC1       
     - For example: microscopy imaging, gene expression profile, genomic sequence, fMRI, pathway simulation.
          