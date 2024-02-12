import Foundation

//----------------------- Operadores -------------------
// Asignación
let nombre = "Diego"
var edad: Int = 27
print("\(nombre) tiene \(edad) años")

// Aritméticos

let suma = 1 + 2
print("Suma: \(suma)")

let resta = 3 - 2
print("Resta: \(resta)")

let multiplicacion = 3 * 2
print("Multiplicación: \(multiplicacion)")

let division = 10 / 2
print("División: \(division)")

let concatenacion = "hello " + "world"
print(concatenacion)

let resto = 9 % 8
print("Resto: \(resto)")

let tres = 3
let negativo = -tres
print("Negativo: \(negativo)")

let cuatro = -4
let positivo = +tres
print("Positivo: \(positivo)")

var compuesto = 2
compuesto += 2
print("Compuesto: \(compuesto)")

//  Comparación
print(1 == 1)
print(2 != 1)
print(2 > 1)
print(1 < 2)
print(1 >= 1)
print(2 <= 1)

// Ternaria
// pregunta ? respuesta1 : respuesta2
let resultado = 2 + 1 == 3 ? true : false
print("Ternaria: \(resultado)")

// Nil-Coalescing
var color: String? = nil
var colorCoche = color != nil ? "Es \(color!)" : "Es nulo"
print(colorCoche)

color = "rojo"
colorCoche = "Es \(color!)" ?? "Es nulo"
print(colorCoche)

// Rango
for index in 1...5 {
    print(index)
}

for index in 1..<5 {
    print(index)
}

let names = ["Anna", "Alex", "Brian", "Jack"]
for name in names[2...] {
    print(name)
}

// Lógicos
print(!(1 == 1))
print(1 == 1 && 2 > 1)
print(1 == 1 || 2 < 1)

// --------------------------------- Estructuras de control --------------------------------

// Bucles for-in
let nombres = ["Anna", "Alex", "Brian", "Jack"]
for nombre in nombres {
    print("Hello, \(nombre)!")
}

// Bucle While 
var numero = 0
while numero < 4 {
    print(numero)
    numero += 1

}

// Bucle Repeat-while
repeat {
    print(numero)
    numero += 1
} while numero < 8

// Condicional if
if numero == 7 {
    print("El número es 7")
} else {
    print("No es 7")
}

// Condicional switch
switch numero {
    case 7:
        print("Es 7")
    case 8:
        print("Es 8")
    default:
        print("No es 7 ni 8")
}

// Transferencia de control
for index in 1...5 {
    if index == 3 {
        continue
    }

    print(index)
}

for index in 1...5 {
    if index == 3 {
        break
    }

    print(index)
}

numero = 5
switch numero {
    case 5:
        print("Es 5")
        fallthrough
    default:
        print("Esto no debería de imprimirse")
}

// Etiquetas
mainLoop: for _ in 1...5 {
    let letras = ["a", "b", "c"]

    secondaryLoop: for letra in letras {

        if letra == "b" {
            break secondaryLoop
        }
        print(letra)
    }
}

// Guard
let people = ["juan", "pablo"]

guard let person = people.first else {
    fatalError("No hay personas")
}
print(person)

// Defer
var score = 1
if score < 10 {
    defer {
        print(score)
    }
    score += 5
}

// Error Handling
enum Error: Swift.Error {
    case error1
    case error2
}

func error() throws {
    throw Error.error1
}

do {
    try error()
} catch Error.error1 {
    print("Error 1")
} catch Error.error2 {
    print("Error 2")
} catch {
    print("Error desconocido")
}

// ---------------------------------- Ejercicio extra ----------------------------------
for index in 10...55 {

    if index % 2 == 0 {
        
        if index != 16 && index % 3 != 0 {
            print(index)
        }
    }

}