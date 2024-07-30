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