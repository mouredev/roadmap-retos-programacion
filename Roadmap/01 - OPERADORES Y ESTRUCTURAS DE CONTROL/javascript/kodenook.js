
let num1 = 3
let num2 = 4

/*
    Arithmetics Operators
*/

// addition
console.log(`sum: ${num1 + num2}`)
// subtraction
console.log(`subtraction: ${num1 - num2}`)
// multiplication
console.log(`multiplication: ${num1 * num2}`)
// division
console.log(`division: ${num1 / num2}`)
// modulus
console.log(`modulus: ${num1 % num2}`)
// exponentation
console.log(`exponentation: ${num1 ** num2}`)


/*
    Assignment Operators
*/

console.log(num3 = 2) // assignment
console.log(num3 += 3) // addition
console.log(num3 -= 1) // subtraction
console.log(num3 *= 2) // multiplication
console.log(num3 /= 3) // division
console.log(num3 %= 2) // modulus
console.log(num3 **= 2) // exponentation

/*
    Comparison Operators
*/

console.log(num1 == num2) // equal
console.log(num1 != num2) // not equal
console.log(num1 === num2) // equal value and type
console.log(num1 !== num2) // not equal value and type
console.log(num1 > num2) // greater than
console.log(num1 < num2) // less than
console.log(num1 >= num2) // greater than or equal than
console.log(num1 <= num2) // less than or equal than

/*
    Logical Operators
*/

console.log(num1 && num2) // true if both are true
console.log(num1 || num2) // true if either are true
console.log(!num1) // true if not true

/*
    Bitwise Operators
*/

console.log(6 & 3) // compare each bit and set it to 1 if both are 1, otherwise it is set to 0
console.log(6 | 3) // compare each bit and set it to 1 if one or both are 1, otherwise it is set to 0
console.log(6 ^ 3) // compare each bit and set it to 1 if only one is 1, otherwise it is set to 0
console.log(~3) // inverts each bit, 0 becomes 1 and 1 becomes 0
console.log(3 << 2) // insert the specified numbers of 0's (in this case 2) from the right
console.log(8 >> 2) // insert the specified numbers of 0's (in this case 2) from the left
console.log(8 >>> 2) // insert the specified numbers of 0's (in this case 2) from the left, result unsigned

/*
    Conditional Assignment
*/

let num4

console.log(true ? 'true' : 'false')
console.log(num4 ?? 'false')

/*
    If
*/

if (false) {
    console.log('true')
} else if (false) {
    console.log('true')
} else {
    console.log('true')
}

/*
    Switch
*/

switch (new Date().getDay()) {
    default:
        day = 'Sunday'
    case 1:
        day = 'Monday'
        break
    case 2:
        day = 'Tuesday'
        break
    case 3:
        day = 'Wednesday'
        break
    case 4:
        day = 'Thursday'
        break
    case 5:
        day = 'Friday'
        break
    case 6:
        day = 'Saturday'
}

console.log(day)

/*
    Loop For
*/

for (let i = 0; i < 5; i++) {
    console.log(i)
}

const person = { fname: 'John', lname: 'Doe', age: 25 };

for (let x in person) {
    console.log(person[x])
}

const cars = ['BMW', 'Volvo', 'Mini']

for (let x of cars) {
    console.log(x)
}

/*
    Loop While
*/

let i = 0

while (i < 10) {
    console.log('The number is ' + i)
    i++
}

/*
    Loop Do-While
*/

do {
    console.log('The number is ' + i)
    i--
}
while (i > 1);

/*
    Exercise
*/

for (let i = 10; i < 56; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i)
    }
}