#1 while loop 
i = 1
while i < 6:
  print(i)
  i += 1
  
#2
x = 5

while x > 0:
    print(x)
    x -= 1

#3
password = ""

while password != "1234":
    password = input("Введите пароль: ")
    
#4
i = 0

while i <= 10:
    print(i)
    i += 2

#5
n = int(input("Введи число: "))
total = 0

while n > 0:
    total += n
    n -= 1

print(total)



#6 while loop break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#7
i = 1

while True:
    if i == 4:
        break
    print(i)
    i += 1

#8
while True:
    word = input("Напиши stop: ")
    if word == "stop":
        break

#9
numbers = [2, 4, 6, 8, 10]
i = 0

while i < len(numbers):
    if numbers[i] == 6:
        print("Найдено!")
        break
    i += 1
    
#10
while True:
    number = int(input("Введи 0 чтобы выйти: "))
    if number == 0:
        break



#11 while loop continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# 12
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    
#13 
numbers = [3, -1, 5, -7, 8]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

#14
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#15
i = 0

while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)



