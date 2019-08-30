# Logical operators
x = 5
print(x > 3 or x < 4)  # Prints True

x = ["Apple", "Banana"]
y = ["Apple", "Banana"]

print(x == y)  # True because x is equal to y as a value
print(x is y)  # False because x is not the same object y even if the value is same

print("Banana" in x) # True because x contains the element "Banana"