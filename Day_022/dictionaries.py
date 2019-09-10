myDict = {
    "name": "Adnan",
    "job": "Udacity"
}


print(myDict["name"])
print(myDict.get("name"))

myDict['age'] = 27
print(myDict)

for item in myDict:
    print(f"{item}: {myDict[item]}")

for x in myDict.values():
    print(x)

for y, z in myDict.items():
    print(y, z)