storage = 10

print("Количество вещей на складе =", storage)

takeout = int(input("Сколько вы хотите взять вещей? >>>"))

storage = storage - takeout

print("В итоге осталось", storage, "вещей")
