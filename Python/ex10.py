import requests
import pickle
irisdata=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
with open("irisdata.txt",'w') as i:
    i.write(irisdata.text)
parseddata=[]
with open("irisdata.txt",'r') as i:
    for items in i:
        if items!=0:
            splitter=items.split('\n')
            parseddata.append(splitter)
parseddata.remove(parseddata[len(parseddata)-1])
for items in parseddata:
    print(items)

filename="irispickled.pkl"
obj=open("irispickled.pkl",'wb')
pickle.dump(parseddata,obj)
obj.close

with open("irispickled.pkl",'rb') as i:
    lst1=pickle.load(i)
    for itmes in lst1:
        print(itmes)