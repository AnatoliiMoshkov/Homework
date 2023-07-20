"""
Реалізуйте програму, яка копіює вміст одного файлу в інший.
"""
first_file = open("First_file.txt", 'r+')
data_first_file = first_file.read()
second_file = open("Second_file.txt", "w+")
second_file.write(data_first_file)
first_file.close()
second_file.close()
