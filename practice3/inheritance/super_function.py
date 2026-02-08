class Animal:
    """
    Parent class representing an animal.
    """

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    """
    Child class inheriting from Animal.
    """

    def __init__(self, name, breed):
        # calling parent constructor
        super().__init__(name)
        self.breed = breed

    def show_info(self):
        print("Name:", self.name)
        print("Breed:", self.breed)


# creating object
dog = Dog("Buddy", "Labrador")

# calling methods
dog.speak()       # inherited from Animal
dog.show_info()   # method of Dog
