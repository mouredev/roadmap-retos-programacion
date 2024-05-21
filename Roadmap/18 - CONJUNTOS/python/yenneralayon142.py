"""
conjuntos
"""
my_set = {2,3,4,5,6}
my_set.add(7) # Añadir elemento al final
print(f"A1{my_set}")
new_element = 1
my_new_set = {new_element, *my_set} # Añadir elemento al inicio
print(f"A2{my_new_set}")
new_elements = {8,9,10}
my_new_set.update(new_elements)
print(f"A3{my_new_set}") #Añadir varios elementos en bloque al final

"""
En Python, los sets no tienen un orden específico de elementos, por lo que técnicamente no puedes
agregar elementos en una posición concreta como podrías hacer con una lista o una tupla
"""

"""
No puedo acceder a una posición, pero puedo eliminar el elemento único
"""
my_new_set.remove(6)
print(f"A5{my_new_set}") # Eliminar elemento unico

"""
En un set no se puede actualizar un elemento ya que trabaja con elementos unicos
"""
print(f"A6",10 in my_new_set) # Comprobar si el elemento está en el conjunto

my_new_set.clear()
print(f"A7 Contenido eliminado  {my_new_set}") #Eliminar todo el contenido del conjunto


"""
Ejercicio
"""

my_set1 = {1,2,3,4}
my_set2 = {4,5,6}

union_set = my_set1.union(my_set2)
print(f"Esta es la unión de los dos conjuntos {union_set}") #Unión

intersection_set = my_set1.intersection(my_set2)
print(f"Esta es la intersección de los dos conjuntos {intersection_set}") #Intersección

difference_set = my_set1.difference(my_set2)
print(f"Esta es la diferencia de los dos conjuntos {difference_set}") #Diferencia
 
simetry_difference = my_set1.symmetric_difference(my_set2)
print(f"Esta es la diferencia simetrica de los dos conjuntos {simetry_difference}") #Diferencia simetrica

