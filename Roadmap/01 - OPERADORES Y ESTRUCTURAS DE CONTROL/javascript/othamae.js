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


// Arithmetic
const num1 = 4
const num2 = 2
const add = num1 + num2
const subtraction = num1 - num2
const multiplication = num1 * num2
const division = num1 / num2
const modulo = num1 % num2
const exponentiation = num1 ** num2

console.log(`ADD (+): ${num1} + ${num2} = ${add}`)
console.log(`SUBTRACTION (-): ${num1} - ${num2} = ${subtraction}`)
console.log(`MULTIPLICATION (*): ${num1} * ${num2} = ${multiplication}`)
console.log(`DIVISION (/): ${num1} / ${num2} = ${division}`)
console.log(`MODULO (%): ${num1} % ${num2} = ${modulo}`)
console.log(`EXPONENTIATION (**): ${num1} ** ${num2} = ${exponentiation}`)

// Logical
const and = true && 1>0 // true as both are true
const or = true || 1<0 // true as one is true
const not = !1>0 // false as 1>0 with ! is false
let andAsigment = 1 
andAsigment &&= 2 // evaluates the right operand and assigns to the left if the left operand is truthy
let orAsigment = 1
orAsigment ||= 2 // evaluates the right operand and assigns to the left if the left operand is falsy

console.log(`AND (&&): true && 1>0 = ${and}`)
console.log(`OR (||): true || 1<0 = ${or}`)
console.log(`NOT (!): !1>0  = ${not}`)
console.log(`AND ASSIGNMENT (&&=): andAsigment &&= 2 => ${andAsigment}`)
console.log(`OR ASSIGNMENT (||=): orAsigment ||= 2 => ${orAsigment}`)


//Comparation
const equal = 1 == 1 // true as both are equal
const notEqual = 1 != 1 // false as both are equal
const greater = 1 > 0 // true as 1>0
const greaterOrEqual = 1 >= 0 // true as 1>=0
const less = 1 < 0 // false as 1<0
const lessOrEqual = 1 <= 0 // false as 1<=0

console.log(`EQUAL (==): 1 == 1 = ${equal}`)
console.log(`NOTEQUAL (!=): 1 != 1 = ${notEqual}`)
console.log(`GREATER THAN (>): 1 > 0 = ${greater}`)+
console.log(`GREATER THAN OR EQUAL (>=): 1 >= 0 = ${greaterOrEqual}`)
console.log(`LESS THAN (<): 1 < 0 = ${less}`)
console.log(`LESS THAN OR EQUAL (<=): 1 <= 0 = ${lessOrEqual}`)


// Assignment
let number = 5
console.log(`ASSIGNMENT (=): number = 5 => ${number}`)
number ++ // increment by one
console.log(`INCREMENT (++): number ++ => ${number}`)
number -- // decrement by one
console.log(`DECREMENT (--): number -- => ${number}`)
number +=3 // increment by three
console.log(`INCREMENT ASSIGNMENT (+=): number  += 3 => ${number}`)
number -=3 // decrement by three
console.log(`SUBTRACTION ASSIGNMENT (-=): number -= 3 => ${number}`)
number *= 2 // multiply by two
console.log(`MULTIPLICATION ASSIGNMENT (*=): number *= 2 => ${number}`)
number /= 2 // divide by two
console.log(`DIVIDE ASSIGNMENT (/=): number /= 2 => ${number}`)
number **= 2 // exponentiation by two
console.log(`EXPONENTIATION ASSIGNMENT (**=): number **= 2 => ${number}`)
number %= 2 // modulo two
console.log(`MODULO ASSIGNMENT (%=): number %= 2 => ${number}`)


// Pertenence
const IN = 1 in [1,2,3] // true as 1 is in the array
const notPertenence = 4 in [1,2,3] // false as 4 is not in the array

console.log(`IN (in): 1 in [1,2,3] = ${IN}`)
console.log(`NOT PERTENENCE (!in): 4 in [1,2,3] = ${notPertenence}`)

// Bitwise
const XOR = 5 ^ 3 // 6 --> returns a number or BigInt whose binary representation has a 1 in each bit position for which the corresponding bits of either but not both operands are 1
console.log(`XOR (^): 5 ^ 3 = ${XOR}`)
let bit = 5
console.log(`ASSIGNATION: bit = 5 => ${bit}`)
bit ^=3 // performs bitwise XOR on the two operands and assigns the result to the left operand. 
console.log(`BITWISE XOR ASSIGNMENT (^=): bit ^=3 => ${bit}`)

// Conditions
// If-Else
const age = 18

if(age >= 18){
    console.log("You can vote")
} else {
    console.log("You can't vote")
}

// Switch
const color = 'green'

switch(color){
    case 'red':
        console.log("Color is red");
        break
    case 'blue':
        console.log("Color is blue");
        break
    default:
        console.log(`Color is ${color}`);
        break
}

// Iteration
// For
let numbersFrom0to9 =''
for(let i = 0; i < 10; i++){ 
  numbersFrom0to9 += i
}
console.log(`FOR LOOP: numbersFrom0to9 = ${numbersFrom0to9}`) 

// ForEach
const arrayNumbers = [1,2,3,4,5]
arrayNumbers.forEach(number => console.log(`FOREACH number in arrayNumbers: ${number}`))

// For...of
for (let number of arrayNumbers){
    console.log(`FOR...OF number in arrayNumbers: ${number}`)
}

// For...in
const object = { a: 1, b:2, c:3, d:4, e:5 }
for (let key in object){
    console.log(`FOR...IN key in object: ${key}, value: ${object[key]}`)
}

// While
let n = 0
while (n< 5){
    console.log(`WHILE n < 5: n = ${n}`)
    n++
}

// Do...While
let m = 0
do {
    m++
    console.log(`DO WHILE m < 5: m = ${m}`)
} while (m < 5)

// Try...catch
const CONSTANT = 'a'
try{
    CONSTANT = 'b'
} catch(error){
    console.log(`ERROR in TRY...CATCH: ${error}`)
}


// EXTRA TASK:
function printNumbersFrom10to55(){
    let n = 10
    console.log('Even numbers between 10 and 55 inclusive, excluding 16 and multiples of 3:')
    while(n <= 55){
        (n!== 16 && n%3!==0 && n%2===0) && console.log(n)
        n++       
    }
}

printNumbersFrom10to55()