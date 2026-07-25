/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

let arr = [1, 2, 3];
console.log("Conjunto de datos original", arr);
arr.push(4);
console.log("Añadir un elemento al final -> push(4)", arr);

arr.unshift(0);
console.log("Añadir un elemento al principio", arr);

arr.push(5, 6, 7);
console.log("Añadir varios elementos en bloque al final", arr);

arr.splice(3, 0, 2.5, 2.7);
console.log(
  "Añadir varios elementos en una posición concreta. Posición 3",
  arr
);

arr.splice(2, 1);
console.log("Eliminar un elemento de una posición concreta. Posición 2", arr);

console.log(
  arr.includes(2) ? "El 2 está en el conjunto" : "El 2 no está en el conjunto"
);
console.log(
  arr.includes(3) ? "El 3 está en el conjunto" : "El 3 no está en el conjunto"
);

arr.splice(0, arr.length);
console.log("Eliminar los datos del conjunto", arr);

console.log("------------------DIFICULTAD EXTRA-----------------");

let arr1 = [0, 1, 2];
let arr2 = [3, 4, 5];
let arr3 = [1, 3, 7];

console.log("UNIÓN");
console.log(
  `La unión de ${arr1} y ${arr2} es ${arr1.toSpliced(arr1.length, 0, arr2)}`
);

console.log("INTERSECCIÓN");
let interseccion = arr1.filter((el) => arr3.includes(el));
console.log(`La intersección de ${arr1} y ${arr3} es ${interseccion}`);

console.log("DIFERENCIA");
console.log(
  `La diferencia de arr1: ${arr1} respecto a arr3: ${arr3} es ${arr1.filter(
    (el) => !arr3.includes(el)
  )}`
);

console.log("DIFERENCIA SIMÉTRICA");
console.log(
  `La diferencia simétrica entre arr1 y arr3 es ${[
    arr1.filter((el) => !arr3.includes(el)),
    arr3.filter((el) => !arr1.includes(el)),
  ]}`
);
