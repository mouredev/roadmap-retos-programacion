/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
*/

// Array
let miArray = [1,2,3,4,5,6,7,8,9,10];
miArray.push(11); // inserción
miArray[2] = 4; // actualización
miArray.splice(0,1); // borrado
miArray.sort() // ordenación

// Sets
let miSet = new Set([1,2,3,4,5,6,7,8,10])
miSet.add(11) // inserción
miSet.delete(2) // borrado

// Objectos
let miObjeto = {
    nombre: 'Emanuel',
    edad: 20,
    facultad: 'ITU',
    carerra: 'Desarrollo de software'
}

miObjeto['semestres'] = 6 // inserción
delete facultad // borrado
miObjeto['edad'] = 21 // actualización

// Map
let miMapa = new Map([
    ["God of War", 1],
    ["Mortal kotmbat", 2],
    ["Batman", 3],
]);
miMapa.set("Mario", 4); // Inserción
miMapa.delete("Mortal kotmbat"); // Borrado
miMapa.set("God of War", 5); // Actualización