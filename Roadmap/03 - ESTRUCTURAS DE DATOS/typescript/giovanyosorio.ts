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

// Creación de estructuras de datos en TypeScript
// Array
let array = [1, 2, 3, 4, 5];
console.log(array);

// Operaciones de inserción y borrado
array.push(6);
console.log(array);
array.pop();
console.log(array);

// Operaciones de actualización
array[0] = 0;
console.log(array);

// Operaciones de ordenación
array.sort((a, b) => a - b);
console.log(array);

// Set
let set = new Set([1, 2, 3, 4, 5]);
console.log(set);

// Operaciones de inserción y borrado
set.add(6);
console.log(set);
set.delete(6);
console.log(set);

// Map
let map = new Map([
  ['a', 1],
  ['b', 2],
  ['c', 3],
]);
console.log(map);

// Operaciones de inserción y borrado
map.set('d', 4);
console.log(map);
map.delete('d');
console.log(map);

// Operaciones de actualización
map.set('a', 0);
console.log(map);

// Operaciones de ordenación
map.set('e', 5);
console.log(map);
console.log([...map.entries()].sort((a, b) => a[1] - b[1]));

// Agenda de contactos
let agenda = new Map<string, string>();

function addContact(name: string, phone: string): void {
  agenda.set(name, phone);
}

function removeContact(name: string): void {
  agenda.delete(name);
}

function updateContact(name: string, phone: string): void {
  agenda.set(name, phone);
}

function searchContact(name: string): void {
   agenda.get(name);
}

// Ejemplo de uso
addContact('Giovany', '1234567890');
addContact('Juan', '0987654321');
console.log(agenda);
removeContact('Juan');
console.log(agenda);
updateContact('Giovany', '0987654321');
console.log(agenda);
searchContact('Giovany');
console.log(agenda);
