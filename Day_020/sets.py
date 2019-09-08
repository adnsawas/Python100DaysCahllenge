mySet = {'orange', 'apple', 'banana', 1, 2}
print(mySet)

# No way to access a specific item in a set. Only by looping
for item in mySet:
    print(item)
# Note that there is no order. Sets do not take care of order

print(3 in mySet)

# You cannot change values of Set items but you can add
mySet.add("sawas")
mySet.update(['hi', 5])
print(mySet)