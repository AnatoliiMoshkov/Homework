"""
Створіть функцію, яка приймає рядок від користувача та записує його у файл.
"""


def add_to_file(string: str):
    file = open("file_ex.txt", 'w')
    file.write(string)
    file.close()


user_input = input("Enter: ")
add_to_file(user_input)
