/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#18 CONJUNTOS
---------------------------------------
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
// ________________________________________________________

// Crear una lista
let myList = ["a", "b", "c"];

// Añade un elemento al final.
myList.push("d");

// Añade un elemento al principio.
myList.unshift("-");

// Añade varios elementos en bloque al final.
myList.push("e", "f");

// Añade varios elementos en bloque en una posición concreta.
myList.splice(4, 0, "-", ">");

// Elimina en una posición concreta.
myList.splice(5, 1);

// Actualiza en una posición concreta.
myList[2] = "-b";

// Mostrar
console.log(myList);

// Comprobar
console.log(`"c" en lista: ${myList.includes("c")}`);
console.log(`"g" en lista: ${myList.includes("g")}`);

// Elimina todo el contenido.
myList.length = 0;
console.log(myList);

// ________________________________________________________
// DIFICULTAD EXTRA

// Crear conjuntos
let set1 = new Set(["a", "b", "c", "d"]);
let set2 = new Set(["c", "d", "e", "f"]);
console.log(`set1: ${[...set1]} - set2: ${[...set2]}`)

// Unión
let union = new Set([...set1, ...set2]);
console.log(`Unión: ${[...union]}`);

// Intersección
let intersection = new Set([...set1].filter(x => set2.has(x)));
console.log(`Intersección: ${[...intersection]}`);

// Diferencia (set1 - set2)
let difference1 = new Set([...set1].filter(x => !set2.has(x)));
console.log(`Diferencia: ${[...difference1]}`);

// Diferencia (set2 - set1)
let difference2 = new Set([...set2].filter(x => !set1.has(x)));
console.log(`Diferencia: ${[...difference2]}`);

// Diferencia simétrica
let symmetricDifference = new Set([
  ...[...set1].filter(x => !set2.has(x)),
  ...[...set2].filter(x => !set1.has(x))
]);
console.log(`Diferencia simétrica: ${[...symmetricDifference]}`);
