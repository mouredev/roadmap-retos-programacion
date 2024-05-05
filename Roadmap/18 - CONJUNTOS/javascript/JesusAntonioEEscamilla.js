/** #18 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Verduras sera mis datos para utilizar
 */

//---EJERCIÓ---
// El conjunto de datos
let list = ['Apio', 'Brocoli', 'Maíz', 'Lechuga'];

// Añade un elemento al final
list.push('Rábano');
console.log('Agregando un elemento al final', list);

// Añade un elemento al principio
list.unshift('Zanahoria');
console.log('Agregando un elemento al inicio', list);

// Añade un bloque de elementos al final
const blockList = ['Champion', 'Cebolla', 'Pimiento'];
list.push(...blockList);
console.log('Agregando un bloque de elementos a la lista', list);

// Añade un bloque de elementos al alguna parte de lista
const block_medList = ['Esparrago', 'Calzaba', 'Papa'];
list.splice(3, 0, ...block_medList);
console.log('Agregando un bloque de elementos a la lista en especifico', list);

// Eliminando un elemento de la lista
list.splice(9, 1);
console.log('Eliminando un elemento a la lista en especifico', list);

// Comprobando un elemento esta en un conjunto de la lista
let elementList = list.includes('Zanahoria');
console.log('Se encuentra el elemento:', elementList);

// Se elimina toda la lista
list.length = 0;
console.log('Se elimino la lista', list);



/**-----DIFICULTAD EXTRA-----*/

//Pendiente

/**-----DIFICULTAD EXTRA-----*/