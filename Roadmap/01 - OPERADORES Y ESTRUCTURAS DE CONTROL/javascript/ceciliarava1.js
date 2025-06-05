// Arithmetic operators + - / % **
let a = 5
let b = 2
let c = 10
let counter = 0
let value = 3

let add = a + b
let subtract = a - b
let division = a / b
let module = a % b
let power = a ** b

// Comparison operators and conditional sentences
for(let i = 0; i < 5; i++) {
    console.log('Hello!')
}

if (b < c) {
    console.log(`${c} is higher than ${b}`)
}

while (counter < a) {
    console.log(`Counter value: ${counter}`)
    counter ++
}

do {
    console.log(`Do while value: ${b}`)
    b++
} while (b != a)

switch (value) {
    case 1: 
        console.log('The value is 1')
        break
    case 2:
        console.log('The value is 2')
        break
    case 3: 
        console.log('The value is 3')
        break
    default:
        console.log('The value do not exists')
}

// Logic operators
if (a > b && b < c) {
    console.log(`${a} is higher than ${b} and ${b} is lower to ${c}`)
}

if (a > b || b < c) {
    console.log(`${a} is higher than ${b} or ${b} is lower to ${c}`)
}

// Create a program that prints to the console all numbers between 10 and 55 (inclusive), even, 
// and that are neither 16 nor multiples of 3.
for(let i = 10; i <= 55; i++) {
    if((i != 16) && i % 2 == 0 && i % 3 != 0) {
        console.log(i)
    }
    
}
