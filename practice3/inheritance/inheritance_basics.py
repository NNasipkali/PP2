class Animal:
    """
    Parent class representing an animal.
    """

    def speak(self):
        """
        Prints a generic animal sound.
        """
        print("The animal makes a sound.")


class Dog(Animal):
    """
    Child class inheriting from Animal.
    """

    def bark(self):
        """
        Prints a dog-specific sound.
        """
        print("The dog barks.")


# creating objects
animal = Animal()
dog = Dog()

# calling methods
animal.speak()
dog.speak()   # inherited from Animal
dog.bark()    # defined in Dog
