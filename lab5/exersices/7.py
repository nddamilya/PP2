#Напишите программу на Python для преобразования строки в стиле snake case в строку в стиле camel case.
txt = input()

words = txt.split('_')
camel = words[0] + ''.join(word.capitalize() for word in words[1:])

print(camel)