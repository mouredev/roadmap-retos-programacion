/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

// Pilas (Stacks - LIFO)  (Last In, First Out)
const pilaDias = ["lunes", "martes", "miercoles", "jueves", "viernes"];
//console.log(pilaDias);

pilaDias.push("sabado");
//console.log(pilaDias);

pilaDias.pop();
//console.log(pilaDias);

// Colas (Queues - FIFO)  (First In, First Out)
const colaDias = ["lunes", "martes", "miercoles", "jueves", "viernes"];

colaDias.push("sabado");
//console.log(colaDias);

colaDias.shift();
//console.log(colaDias);
