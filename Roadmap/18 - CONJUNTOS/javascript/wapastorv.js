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
*/

/* 
La estructura de datos que se va a utilizar es un arreglo, ya que es una estructura que soporta todas las operaciones que se piden en el ejercicio.
*/

let arregloDeNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Agregar un número al final del arreglo
arregloDeNumeros.push(11);
console.log(arregloDeNumeros);// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

// Agregar un número al principio del arreglo
arregloDeNumeros.unshift(0);
console.log(arregloDeNumeros);// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

// Agregar varios números al final del arreglo
arregloDeNumeros.push(12, 13, 14, 15);
console.log(arregloDeNumeros); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 

// Agregar varios números en una posición concreta
arregloDeNumeros.splice(5, 0, 5.1, 5.2, 5.3);
console.log(arregloDeNumeros); // [0, 1, 2, 3, 4, 5, 5.1, 5.2, 5.3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

// Eliminar un elemento en una posición concreta
arregloDeNumeros.splice(5, 1);
console.log(arregloDeNumeros); // [0, 1, 2, 3, 4, 5.1, 5.2, 5.3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

// Actualizar el valor de un elemento en una posición concreta
arregloDeNumeros[5] = 5;
console.log(arregloDeNumeros); // [0, 1, 2, 3, 4, 5, 5.2, 5.3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

// Comprobar si un elemento está en un conjunto
console.log(arregloDeNumeros.includes(5)); // true

// Eliminar todo el contenido del conjunto
//arregloDeNumeros = [];
//console.log(arregloDeNumeros); // []



const array1 = [1, 2, 3, 6];
const array2 = [1, 2, 3, 4, 5];

console.log("Arreglo original 1: ",array1);
console.log("Arreglo original 2: ",array2);

// Crear conjuntos a partir de arreglos
const conjuntoA = new Set(array1);
const conjuntoB = new Set(array2);

// Operaciones de conjuntos con arreglos en JavaScript usando Set y Arreglos directamente
// Set es una estructura de datos que no permite elementos duplicados, por lo que es ideal para trabajar con conjuntos.

// Union de conjuntos

function unionConSet(setA, setB) {
    return new Set([...setA, ...setB]);
}

console.log("Union de conjuntos con SET: ",unionConSet(conjuntoA,conjuntoB)); // [1, 2, 3, 1, 2, 3, 4, 5]

// Union mantenimentdo la estructua de arreglo
const unionArray = (array1, array2) => {
    return [...new Set([...array1, ...array2])];
}
console.log("Union de arreglos",unionArray(array1, array2)); // [1, 2, 3, 4, 5, 6]



// Intersección de conjuntos
// La intersección contiene solo los elementos que están en ambos conjuntos.

function intersectionConSet(setA, setB) {
    return new Set([...setA].filter(x => setB.has(x)));
}
console.log("Intersecion de conjuntos con SET",intersectionConSet(conjuntoA,conjuntoB)); // [1, 2, 3]

// Intersección mantenimentdo la estructua de arreglo
const intersectionArray = (array1, array2) => {
    return array1.filter(value => array2.includes(value));
}
console.log("Intersecion de arreglos",intersectionArray(array1, array2)); // [1, 2, 3]


// Difference de conjuntos
// La diferencia contiene los elementos que están en el primer conjunto pero no en el segundo.

// Diferencia con la estructura de set
const differenceArraySet = (setA, setB) => {
    return new Set([...setA].filter(x => !setB.has(x)));
}
console.log("Diferencia con la estrucura de set: ",differenceArraySet(conjuntoA,conjuntoB)); // [6]

// Diferencia con la estructura de arreglos
const differenceArray = (array1, array2) => {
    return array1.filter(value => !array2.includes(value));
}
console.log("Diferencia con la estructura de arreglos: ",differenceArray(array1, array2)); // [6]

// Diferencia simétrica de conjuntos
// La diferencia simétrica contiene los elementos que están en uno de los conjuntos pero no en ambos.

//Diferencia simétrica con la estructura de set
const symmetricDifferenceArraySet = (setA, setB) => {
    return new Set([...setA].filter(x => !setB.has(x)).concat([...setB].filter(x => !setA.has(x))))
}
console.log("Diferencia simétrica con la estructura de set: ",symmetricDifferenceArraySet(conjuntoA,conjuntoB)); // [4, 5, 6]

// Diferencia simétrica con la estructura de arreglos
const symmetricDifferenceArray = (array1, array2) => {
    return array1.filter(value => !array2.includes(value)).concat(array2.filter(value => !array1.includes(value)));
}

console.log("Diferencia simétrica con la estructura de arreglos: ",symmetricDifferenceArray(array1, array2)); // [4, 5, 6]

