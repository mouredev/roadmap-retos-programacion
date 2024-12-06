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

// Assigment

let constString: String = "This is a string"

print("assigment: \(constString)")


/*
 Arithmetic
 */

// addition
let addition: Int = 2 + 2

print("addition: 2 + 2 = \(addition)")


// substraction
let substraction: Int = 2 - 2

print("substraction: 2 - 2 = \(substraction)")


// multiplication
let multiplication: Int = 2 * 2

print("multiplication: 2 * 2 = \(multiplication)")


// division
let division: Int = 2 / 2

print("division: 2 / 2 = \(division)")


// residue
let residue: Int = 9 % 4

print("residue: 9 % 4 = \(residue)")



/*
 Comparation
 */

//major
let major: Bool = 2 > 1

print("major: 2 > 1 is \(major)")


//minor
let minor: Bool = 1 < 2

print("minor: 1 < 2 is \(minor)")


//equal
let equal: Bool = 1 == 1

print("equal: 1 == 1 is \(equal)")


//different
let different: Bool = 1 != 1

print("different: 1 != 1 is \(different)")


//major equal
let majorEqual: Bool = 1 >= 1

print("majorEqual: 1 >= 1 is \(majorEqual)")


//minor equal
let minorEqual: Bool = 1 <= 1

print("minorEqual: 1 <= 1 is \(minorEqual)")



/*
 Ternary operator
 */

let ternaryOne = 10
let ternaryTwo = 20

print(ternaryOne == ternaryTwo ? "They are same" : "They are different")



/*
 Composite assignment
 */

var compositeAssigment: Int = 1

compositeAssigment += 2

print("if a is 1 then a += 2 is \(compositeAssigment)")



/*
 Operator nil-coalescing
 */

var nilCoalescing: String?

let finalNilCoalescingValue = nilCoalescing ?? "return the b option"

print("if a is nil then a ?? b \(finalNilCoalescingValue)")



/*
Range
 */

print("close range is 1...5")
print("semi-open range is 1..<5")
print("unilateral range is myArray[2...] (from 2nd position)")
print("unilateral range is myArray[...2] (to 2nd position)")
print("unilateral with semi-open range is myArray[..<2] (to 2nd position without the 2nd posiiton)")



/*
Logical
 */

let trueValue = true
let falseValue = false

// NOT !
if !trueValue {
    print("trueValue was denied with not operator")
}


// AND &&
if trueValue && trueValue {
    print("trueValue and trueValue are true")
}


// OR ||
if trueValue || falseValue {
    print("any of values (trueValue or falseValue) is true")
}



/*
Control flow
 */

let names: [String] = [
    "Me",
    "You",
    "Others",
    "Lastname",
    "Middle name",
    "First name"
]

let dictionary = [
    0: "Apple",
    1: "Table",
    2: "Glass",
]


// For-In
for name in names {
    print(name)
}

for (id, word) in dictionary {
    print("id: \(id)")
    print("word: \(word)")
    print("-------------")
}


for name in names[...1] {
    print(name)
}


// While
var count: Int = 0

while count < 3 {
    print(count, "< 3")
    
    count += 1
}


// Repeat While
repeat {
    print(count)
    
    count += 1
} while count < 6


// If
if count > 0 {
    print("if control flow: count > 0 is true")
}


// If else
if count > 100 {
    print("count > 100 is true")
} else {
    print("if else control flow: count > 100 is false")
}


// If else if
if count > 100 {
    print("count > 100 is true")
} else if count < 100 {
    print("if else if control flow: count < 100 is true")
}


// Switch

switch count {
case 0:
    print("count is 0")
default:
    print("my default value")
}

enum MessageStatus {
    case sent
    case delivered
    case read
}

let status: MessageStatus = .read

switch status {
case .sent:
    print("sent")
case .delivered, .read:
    print("maybe ignored")
}


// Guard
let animals = ["cat", "dog", "bird"]

guard let myPet = animals.first else {
    fatalError("You dont have a pet")
}

print(myPet)




/*
 extra
 */

for number in 10...55 {
    let is55 = number == 55
    
    let isAllowedNumber =
        number != 16 &&
        number % 2 == 0 &&
        number % 3 != 0
    
    if is55 || isAllowedNumber {
        print(number)
    }
}
