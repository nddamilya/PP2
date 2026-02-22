#1 Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#2 Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#3 Return Values
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#4 Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")