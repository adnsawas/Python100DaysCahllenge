myDict = {
    "name": "Adnan",
    "job": "Udacity",
    "age": 27
}

myDict2 = myDict
# myDict2 is a reference not a copy

myDict3 = myDict.copy()
# This is a real independent copy

myDict4 = dict(myDict)
# This is also a real independent copy

# Nested dictionaries
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobia",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    },
}

myDict5 = dict(brand="Food", model="Mustang", year=1964)
# Note that keys are not strings
# and : became =
