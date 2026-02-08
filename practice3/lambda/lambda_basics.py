# 1. Lambda that adds two numbers
add = lambda a, b: a + b
print(add(3, 5))


# 2. Lambda that multiplies a number by 2
double = lambda x: x * 2
print(double(10))


# 3. Lambda that checks if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))
print(is_even(7))


# 4. Lambda that returns the length of a string
string_length = lambda s: len(s)
print(string_length("Python"))


# 5. Lambda that converts Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
print(celsius_to_fahrenheit(25))
