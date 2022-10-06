# Вычислить число c заданной точностью d


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def pi_accuracy(a: int) -> float:
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-a-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, a)


a = input_number("Введите точность (количество знаков после запятой) определения числа Pi: ")
pi = pi_accuracy(a)
print(f"Число Pi с заданной Вами точностью {[a]} = {pi}")
