my_list = ["Juan", "Rodriguez", "34", "juserdev"]
print(my_list)

my_list.append("laura")
print(my_list)

my_list.remove("laura")
print(my_list)

my_list_copy = my_list.copy() # Esta funcion crea un acopia de la variable original
my_list_copy.append("laura")
print(my_list_copy)

print(my_list.count("hola")) # esta funcion cuanta cuntas veces se repite lo que esta dentro de los parentesis 
print(my_list.count("34"))

my_list.pop() # Elemina el ultimo indice de la lista
print(my_list)

my_list.remove("Juan") # Elimna el elemento que tenga escrito dentro de los paretesis
print(my_list)

my_list.reverse() # devuele la listra de tras pa lante
print(my_list)

print(my_list[0]) # selecciona el valor en el indice declarado entre corchetes

edad, nombre = my_list # destructurar

print(edad)
print(nombre)

print(my_list)

my_list.append("juan")
print(my_list)

my_list.insert( 2, "juserdev") # agrega un valor en la posicion indicada
print(my_list)

my_list.sort() # ordena
print(my_list)

my_list.clear() # con esta funcion limpa la lista
print(my_list)

### Tupla ###

my_tupla = (34, 1.70, "juan", "rodriguez", "juan")
print(my_tupla)

print(my_tupla.index(34)) # Busca y nos devuelve el indice del valor dentro de los parentesis
print(my_tupla.count("juan"))
my_tupla = list(my_tupla) # lo transforme en lista para poder modificarlo
my_tupla[4] = "juserdev"
print(type(my_tupla))
print(my_tupla)
my_tupla = tuple(my_tupla) # lo transforme en tupla nuevamente
print(type(my_tupla))
print(my_tupla)

### Set

my_set = {"juan", "rodriguez", 34, 1.70}
print(type(my_set))
print(my_set) # muestra el contenido en desorden

my_set.add("juserdev") # Agrega contenido al set
print(my_set) 
print(len(my_set)) # esta funcion sirve con todos para contantar la cantidad de elementos que hay

print("juserdev" in my_set) # confima si existe el elemento #-> true
print("juserdeve" in my_set) # confima si existe el elemento #-> false

my_set.remove("juserdev")
print(my_set)

my_other_set = {"juserdev", "colombia"}

my_set = my_set.union(my_other_set).union({"python"})
print(my_set)

# my_set.clear() # -> elimina el contenido del set
# print(my_set) 
# del my_set # -> borra el set


### dictcionary

my_dict = {
  "nombre": "juan",
  "apellido": "rodirguez",
  "edad": 34,
  "lenguajes": {
    "python",
    "typescript",
    "css"
  }
}

print(my_dict)
print(my_dict["nombre"])

my_dict["nombre"] = "Sebastian"
print(my_dict)
print(my_dict["nombre"])
# print(my_dict[1])

my_dict["calle"] = "monda" # agregue una clave llamada calle y le puse de nombre monda
print(my_dict)

print( "Sebastian" in my_dict)
print( "nombre" in my_dict) # Busca por clave y no por valor

del my_dict["calle"] # Borra un elemento especifico
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())