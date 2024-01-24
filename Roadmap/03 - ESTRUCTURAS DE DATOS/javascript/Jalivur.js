/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

//ESTRUCTURAS DE DATOS:
//ARRAY
console.log(`===============`);
console.log(`ARRAYS: se pueden definir 
de 3 formas:`);
let arr1 = new Array(1, 1.1, "hola", true);
console.log(`let arr1 = new Array (1, 1.1, "hola", true)  
${arr1}`);
console.log(`===============`);
let arr2 = Array(1, 1.1, "hola", true);
console.log(`let arr2 = Array (1, 1.1, "hola", true)
${arr2}`);
console.log(`===============`);
let arr3 = [1, 1.1, "hola", true];
console.log(`let arr3 = [1, 1.1, "hola", true]
${arr3}`);
console.log(`===============`);
console.log(`Tambien se pueden asignar 
como propiedade de un objeto:
let obj1 = {}
obj1.prop = arr3`);
let obj1 = {};
obj1.prop = arr3;
console.log(obj1);
console.log(`===============`);
let arrayEmpty = Array(42);
console.log(`Tambien se pueden crear
sin elementos:
let arryEmpty = Array(${arrayEmpty.length})
${arrayEmpty}
en este caso con longitud ${arrayEmpty.length}.
Siempre y cuando el valor sea un numero entero.`);
console.log(`===============`);
let arrayEmpty2 = new Array(15);
console.log(`Tambien se puede:
let arryEmpty = new Array(${arrayEmpty2.length})
${arrayEmpty2}
en este caso con longitud ${arrayEmpty2.length}.
Si el valor no es numero enter, dara error de rango.`);
console.log(`===============`);
let arrayOneElement = [58];
console.log(`Sin ebargo con la declaracion literal:
let arryOneElement = [${arrayOneElement}]
en este caso es un array de un elemento: ${arrayOneElement}
culla longitud es ${arrayOneElement.length}.`);
console.log(`===============`);
let arrayOneElement2 = Array.of(10.5);
console.log(`Desde ES2015 se puede utilizar el metodo estatico Array.of:
let arryOneElement2 = Array.of(${arrayOneElement2})
en este caso es un array de un elemento: ${arrayOneElement2}
culla longitud es ${arrayOneElement2.length}.`);
console.log(`===============`);









