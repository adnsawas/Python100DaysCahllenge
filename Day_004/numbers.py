import random

x = 1
y = 1.0
z = 1+1j

print(type(x))
print(type(y))
print(type(z))

e = 10e4
print(type(e))
print(e)

x1 = float(x)
y1 = int(y)
z1 = complex(x)

print("This is a random numebr " + str(random.randint(1,10)))