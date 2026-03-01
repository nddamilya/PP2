#Напишите программу на Python для разделения строки по заглавным буквам.
import re

txt = input()

result = re.split(r'(?=[A-Z])', txt)
print(result)