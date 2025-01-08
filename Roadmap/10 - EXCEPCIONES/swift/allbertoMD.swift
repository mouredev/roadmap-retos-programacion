import Foundation


// FUNCIÓN DIVISIÓN
print("\nFUNCIÓN DIVISIÓN")


// Representación del error, de la función de la division.
enum DivisonError: Error {
    case divisionByZero
}

// Definicion de la funcion division con la capacidad de lanzar errores.
func division(number1 n1: Float, numner2 n2: Float) throws -> Float {
    // Lanza el error si el n2 es igual a cero.
    guard n2 != 0 else {
        throw DivisonError.divisionByZero
    }
    return n1 / n2
}

print("\nIntroduce el dividendo:")
var dividend: Float = 0.0
if let input = readLine(), let n1Float = Float(input) {
    dividend = n1Float
}

print("\nIntroduce el divisor:")
var divisor: Float = 0.0
if let input = readLine(), let n2Float = Float(input) {
    divisor = n2Float
}

// Llama a la función y captura el error.
do {
    let result: Float = try division(number1: dividend, numner2: divisor)
    print("\n", result)
} catch DivisonError.divisionByZero {
    print("\nERROR -> división entre cero.")
}


// FUNCIÓN INDICE DEL ARRAY
print("\nFUNCIÓN INDICE DEL ARRAY")


// Representa los errores de la función indice del array.
enum ArrayIndexError: Error {
    case indesUpper
    case indexLower
}

// Declaración de la funcion indice del array con la capacidad de lanzar errores.
func arrayChecker(array arr: [String], index: Int) throws -> String {
    guard index < arr.count else {
        throw ArrayIndexError.indesUpper
    }
    guard index > 0 else {
        throw ArrayIndexError.indexLower
    }

    let value = arr[index]
    
    return value
}

print("\nIntroduce los elementos del array:\nIntroduce exit para parar de añadir.")
var array: [String] = []
while true {
    if let input = readLine() {
        if input == "exit" {
            break
        }
        array.append(input)
    }
}

print("\nIntroduce el indice:")
var arrayIndex = 0
if let input = readLine(), let indexInt = Int(input) {
    arrayIndex = indexInt
}

// Llama a la función y captura los errores.
do {
    let value = try arrayChecker(array: array, index: arrayIndex)
    print("\n", value)
} catch ArrayIndexError.indesUpper {
    print("\nERROR -> indice alto")
} catch ArrayIndexError.indexLower {
    print("\nERROR -> Indece bajo")
}



// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA")


// Representa los errores de la función takeCoffe.
enum BuyCoffeError: Error {
    case invalidCoffe
    case insuficientCoins(coinsNeeded: Int)
    case outOfStock
}

// Modelo de datos del Coffe.
struct Coffe {
    var price: Int
    var count: Int
}

// Define un diccionario con el nombre del cafe y el modelo de datos.
var coffesMenu: [String: Coffe] = [
    "Capuchino": Coffe(price: 7, count: 4),
    "Late": Coffe(price: 4, count: 10),
    "Mocca": Coffe(price: 9, count: 0)
]

// Define la función takeCoffe con la capacidad de lanzar errores.
func takeCoffe(coffeName item: String, coins: Int, amount: Int) throws {
    let coinsInserted = coins

    guard let coffe = coffesMenu[item] else {
        throw BuyCoffeError.invalidCoffe
    }
    guard coffe.count > amount else {
        throw BuyCoffeError.outOfStock
    }
    guard coffe.price <= coinsInserted else {
        throw BuyCoffeError.insuficientCoins(coinsNeeded: coffe.price - coins)
    }
    var coffeChoosen = coffe
    coffeChoosen.count -= amount
    coffesMenu[item] = coffeChoosen

    print("Tu \(item) esta listo.")
}

print("\nQue cafe quieres?")
var coffe = ""
if let input = readLine() {
    coffe = input
}

print("\nCuantos cafes quieres?")
var amount = 0
if let input = readLine(), let amounttInt = Int(input) {
    amount = amounttInt
}

print("\nIntroduce las monedas.")
var coins = 0
if let input = readLine(), let coinsInt = Int(input) {
    coins = coinsInt
}

// Llama a la función y captura los errores.
do {
    try takeCoffe(coffeName: coffe, coins: coins, amount: amount)
} catch BuyCoffeError.invalidCoffe {
    print("\nERROR -> Ese cafe no esta disponible.")
} catch BuyCoffeError.insuficientCoins(let coinsNeeded) {
    print("\nERROR -> Monedas insuficientes, faltan \(coinsNeeded) monedas.")
} catch BuyCoffeError.outOfStock {
    print("\nERROR -> Cafe agotado.")
} catch {
    print("\nERROR -> \(error.localizedDescription)")
}



