#Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавной буквы.
import re

txt = input()

result = re.sub(r'(?<!^)([A-Z])', r' \1', txt)
print(result)