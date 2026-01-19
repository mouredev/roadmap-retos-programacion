// 01-Javascript


// Arithmetic operators
let number_one = 10
let number_two = 3

let sum = number_one + number_two
console.log(`Sum: ${sum}`)

let substract = number_one - number_two
console.log(`Substract: ${substract}`)

let multiply = number_one * number_two
console.log(`Multiply: ${multiply}`)

let division = (number_one / number_two).toFixed(2)
console.log(`Division: ${division}`)


// Control structures
if (sum != 0) {
    console.log('The sum is different than zero')
} else {
    console.log('The sum is zero')
}

let count = 0
while (count < 3) {
    console.log(sum)
    count ++
}

count = 1
do {
    console.log('Hello') 
    count ++
} while (count != 3)


// Exercise
for (let i = 0; i <= 55; i++) {
    if (i != 16 && i % 3 != 0 && i % 2 == 0) {
        console.log(i)
    }
}