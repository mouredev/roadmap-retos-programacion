
# LISTAS
my_list: list = ["Brais", "Black", "Wolfy", "Visionos"]
print(my_list)

# AÑADIR o INSERCIÓN
my_list.append("Kramer")
print(my_list)

# ELIMINACIÓN
my_list.remove("Brais")
print(my_list)

# ACEDER A UNA POSICIÓN
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
# print(my_list[4])   # => No hay POSICIÓN 4; ERROR

# ACTUALIZACIÓN
my_list[1] = "Paquita"
print(my_list)

# ORDENACIÓN
my_list.sort()
print(my_list)  # ORDENA ALFABETICAMENTE
print(type(my_list))


# TUPLAS

# Estructura deonde podemos almacenar mas de 1 DATO
# Pero las TUPLAS son INMUTABLES
# Para uso de DATOS IMUTABLES
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
# ACCESO  A UNA POSICIÓN
print(my_tuple[1])
print(my_tuple[3])
# print(my_tuple[4])  # => No hay POSICIÓN 4; ERROR

# USO DE sorted()...devuelve una LISTA
my_tuple = sorted(my_tuple)     # Pero muestra ERROR por datos 36 int
# Pero se tranasforma a LISTA
# Por lo que se pude CASTEAR a TUPLA

# ORDENACIÓN
my_tuple = tuple(sorted(my_tuple))  # => sorted ordenará numeros y textosaa
print(my_tuple)
print(type(my_tuple))


# SETS
# Son otros tipos de ESTRUCTURAS
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
# INSERCIÓN
my_set.add("mouredev@gmail.com")
my_set.add("mouredev@gmail.com")    # => NO GUARDA DUPLICADOS
# ELIMINACIÓN
my_set.remove("Moure")
print(my_set)
# ORDENACIÓN
my_set = set(sorted(my_set))    # => NO SE PUEDE ORDENAR UN SET
print(my_set)
# print(my_set[0])    # => NO SE PUEDE ACCEDER

print(type(my_set))


# DICCIONARIOS
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
print(my_dict)
# INSERCIÓN
# Se debe ingresar por una CLAVE
my_dict["e-mail"] = "mouredev@gmail.com"
print(my_dict)  # => INSERTA CLAVE e-mail y DATO "moredev@gmail.com"
# ACCESO
print(my_dict["name"])  # => Devuelve "Brais"
# ACTUALIZACIÓN
my_dict["age"] = "37"   # => Se ACTUALIZA age a "37"
print(my_dict)
# ELIMINACIÓN
del my_dict["surname"]  # => CLAVE "surname" y DATO "Moure" se ELIMINAN
print(my_dict)
# ORNDENACIÓN
my_dict = dict(sorted(my_dict.items()))     # => ORDENA las CLAVES
print(my_dict)
print(type(my_dict))
