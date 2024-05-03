/*
Ejercicios:
*/


/*
1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/

// Operadores de cadenas:
let mensaje = 'Hola,'
mensaje += ' Robinson.' // 'Hola, Robinson.'
mensaje += ' Estás aprendiendo JS' // 'Hola, Robinson. Estás aprendiendo JS'

// Operadores Aritméticos:
let suma = 5 + 3; // 8
let resta = 7 - 2; // 5
let multiplicacion = 4 * 6; // 24
let division = 10 / 2; // 5
let modulo = 17 % 3; // 2 (el resto de la división de 17 por 3)

// Operadores de Asignación:
let num = 10;
num += 5 // 15
num -= 3 // 12
num /= 2 // 6
num **= 2 // 36
num %= 6 // 0

// Operadores de comparacion 
let a = 10;
let b = 5;
let c = '10';

// El signo == solo compara si los valores son iguales sin importar rl tipo de dato.
a == b // false
a != b // true
a == c // true
a != c  // false

// El signo === compara el valor y el tipo de dato.
a === b // false
a !== b // true
a === c // false
a !== c  // true

a > b // true
a < b // false
a >= c // true
a <= c  // false


// Operadores lógicos: AND (&&), OR (||) y NOT (!)
let x = true;
let y = false;

x && y // false. Devuelve true si ambas expresiones booleanas son true, de lo contrario devuelve false.
x || y // true. Devuelve true si al menos una de las expresiones booleanas es true. De lo contrario, devuelve false.
!y // true. Invierte el valor booleano de la expresión a la que se aplica. Si la expresión es true, devuelve false, y viceversa.


// Operadores de incremento y decremento
let incremento = 10;
++incremento // 11. Incrementa el valor de la variable en 1 y devuelve el valor incrementado.
incremento++ // Devuelve 11, aunque incremento vale 12.  Incrementa el valor de la variable en 1 y devuelve el valor original de la variable antes del incremento.
incremento // 12

--incremento // 11
incremento-- // 11
incremento // 10


// Operador ternario: condicion ? expresionSiTrue : expresionSiFalse;
let edad = 25;
let mensaje1 = edad >= 18 ? 'Eres mayor de edad.' : 'Eres menor de edad.';
console.log(mensaje); // Imprime 'Eres mayor de edad.'
