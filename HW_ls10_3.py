"""
Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.
"""
try:
    file = open("Example.txt", 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Sorry, a file not found ")

