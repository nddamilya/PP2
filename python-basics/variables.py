#1 Many Values to Multiple Variables
x, y, z = "Strawberry", "Banana", "Cherry"
print(x)
print(y)

#2 Output Variables
x = "Python"
y = "is"
z = "cool"
print(x, y, z)

#3 Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#4 The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#5 Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
