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
 */

// Operadores de asignación
let x = 1;      // Asignación
console.log("El valor de la variable x es: " + x);

x += 1;         // Asignación de adición
console.log("Si a x le sumamos 1 su valor es: " + x);

x -= 1;         // Asignación de resta
console.log("Si a x le restamos 1 su valor es: " + x);

x *= 2;         // Asignación de multiplicación
console.log("Si x lo multiplicamos por 2 su valor es: " + x);

x /= 2;         // Asignación de división
console.log("Si x lo dividimos entre 2 su valor es: " + x);

x = 7;         
x %= 2;         // Asignación de residuo
console.log("Le hemos dado a x el valor 7. Si ahora le asignamos el residuo de la división entre 2 su valor es: " + x);

x = 4;
x **= 2;        // Asignación de exponenciación
console.log("Ahora le hemos asignado a x el valor 4. Si elevamos a 2 el valor de x, ahora su valor es: " + x);

x = 16;
x <<= 2;        // Asignación de desplazamiento a la izq.
console.log("Ahora x vale 16. Si deplazamos dos bits a la izquierda obtenemos el valor: " + x);

x = 16;
x >>= 2;        // Asignación de desplazamiento a la der.
console.log("Ahora x vale 16. Si desplazamos 2 bits a la derecha obtenemos el valor: " + x);

x = 10;
x &= 2;         // Asignación AND bit a bit
console.log("Ahora x vale 10. Si hacemos una operación AND bit a bit con 2 obtenemos el valor: " + x);

x = 10;
x ^= 12;         // Asignación XOR bit a bit
console.log("Ahora x vale 10. Si hacemos una operación XOR bit a bit con 12 obtenemos el valor: " + x);

x = 10;
x |= 2;         // Asignación OR bit a bit
console.log("Ahora x vale 10. Si hacemos la operación OR bit a bit con 2 obtenemos el valor: " + x);

x = 5;
x &&= 2;        // Asignación AND lógico (es equivalente a "if(x){x=2}")
console.log("Ahora x vale 5. Si hacemos la operación AND lógico con 2 obtenemos el valor: " + x);

x = 0;
x ||= 2;        // Asignación OR lógico (es equivalente a "x=x||y")
console.log("Ahora x vale 0. Si hacemos la operación OR lógico con 2 obtenemos el valor: " + x);

x = null;
x ??= 5;        // Asignaciónde anulación lógica
console.log("Ahora x vale NULL. Si hacemos la opereación de anulación lógica con 5 obtenemos el valor: "+ x);

// Operadores de comparación
x = 1;     
let y = x == 1;  // Igual
if (y) {
    console.log("Ahora x vale 1. Si hacemos una comparación de igualdad con 1 obtenemos el valor: " + y);
}
let k = x == 4;
if (!k) {
    console.log("Mientras que si lo comparamos con 4 obtenemos: " + k);
}

x = 4
y = x != 3;     // Distinto de
if (y) {
    console.log("Ahora x vale 4. Si hacemos una comparación de desigualdad con 3 obtenemos que: " + y);
}
k = x != 4;
if(!k) {
    console.log("Mientras que si lo comparamos con 4 obtenemos que: " + k)
}

x = 1;
y = x === 1;    // Estrictamente igual
if (y) {
    console.log("Ahora x vale 1. Si hacemos una comparación de estricta igualdad con 1 entero obtenemos que: " + y);
}
k = x === "1";
if (!k) {
    console.log("Mientras que si lo comparamos con 1 en string obtenemos que: " + k);
}

x =
x !== 4;    // Desigualdad estricta
x > 0;      // Mayor que
x >= 1;     // Mayor o igual que
x < 2;      // Menor que
x <= 1;     // Menor o igual que
            // Nota: Todos retornan TRUE

            /*
// Operadores aritméticos
12 % 5;     // Residuo
++x;        // Incremento
--x;        // Decremento
-x;         // Negación unaria
+y;         // Positivo unario
2 ** 4;     // Exponenciación

// Operadores bit a bit
a & b;      // AND a nivel de bits 
a | b;      // OR a nivel de bits
a ^ b;      // XOR a nivel de bits
~ a;        // NOT a nivel de bits
a << b;     // Desplazamiento a la izquierda
a >> b;     // Desplazamiento a la derecha
a >>> b;    // Desplazamiento a la derecha de relleno cero

// Operadores lógicos
a && b;     // AND lógico
a || b;     // OR lógico
!a;         // NOT lógico

// Operadores de cadena
let myString = "mi";
console.log(myString + "cadena");

// Operador condicional (ternario) (condition ? val1: val2)
let age = 19
let statusFromAge = age >= 18 ? "adult" : "minor";
console.log(statusFromAge);

// Operador coma
let array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let bidimensionalArray = [x, x, x, x, x]
for (let i = 0, j = 9; i <= j; 1++, j--) {
    console.log("a[" + i + "][" + j + "] = " + a[i][j]);
}

// Operadores unarios (operadores con un solo operando)
let myObject = {h : 4}          // Delete
delete myObject.h;

console.log(typeof myObject);    // Typeof

void expression;

// Operadores relacionales
let colors = ["red", "blue", "green"]   // In
console.log("green" in colors);
console.log("banana" in colors);

console.log(colors instanceof Array);   // Instance Of

/* Programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos),
 pares, y que no son ni el 16 ni múltiplos de 3.*/

for(let i = 10; i <= 55; i++) {
    if ((i % 2 == 0) && (i != 16) && (i % 3 != 0)) {
        console.log(i)
    }
}









