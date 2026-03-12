names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate
print("Using enumerate:")
for i, name in enumerate(names):
    print(i, name)

# zip
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

# sorted
numbers = [5, 2, 9, 1]
print("\nSorted:", sorted(numbers))

# type conversion
num_str = "10"
num_int = int(num_str)
print("Converted:", num_int, type(num_int))