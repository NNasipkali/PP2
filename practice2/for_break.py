#1 break 
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#2
numbers = [3, 6, 9, 12, 15]

for n in numbers:
    if n == 9:
        print("Найдено!")
        break

#3
for i in range(100):
    text = input("Введи stop чтобы выйти: ")
    if text == "stop":
        break

#4
numbers = [4, 7, 2, -1, 9]

for n in numbers:
    if n < 0:
        print("Найдено отрицательное число")
        break
    print(n)

#5
word = "programming"

for letter in word:
    if letter == "g":
        print("Буква найдена")
        break