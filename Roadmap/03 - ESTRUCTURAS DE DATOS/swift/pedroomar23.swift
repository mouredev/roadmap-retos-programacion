import Foundation

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

// Ejemplos de estructuras 
struct Person { // Ejemplo 1
    var nombre: String 
    var age: Int 
}
Person(nombre: "Julio", age: 20) // Llamar a la instancia de la estructura
print("El perfil de la persona es", Person(nombre: "Julio", age: 20)) // Print en la consola la instancia de la estructura

struct Car { // Ejemplo 2
    var motor = 20
    var espejos = 25
    var gomas = 30

    func BuyCar(motor: Int, espejos: Int, gomas: Int) -> Int {
        return motor + espejos / gomas * 100
    }

    print("El resultado de la combinada 20 + 25 / 30 * 100 es \(BuyCar(motor: 20, espejos: 25, gomas: 30))")
}
Car(motor: 20, espejos: 25, gomas: 30)
print("El precio de las piezas de los carros es", Car(motor: 20, espejos: 25, gomas: 30))

// Array de cadena de texto (String)
var nombres = Set(["Pedro", "Juan", "Oscar"])

nombres.insert("Carlos") // Añadir un elemento al Array
print("El elemento añadido es \(nombres)")

nombres.contains("Pedro") // Comprobar si exite un elemento en el Array
print("Comprobando si esta Pedro en el Array \(nombres)")

nombres.sorted() // Ordenar de forma ascendente el Array 
print("El array ordenado de forma ascendente \(nombres)")

nombres.remove("Pedro") // Eliminar un elemento del Array 
print("El elemento eliminado es Carlos \(nombres)")

// Array de cadena de enteros (Int)
var numeros = [1, 2, 3, 4]

numeros.append(5) // Añadir un entero al Array
print("5 es el nuevo entero en el array")

numeros.removeFirst(1) // Eliminar un entero del Array
print("El primer entero eliminado es \(numeros)")

numeros.removeAll() // Eliminar todos los enteros del Array
print("Todos lo enteros del Array eliminados \(numeros)")

numeros.sorted() // Ordenar los enteros de forma ascendente
print("Ordenado el Array \(numeros)")

numeros.contains(3) // Comprobando si hay un enetero en específico en el Array
print("Comprobando si 3 esta en el Array")




