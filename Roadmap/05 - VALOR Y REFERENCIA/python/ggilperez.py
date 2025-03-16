# Problem #05 value & pointers

# By value
my_int_1 = 1
my_int_2 = my_int_1
my_int_2 += 1
print(f"{my_int_1 = }")
print(f"{my_int_2 = }")

# By references (pointer)
my_list_1 = [1]
my_list_2 = my_list_1
my_list_2.append(2)
print(f"{my_list_1 = }")
print(f"{my_list_2 = }")


def by_value(my_int: int):
    my_int += 3
    print(f"{my_int = }")


print(f"{my_int_1 = }")
print("by_value(my_int_1)")
by_value(my_int_1)
print(f"{my_int_1 = }")


def by_reference(my_list: list):
    my_list.append(3)
    print(f"{my_list = }")


print(f"{my_list_1 = }")
print("by_reference(my_list_1)")
by_reference(my_list_1)
print(f"{my_list_1 = }")


# Extra

def by_value(my_int_1: int, my_int_2: int) -> tuple:
    my_int_1, my_int_2 = my_int_2, my_int_1
    return my_int_1, my_int_2


def by_reference(my_list_1: list, my_list_2: list) -> tuple:
    my_int_1, my_int_2 = my_list_2, my_list_1
    return my_int_1, my_int_2


my_outter_int_1 = 1
my_outter_int_2 = 2
my_outter_int_1_aux, my_outter_int_2_aux = by_value(my_outter_int_1, my_outter_int_2)

print(f"{my_outter_int_1 = }")
print(f"{my_outter_int_2 = }")
print(f"{my_outter_int_1_aux = }")
print(f"{my_outter_int_2_aux = }")

my_outter_list_1 = [1]
my_outter_list_2 = [2]
my_outter_list_1_aux, my_outter_list_2_aux = by_value(my_outter_list_1, my_outter_list_2)

print(f"{my_outter_list_1 = }")
print(f"{my_outter_list_2 = }")
print(f"{my_outter_list_1_aux = }")
print(f"{my_outter_list_2_aux = }")
