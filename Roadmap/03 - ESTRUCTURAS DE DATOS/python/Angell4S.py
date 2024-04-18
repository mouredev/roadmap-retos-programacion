# Listas
my_list = ["Brais", "Bl4ck", "Wolfy", "Visions"]
print(my_list)

my_list.append("Angel") # Inserción
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
