'''
Задача 1. Нахождение наибольшего общего делителя (НОД) двух чисел
'''
from fractions import Fraction
number1 = int(input('Введите первое целое число: '))
number2 = int(input('Введите второе целое число: '))
# Например number1 = 60, number2 = 7
while number1 != 0 and number2 != 0:
    if number1 > number2:
        number1 = number1 % number2  # 60 / 7 = 4, 4 / 3 = 1
        print(f"Эта {number1} number1")
    else:
        number2 = number2 % number1  # 7 / 4 = 3, 3 / 1 = 0
        print(f"Эта {number2} number2")
print(number1 + number2)  # 1 + 0 = 1

'''
Задание 2. Преобразование числа в шестнадцатеричное
представление
'''
number = int(input('Введите целое число: '))
base = int(input('Введите систему счисления: '))
original_number = number
result_number = ''
while number:
    result_number = str(number % base) + result_number
    number //= base
print(f'Число {original_number} в {
    base}-ичной системе счисления будет: {result_number}')
print(bin(original_number)[2:] if base == 2 else hex(original_number)[2:])
print(bin(original_number) if base == 2 else hex(original_number))

'''
Задача 3. Перевод целого числа в римское число
Программа принимает целое число и возвращает его римское представление в
виде строки.
'''
all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

num = int(input("Введите целое число: "))

roman = ''

while num > 0:
    for i, r in all_roman:
        while num >= i:
            roman += r
            num -= i
print(f"Число {num} в римской системе = {roman}")

'''
Задача 4. Сумма и произведение дробей
Программа принимает две строки вида "a/b" - дробь с числителем и
знаменателем. Возвращает сумму и произведение дробей. Для проверки
используется модуль fractions.
'''


def add_and_multiply_fractions(fraction1, fraction2):

    # Преобразуем строки в объекты класса Fraction

    fraction1 = Fraction(fraction1)

    fraction2 = Fraction(fraction2)

    # Вычисляем сумму и произведение дробей

    sum_fraction = fraction1 + fraction2

    multiply_fraction = fraction1 * fraction2

    # Приводим результаты к строкам вида "a/b"

    sum_fraction_str = f"{sum_fraction.numerator}/{sum_fraction.denominator}"

    multiply_fraction_str = "{multiply_fraction.numerator}/{multiply_fraction.denominator}"

    return sum_fraction_str, multiply_fraction_str


# Вводим две дроби с числителем и знаменателем
fraction1 = input("Введите первую дробь вида a/b: ")

fraction2 = input("Введите вторую дробь вида a/b: ")


# Вызываем функцию для вычисления суммы и произведения дробей

sum_fraction, multiply_fraction = add_and_multiply_fractions(
    fraction1, fraction2)


# Выводим результаты

print("Сумма дробей:", sum_fraction)

print("Произведение дробей", multiply_fraction)
