EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# Crear una lista array
mi_lista = [1, 2, 3, 4, 5]

# Agregar un elemento al final de la lista
mi_lista.append(6)

# Insertar un elemento en una posición específica
mi_lista.insert(2, 10)

# Eliminar un elemento por valor
mi_lista.remove(3)

# Eliminar un elemento por índice
del mi_lista[1]

# Actualizar un elemento por índice
mi_lista[0] = 100

# Ordenar la lista de forma ascendente
mi_lista.sort()

# Ordenar la lista de forma descendente
mi_lista.sort(reverse=True)

# Crear un conjunto de lista
mi_conjunto = {1, 2, 3, 4, 5}

# Agregar un elemento al conjunto
mi_conjunto.add(6)

# Eliminar un elemento por valor
mi_conjunto.remove(3)

# Eliminar un elemento de forma segura si existe
mi_conjunto.discard(10)

# Crear un diccionario con clave:valor
mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Ciudad de México"}

# Agregar una nueva clave-valor al diccionario
mi_diccionario["ocupacion"] = "Estudiante"

# Eliminar una clave-valor por clave
del mi_diccionario["edad"]


# Actualizar el valor de una clave
mi_diccionario["nombre"] = "Carlos"

   
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.

