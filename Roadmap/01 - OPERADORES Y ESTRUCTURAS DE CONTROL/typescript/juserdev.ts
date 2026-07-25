/*
 * EJERCICIO:
 ! - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

let a: number = 5
let b: number = 2

let suma: number = a + b
console.log(suma)

let mult: number = a * b
console.log(mult)

let div: number = a / b
console.log(div)

let modulus: number = a % b
console.log(modulus)

let exponen: number = a ** b
console.log(exponen)

let c: number = 5

console.log(c = b)
console.log(a += b)
console.log(a -= b)
console.log(a *= b)
console.log(a /= b)
console.log(a %= b)
console.log(a = c)
console.log(a ** b)


console.log(a == b)
console.log(a < b)
console.log(a > b)
console.log(a >= b)
console.log(a <= b)
console.log(a != b)

console.log(a && b)
console.log(a || b)
console.log(!a)

const myFunc = ()=>{
    for (let i = 0; i <= 55; i++) {
        if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(i)
        }
    }
}

myFunc()