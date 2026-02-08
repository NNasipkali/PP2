# 1. Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# 2. Filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)


# 3. Filter numbers greater than 10
values = [5, 10, 15, 20, 3]
greater_than_ten = list(filter(lambda x: x > 10, values))
print("Greater than 10:", greater_than_ten)


# 4. Filter strings longer than 4 characters
words = ["cat", "house", "tree", "python"]
long_words = list(filter(lambda word: len(word) > 4, words))
print("Long words:", long_words)


# 5. Filter positive numbers
numbers_list = [-10, -5, 0, 3, 8]
positive_numbers = list(filter(lambda x: x > 0, numbers_list))
print("Positive numbers:", positive_numbers)
