# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def fill_list(n, border_min, border_max) -> list:
    list = [random.randint(border_min, border_max)]
    for i in range(1, n):
        list.append(random.randint(border_min, border_max))
    return list


def unique_list(list) -> list:
    result_list = [list[0]]
    for i in range(1, len(list)):
        for j in range(len(result_list)):
            if list[i] == result_list[j]:
                break
            elif j == len(result_list)-1:
                result_list.append(list[i])
    return result_list


n = input_number("Введите количество элементов списка случайных чисел: ")
border_min = input_number("Введите нижнюю границу значений элементов списка: ")
border_max = input_number("Введите верхнюю границу значений элементов списка: ")
source_list = fill_list(n, border_min, border_max)
result_list = unique_list(source_list)
print(f"Случайная последовательность чисел в соответствии с заданными Вами парметрами {source_list} ")
print(f"Cписок неповторяющихся элементов исходной последовательности {result_list}")
