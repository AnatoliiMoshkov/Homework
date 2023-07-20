"""
Обробіть виняток IndexError, коли програма намагається отримати доступ до неправильного індексу в списку.
"""
list_user_input = input("Enter some numbers: ").split()
index_user_input = int(input("Enter the index to see the number: "))
try:
    print(f"The index number: {list_user_input[index_user_input]}")
except IndexError:
    print("No index number!")
