"""
Створіть функцію, яка приймає два числа від користувача та обробляє помилку, якщо введені дані не є числами.
"""
user_input = input("Enter two numbers: ").split()
try:
    list_numbers_input = [int(i) for i in user_input]
    print(list_numbers_input)
except ValueError:
    print("No numbers were entered")
