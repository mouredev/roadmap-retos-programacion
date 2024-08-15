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

///////////////////////////////////////////////////////////////////////////

// --  OPERADORES  --
/*
    Indice:
        - 01.Operadores de asignación
        - 02.Operadores de comparación
        - 03.Operadores de aritméticos
        - 04.Operadores bit a bit (bitwise)
        - 05.Operadores lógicos
        - 06.Operadores de cadena (string)
        - 07.Operadores condicional (ternario)
        - 08.Operadores coma 
        - 09.Operadores unarios
        - 10.Operadores relacionales
*/

// -- 01 OPERADORES DE ASIGNACIÓN --
let x = 4;
let y = 3;
// Asignación
console.log(x = y); // x = 3

// Asignación de adición
console.log(x += y); // x + y => 4 + 3 = 7

// Asignación de resta
console.log(x -= y); // x - y => 4 - 3 = 1

// Asignación de multiplicación
console.log(x *= y); // x * y => 4 * 3 = 12

// Asignación de división
console.log(x /= y); // x / y => 4 / 3 = 1.333333....

// Asignación de residuo (modulo/module)
console.log(x %= y); // x % y => 4 % 3 = 1

// Asignación de exponenaciación
console.log(x **= y); // x ** y => 4 ** 3 = 64

// Asignación de desplazamientos a la izquierda
console.log(x <<= y); /* Aplica en binario:
    let a = 5; (5 = 00000000000000101)
    a <<= 2; (00000000000010100 = 20)
*/

// Asignación de desplazamientos a la derecha
console.log(x >>= y); /* Aplica en binario:
    let a = 20; (20 = 00000000000010100)
    a >>= 2; (00000000000000101 = 5)
*/

// Asignación de desplazamiento a la derecha sin signo
console.log(x >>>= y); /* Aplica en binario:
    let a = 5; (5 = 00000000000000101)
    a >>>= 2; (00000000000000001 = 1)

    let b = -5 (-00000000000000000000000000000101)
    b >>>= 2; (00111111111111111111111111111110)
*/

// Asignación AND bit a bit (bitwise)
console.log(x &= y); // x & y => 1 & 1 = 1 => true & true = true

// Asignación XOR bit a bit (bitwise)
console.log(x ^= y); /* 
x ^ y => 1 ^ 1 = 0 => true ^ true = false 
x ^ y => 1 ^ 0 = 1 => true ^ false = true 
00101 ^ 00011 = 00110 (5 ^ 3 = 6)
*/ 

// Asignación OR bit a bit (bitwise)
console.log(x |= y); /*
x | y => 1 | 1 = 1 => true | true = true 
x | y => 1 | 0 = 1 => true | false = true 
x | y => 0 | 0 = 0 => false | false = false 
00101 | 00011 = 00111 (5 | 3 = 7)
*/ 

// Asignación AND lógico
/*
    Este evalua el operando de la derecha y lo asigna a la izquierda 
    SOLO si el operando de la izquierda es VERDADERO (Truthy).

    Un valor VERDADERO (Truthy) es aquel que es considerado como "true"
    en una operacion booleana.

    Todos los valores se consideran VERDADEROS (Truthy) si
    no son considerados "Falsy".

    Los valores "Falsy" son:
    false, 0, -0, 0n, "", null, undefined, Nan (Not A Number) y document.all
*/ 
console.log(x &&= y); /*
let a = 1;
let b = 0;

a &&= 2; => Aqui a se convierte en 2.
b &&= 2 => Aqui b NO se convierte en 2 y permanece en 0
*/

// Asignación OR lógico
console.log(x ||= y); /* 
const a = { duracion: 50, titulo: '' };

a.duracion ||= 10;
console.log(a.duracion);
    -Resultado: 50 (Porque a.duracion = true)

a.titulo ||= 'No hay titulo';
console.log(a.tirulo);
    -Resultado: 'No hay titulo' (Porque a.titulo = false)
*/

// Asignación de anulación lógica
console.log(x ??= y); /*
const a = { duration: 50 };

a.speed ??= 25;
console.log(a.speed);
    -Resultado: 25 (Porque el valor "speed" es nulo.)

a.duration ??= 10;
console.log(a.duration);
    -Resultado: 50 (Porque el valor "duration" existe.)
*/

/////////////////////////////////////

// -- 02 OPERADORES DE COMPARACIÓN --

let igual = (x == y); // Devuelve true si los operandos son iguales.
let noEsIgual = (x != y); // Devuelve true si los operandos NO son iguales.
let estrictamenteIgual = (x === y); // Devuelve true si los operandos son iguales y del mismo tipo.
let desigualdadEstricta = (x !== y); // Devuelve true si los operandos son del mismo tipo pero no iguales, o son de diferente tipo.
let mayorQue = (x > y); // Devuelve true si el operando izquierdo es mayor que el operando derecho.
let mayorIgualQue = (x >= y); // Devuelve true si el operando izquierdo es mayor o igual que el operando derecho.
let menorQue = (x < y); // Devuelve true si el operando izquierdo es menor que el operando derecho.
let menorIgualQue = (x =< y); // Devuelve true si el operando izquierdo es menor o igual que el operando derecho.

/////////////////////////////////////

// -- 3 OPERADORES ARITMÉTICOS --

let residuo = "%" // Operador binario. Devuelve el resto entero de dividir los dos operandos. (12 % 5 = 2)

let incremento = "++" /* Operador unario. Agrega uno a su operando.
    Si se usa como operador prefijo (++x), devuelve el valor de su operando después de agregar uno; 
    si se usa como operador sufijo (x++), devuelve el valor de su operando antes de agregar uno.
*/

let decremento = "--" /* Operador unario. Resta uno de su operando. 
    El valor de retorno es análogo al del operador de incremento.
*/

let negacionUnaria = "-" /* Operador unario. Devuelve la negación de su operando. 
    Si x es 3, entonces -x devuelve -3.
*/

let positivoUnario = "+" /* Operador unario. Intenta convertir el operando en un número, si aún no lo es. 
    +"3" devuelve 3. +true devuelve 1.
*/

let operadorExponencial = "**" /* Calcula la base a la potencia de exponente, es decir, baseexponente.
    2 ** 3 devuelve 8. 10 ** -1 devuelve 0.1.
*/

/////////////////////////////////////

// -- 4 OPERADORES BIT A BIT (BITWISE) --

// AND a nivel de bits:
let and = a & b; /* Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos son unos.
    00101
    01101
    -----
    00101
*/

// OR a nivel de bits:
let or = a | b; /* Devuelve un cero en cada posición de bit para el cual los bits correspondientes de ambos operandos son ceros.
    00101
    01101
    -----
    01101
*/

// XOR a nivel de bits:
let xor = a ^ b; /* Devuelve un cero en cada posición de bit para la que los bits correspondientes son iguales. 
[Devuelve uno en cada posición de bit para la que los bits correspondientes son diferentes].
    00101
    01101
    -----
    01000
*/

// NOT a nivel de bits:
let not = ~ a; /* Invierte los bits de su operando.
    00101
    -----
    11010
*/

// Desplazamiento a la izquierda:
let leftShift = a << b; /* Desplaza a en representación binaria b bits hacia la izquierda, desplazándose en ceros desde la derecha.
    let a = 6 (0000110)
    let b = 2
    a << b = 24 (0011000)
*/

// Desplazamiento a la derecha de propagación de signo
let rightShift = a >> b; /* Desplaza a en representación binaria b bits hacia la izquierda, desplazándose en ceros desde la derecha.
    let a = 6 (0000110)
    let b = 2
    a >> b = 1 (00001)
*/

// Desplazamiento a la derecha de relleno cero
let rightZeroFillShift = a >>> b; /* Desplaza a en representación binaria b bits hacia la derecha, descartando los bits desplazados y desplazándose en ceros desde la izquierda.
    let a = 6 (0000110)
    let b = 2
    a >>> b = 1 (0000001)
*/

/////////////////////////////////////

// -- 5 OPERADORS LOGICOS --