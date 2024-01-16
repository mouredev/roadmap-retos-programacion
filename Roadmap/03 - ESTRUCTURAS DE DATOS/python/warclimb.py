# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio
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

# Los tipos de estrucutras de datos en Python son: listas, tuplas, diccionarios y conjuntos

# Listas
## conjunto de datos ordenados por índices
herramientas = ["martillo", "destornillador", "sierra", "taladro"]

# insercion
herramientas.append("alicates")
# borrado
herramientas.remove("sierra")
# actualizacion
herramientas[2] = "serrucho"
# ordenacion
herramientas.sort()

# Tuplas
## Igual que las tablas pero inmutables, se usan para datos que no van a cambiar
power_rangers = ("Jason", "Zack", "Billy", "Trini", "Kimberly")

# Las tuplas no se pueden editar, asi que: ¯\_(ツ)_/¯

# Diccionarios
## conjunto de datos ordenados por claves. en este caso la clave es la herramienta y el valor representa la resistencia.
herramientas_dict = {"martillo": 40, "destornillador": 6, "sierra": 20, "taladro": 80}

# Conjuntos / sets
## conjunto de datos no ordenados, no se pueden repetir
herramientas_set = {"martillo", "destornillador", "sierra", "taladro"}



