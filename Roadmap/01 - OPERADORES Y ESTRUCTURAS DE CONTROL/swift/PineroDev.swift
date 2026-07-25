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

import Foundation

//Operadores Aritméticos

var suma: Double = 10 + 20
var resta: Double = 4.6 - 2.3
var multiplicacion: Double = 2.5 * 3.2
var division: Double = 10 / 2
var modulo: Int = 5 % 2

//Operadores Logicos

var AND: Bool = true && false
var OR: Bool = true || false
var NOT: Bool = !true

//Operadores de asignación
var asigSuma: Int = 2
asigSuma += 10
var asigResta: Int = 20
asigResta -= 1
var asigMultiplicacion: Int = 3
asigMultiplicacion *= 2
var asigDivision: Int = 7
asigDivision /= 2
var asigModulo: Int = 4
asigModulo %= 2

//Operadores de comparación
var operadorIgual: Bool = 10 == 10
var operadorDiferente: Bool = 7 != 11
var operadorMenor: Bool = 5 < 13
var operadorMenorIgual: Bool = 45 <= 45
var operadorMayor: Bool = 16 > 2
var operadorMayorIgual: Bool = 34 >= 65

//----------------------------------------

// Estructuras de control

//For - in
let palabra: String = "Mandarina"
for letra in palabra {
    print(letra)
}

//While
var contador: Int = 1
while contador <= 5 {
    print(contador)
    contador += 1
}

// if (Condicional)
var contador2: Int = 1
if contador2 < 100{
    print("contador2 es menor que 100")
}else {
    print ("contador2 es mayor que 100")
}


// Guard (Condicional)
var numRandom: Int = (Int.random(in: 1..<100))
func pruebaGuard(){
    guard numRandom  >= 50 else {
        print(numRandom, "es menor que 50" )
        return
    }
    
    print(numRandom, " es mayor que 50")
}
pruebaGuard()


//Switch (Condicional)
var numSubmarinos: Int = 5
switch numSubmarinos {
case 0:
    print("No hay submarinos en el mar")
case 1:
    print("Hay un submarino en el mar")
default:
    print("Hay \(numSubmarinos) submarinos en el mar")
}

//-----------------------------------------


for num in 10...55 {
    if num == 16{
        
    }else if num % 3 == 0{
        
    }else {
        print(num)
    }
}
