# Listas
my_list = ["Brais", "Bl4ck", "Wolfy", "Visions"]
print(my_list)

my_list.append("Angel") # Inserción
my_list.append("Angel")
print(my_list)

my_list.remove('Angel') # Eliminación
print(my_list)

print(my_list[1]) # Acceso
my_list[1] = 'Cuervillo' # Modificación
print(my_list)

my_list.sort() # Ordenación
print(my_list)

# Tuplas
my_tuple = ('Moure', 'Dev', '@mouredev', '36')
print(my_tuple[1])# Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(type(my_tuple))
print(my_tuple)

# Sets
my_set = {'Moure', 'Dev', '@mouredev', '36'}
print(my_set)
my_set.add('angel@gmail.com')
my_set.add('angel@gmail.com')
my_set.remove('Moure') # Eliminación
print(my_set)
#print(my_set[0])
my_set = set(sorted(my_set)) # No se puede ordenar, set no es una estructura ordenada
print(my_set)
print(type(my_set))