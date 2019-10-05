mytuple = ("apple", "banana", "cherry")
myIterator = iter(mytuple)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 16
        return self
    
    def __next__(self):
        if self.a <= 18:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))