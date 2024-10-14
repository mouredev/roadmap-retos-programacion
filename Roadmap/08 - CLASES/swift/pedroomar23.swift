import Foundation

/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

// Clase 
class Person {

    // Atributos
    var name: String 
    var age: Int 
    var city: String 
    var work: String 

    // Inicializador 
    init(name: String, age: Int, city: String, work: String) {
        self.name = name 
        self.age = age 
        self.city = city 
        self.work = work 
    }

    // Funcion para imprimir los atributos 
    func perfil() {
        print("Name: \(name)")
        print("Age: \(age)")
        print("City: \(city)")
        print("Work: \(work)")
    }
}

// Instancia para llamar a los atributos de la clase 
var myDates = Person(name: "James", age: 40, city: "New York", work: "Programer")

// Llamar a la funcion para imprimir en la consola 
myDates.perfil()

// Modificar los atributos de la clase 
myDates.name = "Jason"
myDates.age = 30
myDates.city = "Miami"
myDates.work = "Abogado"

// Actualizar los atributos modificados 
myDates.perfil()

// Extra 
class Pila<Numeros> {

    // Array 
    var numeros: [Numeros] = []

    // Agregar un elemento al array 
    func push(_ numeros: Numeros) {
        return numeros.append(numeros)
    }

    // Eliminar el ultimo elemento
    func pop() -> Numeros? {
        return numeros.popLast()
    }

    peek() -> Numeros? {
        return numeros.last 
    }

    // Imprimir en la consola 
    for numero in numeros {
        print(numero)
    }
}

class Cola<Nombres> {

    // Array
    var nombres; [Nombres] = []

    // Añadir un elemento al array 
    func push(_ nombres: Nombres) {
        return nombres.append(nombres)
    }

    // Eliminar el ultimo elemento 
    func pop() -> Nombres? {
        return nombres.removeLast()
    }

    func peek() -> Nombres? {
        return nombres.removelast 
    }

    // Imprimir en la consola 
    for nombre in nombres {
        print(nombre)
    }
}