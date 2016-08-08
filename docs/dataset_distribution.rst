####################
Dataset Distribution
####################

Where and How (can the dataset be accessed):

- Document DataSet Distribution options. This encompasses specifying:

	- data availability (boolean choice: available, unavailable)
	- data formats or mime-types ([terminology needs to be specified] 'resource: <https://github.com/lukaszsliwa/friendly_mime/blob/master/mimes.csv>_`)
	- data access conditions
	- data compression (boolean choice: compressed, uncompressed)
	- data encryption (boolean choice: encrypted, non-encrypted)
	- data privacy protection (fully identifiable, pseudo-anonymized, full anonymized….[terminology needs to be specified])


The image below provides an graphical overview of how to use Biocaddie DATS objects to encode information about dataset availability in a similar file format but from 3 distinct data repositories, each with it own access modalities.

The three INSDC sequence databases (DDBJ, SRA and ENA) exchange their data and provide the same datasets it in the three sites. Let’s consider an example dataset.

The same Dataset identified by accession number DRP000443 can be accessed through the following 3 access URI pages:
`DDBJ: <http://trace.ddbj.nig.ac.jp/DRASearch/study?acc=DRP000443>_`
`SRA: <http://www.ncbi.nlm.nih.gov/sra/DRP000443>_`
`ENA: <http://www.ebi.ac.uk/ena/data/view/DRP000443>_`

While the distributions use the same Format, the accessURL are different as are the Repository but these distributions are all about the same dataset 


.. image:: ./img/DATS-v2.0-postSanDiego-Meeting-Dataset-Distribution-SRA-examples.png
   :alt: A conceptual map detailing Biocaddie DATS distribution for an nucleic acid sequencing dataset as mirrored by 3 INSDC repositories: NCBI SRA, EBI ENA and DDBJ.	

The block below shows a snippet of a Biocaddie DATS JSON document holding key information about dataset distribution. Note the link to *access information* and *data file format* information.

.. code-block:: json

		 "distributions" : [
		    {
		      "identifiers":
		      [
		        {
		          "identifier" : "1",
		          "identifierScheme": ""
		        }
		      ],
		     "dates": [
		        {
		        "date": "2006-05-16",
		         "type": {
		            "value": "creation",
		            "ontologyTermIRI" : ""
		            }
		         },
		        {
		        "date": "2016-04-13",
		        "type": {
		            "value": "modification",
		            "ontologyTermIRI" : ""
		            }
		    }
		  ],
		      "accessModalities" : [
		        {
		          "landingPage": "http://www.uniprot.org/uniprot/P77967",
		          "accessURL" :  "http://www.uniprot.org/uniprot/P77967.fasta"}
		      ],
		      ``"conformsTo"``: [
		        {
		          "identifiers": [
		            {
		              "identifier": "https://biosharing.org/bsg-000228",
		              "identifierScheme": "BioSharing"
		            }
		          ],
		          "name": ``"FASTA"``,
		          "type": {
		            "value": "format",
		            "ontologyTermIRI" : ""
		            }
		        }
		      ],
		   "storedIn" : [
		        {
		        "identifiers": [
		            {
		              "identifier": "http://uniprot.org/uniprot",
		              "identifierScheme": "http"
		            }
		           ],
		          "relatedIdentifiers": [
		            {
		              "identifier": "https://www.biosharing.org/biodbcore-000544",
		              "identifierScheme": "BioSharing"
		            }
		        ],
		        "name": "the Uniprot Knowledge Base",
		        "homepage" : "http://www.uniprot.org",
		        "license" : [
		            {
		                "name": "Copyrighted by the UniProt Consortium, see http://www.uniprot.org/terms Distributed under the Creative Commons Attribution-NoDerivs License"
		            }
		        ],
		        "types" :[
		                {
		                  "value" : "knowledge base",
		                  "ontologyTermIRI" : ""
		                }
		               ],
		        "version": "116"
		      }
		    ],
		    "size" : "12",
		    "unit" : {
		            "value" : "kilobyte",
		            "ontologyTermIRI" : "http://purl.obolibrary.org/obo/UO_0000234"
		            }
		    }
		]

	


