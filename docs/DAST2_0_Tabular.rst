.. list-table::
   :widths: 15 15 30 15 15 15 15
   :header-rows: 1

   * - Entity
     - Property
     - Definition
     - Value(s)
     - Cardinality Requirement Level
     - Relevant Competency Question(s)
     - Notes or Example(s)


   * - ``dataset``
     - ``identifier``
     - Primary identifiers for the dataset.
     - IdentifiersInformation
     - 0..n
     - SHOULD
     - BGUC5

   * - ``dataset``
     - ``alternateIdentifier``
     - Alternate identifiers for the dataset.
     - AlternateIdentifiersInformation
     - 0..n
     - MAY
     - BGUC5

   * - ``dataset``
     - ``Related Identifier``
     - Related Identifier for the dataset.
     - RelatedIdentifierInformation
     - 0..n
     - MAY
     - BGUC5

   * - ``dataset``
     - ``title``
     - The name of the dataset, usually one sentence or short description of the dataset.
     - RelatedIdentifierInformation
     - ``1``
     - ``MUST``
     - BGUC5     