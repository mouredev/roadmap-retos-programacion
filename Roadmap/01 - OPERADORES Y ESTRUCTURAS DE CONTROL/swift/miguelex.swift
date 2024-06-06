import Foundation

// Operadores aritmeticos

let a = 5      
let b = 3      

print("Aritmeticos:")
print("5 + 3 = \(a + b)")
print("5 - 3 = \(a - b)")
print("5 * 3 = \(a * b)")
print("5 / 3 = \(5 / 3)")
print("5 % 3 = \(5 % 3)")

// Operadores de comparación

print("\nDe comparación:")
print("5 == 5 --> \(5 == 5)")
print("10 != 5 --> \(10 != 5)")
print("8 > 3 --> \(8 > 3)")
print("2 < 7 --> \(2 < 7)")

// Operadores de asignación

var edad = 48

print("\nDe asignación:")
print("Mi edad actual: \(edad)")
print("Mi edad el año que viene: \(edad + 1)")
print ("Mi edad hace 5 años: \(edad - 5)")

// Operadores logicos

let verdadero = true
let falso = false

print("\nLógicos:")
print("verdadero AND falso: \(verdadero && falso)")
print("verdadero OR falso: \(verdadero || falso )")
print("NOT verdadero: \(!verdadero)")

// Operadores de identidad

let saludo = "Hola"
let despedida = "Adios"

print("\nIdentidad:")
print("Objetos iguales: \(saludo == despedida)")

// Operadores de pertenencia

let names = ["Migue", "Angel", "Pepe", "Juan", "Rafa"]

print("\nPertenencia:")
print("Contiene el nombre de Migue: \(names.contains("Migue"))")

// Operadores de bits

let x: UInt8 = 0b00111001
let y: UInt8 = 0b00011011

print("\nDe bits:")
print("AND de bits: \(x & y)")
print("OR de bits: \(x | y)")
print("XOR de bits: \(x ^ y)")
print("Desplazamiento izquierda: \(x << 1)")
print("Desplazamiento derecha: \(x >> 1)")

// Estructuras de control

let mes = 2

print("If... else")

if mes != 2 {
    print("Otro mes diferente a febrero")
} else  {
    print("Febrero")
} 

print("switch")

switch mes {
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    default:
        print("Mes desconocido")
}

let nombres = ["Migue", "Angel", "Pepe", "Juan", "Rafa"]

print("For... in")
for nombre in nombres {
    print("Hola \(nombre)")
}


for i in 1...5 {
    print(i)
}

print("while")
var i = 1
while i <= 5 {
    print(i)
    i += 1
}

print("repeat... while")
i = 1
repeat {
    print(i)
    i += 1
} while i <= 5


// Extra

for i in 10...55 {
    if i % 2 == 0 && i != 16 && i % 3 != 0 {
        print(i)
    }
}















