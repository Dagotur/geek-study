# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def exponent():
    arg_1 = int(input("Введите положительное число - "))
    arg_2 = int(input("Введите целое отрицательное число - "))
    if arg_2 == 0:
        return 1
    else:
        return arg_1 ** (-arg_2)


print(exponent())
