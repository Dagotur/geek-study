# Реализовать функцию my_func(),  которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(pos_1, pos_2, pos_3):
    # Если реализовывать через инпут
    # pos_1 = int(input("Первое число - "))
    # pos_2 = int(input("Второе число - "))
    # pos_3 = int(input("Третье число - "))

    if pos_2 > pos_1 < pos_3:
        print(pos_2 + pos_3)
    elif pos_1 > pos_2 < pos_3:
        print(pos_1 + pos_3)
    else:
        print(pos_1 + pos_2)


my_func(4, 66, 3)