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

/******************************************************************************************************

Sitio web consultado para ejercicios: 

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators

*******************************************************************************************************
******************************************************************************************************/

console.log("--------> Tipos de operadores en javascript <--------");
console.log("****************  Operadores de asignación: ****************"); // Operadores de asignación

let numeroBase = 20; // Asignación
console.log("Asignación base =", numeroBase);
numeroBase += 20; // Suma
console.log("Suma 20 =", numeroBase);
numeroBase -= 10; // Resta
console.log("Resta 10 =", numeroBase);
numeroBase /= 2; // División
console.log("Divide 2 =", numeroBase);
numeroBase *= 4; // Multiplicación
console.log("Multiplica 4 =", numeroBase);
numeroBase **= 2; // Exponenciación
console.log("Exponencia 2 =", numeroBase);
numeroBase %= 7; // Resto
console.log("Resto división por 7 =", numeroBase);

/* "A parte de éstos existen otros poco comunes que son:

- Asignación de desplazamiento a la izquierda:            	x <<= y
- Asignación de desplazamiento a la derecha:	            x >>= y	
- Asignación de desplazamiento a la derecha sin signo:	    x >>>= y
- Asignación AND bit a bit:                               	x &= y	
- Asignación XOR bit a bit:                             	x ^= y		
- Asignación OR bit a bit:	                                x |= y	
- Asignación AND lógico:	                                x &&= y	
- Asignación OR lógico:           	                        x ||= y	
- Asignación de anulación lógica:	                        x ??= y

*/

console.log("**************** Operadores de comparación: ****************"); // Operadores de comparación

let numComp = 4;
let numCompDos = 8;

console.log("Igual", numComp, "y", numCompDos, "=", numComp == numCompDos); // Igual
console.log("No igual", numComp, "y", numCompDos, "=", numComp != numCompDos); // No igual
console.log(
  "Estrictamente igual",
  numComp,
  "y",
  numCompDos,
  "=",
  numComp === numCompDos
); // Estrictamente igual
console.log(
  "Estrictamente no igual",
  numComp,
  "y",
  numCompDos,
  "=",
  numComp !== numCompDos
); // Estrictamente no igual
console.log("Mayor", numComp, "que", numCompDos, "=", numComp > numCompDos); // Mayor
console.log(
  "Mayor o igual",
  numComp,
  "que",
  numCompDos,
  "=",
  numComp >= numCompDos
); // Mayor o igual
console.log("Menor", numComp, "que", numCompDos, "=", numComp < numCompDos); // Menor
console.log(
  "Menor o igual",
  numComp,
  "que",
  numCompDos,
  "=",
  numComp <= numCompDos
); // Menor o igual

console.log("**************** Operadores aritméticos: ****************"); // Operadores aritméticos

let a = 2;
let b = 3;
let c = 4;
let d = 5;

console.log("Suma", a, "+", b, "=", a + b); // Suma
console.log("Resta", d, "-", a, "=", d - a); // Resta
console.log("Multiplicación", b, "*", c, "=", b * c); // Multiplicación
console.log("División", c, "/", a, "=", c / a); // División
console.log("Resto", d, "/", a, "=", d % a); // Resto
console.log("Incremento", d, "=", ++d); // Incremento
console.log("Decremento", a, "=", --a); // Decremento
console.log("Negación unaria", a, "=", -a); // Negación unaria
console.log("Positivo unario", b, "=", b); // Positivo unario
console.log("Operador de exponenciación", c, "elevado a", d, "=", c ** d); // Operador de exponenciación

console.log("**************** Operadores bit a bit: ****************"); // Operadores bit a bit

console.log("AND (&) a nivel bits (a & b) =", a & b); // AND
console.log("OR (|) a nivel bits (a | b) =", a | b); // OR
console.log("XOR (^) a nivel bits (a ^ b) =", a ^ b); // XOR    (Anotación --> alt + 94 = ^)
console.log("NOT (~) a nivel bits (~a) =", ~b); // NOT     (Anotación --> alt + 126 = ~)
console.log(
  "Desplazamiento a la izquierda (<<) a nivel bits (a << b) =",
  a << b
); // Desplazamiento a la izquierda
console.log("Desplazamiento a la derecha (>>) a nivel bits (a >> b) =", a >> b); // Desplazamiento a la derecha

console.log("**************** Operadores lógicos: ****************"); // Operadores lógicos

console.log("AND lógico(&&) entre true y false =", true && false); // Devuelve true si ambos operandos son true, de lo contrario false.
console.log("OR lógico(||) entre true y false =", true || false); // Devuelve true si algún operando es true, de lo contrario false.
console.log("NOT lógico(!) de !false =", !false); // Devuelve false si el operando se puede convertir a true, de lo contrario true. ej: false por si solo se puede convertir a true, pero con el ! el resultante seria siempre false.

console.log("**************** Operadores de cadena: ****************"); // Operadores de cadena

console.log(
  "Ejemplo operador en cadena sumando a + b, donde a=(Retos de) y b=(Brais) =",
  "Retos de " + "Brais"
); // Suma de operadores en cadena.

console.log(
  "**************** Operador condicional (ternario): ****************"
); // Operador condicional (ternario)

edad = 21;
let esMayor = edad >= 18 ? "Es mayor de edad" : "Es menor de edad"; // si la edad es mayo o igual a 18 esMayor = Es mayor de edad. Sino es menor de edad.
edad = 17;
esMayor1 = edad >= 18 ? "Es mayor de edad" : "Es menor de edad"; // si la edad es mayo o igual a 18 esMayor = Es mayor de edad. Sino es menor de edad.

console.log("¿ Es mayor de edad con 21 años ? ", esMayor); // Si una condición es true entonces resulta val1, de lo contrario resulta val2
console.log("¿ Es mayor de edad con 17 años ? ", esMayor1); // Si una condición es true entonces resulta val1, de lo contrario resulta val2

console.log("**************** Operador coma: ****************"); // Operador coma

let resultado = (5 + 4, 4 / 2);

console.log(
  "Al evaluar ambos operandos y devolver el último, el resultado de la operación (5+4, 4/2) =",
  resultado
); // Evalúa ambos operandos y devuelve el valor del último operando.

console.log("**************** Operador unarios: ****************"); // Operadores unarios

let numDelete = { a: 23, b: 24 };
delete numDelete.a;
console.log("Variable con a y b de objetos y se elimina a  =", numDelete); // Operador delete que elimina la propiedad de un objeto
let typeOne = "Hola";
let typeTwo = 4;
console.log(
  "El tipo de operando no evaluado de",
  typeOne,
  "y",
  typeTwo,
  "=",
  typeof typeOne,
  typeof typeTwo
); // Operador typeof que devuelve el tipo de operando no evaluado
console.log(
  "El operador void aplicado a typeOne =",
  typeOne,
  "resulta en typeOne =",
  void typeOne
); // Operador void que especifica una expresión que se evaluará sin devolver un valor siempre como "undefined"

console.log("**************** Operador relacionales: ****************"); // Operadores relacionales

var selecciones = ["Argentina", "Alemania", "Brasil", "Francia", "Inglaterra"];

console.log(
  "Operador in devuelve del arreglo de la variable si hay 3 equipos =",
  3 in selecciones
); // Operador in devuelve true si la propiedad especificada está en el objeto especificado
console.log(
  "Operador instance of devuelve de la variable si es un array =",
  selecciones instanceof Array
); // Operador instance of devuelve true si el objeto especificado es del tipo de objeto especificado

console.log(
  "**************** Estructuras de control (bucles e iteración): ****************"
); // Estructuras de control (bucles e iteración)

for (let i = 0; i < 4; i++) {
  console.log("iteración for =", i);
} //for

let count = 0;
do {
  console.log("contador con do..while =", count);
  count++;
} while (count < 3); //do...while

let num = 4;
while (num > 0) {
  console.log("Número con while =", num);
  num--;
} //while

count = 0;
markLoop: while (count < 4) {
  console.log("contador con labeled =", count);
  count++;
  if (count === 4) {
    break markLoop;
  }
} //labeled

for (let count = 0; count < 4; count++) {
  if (count === 4) {
    break;
  }
  console.log("contador con break =", count);
} //break

for (let count = 0; count < 4; count++) {
  if (count === 2) {
    continue;
  }
  console.log("contador con continue en 2 =", count);
} //continue

let proveeedor = {
  nombre: "claro",
  downstream: "50 Mbps",
  upstream: "10 Mbps",
};
console.log("Ejemplo for..in =");
for (let propiedad in proveeedor) {
  console.log(propiedad + ":" + proveeedor[propiedad]);
} //for...in

console.log("Ejemplo for..of =");
let angulos = ["90°", "180°", "230°"];
for (let angulo of angulos) {
  console.log(angulo);
} //for...of

console.log("**************** Dificultad extra: ****************"); // Dificultad extra

for (let count = 10; count <= 55; count++) {
  if (count !== 16 && count % 2 === 0 && count % 3 !== 0) {
    console.log("Números en dificultad extra =", count);
  }
} // Dificultad extra : números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
