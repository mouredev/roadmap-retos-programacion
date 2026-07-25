/*
Operadores
*/

//Operadores arimeticos 
console.log(`Suma: 10 + 3 = ${10 + 3}`)
console.log(`Resta: 10 - 3 = ${10 - 3}`)
console.log(`Multiplicacion: 10 * 3 = ${10 * 3}`)
console.log(`Division: 10 / 3 = ${10 / 3}`)
console.log(`Modulo: 10 % 3 = ${10 % 3}`)
console.log(`Exponente: 10 ** 3 = ${10 ** 3}`)

let a = 5
a++
console.log(`Incremento ++ = ${a}`)

let b = 5
a--
console.log(`Decremento -- = ${b}`)


//Operadores de comparacion 
console.log (`Mayor que: 5 > 3 es ${5 > 3}`)
console.log (`Menor que: 5 < 3 es ${5 < 3}`)
console.log (`Igual a: 5 == 3 es ${5 == 3}`)
console.log (`Igualdad por valor y tipo: 5 === 3 es ${5 === 3}`)
console.log (`No es igual : 5 != 3 es ${5 != 3}`)
console.log (`No son de igual valor o no son de igual tipo: 5 !== 3 es ${5 !== 3}`)

//Operadores logicos
console.log (`AND  &&: 10 + 3 == 13 and 5 - 1 == 4 es ${ 10 + 3 == 13 && 5 - 1 == 4}`)
console.log (`OR  ||: 10 + 3 == 13 or 5 - 1 == 4 es ${ 10 + 3 == 14 || 5 - 1 == 3}`)
console.log (`NOT !: not 10 + 3 == 14 es ${!(10 + 3 == 14)}`)

//Operadores de asignacion
let myNumber = 11 
myNumber += 1 //suma y asignacion
console.log(myNumber) 
myNumber -= 1 //resta y asignacion
console.log(myNumber)
myNumber *= 2 //multiplicacion y asignacion
console.log(myNumber)
myNumber /= 2 //division y asignacion
console.log(myNumber)
myNumber %= 2 //modulo y asignacion
console.log(myNumber)
myNumber **= 2 //exponente y asignacion
console.log(myNumber)
myNumber >>= 2 //desplazamiento a la derecha
console.log(myNumber) 
myNumber <<= 2 //desplazamiento a la izquierda
console.log(myNumber) 
myNumber >>>= 2
console.log(myNumber) 
myNumber &= 2 // AND bit a bit 
console.log(myNumber)
myNumber ^= 2 // bitwise XOR 
console.log(myNumber)
myNumber |= 2 // OR bit a bit
console.log(myNumber)
myNumber &&= 2 // logico y asignacion 
console.log(myNumber)
myNumber ||= 2 // Asignacion logica OR
console.log(myNumber)
myNumber ??= 2 // Asignacion logica nullish
console.log(myNumber)


//Operadores bit a bit 
let e = 15 //1111
let m = 9 //1001
console.log (`AND: 15 & 9 = ${15 & 9}`) // 1001
console.log (`OR: 15 | 9 = ${15 | 9}`) // 1111
console.log (`XOR: 15 ^ 9 = ${15 ^ 9}`) // 0110
console.log (`NOT: ~ 15 = ${~ 15}`) // 0000
console.log (`Desplazamiento a la derecha:  15 >> 9 = ${15 >> 9}`) // 1111
console.log (`Desplazamiento a la derecha de relleno: 15 >>> 9 = ${15 >>> 9}`) // 0
console.log (`Desplazamiento a la izquierda: 15 << 9 = ${15 << 9}`) // 1111000000000


//Operador condicional (ternario)
const isRaining = false
isRaining ? console.log ("Esta lloviendo") : console.log ("No esta lloviendo")

//Operadores de pertenencia 
var miCoche = {marca: "Honda", modelo: "Accord", año: 1998, color: "Azul"};
"marca" in miCoche; // devuelve true
"Rojo" in miCoche; // devuelve false


/*
Estructuras de control
*/


//Condicionales

let age = 68;
let estado = "None";
if (age < 18) {
    estado = "Young";
} else if (age >= 18 && age <= 65) {
    estado = "Adult";
} else {
    estado = "Old";
}

console.log(`La persona esta : ${estado}`)


/*
Bucles
*/

//for
for (let i = 1; i <=10; i++) {
    console.log(`7 x ${i} = ${7*i}`)
}

//while
let number = 0

while (number <= 10){
    number++
}
console.log(number)

//do while

number = 6

do {
    console.log(number)
    number++
} while (number <= 5)


//for of
let myArray = [1, 2, 3, 4]

for (let element of myArray) {
    console.log(element)
}

//break y continue

for (let i = 1; i <= 10; i++) {
    if (i==5){
        continue;
    } else if (i==9){
        break;
    }
    console.log(i);
}


// Manejo de excepciones 

const greet = "Hola"

try {
    greet = "Adios"
} catch (error) {
    console.error("Error: No se puede reasignar una constante")
} finally {
    console.log("Este bloque se ejecuta siempre")
}


// Ejercicio

for (let i = 10; i <= 55; ++i){
    if (i % 2 == 0 && i != 16 && i % 3 != 0) 
    console.log(i)
}
