/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
*/

/* +++++++++ ASIGNACIONES POR VALOR Y POR REFERENCIA +++++++++ */
console.log("+++++++++ ASIGNACIÓN POR VALOR +++++++++");

var a = 10;
var b = "JavaScript";
var x = a;
var y = b;
x = 15;
y = "ECMAScript";

console.log(`El valor de a es: ${a}`);
console.log(`El valor de b es: ${b}`);
console.log(`El valor de x es: ${x}`);
console.log(`El valor de y es: ${y}`);

console.log("+++++++++ ASIGNACIÓN POR REFERENCIA +++++++++");

var x = {
  a: 33,
  b: "Asignación por valor"
}

y = x;

x.a = 16;
x.b = "Asignación por referencia";

console.log("Valor de x:");
console.log(x);
console.log("Valor de y:");
console.log(y);

console.log("+++++++++ FUNCIÓN: ASIGNACIÓN POR VALOR +++++++++");

function asignacionPorValor(reassignObject) {
  reassignObject.age = 40;
}

var person = {
  name: "Peter",
  age: 34,
}

asignacionPorValor(person);
console.log(person);

console.log("+++++++++ ASIGNACIÓN POR REFERENCIA +++++++++");

function asignacionPorReferencia(reassignBountyHunter) {
  reassignBountyHunter.name = "Sylux";

  reassignBountyHunter = {
    name: "Samus Aran",
    specie: "Human",
  }

  return reassignBountyHunter;
}

var bountyHunter = {
  name: "Unknow",
  specie: "Unknow",
}

var bestBountyHunter = asignacionPorReferencia(bountyHunter);

console.log(bountyHunter);
console.log(bestBountyHunter);

/* +++++++++ DIFICULTAD EXTRA +++++++++ */
console.log("+++++++++ EJERCICIO +++++++++");

var a = 19;
var b = "Raúl";
var x = [1, 2, 3, 4];
var y = ["a", "b", "c", "d"];

function invertirPorValor(valor1, valor2) {
  valorIntercambiado1 = valor2;
  valorIntercambiado2 = valor1;

  return [valorIntercambiado1, valorIntercambiado2];
}

var [bToA, aToB] = invertirPorValor(a, b);

console.log(`Valor de a: ${a}. Valor de b: ${b}`);
console.log(`Valor intercambiado de a: ${bToA}. Valor intercambiado de b: ${aToB}`);

function invertirPorReferencia(referencia1, referencia2) {
  var referenciaIntercambiada1 = referencia2;
  var referenciaIntercambiada2 = referencia1;

  return [referenciaIntercambiada1, referenciaIntercambiada2];
}

var [xToY, yToX] = invertirPorReferencia(x, y);

console.log(`Referencia de x: ${x}. Referencia de y: ${y}`);
console.log(`Referencia invertida de x: ${xToY}. Referencia invertida de y: ${yToX} `);
