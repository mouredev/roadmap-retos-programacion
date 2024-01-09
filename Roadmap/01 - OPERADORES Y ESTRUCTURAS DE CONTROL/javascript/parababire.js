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

//Operador asignación (=)
let x;
x = 8;
console.log(x);

let y = 2;
x += y;//Asignación de suma
console.log(x);

let z = 4;
x -= z;//Asignación de resta
console.log(x);
console.log(x *= y);//Asignación de multiplicación
console.log(x /= y);//Asignación de división
/*Existen otros operadores de asignación, pero no quiero extender el reto*/

//Operadores aritméticos binarios (+, -, *, /, %) y unarios (++, --)

let num1 = 10;
let num2 = 20;

let suma = num1 + num2;
console.log(suma);

let saludo = "Hola";
let persona = "Ángel"
console.log(saludo + ", " + persona);//El operador + puede unir cadenas

let num3 = "33";
console.log(+num3);//El operador + puede convertir cadenas en números

let resta = num1 - num2;
console.log(resta);
console.log(-resta);//El operador unario - devuelve la negación de su operando

let mult = num1 * num2;
console.log(mult);

let division = num1 / num2;
console.log(division);

let resto = 10 % 2;
console.log(resto);

let base = 2;
let exp = 4;
let pot = base ** exp;
console.log(pot);

mult++;
console.log(mult);

division--,
console.log(division);

//Operadores lógicos && (AND), || (OR), ! (NOT) y ?? (Nullish Coalescing)

let edad = 44;
let sexo = "masculino";
console.log(edad == 44 && sexo == "masculino");
console.log(edad == 45 || sexo == "masculino");

let futuroDev = false;
console.log(!futuroDev);

let numRetos2024;
let retosActuales = 2;
console.log(numRetos2024 ?? retosActuales);

//Operadores de comparación (>, <, >=, <=, !=, ==, ===)

console.log(num1 < num2);
console.log(num1 > num2);

let edadMinima = 18;
console.log(edad >= edadMinima);

let edadNiño = 10;
console.log(edadNiño <= edadMinima);

console.log(edad != edadNiño);

console.log(edad == "44");
console.log(edad === "44");
console.log(edad !== "44");

//Operadores de bits

/*El operando se convierte a 32 bits antes de la operación de bits*/

let a = 9; //En bits 00000000000000000000000000001001
let b = 12;//En bits 00000000000000000000000000001100
let c = -5;//En bits 11111111111111111111111111111011
let d = 5; //En bits 00000000000000000000000000000101

console.log(a & b);//Devuelve 1 donde los bits de cada operando es 1. De lo contrario devuelve 0.
console.log(a | b);//Devuelve 0 donde los bits de cada operando es 0. De lo contrario devuelve 1.
console.log(a ^ b);//Devuelve 0 donde los bits de cada operando son iguales. De lo contrario devuelve 1.
console.log(~ a);/*Invierte los bits de su operando. El bit más a la izquierda define si el número retornado es negativo o positivo*/
console.log(a << 1);//Agrega un 0 a la derecha del ultimo bit del operando.
console.log(c >> 1);/*Empuja una copia del bit más a la izquierda, los digitos se mueven a la derecha y el ultimo bit (a la derecha) se pierde*/
console.log(d >>> 1);//Un o más 0 bits es empujado a la izquierda y el bit más a la derecha se pierde.

//Estructuras de control

/*Condicionales*/
let año = prompt("Ingresa año de nacimiento?", "");

if (año >= 1965 && año <= 1981) {
  console.log("Perteneces a la generación X");
}

if (año >= 1965 && año <= 1981) {
  console.log("Perteneces a la generación X");
} else {
  console.log("No perteneces a la generación X");
}



if (num1 < num2) {
  console.log("Menor");
} else {
  console.log("Mayor");
}
