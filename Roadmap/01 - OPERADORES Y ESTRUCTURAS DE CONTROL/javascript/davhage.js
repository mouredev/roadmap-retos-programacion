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

let a = 5;
let b = 1;
let verdad = true;
let falso = false;

//? Operadores de asignación

console.log(a = b);//asignación
console.log(a += b);//asignación de adición
console.log(a -= b);//asignación de resta
console.log(a /= b);//asignación de multiplicación
console.log(a %= b);//asignación de residuo
console.log(a **= b);//asignación de exponencia
console.log(a <<= b);//asignación de desplazamiento a la izquierda
console.log(a >>= b);//asignación de desplazamiento a la derecha
console.log(a >>>= b);//asignación de desplazamiento a la derecha sin signo
console.log(a &= b);//asignación de AND bit a bit
console.log(a ^= b);//asignación de XOR bit a bit
console.log(a |= b);//asignación de OR bit a bit
console.log(a &&= b);//asignación de AND lógico
console.log(a ||= b);//asignación de OR lógico
console.log(a ??= b);//asignación de anulación lógica

//? Comparación

console.log(a == b);//igual
console.log(a != b);//no es igual
console.log(a === b);//estrictamente igual
console.log(a !== b);//desigualdad estricta
console.log(a > b);//mayor que
console.log(a >= b);//mayar o igual
console.log(a < b);//menor que
console.log(a <= b);//menor o igual

//? Operadores aritméticos

console.log(a % b);//residuo
console.log(a++);//incremento
console.log(a--);//decremento
console.log(a - b);//resta
console.log(a + b);//suma
console.log(a ** b);//exponenciación

//? Operadores bit a bit

console.log(a & b);//AND a nivel de bits
console.log(a | b);//OR a nivel de bits
console.log(a ^ b);//XOR a nivel de bits
console.log(a << b);//desplazamiento a la izquierda
console.log(a >> b);//desplazamiento a la derecha de propagación de signo
console.log(a >>> b);//desplazamiento a la derecha de relleno cero

//? Operaderes lógicos

console.log(a && b);//AND lógico
console.log(a || b);//OR lógico
console.log(!b);//NOT lógico

//? Operadores condicional (ternario)
console.log(a > b ? 'yes' : 'no');

//? Estructuras de control
//* For
for(let i = 0; i < 10; i++){
    console.log(i);
}
//* While

let i = 2;
while(i < 10){
    if(i % 2 == 0) {
        console.log('Número par', i);
    }
    i++;
}

//* Do While

do {
    if(i % 2 == 0){
        console.log('Número par', i)
    }
    i++;
} while (1 < 2);

//* If, else if else
if(i < 2){
    console.log('menor que 2');
} else if(i === 2){
    console.log('2');
} else {
    console.log('mayor que 2')
}

let accion = 'actualizar';

switch(accion) {
    case 'listar':
        console.log('Acción de listar');
        break;
    case 'guardar':
        console.log('Acción de guardar');
        break;
    default:
        console.log('Acción no reconocida');
}

//! Ejercicio extra

const extra = () => {
    for(let i = 10; i <= 55; i++){
        if(i % 2 === 0 && i % 3 !== 0 && i !== 16){
            console.log(i);
        }
    }
}
extra();