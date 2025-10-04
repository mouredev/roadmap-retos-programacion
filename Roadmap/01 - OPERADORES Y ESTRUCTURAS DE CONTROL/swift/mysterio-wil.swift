/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

import Foundation

print("### OPERADORES ###")

// Operadores Aritméticos
print("\n--- Aritméticos ---")
let a = 10
let b = 3
print("Suma: 10 + 3 = \(a + b)")
print("Resta: 10 - 3 = \(a - b)")
print("Multiplicación: 10 * 3 = \(a * b)")
print("División: 10 / 3 = \(a / b)")
print("Módulo: 10 % 3 = \(a % b)")

// Operadores Lógicos
print("\n--- Lógicos ---")
print("AND (true && false): \(true && false)")
print("OR (true || false): \(true || false)")
print("NOT (!true): \(!true)")

// Operadores de Comparación
print("\n--- Comparación ---")
print("Igualdad (10 == 3): \(10 == 3)")
print("Desigualdad (10 != 3): \(10 != 3)")

// Operadores de Asignación
print("\n--- Asignación ---")
var x = 5
x += 2
print("Suma y asignación: x += 2 -> x = \(x)")

// Operador de Pertenencia (rangos)
print("\n--- Pertenencia (Rangos) ---")
let rango = 1...5
print("¿El rango 1...5 contiene 3? \(rango.contains(3))")

// Operadores de Bits
print("\n--- Bits ---")
let p: UInt8 = 10 // 00001010
let q: UInt8 = 3  // 00000011
print("AND a nivel de bits (10 & 3): \(p & q)")
print("OR a nivel de bits (10 | 3): \(p | q)")

/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 */

print("\n### ESTRUCTURAS DE CONTROL ###")

// Condicionales
print("\n--- Condicionales (if, else) ---")
let edad = 18
if edad < 18 {
    print("Eres menor de edad.")
} else {
    print("Eres mayor de edad.")
}

// Iterativas
print("\n--- Iterativas (for-in) ---")
for i in 1...3 {
    print(i)
}

print("\n--- Iterativas (while) ---")
var contador = 3
while contador > 0 {
    print(contador)
    contador -= 1
}

// Manejo de errores
print("\n--- Manejo de errores (do, try, catch) ---")
enum MiError: Error {
    case errorDeEjemplo
}

func puedeLanzarError() throws {
    throw MiError.errorDeEjemplo
}

do {
    try puedeLanzarError()
} catch {
    print("Se capturó un error: \(error)")
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

print("\n### DIFICULTAD EXTRA ###")
for numero in 10...55 {
    if numero % 2 == 0 && numero != 16 && numero % 3 != 0 {
        print(numero)
    }
}
