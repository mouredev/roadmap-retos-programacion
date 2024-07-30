"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

# Metodos para estructuras de datos 
# Listas

mi_lista = ["Hola Python", "Esto Es", "Una Lista"]
print(mi_lista)

# Inserción

mi_lista.append("Inserta al final")
print(mi_lista)

mi_lista.extend("FINAL")
print(mi_lista)

mi_lista.insert(4,"Inserta en una posición i")
print(mi_lista)

# Borrado

mi_lista.remove("Hola Python")
print(mi_lista)

mi_lista.pop()
print(mi_lista)

mi_lista.pop(0)
print(mi_lista)

"""
mi_lista.clear()  #Este metódo elimina todos los elementos de la lista
print(mi_lista)
"""

# Actualización

print(mi_lista[0])
mi_lista[0] = "Actulizamos la lista"
print(mi_lista[0])
print(mi_lista)

# Ordenación

mi_lista.sort()
print(mi_lista)


# Tuplas

mi_tupla = ("José", "Figueroa", "@JoseAlberto13", "26")
print(type(mi_tupla))
print(mi_tupla)

# Inserción

insertar_tupla = "Venezuela"
mi_nueva_tupla = mi_tupla + (insertar_tupla,) #Para evitar errores se debe incluir una coma antes o despues del elemento a añadir
print(type(mi_nueva_tupla))
print(mi_nueva_tupla)

"""
Las tuplas son inmutables, solo podemos acceder a ellas, mas no modificar su contendio después de su creación.
Para hacer una "inserción" se debe crear nueva tupla, igualandola a la tupla original y sumando la variable o el dato que deseemos agregar . 
"""

# Ordenación

mi_nueva_tupla = tuple(sorted(mi_nueva_tupla)) #Necesario volver a definir el arreglo como tupla, ya que sorted nos devuelve una LISTA
print(type(mi_nueva_tupla))
print(mi_nueva_tupla)


# Sets

mi_set = {"Alberto", "Lucena", "@JoseAlberto13", "26"}
print(type(mi_set))
print(mi_set)

# Inserción

mi_set.add("Chile")
print(mi_set)

# Borrado

mi_set.remove("Alberto")
print(mi_set)

"""
Set estructura desordenada, no se puede ordenar, la ventaja es que los datos dentro de ella no se pueden duplicar.
Y para actualizar sus datos, la mejor manera es eliminar el dato que querramos reemplazar y añadir el nuevo elemento.
"""


# Diccionario

mi_diccionario: dict = {
    "nombre" : "José",
    "apellido": "Figueroa",
    "edad": "26",
    "nacionalidad":"Venezuela"
}
print(type(mi_diccionario))
print(mi_diccionario)
print(mi_diccionario["nacionalidad"])

# Inserción

mi_diccionario["usuario"] = "JoseAlberto13"
print(mi_diccionario)
print(type(mi_diccionario))

# Borrado

del mi_diccionario["apellido"]
print(mi_diccionario)
print(type(mi_diccionario))


# Actualización

mi_diccionario["edad"] = "27"
print(mi_diccionario)
print(type(mi_diccionario))

# Ordenación

mi_diccionario = dict(sorted(mi_diccionario.items()))
print(mi_diccionario)
print(type(mi_diccionario))