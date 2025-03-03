// BASIC OPERATORS
// Arithmetic Operators
console.log(`Suma: 10 + 3 = ${10 + 3}`)
console.log(`Resta: 10 - 3 = ${10 - 3}`)
console.log(`Multiplicación: 10 * 3 = ${10 * 3}`)
console.log(`División: 10 / 3 = ${10 / 3}`)
console.log(`Módulo: 10 % 3 = ${10 % 3}`)
console.log(`Exponente: 10 ** 3 = ${10 ** 3}`)

// Assignment Operators
myNumber = 11
console.log(myNumber)
myNumber += 1  // adds and assigns
console.log(myNumber)
myNumber -= 1  // subtracts and assigns
console.log(myNumber)
myNumber *= 1  // multiplies and assigns
console.log(myNumber)
myNumber / 2  // divides and assigns
console.log(myNumber)
myNumber %= 3  // module and assigns
console.log(myNumber)
myNumber **= 2 // exponent and assigns
console.log(myNumber)

// Unary Operators
myVariable = 3
console.log(myVariable)
myVariable ++ // uses the value, and then increments
console.log(myVariable)
myVariable -- // uses the value, and then decrements
console.log(myVariable)
++ myVariable // increments the value and then uses it
console.log(myVariable)
-- myVariable // decrements the value and then uses it
console.log(myVariable)
- myVariable // changes sign (denies) to 


// COMPARISON OPERATORS
// Equality Operators
console.log(`Igualdad: 10 == 3 = ${10 == 3}`) // checks equal value, not data type 
console.log(`Desigualdad: 10 != 3 = ${10 != 3}`) // checks if the value of a is not equal to that of b, does not check data type
console.log(`Igualdad: 10 > 3 = ${10 > 3}`) // checks if the value of a is greater than that of b
console.log(`Igualdad: 10 >= 3 = ${10 >= 3}`) // checks if the value of a is greater than or equal to that of b
console.log(`Igualdad: 10 < 3 = ${10 < 3}`) // check if the value of a is less than that of b
console.log(`Igualdad: 10 <= 3 = ${10 <= 3}`) // checks if the value of a is less than or equal to that of b

// Identity Operators
myNewNumber = 1.0
console.log(`My number is myNewNumber es ${myNumber === myNewNumber}`)  // checks if the value and data type of a is equal to that of b
console.log(`My number is not myNewNumber es ${myNumber !== myNewNumber}`)  // checks if the value and data type of a is not equal to that of b


// LOGICAL OPERATORS
console.log(`AND: 10 + 3 = 13 && 5 - 1 = 4 ${10 + 3 == 13 && 5 - 1 == 4}`)
console.log(`OR: 10 + 3 = 13 || 5 - 1 = 2 ${10 + 3 == 13 || 5 - 1 == 2}`)
console.log(`NOT: 10 + 3 = 14 ${10 + 3 != 14}`)

// IN - NOT IN OPERATOR
let myName = "gera";
console.log(`g in gera: ${myName.includes("g")}`) // true

let myName2 = "gera";
console.log(`x not in gera: ${!myName2.includes("x")}`) // true, because "x" is not in "gera"

// BIT OPERATORS
a = 10  // 1010
b = 3   // 0011
console.log(`AND: 10 & 3: ${10 & 3}`)  // # 0010  this equals to 2
console.log(`OR: 10 | 3: ${10 | 3}`)   // # 1022  this equals to 11
console.log(`XOR: 10 ^ 3: ${10 ^ 3}`)  // # 1001  this equals to 9
console.log(`NOT: ~10: ${~10}`)  // #             this equals to -11
console.log(`Desplazamientoa a la derecha: 10 >> 2: ${10 >> 2}`)  // # 0010       this equals to 2
console.log(`Desplazamientoa a la izquierda: 10 << 2: ${10 << 2}`)  // # 101000   this equals to 40


/***************************
 * ESTRUCTURAS DE CONTROL  *
 ***************************/
// CONDICIONALES
// IF
let myString = "gerardov"

if (myString == "gerardov"){
    console.log("myStrins es 'gerardov'")
} else if (myString == "guzman"){
    console.log("myString también es 'guzman'")
} else{
    console.log("myString no es 'gerardov'")
}

// ITERATIVAS
// FOR
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// WHILE
for (let i = 0; i < 7; i++) {
    console.log(i);
}

// MANEJO DE EXCEPCIONES
try {
    console.log(3/d)
} catch (error) {
    console.log("Se ha producido un error, revisa la operación nuevamente.")
} finally {
    console.log("Ha finalizado el informe de estado.")
}


// EXTRA
for (let i = 10; i <= 55; i++){
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}
