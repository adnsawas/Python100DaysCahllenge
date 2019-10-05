class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname, self.lname)

x = Person("John", "Doe")
x.printName()

class Student(Person):
    pass

y = Student("Mike", "Olsen")
y.printName()

class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
    
z = Student2("Adnan", "Sawas")
z.printName()