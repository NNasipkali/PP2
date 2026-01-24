#1 A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)
#2 Variables do not need to be declared with any particular type, and can even change type after they have been set
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#3 if you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
#4 Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#5 Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)