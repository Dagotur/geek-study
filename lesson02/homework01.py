data_list = ["twelve", 322, None, 3.14, True, set("random")]
print(data_list)


def check_type(el):
    for el in range(len(data_list)):
        print(type(data_list[el]))
    return


print(check_type(data_list))
