#1 while loop break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#2
i = 1

while True:
    if i == 4:
        break
    print(i)
    i += 1

#3
while True:
    word = input("Напиши stop: ")
    if word == "stop":
        break

#4
numbers = [2, 4, 6, 8, 10]
i = 0

while i < len(numbers):
    if numbers[i] == 6:
        print("Найдено!")
        break
    i += 1
    
#5
while True:
    number = int(input("Введи 0 чтобы выйти: "))
    if number == 0:
        break