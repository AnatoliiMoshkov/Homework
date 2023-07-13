"""
1. Програма буде брати зі списку слів одне рандомне слово.
2. Програма буде отримувати від користувача число - кількість спроб вгадати
3. Далі програма буде чекати від користувача або букву, або ціле слово.
4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число, якщо так то говорити
що користувач вгадав слово, або писати що слово не правильне.
5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові, та якщо є,
виводити наше слово, де зірочками будуть закриті всі літери, які користувач ще не вгадав, або "Такої літери немає"
6. Якщо кількість спроб закінчиться, потрібно сказати користувачу, що він програв та закінчити роботу програми.

Приклад:
Програмою обрано слово "apple"
Вхід: 10 (10 спроб вгадати слово)
Вхід: "a"
Вихід: "a****"
Вхід: "d"
Вихід: "Такої літери немає"
Вхід: "l"
Вихід: "a**l*"
Вхід: "e"
Вихід: "a**le"
Вхід: "apple"
Вихід: "Вітаю, ви вгадали слово" """

import random as rd


def field_of_miracles(user_input: str):
    sl_string = user_input.lower()
    list_words = [i.strip('!?,.') for i in sl_string.split()]
    choice_word = rd.choice(list_words)
    str_choice_word = ''.join(choice_word)
    r_word = [i for i in choice_word]
    changed_word = ['*' for i in r_word]
    string_ch_word = ''.join(changed_word)
    attempts_number = int(input('Введіть кількість спроб: '))
    i = 0

    while i < attempts_number:
        if string_ch_word == str_choice_word:
            return print(f"Ви вгадали слово - {choice_word}")

        user_try = input('Введіть одне слово або ціле слово: ')

        if len(user_try) > 1:
            if user_try == choice_word:
                return print(f"Ви вгадали слово - {choice_word}")
            else:
                i += 1
                print('Слово не правильне')

        if user_try in r_word:
            for index, x in enumerate(r_word):
                if x == user_try:
                    string_ch_word = string_ch_word[:index] + user_try + string_ch_word[index+1:]
            print(string_ch_word)
        else:
            i += 1
            print("Такої літери немає")

    return print('Кількість спроб закінчилася - Ви програли!')


user_input = input("Введіть речення для гри: ")

field_of_miracles(user_input)
