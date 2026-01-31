#1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#2
number = 15
if number > 0:
  print("The number is positive")
  
#3 short hand if
a = 5
b = 2
if a > b: print("a is greater than b")

#4 You can have if statements inside if statements. This is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#5 
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")