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


class Vehiculo {
    var marca: String
    var modelo: String
    var año: Int
    
    init(marca: String, modelo: String, año: Int) {
        self.marca = marca
        self.modelo = modelo
        self.año = año
    }
    
    func imprimirDatos() {
        print(marca)
        print(modelo)
        print(año)
        
    }
}

var miVehiculo = Vehiculo(marca: "Toyota", modelo: "Corolla", año: 2020)
miVehiculo.imprimirDatos()


//-------------------------------------

class Stack <T>{
    var items: [T]
    
    init(items: [T] ){
        self.items = items
    }
    
    func push(_ element: T) { // Declaro el argumento con _ para que no sea necesario indicar el nombre cuando se le pase en la llamada
        items.append(element)
    }
    
    func pop() -> T? { //Lo declaro como opcional ? por si el array esta vacio
        return items.popLast()
    }
}


let stack = Stack<Int>(items: [1, 2, 3])
stack.push(4)
print(stack.pop() ?? 0) // Uso ?? para que al imprimir no aparezca opcional


class Queue<T>{
    var items: [T]
    
    init(items: [T] ){
        self.items = items
    }
    
    func enqueue(_ element: T) { 
        items.append(element)
    }
    
    func dequeue() -> T? {
        return items.removeFirst()
    }
}

let queue = Queue<Int>(items: [1, 2, 3, 5, 6])
queue.enqueue(7)
print(queue.dequeue() ?? 0)
