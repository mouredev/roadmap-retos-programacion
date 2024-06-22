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

let data = [1, 2, 3, 4, 5];
console.log(data);  // [1, 2, 3, 4, 5]

// Añadir un elemento al final
data.push('final');
console.log(data);  // [1, 2, 3, 4, 5, 'final']

// Añadir un elemento al principio
data.unshift('start');
console.log(data);  // ['start', 1, 2, 3, 4, 5, 'final']

// Añadir varios elementos en bloque al final
data.push(['final', 'elements', 3])
console.log(data);  // ['start', 1, 2, 3, 4, 5, 'final', ['final', 'elements', 3]]

// Añadir varios elementos en bloque en una posición concreta
data.splice(2, 0, ['more', 'data', 'position', 2]);
console.log(data);
// ['start', 1, ['more', 'data', 'position', 2], 2, 3, 4, 5, 'final', ['final', 'elements', 3]]

// Elimina un elemento en una posición concreta
data.splice(3, 1);
console.log(data);
// ['start', 1, ['more', 'data', 'position', 2], 3, 4, 5, 'final', ['final', 'elements', 3]]

// Actualiza el valor de un elemento en una posición concreta
data[1] = true;
console.log(data);
// ['start', true, ['more', 'data', 'position', 2], 3, 4, 5, 'final', ['final', 'elements', 3]]

// Comprueba si un elemento está en un conjunto
console.log(data.includes('dato'));  // false
console.log(data.includes(5));  // true

// Elimina todo el contenido del conjunto
data.splice(0);
console.log(data);  // []


/*
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

const data1 = [1, 2, 3, 4];
const data2 = [1, 2, 3, 4, 5, 6, 7];

const union = [...new Set([...data1, ...data2])];
console.log('Union:', union);

const intersection = data1.filter(item => data2.includes(item));
console.log("Intersection:", intersection);

const diff12 = data1.filter(item => !data2.includes(item));
console.log('Difference 1-2:', diff12);
const diff21 = data2.filter(item => !data1.includes(item));
console.log('Difference 2-1:', diff21);

const symmetricDiff = [...new Set([...diff12, ...diff21])];
console.log('Symmetric difference:', symmetricDiff);