import json

mymodel = UserProfile()
LIST=[1,2,3,4]
mymodel.mylist=json.dumps(LIST)
mymodel.save()


jsondec=json.decoder.JSONDecoder()
myPythonList = jsonDec.decode(mymodel.myList)

for i in myPythonList:
    print i