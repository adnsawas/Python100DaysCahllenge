def my_f(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_f(fruits)

def my_return_f(x = 2):
    return 5 * x

print(my_return_f(3))
print(my_return_f(4))
print(my_return_f(6))
print(my_return_f())

# Arbitrary Arguments
# Unlimited number of arguments
def arbitrary_f(*kids):
    print("The youngest kid is " + kids[2])

arbitrary_f("Emil", "Tobias", "Linus")

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results:")
tri_recursion(6)