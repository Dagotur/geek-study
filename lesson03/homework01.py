# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide():
    while True:
        try:
            arg_1 = float(input("Введите первое число >>> "))
            arg_2 = float(input("Введите второе число >>> "))
            result = arg_1 / arg_2

            if result.is_integer():
                print(round(result))
            else:
                print(round(result, 2))
            break

        except ZeroDivisionError:
            print("На ноль делить нельзя!")
        except ValueError:
            print("Нужно вводить числа!")


divide()
