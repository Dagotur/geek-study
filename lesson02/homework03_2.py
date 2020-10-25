user_input = int(input("Введите число от 1 до 12 >>> "))
season_list = ["зимний", "весенний", "летний", "осенний"]

if user_input == 1 or 2 or 12:
    print("Это", season_list[0], "месяц")
elif user_input == 3 or 4 or 5:
    print("Это", season_list[1], "месяц")
elif user_input == 6 or 7 or 8:
    print("Это", season_list[2], "месяц")
elif user_input == 9 or 10 or 11:
    print("Это", season_list[3], "месяц")
