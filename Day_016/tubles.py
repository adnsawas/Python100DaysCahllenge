myTuble = ("me", "him", "her")
print(myTuble)

# To make one value tuble, put a ,
oneValueTuble = (5,)
print(oneValueTuble)

print(myTuble[1])
for value in myTuble:
    print("This value is:", value)

# This prints the index of a tuble value
# But raises an error if value not found
print(myTuble.index("me"))

del oneValueTuble

print(myTuble[1:3])