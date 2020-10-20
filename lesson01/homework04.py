num = int(input("Введите целое положительное число >>>"))

big = num % 10

while num >= 1:
    num = num // 10
    if num % 10 > big:
        big = num % 10
    if num > 9:
        continue
    else:
        print(big, "- это максимальная цифра в этом числе")
        break
