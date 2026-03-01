#Напишите программу на Python, которая заменяет все вхождения пробела, запятой или точки двоеточием.
import re

txt = input()

result = re.sub(r'[ ,.]', ':', txt)
print(result)