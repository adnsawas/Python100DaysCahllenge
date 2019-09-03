theList = ["A", "B", "C", "D", "F "]

print("List length:", len(theList))
theList.append("G")
theList.insert(4, "E")
theList.remove("A")
theList.pop() # Remove last item
theList.pop(2) # Remove item at index 2
print(theList)

theSecList = theList.copy()
theList.clear()

# Another way to copy a list
theThirdList = list(theList)

# Another way to create lists
theForthList = list(("1", "2", "3"))
theForthList.reverse()
print(theForthList)
