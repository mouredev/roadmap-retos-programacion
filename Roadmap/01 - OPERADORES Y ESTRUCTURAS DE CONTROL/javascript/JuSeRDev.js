//  ! EJERCICIO:
//  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...(Ten en cuenta que cada lenguaje puede poseer unos diferentes)

// asignacion

let a = 11
let b = 3


console.log(a += b)
console.log(a -= b)
console.log(a *= b)
console.log(a /= b)
console.log(a %= b)
console.log(a **= b)
console.log(a <<= b)
console.log(a >>= b)
console.log(a >>>= b)
console.log(a &= b)
console.log(a |= b)
console.log(a ||= b)
console.log(a ??= b)

//  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...
//  * - Debes hacer print por consola del resultado de todos los ejemplos.

let igual

console.log(igual = a == b)
console.log(igual = a === b)
console.log(igual = a < b)
console.log(igual = a > b)
console.log(igual = a <= b)
console.log(igual = a >= b)
console.log(igual = a != b)


//  * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0 ) {
        console.log(i);
    }   
}


//  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
