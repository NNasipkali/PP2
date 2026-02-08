#1
def greet(name):
    """
    This function prints a greeting using a name argument.
    """
    print("Hello", name)
greet("Nursultan")
#2 
def show_age(age):
    """
    This function prints the age passed as an argument.
    """
    print("Age:", age)
show_age(20)
#3
def add_numbers(a, b):
    """
    This function prints the sum of two numbers.
    """
    print("Sum:", a + b)
add_numbers(5, 7)
#4 
def greet_with_default(name="Guest"):
    """
    This function uses a default argument value.
    """
    print("Welcome", name)
greet_with_default()
greet_with_default("Nursultan")
#5 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
