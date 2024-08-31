// Operadores Aritméticos
let num1 = 10
let num2 = 5

let add = num1 + num2
let subtract = num1 - num2
let multiply = num1 * num2
let divide = num1 / num2
let module = num1 % num2

print("Add: \(add),  subtract: \(subtract), multiply: \(multiply), divide: \(divide), module: \(module)")

// Control Flow
// For-In Loop
var numberOfDays = 5
for num in 0..<numberOfDays {
    print("Number: \(num)")  
}

// While Loop
var month = 1

while month < 13 {
    print("Month: \(month)")   
    month += 1 
}

// Repeat-While Loop
var year = 2024

repeat {
    print("Hello!") 
} while  year == 2023

// Conditional Statements
// if / else
var age = 21
var haveMoney = true

if age >= 18 && haveMoney {
    print("Genial!! eres adulto con dinero!.")
} else if age >= 18 {
    print("Bienvenido al mundo de los adultos sin dinero XD.")
} else {
    print("Eres aún pequeño sin responsabilidades")
}

// Switch
let dayOfTheWeek = "Friday"

switch dayOfTheWeek {
    case "Monday":
    print("It's monday")
    case "Tuesday":
    print("It's tuesday")
    case "Wednesday":
    print("It's wednesday")
    case "Thursday":
    print("It's thursday")
    case "Friday":
    print("It's friday")
    default:
    print("Not a day of the week") 
}

/*
Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for number in 10...55 {
    if number != 16 && !(number % 3 == 0){
        if number % 2 == 0 {
            print(number)
            
        } 
    }
}

// Expected Output: 10,14,20,22,26,28,32,34,38,40,44,46,50,52

