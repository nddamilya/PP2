#Напишите программу на Python, которая сопоставляет строку, содержащую символ '', 
#за которым 'a'следует ноль или более 'b'символов ''.
import re

txt = input()

if re.fullmatch(r'ab*', txt):
    print("Match")
else:
    print("No match")