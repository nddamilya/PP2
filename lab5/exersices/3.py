#Напишите программу на Python для поиска последовательностей строчных букв, 
#соединенных знаком подчеркивания.
import re

txt = input()

result = re.findall(r'[a-z]+_[a-z]+', txt)
print(result)