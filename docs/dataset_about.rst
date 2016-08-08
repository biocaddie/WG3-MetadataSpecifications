#############
Dataset About
#############

Describing what the dataset is about (i.e what was the scope, objective, materials) and providing information about the type of data associated with the given dataset:

* Document the nature of information available in a dataset through the Biocaddie **data type** object.

In this context, the ‘data type’ required to annotate a DataSet should be viewed as a ‘content type’ [terminology needs to be specified]). This encompasses the nature of the signal recorded in a dataset or information content of interest. For instance, gene expression data or phenotypic data, electronic health records….
	Mime type may be used.
		* chemical
		* sequence
		* spectrum
		* audio
		* image
		* video
		* ...	

	but other descriptors may be used such as Biosharing, Scicrunch or re3data category/data domain descriptors.

  * Data aggregation type:
  In the context of DataMed indexing, the information obtained from repositories may correspond to datasets served individually or may correspond to collections or records. As these 2 situations represent a very different metadata context, the Biocaddie DATS model allows to distinguish between the two cases.

		* collection (as in 'collection of instances')
		* singleton (as in ‘individual instance’)

  * Data refinement type: 
To describe the level of data processing associated with the data available from the dataset and its distributions....[terminology needs to be specified])

		* raw data
		* preprocessed data
		* analyzed data
		* summarized data
		* curated data
		* reannotated data
		* ...

* data privacy protection type: (applicable only to human/clinical data)

		* fully identifiable none
		* pseudo-anonymized data
		* fully anonymized data
		* not information available
		* ...


* Document the Material, object, scope and Biological Entities  the dataset is about and their characteristics or properties.

* Document the nature of intervention and Treatment applied to the Material, if any or if applicable.

* Data Types and specific Platform
Currently, in DataMed, datasets can be search according to Data Type (.e.g Proteomics data) and/or by Platform (e.g. Illumina)
DATS provides a mechanism via DataType object to qualify the nature of the data collected in a Dataset. The 4 facets/attributes allow to incrementally specify the type of information contained by the data and how it has been produced

	* data acquisition / method type:
		This attribute allows to indicate the technique or technology , also known sometimes as data modality used to acquire the signal. For instance:

		* ‘crystallography’,
		* ‘mass spectrometry’
		* ‘nucleic acid sequencing’,
		* ‘computational simulation’
		* ‘questionaire based survey’ 
		* 'nuclear magnetic resonance spectroscropy'
		* 'nuclear magnetic resonance imaging'
		* 'questionnaire'
		* ...


	* platform/instrument type
		* Agilent, Bruker,Affymetrix,Illumina,SeaHorse
		* HumanHap550v3.0
		* HumanExome-12 v1.1 BeadChip
		* Sentrix Human-6 Expression BeadChip
		* SureSelect Human All Exon v2 - 44Mb
		* HiSeq 2000
		* ...







