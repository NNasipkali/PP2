#1 
def get_greeting():
    """
    this funcrion show a message
    """
    return "Hello from a function"
message = get_greeting()
print(message)

#2
def multiply_numbers(a, b):
    """
    This function returns the product of two numbers.
    """
    return a * b
result_product = multiply_numbers(4, 6)
print("Product:", result_product)
#3
def add_numbers(a, b):
    """
    This function returns the sum of two numbers.
    """
    return a + b
#we can result directly 
print(add_numbers(5, 6))
#4 
def fahrenheit_to_celsius(fahrenheit):
    """
    This function converts Fahrenheit to Celsius and returns the result.
    """
    return (fahrenheit - 32) * 5 / 9
temperature_c = fahrenheit_to_celsius(77)
print("Temperature in Celsius:", temperature_c)

#5 
def is_positive(number):
    """
    This function checks if a number is positive and returns True or False.
    """
    return number > 0
print("Is 10 positive?", is_positive(10))
print("Is -5 positive?", is_positive(-5))
