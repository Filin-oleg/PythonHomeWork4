# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


import random


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод ")
    return number


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


def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        result = pol.read()
        return result


def transform_polinom(user_polynom: str, user_file: str):
    polyn = user_polynom.replace("$", "")
    polyn = polyn.replace("**", "^")
    polyn = polyn.replace(" ", "")
    polyn = polyn[:-2]
    return polyn


def num_list(p: str, a: str) -> int:
    if p.index(a) == 0:
        n = 1
    elif p.index(a) == 1:
        if p[0] == '-':
            n = -1
        elif p[0] == '+':
            n = 1
        else:
            n = p[0]
    else:
        n = int(p[:p.index(a)])
    return n


def degree_list(p: str) -> int:
    if p.find('-') != -1 and p.find('+') != -1:
        ind = min(p.index('-'), p.index('+'))
    elif p.find('-') != -1 and p.find('+') == -1:
        ind = p.index('-')
    elif p.find('-') == -1 and p.find('+') != -1:
        ind = p.index('+')
    else:
        ind = len(p)
    return ind


def fill_missing_coeff(p: str) -> list:
    n = []
    degree = []
    while len(p) > 0:
        if p.find('x^') != -1:
            n.append(num_list(p, 'x^'))
            p = p[:0] + p[p.index('x^'):]
            ind = degree_list(p)
            degree.append(int(p[2:ind]))
            p = p[:0] + p[ind:]
        elif p.find('x') != -1:
            n.append(num_list(p, 'x'))
            p = p[:0] + p[p.index('x'):]
            ind = degree_list(p)
            degree.append(1)
            p = p[:0] + p[1:]
        else:
            n.append(int(p[:len(p)]))
            degree.append(0)
            p = p[:0] + p[len(p):]
    for i in range(1, len(n)):
        if degree[i-1] - degree[i] != 1:
            for j in range((degree[i-1] - degree[i])-1):
                n.insert(i+j, 0)
                degree.insert(i+j, degree[i+j-1]-1)
    if degree[-1] != 0:
        for i in range(len(degree), len(degree) + degree[-1]):
            n.insert(i, 0)
            degree.insert(i, degree[i-1]-1)
    return n


def addition_coefficients(user_polinom: list, complimentary: int) -> list:
    for i in range(complimentary):
        user_polinom.insert(0, 0)
    return user_polinom


def sum_polinom(tp1: list, tp2: list) -> list:
    if len(tp1) != len(tp2):
        complementary = abs(len(tp1) - len(tp2))
        if len(tp1) < len(tp2):
            tp1 = addition_coefficients(tp1, complementary)
        else:
            tp2 = addition_coefficients(tp2, complementary)
    result = []
    for i in range(len(tp1)):
        result.append(tp1[i] + tp2[i])
    return result


k1 = input_number("Задайте натуральную степень 1-го многочлена k1: ")
k2 = input_number("Задайте натуральную степень 2-го многочлена k2: ")
coeff_polinom1 = fill_coefficients(k1, 0, 100)
coeff_polinom2 = fill_coefficients(k2, 0, 100)
my_file1 = "Polynom1.txt"
my_file2 = "Polynom2.txt"
call_record(k1, coeff_polinom1, my_file1)
call_record(k2, coeff_polinom2, my_file2)
polynom1 = read_file(my_file1)
polynom2 = read_file(my_file2)
p1 = transform_polinom(polynom1, my_file1)
p2 = transform_polinom(polynom2, my_file2)
tp1 = fill_missing_coeff(p1)
tp2 = fill_missing_coeff(p2)
result = sum_polinom(tp1, tp2)
my_file_result = 'Result_polynom.txt'
call_record(len(result)-1, result, my_file_result)
print("Сумма многочленов, находящихся в файлах [Polynom1.txt] и [Polynom2.txt] записана в файл [Result_polynom.txt] ")
