myDict = {
    "name": "Adnan",
    "job": "Udacity",
    "age": 27
}

# Check if key exists
print("name" in myDict)

print(len(myDict))
myDict["learning"] = "python"
myDict.pop("job") # Throws an error if no match key

print(myDict.popitem())
# Removes and pop last added item

myDict.clear()
# Remove all items

del myDict
# Remove dictionary from memory