class Student:
    """
    This class represents a student with name and age.
    """

    def __init__(self, name, age):
        """
        Initializes the student object with name and age.
        """
        self.name = name
        self.age = age

    def show_info(self):
        """
        Prints student information.
        """
        print("Name:", self.name)
        print("Age:", self.age)


# creating objects using __init__
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# calling methods
student1.show_info()
student2.show_info()


class Book:
    """
    This class represents a book.
    """

    def __init__(self, title, author, pages):
        """
        Initializes the book with title, author, and number of pages.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        """
        Prints book information.
        """
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


# creating book objects
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Python Basics", "John Smith", 250)

# calling methods
book1.show_info()
book2.show_info()
