import Foundation
// Reto #08 CLASES

// Definimos la clase
class Spartan {
    var name: String
    var id: Int
    var rank: String

    init(name: String, id: Int, rank: String) {
        self.name = name
        self.id = id
        self.rank = rank
    }

    func printData() {
        print("Name: \(name)")
        print("Spartan ID: \(id)")
        print("Rank: \(rank)")
    }
}

var spartanSoldier = Spartan(name: "John", id: 117, rank: "Master Chief Petty Officer of the Navy")
spartanSoldier.printData()

// Modificación de los datos introducidos previamente en los datos de los atributos de la clase
spartanSoldier.name = "Linda"
spartanSoldier.id = 058
spartanSoldier.rank = "Petty Officer Second Class"

spartanSoldier.printData()

// 🧩 DIFICULTAD EXTRA 🧩 - CLASE PILA Y COLA

// Pila/Stack
class Stack<T> {
    var items: [T] = []

    // Adición de elementos dentro del stack
    func push(_ items: T) {
        items.append(item)
    }
    // Supresión de elementos dentro del stack
    func pop() -> T? {
        return items.popLast()
    }
    // Retorna el nº de elementos dentro del Stack
    func count() -> Int {
        return items.count
    }
    // Imprimir el contenido del Stack
    func printData() {
        print("Stack: ")
        for item in items {
            print(item)
        }
    }
}

// Cola/Queue
class Queue<T> {
    var items: [T] = []
    items.append(item)
}

func dequeue() -> T? {
    if items.isEmpty {
        return nil
    } else {
        return items.removeFirst()
    }
}

func count() -> Int {
    return items.count
}

func printData() {
    print("Queue: ")
    for item in items {
        print(item)
    }
}

