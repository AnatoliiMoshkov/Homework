"""
Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.
"""
file = open("First_file.txt", 'r+')
list_file = file.read().split()
words_number = 0
for i in list_file:
    words_number += 1
file.close()
print(f"Words in file: {words_number}")
