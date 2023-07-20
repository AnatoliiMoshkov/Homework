"""
Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**, якщо друге число дорівнює нулю.
"""


def func_div(first_number: int, second_number: int):
    try:
        result = first_number / second_number
        return print(result)
    except ZeroDivisionError:
        return print("Can't be divided by 0")


number_first_input = int(input("Enter the number to be divided: "))
number_second_input = int(input("Enter the number to divide by: "))
func_div(number_first_input, number_second_input)
