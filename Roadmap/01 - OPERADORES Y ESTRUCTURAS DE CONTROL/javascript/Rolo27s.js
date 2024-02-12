// Reto #01 -> OPERADORES Y ESTRUCTURAS DE CONTROL
// Fuente con más información: https://www.w3schools.com/js/js_operators.asp

/** Recordar que para usar la terminal con javascript es necesaria la instalación de NodeJS.
 *  En mi caso, para ejecutar el código y que se muestren los console.log ejecutaré este comando en mi ruta relativa de este código.
 *  .\roadmap-retos-programacion\Roadmap\01 - OPERADORES Y ESTRUCTURAS DE CONTROL\javascript> node Rolo27s.js
 */

// Defino un par de variables
let num1 = 27;
let num2 = 4;

// Operadores aritméticos:
console.log("**** Operadores aritméticos ****");
console.log(`Suma de ${num1} con ${num2} = ${num1 + num2}`);
console.log(`Resta de ${num1} con ${num2} = ${num1 - num2}`);
console.log(`Multiplicación de ${num1} con ${num2} = ${num1 * num2}`);
console.log(`División de ${num1} con ${num2} = ${num1 / num2}`);
console.log(`Resto o módulo de ${num1} con ${num2} = ${num1 % num2}`);
console.log(`Potencia de ${num1} a la ${num2} = ${num1 ** num2}`);

console.log(`Incremento de ${num1} en 1: ${++num1}`); // Para mostrar el valor de num1 sumado 1 tengo que usar el operador ++ antes de la variable. Es decir, primero opero y luego muestro. Si escribiese num1++, el valor de num1 se aumentaría pero no saldría reflejado en ese console log, ya que primero se mostraría y luego se ejecutaría la operación. En ese caso, se podría ver luego el valor de num1 que aumentó.

console.log(`Decremento de ${num2} en 1: ${--num2}`); // Misma lógica que el caso de arriba con num1.

console.log("\n\n**** Operadores de asignación ****");
// Operadores de asignación:
let newNumber = 7;
console.log(`The new number is ${newNumber}`);
newNumber = num1;
console.log(`Now the new number is ${newNumber}, like our num1 variable`); // Me acabo de dar cuenta que mezcle el ingles...
newNumber = 7; // Restart newNumber to 7

// Se pueden hacer todas la operaciones aritméticas explicadas al comienzo del código y luego asignarlas a otra variable con '='. Generalmente se usan expresiones simplificadas cuando se quiere hacer una operación aritmética y guardar el resultado sobrescribiendo el valor de alguna variable. Por ejemplo en lugar de escribir x = x + y (lo cual es válido), se suele usar x += y.

console.log("\n\n**** Operadores de comparación ****"); // Se utilizan para implementar lógica a nuestro programa. Se resolverá con True o False.

let comparacion1 = num1 > num2; // comparacion1 en este caso valdrá true.
console.log(comparacion1);

let comparacion2 = num1 < num2; // comparacion2 en este caso valdrá false.
console.log(comparacion2);

let comparacion3 = num1 == "28"; // comparacion3 en este caso valdrá true porque se compara de manera no estricta.
console.log(comparacion3);

let comparacion4 = num1 === "28"; // comparacion4 en este caso valdrá false porque se compara de manera estricta.
console.log(comparacion4);

let comparacion5 = num1 != "Real"; // Sera true, porque num1 es 28, que es diferente del string "Real".
console.log(comparacion5);

console.log("\n\n**** Operadores lógicos ****"); // Se utilizan para implementar lógica a nuestro programa. Se resolverá con True o False.
// Existe 3: &&, || y ! (AND, OR, NOT)
let condicion1 = num1 == 28 && num2 == 3; // sera true, porque num1 es 28 y num2 es 3.
console.log(condicion1);

let condicion2 = num1 == 28 || num2 == 2; // sera true, porque num1 es 28, aunque num2 no sea 2.
console.log(condicion2);

let condicion3 = num1 == 22 || num2 == 2; // Aquí si sera false, porque no es verdad ninguna de las dos condiciones.
console.log(condicion3);

console.log("\n\n**** Control de tipo ****");
console.log(typeof num1); // Tipo de variable de num1
console.log(typeof condicion1); // Tipo de variable de num1

// También existe instaceof, que sirve para saber si un objeto es una instancia de ese tipo de objeto. Devuelve un booleano.

console.log("\n\n**** Operadores Bitwise ****"); // No he usado esto en mi vida.
// &, |, ~, ^, <<, >>, >>>.
// AND, OR, NOT, XOR, left shift, right shift, unsigned right shift.

// ------------ DIFICULTAD EXTRA ---------
console.log("\n\n**** Dificultad extra ****");
for (let i = 10; i <= 55; i++) {
	if (i % 2 == 0 && i != 16 && i % 3 != 0) console.log("Valores filtrados:", i);
}
// Pues miré mas o menos y no vi ningún resultado raro. ¿Cual era la peculiaridad?
