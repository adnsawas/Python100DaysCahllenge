# Day 39 Challenge
def recursiveFunction(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return base * recursiveFunction(base, power - 1)


print(recursiveFunction(5, 3))

myList = [-4, -6, -5, -1, 2, 3, 7, 9, 88]

evenNumbers = lambda numbers: [n for n in numbers if n % 2 == 0]
print(evenNumbers(myList))