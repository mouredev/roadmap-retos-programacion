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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// ARRAY

const fruits: string[] = ['apple', 'orange', 'pear', 'banana'];

// Insert new items

fruits.push('melon');               // append at the end
fruits.unshift('strawberry');       // insert at the beginning
fruits.splice(2, 0, 'pineapple');   // insert in position 2 (starts at 0)

console.log(fruits);
// [ 'strawberry', 'apple', 'pineapple', 'orange', 'pear', 'banana', 'melon' ]

// Remove items from array

fruits.pop();           // removes 'melon' and returns it from array
fruits.shift();         // removes 'strawberry' and returns it
fruits.splice(2, 1);    // removes the item in position 2 (starts at 0)

console.log(fruits);    // [ 'apple', 'pineapple', 'pear', 'banana' ]

// Update the array

fruits[1] = 'peach';    // Modify the item at index 1 to 'peach'
console.log(fruits);    // [ 'apple', 'peach', 'pear', 'banana' ]
fruits.splice(2, 1, 'melon');   // Remove item at 2nd index and add there the 'melon' value
console.log(fruits);            // [ 'apple', 'peach', 'melon', 'banana' ]

// Order arrays

console.log(fruits);    // [ 'apple', 'peach', 'melon', 'banana' ]
const orderedFruits: string[] = fruits.slice().sort();    // Order without modifying the original
console.log(fruits);    // [ 'apple', 'peach', 'melon', 'banana' ]
console.log(orderedFruits); // [ 'apple', 'banana', 'melon', 'peach' ]

const numbers = [1, 4, 2, 8, 11];
let orderedNumbers: number[] = numbers.slice().sort((a, b) => a - b);   // to order numbers in ascending
console.log(orderedNumbers);    // [ 1, 2, 4, 8, 11 ]
orderedNumbers = numbers.slice().sort((a, b) => b - a);   // to order numbers in descending
console.log(orderedNumbers);    // [ 11, 8, 4, 2, 1 ]


// SET -> removes duplicates

const fruitsSet: Set<string> = new Set(['apple', 'orange', 'pear', 'banana', 'banana']);
console.log(fruitsSet);
// Set { 0: 'apple', 1: 'orange', 2: 'pear', 3: 'banana' }

// Insert new items

fruitsSet.add('melon');
console.log(fruitsSet);
// Set { 0: 'apple', 1: 'orange', 2: 'pear', 3: 'banana', 4: 'melon' }

// Remove one item

fruitsSet.delete('pear');
console.log(fruitsSet);
// Set { 0: 'apple', 1: 'orange', 2: 'banana', 3: 'melon' }

// Remove all

fruitsSet.clear();
console.log(fruitsSet);
// Set {}


// OBJECTS

interface Person {
    name: string,
    age: number,
    country?: string
}

const person: Person = {
    name: 'Naia',
    age: 25
};

// Insert new data

person.country = 'Spain';
console.log(person);
// { name: 'Naia', age: 25, country: 'Spain' }

// Update data

person.age = 26;
console.log(person);
// { name: 'Naia', age: 26, country: 'Spain' }

// Remove data

delete person.country;
console.log(person);
// { name: 'Naia', age: 26 }