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

// 🔥 Aritméticos
let suma = 10 + 5;
let resta = 10 - 5;
let multiplicacion = 10 * 5;
let division = 10 / 5;
let modulo = 10 % 5;

// 🔥 Lógicos
let and = true && false; // false
let or = true || false; // true
let not = !true; // false

// 🔥 De comparación
let igual = 10 == 5; // false
let diferente = 10 != 5; // true
let mayorQue = 10 > 5; // true
let menorQue = 10 < 5; // false
let mayorOIgualQue = 10 >= 5; // true
let menorOIgualQue = 10 <= 5; // false

// 🔥 Asignación
let asignacion = 10;
asignacion += 5; // 10 + 5 = 15
asignacion -= 5; // 10 - 5 = 5
asignacion *= 5; // 10 * 5 = 50
asignacion /= 5; // 10 / 5 = 2
asignacion %= 5; // 10 % 5 = 0

// 🔥 Identidad
let igualEstricto = 10 === 10; // true
let diferenteEstricto = 10 !== 10; // false

// 🔥 Pertenencia
let array = [1, 2, 3];
let pertenece = 2 in array; // true

// 🔥 Bits
let andBits = 10 & 5; // 0
// 1010 (10) AND 
// 0101 (5)
// ----
// 0000 (0) , Si ambos bits son 1, es = 1, sino es 0.

let orBits = 10 | 5; // 15
// 1010 (10) OR 
// 0101 (5)
// ----
// 1111 (15) , Si al menos uno de los bits es 1, es = 1, sino es 0.

let xorBits = 10 ^ 5; 
// 1010 (10) XOR
// 0101 (5)
// ----
// 1111 (15) , Si los bits son diferentes, es = 1, si son iguales es 0.

let notBits = ~10; 
// 0000 1010 NOT(10)
// ---------
// 1111 0101 (-11), 0 se convierte en 1 y 1 se convierte en 0. 

let desplazamientoIzquierda = 10 << 2; // 40
// 0000 1010 (10) << 2 
// ---------
// 0010 1000 (40) , Desplaza los bits del número hacia la izquierda, y deja un 0

let desplazamientoDerecha = 10 >> 2; // 2
// 0000 1010 (10) >> 2
// ---------
// 0000 0010 (2) , Desplaza los bits del número hacia la derecha, los de la derecha se descartan.
desplazamientoDerecha = -10 >> 2; // -3
// 1111 0110 (-10) >> 2
// ---------
// 1111 1101 (-3) , Al desplazar a la derecha, este bit de signo se copia en las nuevas posiciones a la izquierda.
let desplazamientoDerechaSinSigno = 10 >>> 2; // 2
// 0000 1010 (10) >>> 2
// ---------
// 0000 0010 (2) , 

// Similar al desplazamiento a la derecha, 
// pero en lugar de copiar el bit de signo, 
// se añaden ceros por la izquierda.

desplazamientoDerechaSinSigno = -10 >>> 2; // 61
// 11110110 (-10) >>> 2
// ---------
// 00111101 (61)
// 
// En el desplazamiento a la derecha sin signo, 
// Se añaden ceros a la izquierda en lugar de copiar el bit de signo.


// 🔥 Condicionales
if (10 > 5) {
    console.log("10 es mayor que 5");
} else {
console.log("10 no es mayor que 5");
}

// 🔥 Iterativas
for (let i = 0; i < 10; i++) {
console.log(i);
}

let i = 0;
while (i < 10) {
console.log(i);
i++;
}

// 🔥 Excepciones
try {
let resultado = 10 / 0;
} catch (error) {
console.log("Se capturo error: división por cero");
}


// 🔥 Extra
for (let i = 10; i <= 55; i++) {
    //   (pares)  Y  (ni 16) Y  (ni multi de 3) O (el extremo 55)
    if ( (i%2==0) && (i!=16) && ( i % 3 !== 0 ) || (i == 55) ){
        console.log(i)
    }
}