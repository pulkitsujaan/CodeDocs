import json
#loads---to convert a json compatible data to python compatible data
#load----to convert a json compatible file data to python compatible data
data='{"var1":"Pulkit","var2":"Vani"}'
parse=json.loads(data)
print(parse['var2'])
#dumps-----to convert python compatible data to json compatible data
# data1 = {"Name":"Pulkit",
#         "Class":9,
#         "School":"The Avenue Public School",
#         "City":"Meerut",
#         "Passout":False
#         }
# jsoncomp=json.dumps(data1,sort_keys=data1)
# print(jsoncomp)
# with open("test.json", "r") as content:
#   print(json.load(content))