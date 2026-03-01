#Напишите программу на Python для поиска последовательности, в которой сначала идет заглавная буква, 
#а затем строчная.
import re

txt = input()

result = re.findall(r'[A-Z][a-z]+', txt)
print(result)