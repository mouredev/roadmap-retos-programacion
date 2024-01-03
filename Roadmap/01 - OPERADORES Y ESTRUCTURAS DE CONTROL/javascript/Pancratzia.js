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
 * LAURA ORTEGA - 02/01/2024
 */

/***************************************************************************/
/* 1-OPERADORES DEL LENGUAJE */

console.log('OPERADORES DE ASIGNACIÓN');
console.log('Para asignar un valor a una variable, se utiliza el signo de igual (=)');
let numero = 10; //Asignación

numero +=2; //Asignación de adición
console.log('Existe la asignación de adición, donde se suma el valor de una variable con otro. El signo utilizado es (+=). Por ejemplo, si el valor de la variable es 10, el resultado de (10+2) es ' + numero);

numero-=2; //Asignación de resta
console.log('Opuesto a ella está la asignación de resta, donde se resta el valor de una variable con otro. El signo utilizado es (-=). Por ejemplo, si el valor de la variable es 12, el resultado de (12-2) es ' + numero);

numero*=3; //Asignación de multiplicación
console.log('Tenemos también la asignación de multiplicación, donde se multiplica el valor de una variable con otro. El signo utilizado es (*=). Por ejemplo, si el valor de la variable es 10, el resultado de (10*3) es ' + numero);

numero/=3; //Asignación de división
console.log('Y  asignación de división, donde se divide el valor de una variable con otro. El signo utilizado es (/=). Por ejemplo, si el valor de la variable es 30, el resultado de (30/3) es ' + numero);
let resto = numero;

resto %=3; //Asignación de residuo
console.log('Contamos además con la asignación de residuo (o resto), donde se obtiene el residuo de una división. El signo utilizado es (%=). Por ejemplo, si el valor de la variable es 30, el resultado de (30%3) es ' + resto);

numero**=2; //Asignación de potencia
console.log('Y  asignación de potencia, donde se obtiene la potencia de un número. El signo utilizado es (**=). Por ejemplo, si el valor de la variable es 10, el resultado de (10**2) es ' + numero);

/***************************************************************************/