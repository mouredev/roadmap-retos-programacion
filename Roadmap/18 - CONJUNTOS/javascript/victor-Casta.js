/*
  * Usando JavaScript, crea un conjunto de datos y realiza las siguientes operaciones:
  * - Añade un elemento al final.
  * - Añade un elemento al principio.
  * - Añade varios elementos en bloque al final.
  * - Añade varios elementos en una posición específica.
  * - Elimina un elemento de una posición específica.
  * - Actualiza el valor de un elemento en una posición específica.
  * - Comprueba si un elemento está en el conjunto.
  * - Elimina todo el contenido del conjunto.
*/

// Inicializa la lista de números
const numberList = [1, 2, 3];

console.log(`Lista original: ${numberList}`);

// Añade un elemento al final de la lista
numberList.push(4);
console.log(`Añadiendo elemento al final: ${numberList}`);

// Añade un elemento al inicio de la lista
numberList.unshift(0);
console.log(`Añadiendo elemento al inicio: ${numberList}`);

// Añade varios elementos al final de la lista
numberList.push(5, 6, 7);
console.log(`Añadiendo bloque de elementos al final: ${numberList}`);

// Añade varios elementos en una posición específica (índice 2)
numberList.splice(2, 0, -3, -4);
console.log(`Añadiendo bloque de elementos en una posición: ${numberList}`);

// Elimina un elemento de una posición específica (índice 2)
numberList.splice(2, 1);
console.log(`Eliminando un elemento de una posición: ${numberList}`);

// Actualiza el valor de un elemento en el índice 2
numberList[2] = -1;
console.log(`Actualizando el valor de un elemento: ${numberList}`);

// Comprueba si un elemento específico existe en la lista
console.log(`¿Existe el elemento -1 en la lista? ${numberList.includes(-1)}`);

// Elimina todo el contenido de la lista
numberList.length = 0;
console.log(`Eliminando todo el contenido: ${numberList}`);

/* -------- Operaciones con Sets -------- */

console.log('Unión de conjuntos:');
const set1 = new Set([1, 2, 0]);
const set2 = new Set([3, 4, 0]);

// Realiza la operación de unión añadiendo elementos de set2 a set1
for (let item of set2) {
  set1.add(item);
}
console.log(set1);

console.log('Intersección de conjuntos:');
const set3 = new Set([1, 2, 0]);
const set4 = new Set([3, 4, 0]);
const set5 = new Set();

// Realiza la operación de intersección
for (let item of set4) {
  if (set3.has(item)) {
    set5.add(item);
  }
}
console.log(set5);  // Debería mostrar Set { 0 }

console.log('Diferencia de conjuntos:');
const set6 = new Set([1, 2, 0]);
const set7 = new Set([3, 4, 0]);
const set8 = new Set();

// Realiza la operación de diferencia (set6 - set7)
for (let item of set6) {
  if (!set7.has(item)) {
    set8.add(item);
  }
}
console.log(set8);  // Debería mostrar Set { 1, 2 }

console.log('Más operaciones con conjuntos:');

// Unión usando el operador spread
const set9 = new Set([1, 2, 0]);
const set10 = new Set([3, 4, 0]);
const setUnion = new Set([...set9, ...set10]);

// Intersección usando filter
const intersection = new Set([...set9].filter(item => set10.has(item)));

// Diferencia (set10 - set9)
const difference1 = new Set([...set10].filter(item => !set9.has(item)));

// Diferencia (set9 - set10)
const difference2 = new Set([...set9].filter(item => !set10.has(item)));

console.log(setUnion);  // Resultado de la unión
console.log(intersection);  // Resultado de la intersección
console.log(difference1);  // Resultado de la diferencia (set10 - set9)
console.log(difference2);  // Resultado de la diferencia (set9 - set10)

// Diferencia simétrica (elementos en set9 o set10, pero no en ambos)
const symmetricDifference = new Set([...difference1, ...difference2]);
console.log(symmetricDifference);  // Resultado de la diferencia simétrica