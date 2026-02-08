class Person:
    """
    This class represents a simple person.
    """
    name = "Unknown"
    age = 0

    def show_info(self):
        """
        This method prints person's information.
        """
        print("Name:", self.name)
        print("Age:", self.age)


# creating objects of the class
person1 = Person()
person2 = Person()

# changing attributes
person1.name = "Alice"
person1.age = 25

person2.name = "Bob"
person2.age = 30

# calling methods
person1.show_info()
person2.show_info()


class Car:
    """
    This class represents a simple car.
    """
    brand = "Unknown"
    year = 0

    def show_details(self):
        """
        This method prints car details.
        """
        print("Brand:", self.brand)
        print("Year:", self.year)


# creating car objects
car1 = Car()
car2 = Car()

# setting attributes
car1.brand = "Toyota"
car1.year = 2018

car2.brand = "BMW"
car2.year = 2022

# calling methods
car1.show_details()
car2.show_details()
