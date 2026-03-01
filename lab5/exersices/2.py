#Напишите программу на Python, которая сопоставляет строку, содержащую символ , 
#'a'за которым следуют два-три символа 'b'.
import re

txt = input()

if re.fullmatch(r'ab{2,3}', txt):
    print("Match")
else:
    print("No match")