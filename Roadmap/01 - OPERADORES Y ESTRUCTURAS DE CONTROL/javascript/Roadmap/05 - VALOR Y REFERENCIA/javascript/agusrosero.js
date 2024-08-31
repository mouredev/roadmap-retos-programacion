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

// Asignación de variables por valor
let a = "Javascript";
let b = a;
b += "!";
console.log(a);
console.log(b);

// Asignación de variable por referencia
// Objetos
let person_1 = {
  name: "Hernan",
  age: 23,
};
let person_2 = person_1;
person_2.name = "Agustin";
person_2.age = 24;
console.log("person 1", person_1);
console.log("person 2", person_2);

// Array
let miArray = [1];
let miArray2 = miArray;
console.log(miArray);
console.log(miArray2);

// Funcion por valor
function funcionPorValor(str) {
  str = "Mi valor";
  return str;
}

let valor = "Fuera de la funcion";
console.log(funcionPorValor(valor));

// Funcion por referencia
function funcionPorReferencia(objeto) {
  objeto.propiedad = "Modificado";
  console.log("Dentro de la funcion", objeto);
}

let objeto = { propiedad: "Original" };
console.log("Antes de la funcion:", objeto);
funcionPorReferencia(objeto);
console.log("Despues de la funcion:", objeto);
