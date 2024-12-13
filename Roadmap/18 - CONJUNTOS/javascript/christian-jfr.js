// #18 CONJUNTOS

/**
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 */

let colorSet = ['#0099ff', '#00ff99'];
console.log(colorSet); // [ '#0099ff', '#00ff99' ]

// * Añade un elemento al final.
colorSet.push('#99ff00');
console.log(colorSet); // [ '#0099ff', '#00ff99', '#99ff00' ]

// * Añade un elemento al principio.
colorSet.unshift('#9900ff');
console.log(colorSet); // [ '#9900ff', '#0099ff', '#00ff99', '#99ff00' ]

// * Añade varios elementos en bloque al final.
let colorSet2 = ['#ff0099', '#ff9900'];
colorSet.push(...colorSet2);
console.log(colorSet); // [ '#9900ff', '#0099ff', '#00ff99', '#99ff00', '#ff0099', '#ff9900' ]

// * Añade varios elementos en bloque en una posición concreta.
let colorSet3 = ['#ffaaff', '#aaffff'];
colorSet.splice(1, 0, ...colorSet3);
console.log(colorSet); // [ '#9900ff', '#ffaaff', '#aaffff', '#0099ff', '#00ff99', '#99ff00', '#ff0099', '#ff9900' ]

// * Elimina un elemento en una posición concreta.
colorSet.splice(3, 1);
console.log(colorSet); // [ '#9900ff', '#ffaaff', '#aaffff', '#00ff99', '#99ff00', '#ff0099', '#ff9900' ]

// * Actualiza el valor de un elemento en una posición concreta.
colorSet[0] = '#ffffaa';
console.log(colorSet); // [ '#ffffaa', '#ffaaff', '#aaffff', '#00ff99', '#99ff00', '#ff0099', '#ff9900' ]

// * Comprueba si un elemento está en un conjunto.
console.log(colorSet.includes('#ffffaa')); // true
console.log(colorSet.includes('#000000')); // false

// * Elimina todo el contenido del conjunto.
conjuntoDatos.length = 0;

/**
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 */

// * Unión.
const setOne = new Set([1, 2, 3, 5, 8, 13]);
const setTwo = new Set([1, 2, 2, 4, 8, 32]);
const union = setOne.union(setTwo);
console.log(union); // -> Set(8) { 1, 2, 3, 5, 8, 13, 4, 32 }

// * Intersección.
const intersection = setOne.intersection(setTwo);
console.log(intersection); // -> Set(3) { 1, 2, 8 }

// * Diferencia.
const differenceOne = setOne.difference(setTwo);
console.log(differenceOne); // -> Set(3) { 3, 5, 13 }

const differenceTwo = setTwo.difference(setOne);
console.log(differenceTwo); // -> Set(2) { 4, 32 }

// * Diferencia simétrica.

const symmetricDifference = setOne.symmetricDifference(setTwo);
console.log(symmetricDifference); // -> Set(5) { 3, 5, 13, 4, 32}
