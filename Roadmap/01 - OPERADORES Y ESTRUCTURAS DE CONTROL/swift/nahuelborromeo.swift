import Foundation

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


// OPERADORES ARITMÉTICOS:
let suma = 5 + 2
let resta = 10 - 3
let multiplicacion = 10 * 5
let division = 21 / 3
let modulo = 15 % 4
let potencia = pow(2.0, 3.0)

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)
print("Módulo: ", modulo)
print("Potencia: ", potencia)


// OPERADORES LÓGICOS
let andOperator = true && true
let orOperator = true || false
let notOperator = !true

print("\nOperador AND: ", andOperator)
print("Operador OR: ", orOperator)
print("Operador NOT: ", notOperator)

// OPERADORES DE COMPARACIÓN

let igual = 5 == 5
let distinto = 4 != 5
let mayor = 7 > 3
let menor = 6 < 2
let mayorOIgual = 7 >= 2
let menorOIgual = 6 <= 6

print("\nIgual: ", igual)
print("Distinto: ", distinto)
print("Mayor que: ", mayor)
print("Menor que: ", menor)
print("Mayor o igual que: ", mayorOIgual)
print("Menor o igual que: ", menorOIgual)


// OPERADORES DE ASIGNACIÓN
var x = 5 //Operador de asignación
x += 2 //Más igual
x -= 4 //Menos igual
x *= 3 //Por igual
x /= 2 //Entre igual

print("\nAsignación: ", x)

// Operadores de identidad
let a = [1, 2, 3]
let b = [1, 2, 3]
let identidad = a == b
let noIdentidad = a != b

print("\nOperadores de identidad:")
print("Idéntico:", identidad)
print("No idéntico:", noIdentidad)

// Operadores de pertenencia
let lista = [1, 2, 3, 4, 5]
let pertenece = 3
let noPertenece = 6
print("\nOperadores de pertenencia:")
print("Pertenece:", lista.contains(pertenece))
print("No pertenece:", !lista.contains(noPertenece))

// Operadores de bits
let bitwiseAnd = 5 & 3
let bitwiseOr = 5 | 3
let bitwiseXor = 5 ^ 3
let bitwiseNot = ~5
let shiftIzquierda = 5 << 1
let shiftDerecha = 5 >> 1

print("\nOperadores de bits:")
print("AND:", bitwiseAnd)
print("OR:", bitwiseOr)
print("XOR:", bitwiseXor)
print("NOT:", bitwiseNot)
print("Shift izquierda:", shiftIzquierda)
print("Shift derecha:", shiftDerecha)

// Estructuras de control

// Condicionales
if 6 > 2 {
    print("\nCondicional:")
    print("5 es mayor que 3")
}

// Iterativas
print("\nIterativas:")
for i in 10...55 {
    if i == 16 || i % 3 == 0 {
        continue
    }
    print(i)
}

// Excepciones
print("\nExcepciones:")
do {
    let resultado = try dividir(dividendo: 30, divisor: 0)
    print(resultado)
} catch {
    print("Error: división por cero")
}

func dividir(dividendo: Int, divisor: Int) throws -> Int {
    if divisor == 0 {
        throw CustomError.divisionByZero
    }
    return dividendo / divisor
}

enum CustomError: Error {
    case divisionByZero
}

