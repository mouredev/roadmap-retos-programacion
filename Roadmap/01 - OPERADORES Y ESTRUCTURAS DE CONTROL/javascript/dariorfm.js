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


// OPERADORES ARITMETICOS
let a, b, c;

a = 5;
b = 3;
c = 2;

let suma = a + b;

let resta = b - c;

let multiplicacion = a * b *c;

let division = b / c;

let modulo = b % c;


console.log( `\nSuma de a + b = ${suma}\nResta de b - c = ${resta}\nMulplicación de a * b * c = ${multiplicacion}\n...etc.\n`, )


// OPERADORES DE INCREMENTO Y DECREMENTO
console.log(a,`\n`);

++a;
console.log(a,` incrementa de 1\n`);

--a;
console.log(a,` decrementa de 1\n`);

// * Recuerda que que el navegador devuelve el valor actual y luego incrementa la variable. 
// * Puedes ver que se ha incrementado si devuelves el valor variable nuevamente
a++;
console.log(a,` incrementa de 1\n`);

a--;
console.log(a,` decrementa de 1\n`);


// OPERADORES DE ASIGNACION

a = 1; // Asigna o reasigna un valor

// --> toma el valor de la variable y ejecuta la operación y asigna el resultado a la misma variable.
console.log(a += 3); // Adición asignación
console.log(a -= 2); // Resta asignación   
console.log(a *= 4); // Mulitplicación asignación
console.log(a /= 2); // División asignación
console.log(a %= 3); // Modulo asiganción



// OPERADORES DE COMPARACION

// --> Los resultados de estos pueden ser true o false.

console.log(a == b);    // Compruebas valores pero no el tipo de dato
console.log( a === b);  // Comprueba si los valores izquierdo y derecho son idénticos entre sí
console.log( a !== b);  // Comprueba si los valores izquierdo y derecho NO son idénticos entre sí
console.log( a < b);    // Comprueba si el valor izquierdo es menor que el derecho
console.log( a > b);    // Comprueba si el valor izquierdo es mayor que el derecho
console.log( a <= b);   // Comprueba si el valor izquierdo es mayor que el derecho
console.log( a >= b);   // Comprueba si el valor izquierdo es mayor o igual que el derecho


// OPERDADORES LOGICOS

// Operador lógico AND &&
console.log(true && true);   // → true
console.log(true && false);  // → false
console.log(false && false); // → false

//Operador lógico OR ||
console.log(true || true);   // → true
console.log(true || false);  // → true
console.log(false || false); // → false

//Operador lógico NOT !
console.log(!true);  // → false
console.log(!false); // → true


// ESTRUCTURAS DE CONTROL 

