class Father:
    """
    First parent class.
    """

    def skills(self):
        print("Father: driving and repairing")


class Mother:
    """
    Second parent class.
    """

    def skills(self):
        print("Mother: cooking and teaching")


class Child(Father, Mother):
    """
    Child class inheriting from Father and Mother.
    """

    def show_skills(self):
        print("Child skills:")
        Father.skills(self)
        Mother.skills(self)


# creating object
child = Child()

# calling methods
child.show_skills()
