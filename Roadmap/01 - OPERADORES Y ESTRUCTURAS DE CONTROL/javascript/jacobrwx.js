// Tipos de Operadores en Javascript

// Variables de ejemplo
let a = 25;
let b = 10;
let result;

/* Operadores Aritméticos
*/

// Suma
result = a + b;

// Resta
result = a - b;

// Multiplicacion
result = a * b;

// Division
result = a / b;

// Modulo
result = a % b;

/* Operadores de Asignación
*/

// Asignacion simple
result = 100;

// Suma y asignacion
result += a;

// Resta y asignacion
result -= b;

// Multiplicacion y asignacion
result *= a;

// Division y asignacion 
result /= b;

/* Operador Incremento/Decremento
*/

// Incremento
result = ++a;

// Decremento
result = --b;

/* Operadores de Comparacion
*/

// Igualdad, conversion de tipo
result = a == b;

// Igualdad estricta
result = a === b;

// Desigualdad
result = a != b;

// Desigualdad estricta
result = a !== b;

// Mayor que
result = a > b;

// Menor que 
result = a < b;

// Mayor o Igual que 
result = a >= b;

// Menor o Igual que
result = a <= b;

/* Operadores Logicos
*/

// AND logico
result = a < b && b == a;

//OR logico
result = a == b || b < a;

//NOT logico
let isTrue = true;
result = !isTrue;

/* Operadores Condicionales
*/

// Ternario
let isEven = a % 2 === 0 ? "Even" : "Odd";

/* Operadores de Tipo
*/

// Typeof
result = typeof a;

/* ESTRUCTURAS DE CONTROL

Existe 8 tipos de estructuras de control

1. if
2. for
3. while
4. do-while
5. for...in
6. for...of
7. switch
8. estructura de control con operador ternario
*/

for (let num = 10; num <= 55; ++num) {
    if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
        console.log(num);
    }
}