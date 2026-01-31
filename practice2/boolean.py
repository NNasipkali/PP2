#1 When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(10 > 9)
print(10 == 9)
print(10 < 9)
#Booleans as Comparison Results сравнения

#2 Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#If Statement, If Else
  
#3 any non-empty string → True / empty string "" → False
print(bool("Hello"))
print(bool(15))

#4 Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#Boolean Values bool(x)

#5
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
#Boolean Operators and/or/not

#6 boolean operators
x = 3

print(x < 5 or x > 10)   # True
print(x > 5 or x > 10)   # False

#7 Booleans as Comparison Results
a = 6
b = 9

result = a <= b
print(result)   # True

#8 boolean values 
a = True
b = False

print(a)
print(b)

#9 boolean operators not
is_logged_in = False

if not is_logged_in:
    print("Пожалуйста, войдите в систему")
    
#10 Booleans as comparison results
x = 10
y = 7

print(x > y)     # True
print(x == y)    # False
print(x != y)    # True


