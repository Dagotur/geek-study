# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def number_sum():
    result = 0
    x = False

    while not x:
        number = input("Введите числа через пробел или 0, чтобы выйти >>> ").split()
        start = 0

        for el in range(len(number)):
            if number[el] == "0":
                x = True
                break
            else:
                start = start + int(number[el])
        result = result + start
        print(f"Текущая сумма равна {result}")
    print(f"Итоговая сумма равна {result}")


number_sum()
