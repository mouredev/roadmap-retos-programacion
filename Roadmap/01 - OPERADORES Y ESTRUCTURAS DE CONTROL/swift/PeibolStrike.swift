//import UIKit
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

// Operadores Aritméticos
let suma = 2 + 3
let resta = 8 - 3
let multiplicacion = 4 * 3
let division = 10 / 2
let modulo = 5 % 2

print("Los operadores aritméticos son: Suma, Resta, Multiplicación, División y Módulo")
print("Suma: \(suma) \nResta: \(resta) \nMultiplicación: \(multiplicacion) \nDivisión: \(division) \nMódulo: \(modulo) \n")

// Operadores Lógicos
let operadorNot = !false
let operadorAnd = true && false
let operadorOr = true || false

print("Los operador lógicos son: NOT(!), AND(&&) y OR(||)")
print("Operador lógico NOT: \(operadorNot) \nOperador lógico AND: \(operadorAnd) \nOperador lógico OR: \(operadorOr) \n")

//Operadores de Comparación
let igual = 2 == 2
let noIgual = 2 != 4
let mayor = 8 > 3
let mayorIgual = 7 >= 6
let menor = 9 < 2
let menorIgual = 9 <= 16

print("Los operadores de comparación son: igual(==), no igual(!=), mayor(>), menor(<), mayor o igual(>=) y menor o igual(<=)")
print("Operador de comparación igual: \(igual) \nOperador de comparación no igual: \(noIgual) \nOperador de comparación mayor: \(mayor) \nOperador de comparación menor: \(menor) \nOperador de comparación mayor o igual: \(mayorIgual) \nOperador de comparación menor o igual: \(menorIgual) \n")

// Operadores de asignación
print("Los operadores de asignación sirven para inicializar o actualizar el valor de una variable")
var asignarValor = 11
asignarValor += 4
print("Aqui sumamos: \(asignarValor)")
asignarValor -= 5
print("Aqui restamos: \(asignarValor)")
asignarValor *= 2
print("Aqui multiplicamos: \(asignarValor)")
asignarValor /= 5
print("Aqui dividimos: \(asignarValor)")
print("Esto se realiza sobre el útlimo valor que va teniendo nuestra variable \n")

// Operadores de Identidad
class Persona {
    var nombre: String

    init(nombre: String) {
        self.nombre = nombre
    }
}
let persona1 = Persona(nombre: "Pablo")
let persona2 = Persona(nombre: "Brais")
print("Los operadores de identidad son: Idéntico a (===) y No idéntico a (!==)")
if persona1 === persona2 {
    print("persona1 y persona2 tienen el mismo valor")
} else {
    print("persona1 y persona2 no tienen el mismo valor")
}
if persona1 !== persona2 {
    print("persona1 y persona2 no tienen el mismo valor \n")
} else {
    print("persona1 y persona2 tienen el mismo valor \n")
}

// Operadores de pertenencia
print("Los operadores de pertenencia son: constaint, constaint(where: ) y isSubset(of: )")
let numeros = [1, 2, 3, 4, 5]

if numeros.contains(3) {
    print("El número 3 está en el array")
} else {
    print("El número 3 no está en el array")
}

let nombres = ["Pablo", "Juan", "Brais", "Carlos"]

if nombres.contains(where: { $0.count > 4 }) {
    print("Hay nombres con más de 4 caracteres en la lista")
} else {
    print("No hay nombres con más de 4 caracteres en la lista")
}

let conjunto1: Set<Int> = [1, 2, 3]
let conjunto2: Set<Int> = [2, 3]

if conjunto2.isSubset(of: conjunto1) {
    print("El conjunto2 es un subconjunto de conjunto1  \n")
} else {
    print("El conjunto2 no es un subconjunto de conjunto1 \n")
}

// Operadores de bits
print("Los operadores de bits son: AND(&), OR(|), XOR(^), NOT(~), Desplazamiento a la izquierda(>>) y Desplazamiento a la derecha(<<)")
let resultadoAnd = 0b1010 & 0b1100
let resultadoOr = 0b1010 | 0b1100
let resultadoXor = 0b1010 ^ 0b1100
let resultadoNot = ~0b1010
let resultadoDerecha = 0b0010 << 1
let resultadoIzquierda = 0b1000 >> 2
print("AND: \(resultadoAnd) \nOR: \(resultadoOr) \nXOR: \(resultadoXor) \nNOT \(resultadoNot) \nDesplazamiento a la Derecha: \(resultadoDerecha) \nDesplazamiento a la Izquierda: \(resultadoIzquierda) \n")

// Estructuras de Control

// Condicionales
print("Las estructuras de control condicionales son: if, switch, guard y condicionales ternarias")
    // if
let numero = 20
if numero % 3 == 0 {
    print("IF: El número \(numero) es impar ")
} else {
    print("IF: El número \(numero) es par")
}
    // switch
let opcion = 2

switch opcion {
    case 1:
        print("SWITCH: Opción 1 seleccionada")
    case 2:
        print("SWITCH: Opción 2 seleccionada")
    default:
        print("SWITCH: Opción no reconocida")
}

    // guard
func validarEdad(edad: Int) {
    guard edad >= 18 else {
        print("GUARD: Eres menor de edad")
        return
    }

    print("GUARD: Eres mayor de edad")
}

validarEdad(edad: 20)

    // Condicionales ternarias
let esPar = 10 % 2 == 0 ? true : false
print("Condicionales ternarias: \(esPar) \n")


// Iterativas
print("Las estructuras de control iterativas son: For-In, While y Repeat-While")
    // For-In
let numeros1 = [1, 2, 3, 4, 5]

for numero in numeros1 {
    print(numero)
}

    // While
var contador = 0

while contador < 5 {
    print("El contador en la estructura de control While vale \(contador)")
    contador += 1
}

    // Repeat-While
var contador1 = 0

repeat {
    print("El contador en la estructura de control Repeat-While vale \(contador1)")
    contador1 += 1
} while contador1 < 5
print("\n")

// Excepciones
enum ErrorPersonalizado: Error {
    case errorPersonalizado
}

func lanzarExcepcion() throws {
    throw ErrorPersonalizado.errorPersonalizado
}

do {
    try lanzarExcepcion()
    print("Excepciones: No hay errores")
} catch ErrorPersonalizado.errorPersonalizado {
    print("Excepciones: Hay un error personalizado")
} catch {
    print("Excepciones: Hay un error")
}
print("\n")

// Ejercicio Opcional
/*
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for numero in 10...55 {
    if numero % 2 == 0 && numero != 16 && numero % 3 != 0 {
        print("El número \(numero) es par, no es 16 y no es múltiplo de 3")
    }
}