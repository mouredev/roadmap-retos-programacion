import Foundation

// Operadores Aritméticos
let addition = 11 + 33
let subtaction = 99 - 10
let multiplicacion: Int = 4 * 4
let division: Double = 140 / 3
let modulus: Int = 720 % 420

print("\nOperadores Aritméticos\n")
print("Resultado del aperador de suma: \(addition)")
print("Resultado del operador de resta: \(subtaction)")
print("Resultado del operador de multiplicación: \(multiplicacion)")
print("Resultado del operador de división: \(division)")
print("Resultado del operador de modulo \(modulus)")


// Operadores de Asignación
var numberByAssignment: Int = 777
let assignmetSimbol: Int = numberByAssignment
var additionAssignment: Int = 222
additionAssignment += numberByAssignment
var subtractionAssignment: Int = 300
subtractionAssignment -= numberByAssignment
var multiplicationAssignment: Int = 10
multiplicationAssignment *= numberByAssignment
var divisionAssignment: Double = 1423
divisionAssignment /= Double(numberByAssignment)
var modulusAssignment: Int = 5555
modulusAssignment %= numberByAssignment

print("\nOperadores de Asignación\n")
print("Resultado de suma asignación: \(additionAssignment)")
print("Resultado de resta adignación: \(subtractionAssignment)")
print("Resultado de multiplicación asignación: \(multiplicationAssignment)")
print("Resultado de división asignación: \(divisionAssignment)")
print("Resultado de modulo asignación: \(modulusAssignment)")


// Operadores de Igualdad
let equalTo = 0 == 0
let notEqualTo = 10 != 10
let greaterThan = 12 > 11
let lessThan: Bool = 90 < 99
let greaterThanOrEqualTo: Bool = 24 >= 124
let lessThanOrEqualTo: Bool = -1 <= 0

print("\nOperadores de Igualdad\n")
print("Resultado de igual que: \(equalTo)")
print("Resultado de no igual que: \(notEqualTo)")
print("Resultado de mayor que: \(greaterThan)")
print("Resultado de menor que: \(lessThan)")
print("Resultado de mayor o igual que: \(greaterThanOrEqualTo)")
print("Resultado de menor o igual que: \(lessThanOrEqualTo)")


// Operadores de Logicos
let and: Bool = true == true && false == false
let or: Bool = 1 > 11 || "or" == "or"
let not: Bool = !false

print("\nOperadores Logicos\n")
print("Resultado de AND: \(and)")
print("Resultado de OR: \(or)")
print("Resultado de NOT: \(not)")

// Operador Ternario
let ternaryOerator: String = true ? "Hola" : "Adios"

print("\nOperador Ternario\n")
print("Resultado del operador ternario: \(ternaryOerator)")


// Operadores de Rango
let closedRange: ClosedRange = 0...10
let range: Range = 11..<21
var numbersOfTheClosedRange: [Int] = []
var numbersOfTheRange: [Int] = []
for n in closedRange {
    numbersOfTheClosedRange.append(n)
}
for n in range {
    numbersOfTheRange.append(n)
}

print("\nOperadores de Rango\n")
print("Resultade del rango cerrado: \(numbersOfTheClosedRange)")
print("Resultado del rango: \(numbersOfTheRange)")


// Operadores de Bits
let firstBinary =  43 //0b00101011
let secondBinary = 56 //0b00111000
let bitwiseAND = firstBinary & secondBinary
let bitwiseOR: Int = firstBinary | secondBinary
let bitwiseXOR: Int = firstBinary ^ secondBinary
let leftShift: Int = firstBinary << 1
let rightShift: Int = secondBinary >> 1

print("\nOperadores d Bits\n")
print("Resultado del operador de Bit AND: \(bitwiseAND)")
print("Resultade del operador de Bit OR: \(bitwiseOR)")
print("Resultado del operador de Bit XOR: \(bitwiseXOR)")
print("Resultado del operador de Bit desplazamiento a la izauierda: \(leftShift)")
print("Resultado del operador de Bit desplazamiento a la derecha: \(rightShift)")


// Exepción
enum MyError: Error {
    case error1
    case error2
}
func functionExample() throws {
    MyError.error1
}
print("\nExepción\n")

do {
    try functionExample()
    print("Resusltade de exepción con exito")
} catch MyError.error1 {
    print("Resultado de exepción fallida")
} catch MyError.error2 {
    print("Resultado de exepción fallida")
}


// Estructura de control if else
print("\nEstructura de Control if else\n")
if true == true {
    print("Resultado del la estructura de control if")
} else {
    print("Resultado de la estructura de control else")
}


// Estructura de Control switch
print("\nEstructura de Control switch\n")
let int: Int = 100
switch int {
    case 10:
        print("Resultado de la estructura de control switch: \(int)")
    case 100:
        print("Resultado de la estrura de control switch: \(int)")
    case 1000:
        print("Resultado de la estructura de control switch \(int)")
    default:
        print("Resultado de la estructura de control switch: defaul")
}


// Estructura de Iteración for
let word: [String] = ["s", "w", "i", "f", "t"]
var swiftWord: String = ""
for character in word {
    swiftWord.append(character)
}
print("\nEstructura de Iteración for\n")
print("Resultado de la estructura de iteración for: \(swiftWord)")


// Estructura de Iteración while
var element: Int = 20
while element < 40 {
    element += 1
}
print("\nEstructura de Iteración while\n")
print("Resultado de la estructura de iteración while: \(element)")


// Estructura Iterative repeat while
repeat {
    element -= 1
} while element > 20

print("\nEstructura de Iteración repeat while\n")
print("Resultado de la estructura de iteración repeat while: \(element)")




// Dificultad Extra
print("\nEjercició Dificultad Extra\n")
for n in 10...55 {
    if n == 16 || n % 3 == 0 {
        continue
    }
    if n % 2 == 0 {
        print(n)
    }
}