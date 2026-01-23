#1 Slicing
b = "Hello, World!"
print(b[2:5])             
b = "Hello, World!"
print(b[2:])              #Slice To the End

#2 Modify Strings
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))

#3 String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#4Split String
a = "Hello, World!"
print(a.split(","))       # returns ['Hello', ' World!']

#5 String Methods
a = "Hello, World!"
print(a.isalpha())
print(a.digit())
print(a.upper())