import Foundation

// RETO #01 OPERADORES Y ESTRUCTURAS DE CONTROL

// OPERADORES DE ASIGNACIÓN
/* El operador (=) no devuelve ningún valor.
Su función es asignarle al operando de la izq,
un valor con el operando de la dch. */

var myVariable = 2.4
var mySecondVariable = 6.2
var myThirdVariable = 4.8

myVariable = myThirdVariable
print("Operador de asignación:", myVariable)


// OPERADORES ARITMÉTICOS
/* Swift soporta los operadores aritméticos estándar
para todos los tipos numéricos. 
    - Suma(+)
    - Resta(-)
    - Multiplicación(*)
    - División(/)*/
let miSuma = 4 + 2 // Esto es una suma
// Podemos asignar y realizar una suma en una misma operación
let otraSuma = 4
otraSuma += 2
print(otraSuma)
// Esta sería otra forma de hacer la asignación anterior.
let otraSuma = 4
otraSuma = otraSuma + 2
print(otraSuma)

let miResta = 4 - 2 // Esto es una resta
// Asignar y restar
let otraResta = 4
otraResta -= 2
print(otraResta)
// Otra forma de asignar y operar.
let otraResta = 4
otraResta = otraResta - 2
print(otraResta)

let miMultiplicacion = 4 * 2 // Esto es una multiplicación
// Asignar y multiplicar
let otraMultiplicacion = 4
otraMultiplicacion *= 2
print(otraMultiplicacion)
// Otra forma de asignar y operar
let otraMultiplicacion = 4
otraMultiplicacion = otraMultiplicacion * 2
print(otraMultiplicacion)

let division = 4 / 2 // Esto es una división
// Asignar y dividir
let otraDivision = 4
otraDivision /= 2
print(otraDivision)
// Otra forma de asignar y dividir
let otraDivision = 4
otraDivision = otraDivision / 2
print(otraDivision)

let resto = 9 % 4 // Esto es un operador módulo/resto.
// Asignar y calcular el resto
let otroResto = 9
otroResto %= 4
print(otroResto)


// OPERADORES DE COMPARACIÓN
/* Los operadores de comparación devuelve un valor
booleano indicando si el enunciado es (true) o (false). Estos
son los operadores con los que cuenta Swift:
    - Igual que (==)
    - No igual que (!=)
    - Mayor que (>)
    - Menor que (<)
    - Mayor o igual que (>=)
    - Menor o igual que (<=) */
var igual = 1 == 1 // (true) 1 es igual a 1
var noIgual = 2 != 1 // (true) 2 no es igual a 1
var mayorQue = 2 > 1 // (true) 2 es mayor que 1
var menorQue = 1 < 2 // (true) 1 es menor que 2
var mayorIgual = 1 <= 1 // (true) 1 es mayor o igual que 1
var menorIgual = 2 <= 1 // (false) 2 no es menor o igual que 1


// OPERADORES LÓGICOS
/* Los operadores lógicos modifican los valores lógicos
booleanos. Swift soporta tres operadores lógicos básicos:
    - NO (NOT) lógico (!)
    - Y (AND) lógico (&&)
    - O (OR) lógico (||)*/
let acceptConst = false
if !acceptConst {
    print("No acepta el consentimiento")
} /* Declaramos la variable y decimos que es falsa.
Entonces, si NO se acepta el consentimiento (!acceptConst es true) =
(acceptConst es false). Sale el print.*/

let inputPin = true
let retinaScan = false

if inputPin && retinaScan {
    print("Welcome home Mr. Stark")
} else {
    print("ACCESS DENIED")
}
/* Ambos valores deben ser (true) para que toda la expresión
sea (true). Si uno de los valores es (false) la expresión será
(false). Si el primer valor es (false) el segundo, no será evaluado.
Evaluación cortocircuito */

let inputPin = false
let retinaScan = true

if inputPin || retinaScan {
    print("Welcome home, Mr. Stark")
} else {
    print("ACCESS DENIED")
}
/* El operador lógico O (OR) también utiliza la evaluación
cortocircuito para evaluar las expresiones. Si uno de los dos
valores booleanos es (true), toda la expresión es (true).*/


// OPERADORES DE BITS
let areUaOne: UInt8 = 0b00001111
let invertedBits = ~areUaOne // Esto es igual a 11110000
// Operador bit a bit AND (&)
let firstSixBits: UInt8 = 0b11111100
let lastSixBits: UInt8 = 0b00111111
let middleFourBits = firstSixBits & lastSixBits // Esto es igual a 00111100
// Operador bit a bit OR (|)
let someBits: UInt8 = 0b10110010
let moreBits: UInt8 = 0b01011110
let combineBits = someBits | moreBits // Esto es igual a 11111110
// Operador bit a bit XOR (^)
let firstBits: UInt8 = 0b00010100
let otherBits: UInt8 = 0b00000101
let outputBits = firstBits ^ otherBits // Esto es igual a 00010001
// Desplazamiento izquierda/derecha
let shiftBits: UInt8 = 4 // Equivale a 00000100 en binario
shiftBits << 1 // Equivale a 00001000 en binario
shiftBits << 2 // Equivale a 00010000 en binario
shiftBits >> 1 // Equivale a 00000010 en binario
shiftBits >> 2 // Equivale a 00000001 en binario
// Ejemplo con operadores bit a bit.
let firstConstantBit: UInt8 = 0b00010100
let secondConstantBit: UInt8 = 0b00000101
let operatorAnd = firstConstantBit & secondConstantBit
let operatorOr = firstConstantBit | secondConstantBit
let operatorXOR = firstConstantBit ^ secondConstantBit
let shiftLeft = firstConstantBit << 2
let shiftRight = firstConstantBit >> 2

print("Bitwise AND (&):", operatorAnd)
print("Bitwise OR (|):", operatorOr)
print("Bitwise XOR (^):", operatorXOR)
print("Bitwise Left Shift (<<):", shiftLeft)
print("Bitwise Right Shift (>>):", shiftRight)


// OPERADORES DE IDENTIDAD
/* Podemos saber si dos constantes o variables se refieren
a la misma instancia de una clase. Para esto Swift ofrece
dos operadores de identidad:
    - Idéntico a (===)
    - No idéntico a (!==) */
let person1 = "Alan Turing"
let person2 = "Alan Turing"
let scientific = person1 == person2

print("Scientifics refer to Alan Turing:", scientific)


// OPERADORES DE PERTENENCIA
/* Este tipo de operadores evalúan si un objeto (x)
pertenece a otro. Como si quisieramos saber si dentro de
un contenedor hay un objeto determinado.*/
let container = ["MacBook", "iPad", "iPhone", "AirPods"]
let containAirPods = container.contains("AirPods")
let containAppleWatch = container.contains("Apple Watch")

print("Are there any AirPods in the container?:", containAirPods)
print("Are there any Apple Watch in the container?: ", containAppleWatch)


// ESTRUCTURAS DE CONTROL
/* Condicionales: Este tipo de estructuras de control nos
sirven cuando necesitamos que el valor de alguna de las variables
o de alguna condición sea evaluada para posteriormente, se ejecute
la instrucción. */
let radioBohr: Double = 52.9

if radioBohr != 52.9 {
    print("Bohr radius is correct:", radioBohr, "NO")
} else {
    print("Bohr radius is correct:", radioBohr, "YES")
}

/* Iterativas: Son instrucciones repetitivas, también denominado
bucle. Su finalidad es ejecutar las mismas instrucciones de código
una y otra vez siempre y cuando se cumpla una determinada condición.*/
print("Fibonacci Sequence:", "Fn = Fn-1 + Fn-2")

func fibonacciSequence(num: Int) -> Int {
    var n1 = 0
    var n2 = 1

    var nR = 0

    for _ in 0..<num{
        nR = n1
        n1 = n2
        n2 = nR + n2
    }
    return n1
}

var val = 10

for i in 0...val{
   let output = fibonacciSequence(num: i)
   print(output)
} 

// Excepciones
enum myError: Error {
    case notExist
}

func returnException() throws {
    throw myError.notExist
}

do {
    try returnException()
    print("Exception: Successful")
} catch myError.notExist {
    print("Exception: Not Exist!")
} catch {
    print("Exception: An ERROR has occurred")
}

// DIFICULTAD EXTRA (Opcional)
/* Crea un programa que imprima por consola todos los
números comprendidos entre 10 y 55 (inclusive), pares,
y que no son ni el 16 ni múltiplos de 3.*/
for num in 10...55 {
    if num % 2 == 0, num != 16, num % 3 != 0 {
        print(num)
    }
}