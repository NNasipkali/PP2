# 1. Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)


# 2. Convert list of Celsius temperatures to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print("Fahrenheit:", fahrenheit)


# 3. Convert all strings to uppercase
names = ["alice", "bob", "charlie"]
upper_names = list(map(lambda name: name.upper(), names))
print("Uppercase names:", upper_names)


# 4. Add 10 to each number
values = [5, 10, 15]
new_values = list(map(lambda x: x + 10, values))
print("Values +10:", new_values)


# 5. Get length of each word
words = ["Python", "lambda", "map"]
lengths = list(map(lambda word: len(word), words))
print("Word lengths:", lengths)
