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

const suma = a + b;
const resta = a - b
const division = a / b
const multiplicacion = a * b
const a = 23
const c= ++a
const b = --a
//Asignación:
const x = x + y
const y = x | y
//logicos AND
true && true
true && false
//logicos OR
true || true
true || false
'abc' || null
undefined || 'abc'
// bit a bit
a |= b // a = a |b


//BONUS

let num1 = 10
let num2 = 55
for (let i = num1; num1 <= num2; num1++) {
    if(i %2 === 0 && i !==16 && i % 3 !== 0){
        console.log(i)
    }
    
}
