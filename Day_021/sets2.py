mySet = {'orange', 'apple', 'banana', 1, 2}
print(len(mySet))

mySet.remove('apple')
# If item was not found, an error is thrown

mySet.discard('banana')
# No error is thrown if iten is not found

mySet.pop()
# Removes a random item since sets are not ordered

mySet.clear()
# Remove all items but set itself is still allocating memory

del mySet
# the set does not allocate memory anymore

myNewSet = set(('orange', 'apple', 'banana'))
print(myNewSet)