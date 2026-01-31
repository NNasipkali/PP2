#1 continue 
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#2 
numbers = [5, -3, 8, -1, 4]

for n in numbers:
    if n < 0:
        continue
    print(n)

#3 
word = "python"

for letter in word:
    if letter == "h":
        continue
    print(letter)

#4 
for i in range(1, 13):
    if i % 3 == 0:
        continue
    print(i)

#5 
words = ["hello", "", "python", "", "code"]

for w in words:
    if w == "":
        continue
    print(w)
