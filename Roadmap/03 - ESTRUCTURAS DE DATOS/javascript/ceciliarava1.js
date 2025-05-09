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

// *********** Array ***********
let myArray = [] 

// Array methods
myArray.push(1, 2, 3, 4, 5) // Push elements
myArray.pop() // Delete the last element
myArray.shift() // Delete the first element
myArray.unshift('Hello') // Add element to the init
// console.log(myArray.slice(0,2)) // Print two first elements

// to insert "Feb" at index 1:
let months = ["Jan", "March", "April", "June"];
months.splice(1, 0, "Feb");
// console.log(months); // ["Jan", "Feb", "March", "April", "June"]

// To replace an element at index 4 with "May":
months.splice(4, 1, "May");
// console.log(months); // ["Jan", "Feb", "March", "April", "May"]


// *********** Set ***********
let mySet = new Set(['Hello', true, 7])

// Methods
mySet.add('Hellooo')
// console.log(mySet)

mySet.delete(7)
// console.log(mySet)

// console.log(mySet.has('Hello'))
// console.log(mySet.size)

let myArray1 = Array.from(mySet) // Create an array from a set
// console.log(myArray1)

mySet = new Set(myArray1) // Create a set from an array
// console.log(mySet)


// *********** Map ***********
let myMap = new Map( [
    ['name', 'Lia'],
    ['color', 'blue']
])

// console.log(myMap)
myMap.set('alias', 'li')
myMap.set('name', 'LIA')
// console.log(myMap)

// console.log(myMap.get('name'))
// console.log(myMap.has('name'))
// console.log(myMap.delete('color'))
// console.log(myMap)

// console.log(myMap.keys())
// console.log(myMap.values())

myMap.clear()
// console.log(myMap)

// *********** Object ***********

let person = {
    name: 'Matias',
    age: 10,
    walk: function() {
        console.log('Walking')
    }
}

person.name = 'Brais'
delete person.age
person.color = 'blue'
person.walk()
console.log(person)

// keys
for (let key in person) {
    console.log(key)
}

// values
for (let key in person) {
    console.log(person[key])
}

// constructor (no, it must be a class)
class Person {
    constructor(name, age) {
        this.name = name,
            this.age = age
    }
}

let person1 = new Person('Ludmila', 13)
console.log(person1)