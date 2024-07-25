# ------ I. Ejercicio

my_set = [i for i in range(10)]
print(my_set)

my_set.append(10)
print(my_set)

my_set.insert(0, 11)
print(my_set)

my_set.extend([12, 13, 14])
print(my_set)

my_set[4:4] = [15, 16, 17]
print(my_set)

my_set.pop(2)
print(my_set)

my_set[0] = -1
print(my_set)

print(17 in my_set)

my_set.clear()
print(my_set)

# ------ II. Extra

my_set_1 = {2, 3, 6, 7}
my_set_2 = {3, 5, 7, 9}

print(my_set_1.union(my_set_2))
print(my_set_1.intersection(my_set_2))
print(my_set_1.difference(my_set_2))
print(my_set_1.symmetric_difference(my_set_2))
