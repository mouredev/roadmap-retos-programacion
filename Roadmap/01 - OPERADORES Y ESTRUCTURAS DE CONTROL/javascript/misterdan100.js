// #01 OPERADORES Y ESTRUCTURAS DE CONTROL

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators
// most common assignament symbols
let x = 100
x = 200 // asigna un valor
x += 100 // suma un valor
x -= 100 // resta un valor
x *= 100 // multiplica un valor
x /= 100 // divide un valor
x %= 100 // devulve el residuo de un division
x **= 100 // asigna una exponenciacion

// comparison operators
let equal = '==' // return true if the operands are equal
let notEqual = '!=' // return true if the operands are not equal
let strictEqual = '===' // return true if the operators are equal value and type
let strictNotEqual = '!==' // return true if the operators are not equal value and type
let greaterThan = '>' // return true if the first value if greater than the second
let greaterThanOrEqual = '>=' // return true if first value is greater or equal thant the second
let lessThan = '<' // return true if the first value if less than the second
let lessThanOrEqual = '<=' // return true if first value is less or equal thant the second

// Control flow structures
//* if ... else
// validate if a condion is true if no do another thing
if (true) {
    console.log('condition is true')
} else {
    console.log('condition is false')
}

//* if ... else if ... else 
// allow validate several condicions
if (true) {
    console.log('condition is true')
} else if (true) {
    console.log('second condition as true')
} else if (true) {
    console.log('third condition as true')
} else {
    console.log('condition is false')
}

//* switch
// allows avaluate defferents cases where the condicion can be true
switch (true) {
    case true:
        console.log('first case is true')
        break;
    case true:
        console.log('first case is true')
        break;
    // …
    default:
        console.log('default result if anycase is true')
}

//* while
// allows execute a code block while a condition is true
let condition = true
while(condition) {
    // code block
}

//* do ... while
// allows execute a code block at least one time and the rest while a condition is true
condition = true
do {
    // code block
} while(condition)

//* try... catch
// if there is some error while the execution 'catch' capture the error without break the application
try {
    // some fetch process
} catch (error) {
    console.log(error)
}