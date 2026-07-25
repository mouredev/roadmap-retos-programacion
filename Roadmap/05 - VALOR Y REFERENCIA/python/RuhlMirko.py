print("Asignacion por valor:")
first_int = 123
second_int = 321
print(f"a: {first_int}")
print(f"b: {second_int}")
second_int = first_int
first_int = 234
print(f"A: {first_int}")
print(f"B: {second_int}")

print("\nAsignacion por referencia:")
first_list = [40, 60]
second_list = first_list
second_list.append(80)
print(first_list)
print(second_list)

print("\nFunciones: ")


def modify_int(my_int: int):
    my_int += 20
    print(my_int)


def modify_list(my_list: list):
    my_list.append(30)
    my_second_list = my_list
    my_second_list.append(30)
    print(my_list)
    print(my_second_list)


first_int = 10
first_list = [10, 20]
print(first_int)
modify_int(first_int)

modify_list(first_list)
print(first_list)

print("\n\nDificultad Extra:")


def invert_values(a, b):
    new_a = b
    new_b = a
    return f"A:{new_a}, B:{new_b}"


def invert_references(list_a, list_b):
    c_list = list_a
    list_a = list_b
    list_b = c_list
    return f"A:{list_a}, B:{list_b}"


first_var = 2024
second_var = 2020
print(f"Original state = A:{first_var} - B:{second_var}")
print(f"Modified version = {invert_values(first_var, second_var)}")


print(f"Original state = A:{first_list} - B:{second_list}")
print(f"Modified version = {invert_references(first_list, second_list)}")
