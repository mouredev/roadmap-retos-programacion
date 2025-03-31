/*
# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 * */

// Operadores

// 1.1. Operadores Aritméticos
let a = 10;
let b = 5;

console.log(a + b)
console.log(a - b)
console.log(a * b)
console.log(a / b)
console.log(a % 2)
console.log(a ** 2)

// 1.2. Operadores lógicos

console.log(true && false) // AND
console.log(false || true)  // OR
console.log(!true)  // NOT

// 1.3. Operadores de asignación

console.log(a == "10") // Igualdad por valor y no identidad = true
console.log(a === "10") // Igualdad por valor e identidad = false 
console.log(a > b)
console.log(a < b)
console.log(a >= b)
console.log(a <= b)
// Distinto
console.log(a != 10) // Distinto por valor
console.log(a !== "10") // Distinto por valor e igualdad

// 1.4. Operadores de asignación
let c = 10;
c += 10; // c = c + 10
console.log(c)
c -= 10; // c = c - 10
console.log(c)
c *= 10; // c = c * 10
console.log(c)
c /= 10; // c = c / 10
console.log(c)
c %= 10; // c = c % 10
console.log(c)
c = 10
console.log(c)
c **= 2 // c = c ** 2
console.log(c)

// 1.5. Operadores de identidad

console.log(5 === 5)
console.log(5 === "5")

// 1.6. Operadores de pertenencia

let myArray = [1, 2, 3, 4, 5]
console.log(myArray.includes(5))
console.log(myArray.includes(6))

let obj = {key: "value"}
console.log("key" in obj)

// 1.7. Operadores Bitwise
console.log("\n=== Operadores Bitwise ===");
let d = 5, e = 3;  // 0101 & 0011
console.log("AND:", d & e);   // 0001 = 1
console.log("OR:", d | e);    // 0111 = 7
console.log("XOR:", d ^ e);   // 0110 = 6
console.log("NOT:", ~d);      // 11111010 (complemento a 2)
console.log("Left shift:", d << 1);  // 1010 = 10
console.log("Right shift:", d >> 1); // 0010 = 2

// 2. Estructuras de control

// 2.1. if, else if, else

a = 10, b = 5

if (a > b) {
    console.log(`${a} es mayor que ${b}`)
} else if (a < b) {
    console.log(`${a} es menor que ${b}`)
} else {
    console.log(`${a} es igual que ${b}`)
}

// 2.2. Operador ternario

let message = a >= b ? `${a} es mayor o igual que ${b}` : `${a} es menor que ${b}`
console.log(message)

// 2.3. switch case

let numberDay = 1
switch (numberDay) {
    case 1:
    case 2:
    case 3:
        console.log("Entre semana")
        break
    case 4:
    case 5:
        console.log("Ya casi es fin de semana")
        break
    case 6:
    case 7:
        console.log("Fin de semana, yupi!")
        break
    default:
        console.log("No es un día de la semana")
}

// 2.4. for Loop

for (let i = 0; i < 5; i++) {
    console.log(i)
}


// For para iterables, accediendo por su indice

let names = ["Duban", "Jheison", "Anderson"]


for (let i = 0; i < names.length; i++) {
    console.log(names[i])
}

// 2.4.1 For ... of (para iterables)


for (let name of names) {
    console.log(name)
}

// 2.4.2 For ... in (para objetos)

let obj2 = {
    name: "Duban", 
    lastname: "Quiroga",
    age: 26
}

for (let key in obj2) {
    console.log(key, obj2[key])
}

// 2.4.3 ForEach (para iterables)

names.forEach((value, index) => {
    console.log(`${++index} - ${value}`)
})

// 2.5. while

let i = 0

while (i < 5) {
    console.log(i)
    i++
}

i = 5

// 2.5.1. do ... while

do {
    console.log(i)
    i++
} while (i < 5)


// 3. Excepciones

try {
    throw Error("Este es un mensaje de error") // Genera una excepcion
} catch (e) {
    console.log(e.message)
} finally {
    console.log("Finally siempre se ejecuta")
}

/* 
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        console.log(i)
    }
}