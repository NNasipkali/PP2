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
    Child class that overrides the speak method.
    """

    def speak(self):
        """
        Overrides the parent speak method.
        """
        print("The dog barks.")


# creating objects
animal = Animal()
dog = Dog()

# calling methods
animal.speak()
dog.speak()
