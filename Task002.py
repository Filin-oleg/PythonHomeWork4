# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def check_number(n: int):
    i = 2
    while n % i != 0 or i == n - 1:
        i += 1
    if i == n:
        return n


def fill_list(n: int) -> list:
    simple_list = [1]
    for i in range(2, n+1):
        if n % i == 0:
            if check_number(i) != None:
                simple_list.append(check_number(i))
            else:
                continue
    return simple_list


n = input_number("Введите натуральное число N: ")
list = fill_list(n)
print(list)
