import Foundation

//Arithmetics
print("Addition: 10 + 3 = \(10 + 3)")
print("Substraction: 10 - 3 = \(10 - 3)")
print("Multiplication: 10 * 3 = \(10 * 3)")
print("Division: 10 / 3 = \(10 / 3)")
print("Modulus: 10 % 3 = \(10 % 3)")

//Comparative
print("Equality: 10 == 3 is \(10 == 3)")
print("Inequality: 10 != 3 is \(10 != 3)")
print("Greater than: 10 > 3 is \(10 > 3)")
print("Less than: 10 < 3 is \(10 < 3)")
print("Greater than or equal: 10 >= 3 is \(10 >= 3)")
print("Less than or equal: 10 <= 3 is \(10 <= 3)")

//Logical operators
print("AND: 5 + 5 == 3 && 5 + 4 == 9 = \(5 + 5 == 3 && 5 + 4 == 9)")
print("OR: 5 + 5 == 3 || 5 + 4 == 9 = \(5 + 5 == 3 || 5 + 4 == 9)")
print("NOT: !(5 + 5 == 3) is \(!(5 + 5 == 3))")

// Assignment operators
var myNumber = 11
print(myNumber)
myNumber += 1
print(myNumber)
myNumber -= 1
print(myNumber)
myNumber *= 2
print(myNumber)
myNumber /= 2
print(myNumber)
myNumber %= 2
print(myNumber)

// Identity operators
let myNewNumber = myNumber
print("myNumber is myNewNumber is \(myNumber == myNewNumber)")
print("myNumber is not myNewNumber is \(myNumber != myNewNumber)")

// Membership operators
print("'u' in 'mouredev' = \("mouredev".contains("u"))")
print("'b' not in 'mouredev' = \(!"mouredev".contains("b"))")

// Bitwise operators
let a = 10
let b = 3
print("AND: 10 & 3 = \(a & b)")
print("OR: 10 | 3 = \(a | b)")
print("XOR: 10 ^ 3 = \(a ^ b)")
print("NOT: ~10 = \(~a)")
print("Right shift: 10 >> 2 = \(a >> 2)")
print("Left shift: 10 << 2 = \(a << 2)")

/*
Control structures
*/

// Conditionals
let myString = "Carlos"

if myString == "calonsocamina" {
    print("myString is 'calonsocamina'")
} else if myString == "Carlos" {
    print("myString is 'Carlos'")
} else {
    print("myString is neither 'calonsocamina' or 'Carlos'")
}

// Loops
for i in 0...10 {
    print(i)
}

var i = 0
while i <= 10 {
    print(i)
    i += 1
}

// Exception handling
do {
    let _ = try divide(10, by: 0)
} catch {
    print("An error has occurred")
}
print("Exception handling has finished")

// Example function for throwing division error:
func divide(_ numerator: Int, by denominator: Int) throws -> Int {
    if denominator == 0 {
        throw NSError(domain: "DivisionByZero", code: 1, userInfo: nil)
    }
    return numerator / denominator
}

//Extra
for number in 10...55 {
    if number % 2 == 0 && number != 16 && number % 3 != 0{
        print(number)
    }
}
