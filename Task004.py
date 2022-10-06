# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.


import random


def fill_coefficients(k, min=0, max=100) -> list:
    new_list = [random.randint(min, max)]
    while new_list[0] == 0:
        new_list[0] = random.randint(min, max)
    for i in range(1, k+1):
        new_list.append(random.randint(min, max))
    return new_list


def writing_file(k: int, user_list, user_file: str):
    with open(user_file, "w", encoding="utf-8") as pol:
        if user_list[0] == 1:
            pol.write(f"x^{k}")
        else:
            pol.write(f"{user_list[0]}x^{k}")
        for i in range(1, k+1):
            if user_list[i] != 0:
                if user_list[i] > 0:
                    pol.write("+")
                if user_list[i] != 1:
                    pol.write(f'{user_list[i]}')
                if i != k and i != k-1:
                    pol.write(f"x^{k-i}")
                elif i == k-1:
                    pol.write("x")
        pol.write("=0")


def call_record(k: int, coeff_polinom: list, user_file: str):
    if user_file[-4:len(user_file)] == ".txt":
        writing_file(k, coeff_polinom, user_file)
    else:
        print("Не определён тип файла. Распознаются файлы с разрешением .txt")


k = int(input("Задайте натуральную степень многочлена k: "))
coeff_polynom = fill_coefficients(k)
my_file = "Polynominal.txt"
call_record(k, coeff_polynom, my_file)
print("Многочлен заданной Вами степени [k] записан в файл [Polynominal.txt] ")
