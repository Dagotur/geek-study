# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]

all_multiply = reduce(lambda x, y: x * y, my_list)
all_sum = reduce(lambda x, y: x + y, my_list)

print(f"Результат перемножения всех элементов = {all_multiply}")
print(f"Результат сложения всех элементов = {all_sum}")
