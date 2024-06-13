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
const mySet = new Set();

// Añade un elemento
mySet.add(1);
mySet.add(2);
mySet.add(3);
// Añade varios elementos en bloque al final.
mySet.add([4, 5, 6]);
// Elimina un elemento en una posición concreta.
mySet.delete(3);
// Comprueba si un elemento está en un conjunto.
console.log(mySet.has(2));
console.log(mySet);

// DIFICULTAD EXTRA:
// Unión
conjunto1 = new Set([1, 2, 3, 4]);
conjunto2 = new Set([5, 6, 7, 8]);
const union = [...new Set([...conjunto1, ...conjunto2])];
console.log(union);

// Intersección
const firstSet = new Set([1, 2, 3, 4, 5]);
const secondSet = new Set([4, 5, 6, 7, 8]);
const commonElements = [...firstSet].filter((element) =>
  secondSet.has(element)
);
const set = new Set(commonElements);
console.log(set);

// Diferencia
const firstSet2 = new Set([1, 2, 3, 4, 5]);
const secondSet2 = new Set([4, 5, 6, 7, 8]);

const diffElements = [...firstSet2].filter(
  (element) => !secondSet2.has(element)
);
const set2 = new Set(diffElements);
console.log(set2);

// Diferencia simétrica
const firstSet3 = new Set([1, 2, 3, 4, 5]);
const secondSet3 = new Set([4, 5, 6, 7, 8]);

const firstOnlyElements = [...firstSet3].filter(
  (element) => !secondSet3.has(element)
);
const secondOnlyElements = [...secondSet3].filter(
  (element) => !firstSet3.has(element)
);
const set3 = new Set([...firstOnlyElements, ...secondOnlyElements]);
console.log(set3);
