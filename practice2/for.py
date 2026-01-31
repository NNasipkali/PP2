#1 for loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
for x in "banana":
  print(x)

#3
for i in range(1, 6):
    print(i)

#4
total = 0

for i in range(1, 6):
    total += i

print(total)

#5
numbers = [2, 4, 6, 8]

for n in numbers:
    print(n * 2)
    
#6 break 
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#7 
numbers = [3, 6, 9, 12, 15]

for n in numbers:
    if n == 9:
        print("Найдено!")
        break

#8 
for i in range(100):
    text = input("Введи stop чтобы выйти: ")
    if text == "stop":
        break

#9 
numbers = [4, 7, 2, -1, 9]

for n in numbers:
    if n < 0:
        print("Найдено отрицательное число")
        break
    print(n)

#10 
word = "programming"

for letter in word:
    if letter == "g":
        print("Буква найдена")
        break

#11 continue 
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#12 
numbers = [5, -3, 8, -1, 4]

for n in numbers:
    if n < 0:
        continue
    print(n)

#13 
word = "python"

for letter in word:
    if letter == "h":
        continue
    print(letter)

#14 
for i in range(1, 13):
    if i % 3 == 0:
        continue
    print(i)

#15 
words = ["hello", "", "python", "", "code"]

for w in words:
    if w == "":
        continue
    print(w)


