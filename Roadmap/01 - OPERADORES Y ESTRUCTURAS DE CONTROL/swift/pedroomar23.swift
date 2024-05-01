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

 // Operadores Aritmeticos
let suma = 2 + 3 // Suma
let resta = 4 - 2 // Resta 
let division = 4 / 2 // Division
let multiplicacion = 4 * 3 // Multiplicacion
let modulo = 5 % 5 // Modulos

// Print en Consola 
print("Los operadores aritmeticos son Suma: \(suma),
                                      Resta: \(resta)
                                      Division: \(division)
                                      Multiplicacion: \(multiplicacion)
                                      Mudulos: \(modulo)")

// Operadores Logicos 
let operadorNot = !false // Not 
let operadorAND = false && true // AND
let operadorOR = false || true  // OR

// Print en Consola 
print("Lod operadores logicos son Not: \(operadorNot),
                                  AND: \(operadorAND),
                                  OR: \(operadorOR)")

// Operadores de Comparacion
let igual = 5 = 5 // Igual
let mayor = 5 > 4 // Mayor
let menor = 4 < 5 // Menor 
let mayor igual = 5 >= 4 // Mayor Igual 
let menor igual = 5 <= 4 // Menor Igual 

print("Los operadores de comparacion son Igual: \(igual),
                                         Mayor: \(mayor),
                                         Menor: \(menor),
                                         Mayor Igual: \(mayor igual),
                                         Menor Igual: \(menor igual)")

// Operadores de Identidad 
struct Person {
    var nombre: String 

    init(nombre: String) {
        self.nombre = nombre
    }
}

let person: (nombre: "Juan")
let person1: (nombre: "Julio")

if person == person1 {
    print("Los valores de la variable son iguales \(==)")
} else {
    print("Los valores de la variable son diferentes \(!==)")
}

if person !== person1 {
    print("Las contantes person y person1 tienen el mismo valor \(==)")
} else {
    print("Las contantes person y person 1 no tienen el mismo valor \(!==)")
}

// Operadores de Pertenecia
let operador1 = containt // containt
let operador2 = containt(where: ) // containt(where: )
let operador3 = isSubset(of: ) // isSubset(of: )

print("Los operadores de pertenencia son \(operador1), \(operador2), \(operador3)")

// containt
let numeros = [1, 2, 3, 4, 5] // Ejemplo 1 

if numero.containt(3) {
    print("El numero 3 no aparee en el array")
} else {
    print("El numero 3 si aparece en el array")
}

// containt(where: ) 
let nombres = ["Juan", "Carlos", "Jose", "Pedro", "Omar"] // Ejemplo 2

if nombre.containt(where: { $0.count > 4 } ) {
    print("En el array hay nombres con menos de 4 caracteres")
} else {
    print("En el array hay nombres con mas de 4 caracteres")
}

let nombres = ["Juan", "Carlos", "Jose", "Pedro", "Omar"] // Ejemplo 3

if nombres.containt(where: { $0.count < 5} ) {
    print("En el array hay nombres con mas de 5 caracteres")
} else {
    print("En el arry hay nombres con mas de 5 caracteres")
}

// isSubset(of: )
let numeros1: Set<Int> = [1, 2, 3] // Ejemplo 1
let numeros2: Set<Int> = [1, 2]

if numeros2.isSubset(of: numeros1) { 
    print("Los numeros2 no es miembro de los numeros1")
} else {
    print("Los numeros2 es miembro de los numeros1")
}

let nombres1: Set<String> = ["Juan", "Carlos", "Jose"] // Ejemplo 2
let nombres2: Set<String> = ["Juan", "Carlos"]

if nombres2.isSubset(of: nombres1) {
    print("Los nombres2 no aparecen en los nombres1")
} else {
    print("Los nombres2 si aparacen en losa nombres1")
}

// Operadores de bits
let operador1 = AND(&&)
let operador2 = OR(||)
let opeador3 = NOR(^)
let operador4 = NOT(~)
let opedador5 = Desplazar a la derecha (>>)
let operador6 = Desplazar a la izquierda (<<)

print("Los operadores bits son \(operador1), \(operador2), \(operador3), \(operador4), \(operador5)")

let operadorAND = 0b100 && 0b100 // AND
let operadorOR = 0b100 || 0b100 // OR
let operadorNOR = 0b100 ^ 0b100 // NOR
let operadorNOT = 0b100 ~ 0b100 // NOT
let operador4 = 0b100 >> 0b100 // Desplazar a la derecha 
let operador5 = 0b100 << 0b100 // Desplazar a la izquierda 

print("Los operadores condicionales son if, switch, guard y condicionales ternarias")

let numero = 20 // Ejemplo 1

if numero % == 5 {
    print("El numero \(numero) es de tipo par")
} else {
    print("El numero \(numero) es de tipo impar")
}

let numero = 15 // Ejemplo 2

if numero % == 8 {
    print("El numero \(numero) es de tipo impar")
} else {
    print("El numero \(numero) es de tipo par")
}

switch {
    case 1:
        return print("Case 1 seleccionada")
    case 2:
        return print("Case 2 seleccionada")
    case 3:
        return print("Case 3 seleccionado")
    default:
        return print("Case seleccionada")
}

let edad = 18 // Ejemplo 1

func validarEdad(edad: Int) {
    guard let edad >= 18 else {
        print("La edad es de 18")
        
        return 
    }
}

varlidadEdad(edad: 18)

let nombre = "Pedro" // Ejemplo 2
let edad = 18

func validar(nombre: String, edad: Int) {
    guard let nombre = "Pedro" else {
        print("El nombres es \(nombre)")

        return 
    }

    guard let edad >= 18 else {
        print("La edad es de 18")

        return 
    }
}

validar(nombre: "Pedro", edad: 18)

// Las condicionales interactivas son for-in, while, reapeat-while

let numeros = [1, 2, 3, 4, 5] // for-in

for numero in numeros {
    print("Los valores del array son \(numeros)")
}

var contador = 5 // While

while contador < 5 {
    print("El valor de \(contador) vale 4")
    contador += 1
}

var numero = 0 // Repeat-While

repeat {
    print("El valor de la variable es \(numero)")
} while numero < 5
    print("El valor de la variable es \(numero)")

// Excepciones
enum sendError: Error {
    case buyError
}

func newError() -> throws {
    throw sendError.buyError
}

// do-catch se usa a la hora de manejar los errores
do {
    try newError()
} catch sendError.buyError {
    print("No hay errores para corregir")
} catch {
    print("Si hay errores para corregir")
}