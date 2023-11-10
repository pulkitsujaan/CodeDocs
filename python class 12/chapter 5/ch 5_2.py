'''Dictionary Methods'''

myDict={
    'Key':'Value',
    "Train":"Transport medium",
    "Marks":[98,99,80,79],
    "nested":{"Pants":"wearable"},
    9:69
}

# # these can be used in the data by typecasting into list
# print(myDict.keys())#gives us the keys of the dictionary
# print(myDict.values())#gives us the values of the dictionary
# print(myDict.items())#gives us the (key,value) for each item


# #update method
# print(myDict)
# updateDict={
#     "python":'snake and language'
# }
# myDict.update(updateDict)
# print(myDict)

print(myDict.get('Train'))#returns None if key not present, [] brackets throw error
