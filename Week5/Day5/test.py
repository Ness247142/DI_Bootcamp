
JSON

dump, dumps, load, loads

dump/dumps
convert python to json
(s) -> String 


load/loads
convert json to python
(s) -> String 

import json

obj = {
	"A" : "aaaa",
	"nums": [1,2,3]
}

with open("myfile.json", "w") as f: # Convert obj into a json file
	json.dump(obj, f)


with open("myfile.json", "w") as f:
	f.write(json.dump(obj))
