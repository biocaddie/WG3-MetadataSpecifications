from pyld import jsonld
import json
from os.path import join

doc = json.load(open(join("../json-instances/", "PDB-5AEM.jsonld")))

print("loaded jsonld", doc)

context = json.load(open(join("../json-schemas/contexts/", "dataset_sdo_context.jsonld")))

print("loaded context")

compacted = jsonld.compact(doc, context)

print("-------------COMPACTED")

print(json.dumps(compacted, indent=2))

expanded = jsonld.expand(compacted)

print("-------------EXPANDED")

print(json.dumps(expanded, indent=2))

flattened = jsonld.flatten(compacted)
