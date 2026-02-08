class Student:
    """
    This class demonstrates class variables and instance variables.
    """

    school_name = "High School"   # class variable

    def __init__(self, name):
        self.name = name          # instance variable

    def show_info(self):
        """
        Prints student information.
        """
        print("Name:", self.name)
        print("School:", Student.school_name)


# creating objects
student1 = Student("Alice")
student2 = Student("Bob")

# showing initial values
student1.show_info()
student2.show_info()

print("----- Changing class variable -----")

# changing class variable
Student.school_name = "International School"

# showing values again
student1.show_info()
student2.show_info()
