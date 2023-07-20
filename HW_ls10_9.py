"""
Створіть функцію, яка видаляє вказаний рядок з текстового файлу.
"""
import txt as txt


def del_line(file: txt, index: int):
    file_doc = open(file, 'r')
    file_doc.seek(0)
    file_lines = file_doc.readlines()
    file_lines.pop(index-1)
    file_doc.close()
    file_doc = open(file, 'w')
    for line in file_lines:
        file_doc.write(line)
    file_doc.close()


file_user = 'Delete_line.txt'
user_input = int(input("Enter a number of line to remove: "))
del_line(file_user, user_input)
