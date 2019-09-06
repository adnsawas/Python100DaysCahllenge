# Question 1
# ========================================================
myList = [
    "Orange",
    "Apple",
    "Pinapple",
    "Orange",
    "Strawberry"
]

# Apply 4 list functions
myList.append("Cherry")
myList.remove("Strawberry")
myList.sort()
print("myList values:", myList)
print(f"The list has {myList.count('Orange')} ornages")

# ========================================================

# Question 2
# ========================================================
myTuble = ("java", "python", "swift")

# Write some code to find the value "python" in myTuble
valueExists = False
for item in myTuble:
    if item == "python":
        valueExists = True
        break

if valueExists:
    print("The value \"python\" exists in myTuble")
else:
    print("The value \"python\" doex not exist in myTuble")
