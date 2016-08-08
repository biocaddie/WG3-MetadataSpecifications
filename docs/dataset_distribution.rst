####################
Dataset Distribution
####################

Where and How (can the dataset be accessed):

- Document DataSet Distribution options. This encompasses specifying:

	- data availability (boolean choice: available, unavailable)
	- data formats or mime-types ([terminology needs to be specified] resource:https://github.com/lukaszsliwa/friendly_mime/blob/master/mimes.csv)
	- data access conditions
	- data compression (boolean choice: compressed, uncompressed)
	- data encryption (boolean choice: encrypted, non-encrypted)
	- data privacy protection (fully identifiable, pseudo-anonymized, full anonymized….[terminology needs to be specified])

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
		      "conformsTo": [
		        {
		          "identifiers": [
		            {
		              "identifier": "https://biosharing.org/bsg-000228",
		              "identifierScheme": "BioSharing"
		            }
		          ],
		          "name": "FASTA",
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



.. image:: ./img/DATS-v2.0-postSanDiego-Meeting-Dataset-Distribution-SRA-examples.png
   :alt: A conceptual map detailing Biocaddie DATS distribution for an nucleic acid sequencing dataset as mirrored by 3 INSDC repositories: NCBI SRA, EBI ENA and DDBJ.		


