#Напишите программу на Python для преобразования заданной строки в стиле camel case в стиль snake case.
import re

txt = input()

result = re.sub(r'([A-Z])', r'_\1', txt).lower()
print(result)