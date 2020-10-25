# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_input = input("Введите строку из нескольких слов")
new_input = []
num = 1
for el in range(user_input.count(' ') + 1):
    new_input = user_input.split()
    if len(str(new_input)) <= 10:
        print(f" {num} {new_input[el]}")
        num += 1
    else:
        print(f" {num} {new_input[el][0:10]}")
        num += 1
