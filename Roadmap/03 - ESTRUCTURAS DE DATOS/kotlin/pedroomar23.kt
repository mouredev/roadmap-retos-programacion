/*
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
 */

// Array 
val myArray = Array(1, 2, 3, 4)

// Insersion 
myArray.add(5)

// Borrado 
myArray.removeAt(2)

// Actualizacion 
for (i in myArray) {
    print(i)
}

// Ordenacion 
myArray.sort()

// Listas 
val myList = ListOf(1, 2, 3, 4)

// Insersion 
myList.add(5)

// Borrado
myList.removeAt(1)

// Actualizacion 
for (a in myList) {
    print(a)
}

// Ordenacion 
myList.sort()



