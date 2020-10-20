number = int(input("Введите число от 1 до 9 >>>"))

number1 = number
number2 = number * 10 + number
number3 = number * 100 + number * 10 + number

result = number1 + number2 + number3

print(f"{number1} + {number2} + {number3} = {result}")
