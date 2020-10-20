time_input = int(input("Введите время в секундах >>>"))

hour = time_input // 3600
minute = (time_input - hour * 3600) // 60
second = time_input - (hour * 3600 + minute * 60)

print(f"Сформатировано - {hour}:{minute}:{second}")
