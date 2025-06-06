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

// Aritmeticos
let a = 3
let b = 2
console.log (a / b) // Division
console.log (a * b) // Multipilicación
console.log (a - b) // Resta
console.log (a + b) // Suma
console.log (a % b) // Modulo
console.log (a ** b) //Exponente
a++ // Incremento
b-- // Decremento
console.log (b)
console.log (a)

// logicos
 let x = true 
 let y = false

 console.log (x && y) // AND Lógico
 console.log (x || y) // OR lógico
 console.log (!x) // NOT lógico

// Comparacion

let c = 5
let d = 10

console.log (c == d) // Igualdad
console.log(c !== d); // Desigualdad estricta
console.log(c > d); // Mayor que
console.log(c < d); // Menor que
console.log(c >= d); // Mayor o igual que
console.log(c <= d); // Menor o igual que

// Asigncación
let e 
e += 5; // Asignación de suma
e -= 3; // Asignación de resta
e *= 2; // Asignación de multiplicación
e /= 2; // Asignación de división
e %= 3; // Asignación de módulo
e **= 2; // Asignación de exponenciación

// Identidad

let f = 5;
let g = '5';

console.log(f === g); // Igualdad estricta
console.log(f !== g); // Desigualdad estricta

// Pertenencia

let myArray = [1,2,3,4,5]

console.log (3 in myArray) // Verifica si el indice 3 existe en el array
console.log ('Hola' in myArray) // Verifica si la propiedad 'length' existe en el array

let h = 5; // 0101 en binario
let i = 3; // 0011 en binario

console.log(h & i); // AND bit a bit
console.log(h | i); // OR bit a bit
console.log(h ^ i); // XOR bit a bit
console.log(~h); // NOT bit a bit
console.log(h << 1); // Desplazamiento a la izquierda
console.log(h >> 1); // Desplazamiento a la derecha
console.log(h >>> 1); // Desplazamiento a la derecha sin signo

// Condicionales
a = 2
b = 3
let text
if (a == b) {
    text = "a es igual a b"
} else if (a > b) {
    text = 'a es mayor que b'
} else {
    text = "a es menor que b"
}
console.log (text)

text = (text == "a es mayor que b") ? true :  false
console.log (text)

let myName = "Luiss"

switch (myName) {
    case "Jose":
        console.log (`Hola, ${myName}`)
        break;
    case "Luis":
        console.log (`Hola, ${myName}`)
        break;
    default:
        console.log (`Hola, ${myName}`)
        break;
}

// Iterativas

for (let i = 0; i < myArray.length; i++) { 
    console.log (myArray[i])
}

for (let value of myArray) {
    console.log (value)
}

let myMap = {b: 'canada', a: 'Korea', c: "Venezuela"}

for (let key in myMap) {
    console.log (`${key}: ${myMap[key]}`)
}

i = 0
while (i < myArray.length) {
    console.log (myArray[i])
    i++
}
i = 1
do {
    console.log ("Contador " + i)
    i++
} while (i <= 10);

// Exepciones

function Contador(i) {
    if (typeof i == "number") {
        let a = 1
        while (a <= i){
            console.log ('Contador: ', a)
            a++
        }
    } else {
        throw new Error ("la variable no es un numero")
    }
}
try {
    Contador (6)
} catch (error) {
    console.log ('Se ha producido un error : ', error.message)
} finally {
    console.log ("Bloque Finalizado")
}

// * Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
myArray = []
function AddNumberArray (valor, limite) {
    while (valor <= limite) {
        if (valor % 2 === 0 && valor !== 16 && valor % 3 !== 0) {
            myArray.push (valor)
        }
        valor++;
    }
}

AddNumberArray(10, 55)
console.log(myArray)