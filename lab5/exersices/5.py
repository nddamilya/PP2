#Напишите программу на Python, которая сопоставляет строку, содержащую символ , 
#'a'за которым следует любой символ, заканчивающийся на 'b'.
import re

txt = input()

if re.fullmatch(r'a.*b', txt):
    print("Match")
else:
    print("No match")