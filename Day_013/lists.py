myList = [1, 2, 3, "One", "Two"]
myNumbers = [1.1, 1.2, 2.3, 3.14, 4.5, 7.91]

# Change an item value
myList[2] = "Three"

print("Third item of myList is:", myList[2])

print("Printing the entire myNumbers list:")
for number in myNumbers:
    print(number)

# Delete an item
del myList[2]
print(myList)

# Delete the entire list
del myList
print(myList)
# This last print causes an error since the variable is not defined anymore