"""
Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст,
виводячи рядки, які є у першому файлі, але відсутні у другому.
"""
first_file = open('First_file.txt', "r")
second_file = open('Second_file.txt', "r")
ff_lines = first_file.readlines()
fs_lines = second_file.readlines()
for line in ff_lines:
    if line not in fs_lines:
        print(line, end='')

first_file.close()
second_file.close()
