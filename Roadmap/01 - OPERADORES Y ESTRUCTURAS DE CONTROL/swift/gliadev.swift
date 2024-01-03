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
 * DIFICULTAD EXTRA:
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
// constate no podemos cambiarla
let nombre = "Patata"
// variables podemos cambiarla
var edad = 21


// Operadores
let suma = 5 + 2
let resta = 5 - 3
let multiplicacion = 5 * 3
let division = 5 / 3
let modulo = 5 % 3

print("Aritmeticos: \(suma),\(resta),\(multiplicacion),\(division),\(modulo)")

// operadores logicos
let verdadero = true
let falso = false
// AND && OR || NOT !
print("Logicos: \(verdadero && false), \(verdadero || falso), \(!verdadero)")


// operadores de comparacion
let numeroUno = 5
let numeroDos = 3
print("\(numeroUno == numeroDos)") //  igualdad
print("\(numeroUno != numeroDos)") //  no igualdad distinto
print("\(numeroUno >= numeroDos)")  // mayor  o igual que
print("\(numeroUno <= numeroDos)")  // menos o igual que
print("\(numeroUno > numeroDos)")  // mayor  que
print("\(numeroUno < numeroDos)")  // menor  que
// tendremos el operador === triple de igualdad que lo usamos dentro del ambito de un condicional


// operadores asignación
var contador = 10 // tiene un valor de 10
contador += 5  // le sumamos 5 a contador y contador ahora vale 15
print(contador)
contador -= 3  // contador ahora es 12
print(contador)
contador *= 2  // contador ahora es 24
print(contador)
contador /= 4  // contador ahora es 6
print(contador)

// operadores en Bits



// estructuras de control
// if, else if, else, switch
let edadDos = 17

if edadDos < 18 { // si edadDos es mayor o igual a 18
    print("Con \(edadDos) eres menor de edad")
} else if edadDos >= 18 && edadDos < 60 {
    print("Con \(edadDos) eres un adulto")
} else {
    print("Con \(edadDos) eres un adulto mayor!!!")
}

//switch
switch edadDos {
case 0..<18:
    print("Eres menor de edad.")
case 18..<60:
    print("Eres adulto")
default:
    print("Eres adulto Mayor!!")
}

// bucles for
for i in 1...5 {
    print(i)
}

// while
var contadorTres = 1
while contadorTres <= 3 {
    print("Número: \(contadorTres)")
    contadorTres += 1
    print(contadorTres)
}



// parte extra

//* DIFICULTAD EXTRA:
//* Crea un programa que imprima por consola todos los números comprendidos
//* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//*

for num in 10...55 {
    if num != 16, num % 2 == 0, num % 3 != 0 {
        print(num)
    }
}
