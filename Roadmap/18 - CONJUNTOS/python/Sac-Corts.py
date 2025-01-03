my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

my_list.insert(0, 0)
print(my_list)

my_list.extend([7, 8, 9])
print(my_list)

my_list[4:4] = [22, 23]
print(my_list)

del my_list[4]
del my_list[4]
print(my_list)

my_list[9] = 10
print(my_list)

element = 10
in_list = element in my_list
print(in_list)

my_list.clear()
print(my_list)

### Ejercicio Extra ###

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Conjunto a:", set_a)
print("Conjunto b:", set_b)

# Unión
union = set_a | set_b
print("Unión:", union)

# Intersección
intersection = set_a & set_b
print("Intersección:", intersection)

# Diferencia
difference = set_a - set_b
print("Diferencia:", difference)

# Diferencia Simétrica
symmetrical_difference = set_a ^ set_b
print("Diferencia Simétrica:", symmetrical_difference)