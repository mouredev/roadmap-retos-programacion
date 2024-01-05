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


// OPERADORES ARITMÉTICOS
let suma = 5 + 3
let resta = 10 - 4
let multiplicacion = 2 * 6
let division = 8 / 2
let modulo = 15 % 7

print("Aritméticos:")
print("Suma: \(suma)")
print("Resta: \(resta)")
print("Multiplicación: \(multiplicacion)")
print("División: \(division)")
print("Módulo: \(modulo)")


// OPERADORES LÓGICOS
let andLogico = true && false
let orLogico = true || false
let notLogico = !true

print("\nLógicos:")
print("AND lógico: \(andLogico)")
print("OR lógico: \(orLogico)")
print("NOT lógico: \(notLogico)")


// OPERADORES DE COMPARACIÓN
let igual = 5 == 5
let diferente = 10 != 5
let mayorQue = 8 > 3
let menorQue = 2 < 7

print("\nDe comparación:")
print("Igual: \(igual)")
print("Diferente: \(diferente)")
print("Mayor que: \(mayorQue)")
print("Menor que: \(menorQue)")


// OPERADORES DE ASIGNACIÓN
var variableAsignada = 42
variableAsignada += 8

print("\nDe asignación:")
print("Variable asignada: \(variableAsignada)")


// OPERADORES DE IDENTIDAD
let objeto1 = "Hola"
let objeto2 = "Hola"
let sonIguales = objeto1 == objeto2

print("\nDe identidad:")
print("Objetos iguales: \(sonIguales)")


// OPERADORES DE PERTENENCIA
let lista = [1, 2, 3, 4, 5]
let contieneTres = lista.contains(3)

print("\nDe pertenencia:")
print("Contiene el número 3: \(contieneTres)")


// OPERADORES DE BITS
let a: UInt8 = 0b00101010
let b: UInt8 = 0b00001111
let resultadoAND = a & b
let resultadoOR = a | b
let resultadoXOR = a ^ b
let desplazamientoIzquierda = a << 1
let desplazamientoDerecha = a >> 1

print("\nDe bits:")
print("AND de bits: \(resultadoAND)")
print("OR de bits: \(resultadoOR)")
print("XOR de bits: \(resultadoXOR)")
print("Desplazamiento izquierda: \(desplazamientoIzquierda)")
print("Desplazamiento derecha: \(desplazamientoDerecha)")


// ESTRUCTURAS DE CONTROL
// Condicionales
let numero = 25

if numero % 2 == 0 {
    print("\nCondicionales: \(numero) es par.")
} else {
    print("\nCondicionales: \(numero) es impar.")
}

// Iterativas
print("\nIterativas: Números entre 10 y 55 (pares, no 16 ni múltiplos de 3):")
for i in 10...55 {
    if i % 2 == 0 && i != 16 && i % 3 != 0 {
        print(i)
    }
}

// Excepciones
enum MiError: Error {
    case errorPersonalizado
}

func lanzarExcepcion() throws {
    throw MiError.errorPersonalizado
}

do {
    try lanzarExcepcion()
    print("\nExcepciones: Operación exitosa.")
} catch MiError.errorPersonalizado {
    print("\nExcepciones: ¡Se ha producido un error personalizado!")
} catch {
    print("\nExcepciones: ¡Se ha producido un error!")
}


//EJERCICIO OPCIONAL
print("Números entre 10 y 55 (pares, no 16 ni múltiplos de 3):")

for numero in 10...55 {
    if numero % 2 == 0 && numero != 16 && numero % 3 != 0 {
        print(numero)
    }
}

