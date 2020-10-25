new_list = list(
    map(str, input("Введите элементы через пробел, которые хотите добавить в список >>>").strip().split(' ')))
print("Элементы - ", new_list)

length = (len(new_list))
i = 0
el = 0

while i < length:
    i += 1

for elem in range(int(len(new_list) / 2)):
    new_list[el], new_list[el + 1] = new_list[el + 1], new_list[el]
    el += 2

print("Элементы после махинации -", new_list)
