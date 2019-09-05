myTuble = ("apple", "banana", "cherry")
print("cherry" in myTuble)

print(("value",) * 3)
print(("value") * 3) # without the comma ,

print(myTuble + (1,2))

print(len(myTuble))

# to convert list to a tuble
myList = [1,3,5,7,0,8,5]
myTubleFromList = tuple(myList)
print(myTubleFromList)

print("count of 5:", myTubleFromList.count(5))
print("index of 7:", myTubleFromList.index(7))