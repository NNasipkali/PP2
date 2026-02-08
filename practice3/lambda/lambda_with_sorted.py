# 1. Sort numbers in ascending order
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)


# 2. Sort numbers in descending order
numbers_desc = sorted(numbers, reverse=True)
print("Sorted descending:", numbers_desc)


# 3. Sort strings by length
words = ["apple", "banana", "kiwi", "cherry"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print("Sorted by length:", sorted_by_length)


# 4. Sort list of tuples by second element
points = [(1, 3), (4, 1), (2, 2)]
sorted_points = sorted(points, key=lambda item: item[1])
print("Sorted by second value:", sorted_points)


# 5. Sort dictionary items by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = sorted(scores.items(), key=lambda item: item[1])
print("Sorted dictionary by value:", sorted_scores)
