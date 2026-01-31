#1
x = int(input())

match x:
    case 1:
        print("Один")
    case 2:
        print("Два")
    case 3:
        print("Три")
    case _:
        print("Другое число")
#2
day = int(input())

match day:
    case 1:
        print("Понедельник")
    case 2:
        print("Вторник")
    case 3:
        print("Среда")
    case 4:
        print("Четверг")
    case 5:
        print("Пятница")
    case 6:
        print("Суббота")
    case 7:
        print("Воскресенье")
    case _:
        print("Нет такого дня")
#3 
a = int(input())
op = input()
b = int(input())

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Неизвестная операция")
#4
score = int(input())

match score:
    case s if s >= 90:
        print("A")
    case s if s >= 75:
        print("B")
    case s if s >= 60:
        print("C")
    case _:
        print("F")
#5 
n = int(input())

match n:
    case 0:
        print("Ноль")
    case _:
        if n > 0:
            print("Положительное число")
        else:
            print("Отрицательное число")


