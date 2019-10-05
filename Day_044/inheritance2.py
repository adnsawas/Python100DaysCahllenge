class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduateYear = year
    
    def welcome(self):
        print(f"Welcome {self.fname} to the class of {self.graduateYear}")

x = Student("Adnan", "Sawas", 2010)
x.printName()
x.welcome()