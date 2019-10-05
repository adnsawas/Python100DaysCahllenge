# Create a Library class
class Library:
    shelf = 45
    book = 300

class Science_Section(Library):
    name = "Physics books"

x = Science_Section()
print(x.shelf, x.book, x.name)
x.book = 20
x.shelf = 4
print(x.shelf, x.book, x.name)