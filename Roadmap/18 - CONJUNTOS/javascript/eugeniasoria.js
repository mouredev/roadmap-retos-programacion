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

// Conjunto de datos
let conjunto = new Set(['Ash', 'Luna', 'Alma']);
console.log('Conjunto inicial: ', conjunto);

//Elemento añadido al final
conjunto.add('Ciri');
console.log('Elemento añadido al final: ', conjunto);

//Elemento añadido al principio
let unArray = Array.from(conjunto);
unArray.unshift('Camila');
conjunto = new Set(unArray);
console.log('Elemento añadido al principio: ', conjunto);

let numerosArray = [1, 2, 3];
let letrasArray = ['a', 'b', 'c'];
conjunto.add(numerosArray);
conjunto.add(letrasArray);
let objeto = {nombre: 'miobjeto', dato: 123}
conjunto.add(objeto);
console.log('Elementos en bloque añadidos al final: ', conjunto);

unArray = Array.from(conjunto);
let otroArray = [5, 10, 15];
unArray.splice(3, 0, otroArray);
conjunto = new Set(unArray);

let otroObjeto = {nombre: 'otroObjeto', numero: 888, codigo: 'ASD543'}
unArray.splice(1, 0, otroObjeto);
conjunto = new Set(unArray);

console.log('Elementos en bloque añadidos en posicion concreta(3 y 1): ', conjunto);

unArray = Array.from(conjunto);
unArray.splice(4,1)
conjunto = new Set(unArray);
console.log('Eliminar un elemento en posicion concreta(4): ', conjunto);

unArray = Array.from(conjunto);
unArray.splice(2,1);//Quito Ash
unArray.splice(2,0, 'AshMejorado');//Quito Ash
conjunto = new Set(unArray);
console.log('Actualizar elemento en posicion concreta(2): ', conjunto);

console.log('Comprobar si el elemento "AshMejorado" está en el conjunto: ', conjunto.has('AshMejorado'));
console.log('Comprobar si el elemento "EsteNoEstá" está en el conjunto: ', conjunto.has('EsteNoEstá'));
console.log('Comprobar si el elemento "[1, 2, 3]" está en el conjunto: ', conjunto.has([1, 2, 3]));
console.log('Comprobar si el elemento "numerosArray" está en el conjunto: ', conjunto.has(numerosArray));

conjunto.clear();
console.log('Eliminar todo el contenido del conjunto: ', conjunto);


console.log('\n\nDIFICULTAD EXTRA\n')

let conjA = new Set([3, 6, 9, 12]);
let conjB = new Set([2, 4, 6, 8, 10, 12]);
console.log('Conjunto A: ', conjA);
console.log('Conjunto B: ', conjB);

const union = [...new Set([...conjA, ...conjB])];
console.log('A union B: ', union);

let arrA = Array.from(conjA);
let arrInterseccion = arrA.filter((elem) => (conjB.has(elem)) ? elem : null);
let interseccion = new Set(arrInterseccion);
console.log('A intersección B: ', interseccion);

arrA = Array.from(conjA);
let arrDiferencia = arrA.filter((elem) => (conjB.has(elem)) ? null : elem);
let diferenciaAB = new Set(arrDiferencia);
console.log('Diferencia A - B: ', diferenciaAB);

let arrB = Array.from(conjB);
arrDiferencia = arrB.filter((elem) => (conjA.has(elem)) ? null : elem);
let diferenciaBA = new Set(arrDiferencia);
console.log('Diferencia B - A: ', diferenciaBA);

let diferenciaSimetrica = [...new Set([...diferenciaAB, ...diferenciaBA])];
console.log('Diferencia simétrica (A-B) U (B - A): ', diferenciaSimetrica);