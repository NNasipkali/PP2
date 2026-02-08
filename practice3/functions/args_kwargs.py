""" *args Используется, когда: 
не знаешь заранее, сколько аргументов передадутаргументы идут просто списком """
"""**kwargs Используется, когда:
аргументы передаются по имениформат ключ=значение"""

def print_numbers(*args):
    """
    This function prints all numbers passed as arguments.
    """
    print("Numbers:", args)


def sum_numbers(*args):
    """
    This function returns the sum of all arguments.
    """
    return sum(args)


def print_person_info(**kwargs):
    """
    This function prints person information using keyword arguments.
    """
    print("Person info:", kwargs)


def greet_people(**kwargs):
    """
    This function prints greeting messages using names.
    """
    for key, value in kwargs.items():
        print(key, ":", value)


# calling functions with *args
print_numbers(1, 2, 3)
print_numbers(10, 20, 30, 40)

total = sum_numbers(5, 10, 15)
print("Sum:", total)


# calling functions with **kwargs
print_person_info(name="Alice", age=20, city="Almaty")

greet_people(person1="John", person2="Emma", person3="Alex")
