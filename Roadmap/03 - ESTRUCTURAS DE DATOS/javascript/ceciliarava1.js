// 03-Javascript


/*
 * EJERCICIO:
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */


// Array
let myArray = new Array()
myArray = [1, 2, 3]

myArray.push(4)
myArray.pop()
myArray[0] = 200
myArray = myArray.sort((a, b) => a - b); // Ascending sort
myArray = myArray.sort((a, b) => b - a); // Descending sort
// console.log(myArray)


/* Set
    Can not update and sort because has no index, and are unique elements
*/
let mySet = new Set()
mySet = new Set(["Cat", "Dog", "Fox"])
mySet.add('Elephant')
mySet.delete("Cat")
// console.log(mySet)


/* Map
    Insertion order
*/
let myMap = new Map()
myMap = new Map([
  ["Name", "Cat"],
  ["Age", 21],
])
myMap.set("Location", "Chile")
myMap.delete("Name")
myMap.set("Location", "France")
// console.log(myMap)


// Exercise
class Contact {
    constructor(name, phoneNumber) {
        this._name = name
        this._phoneNumber = phoneNumber
    }

    set name(newName) {
        if (typeof newName == 'string') {
            this._name = newName 
        } else {
            console.log('Name must be a string')
        }
    }

    set phoneNumber(newPhoneNumber) {
        let phoneLength = newPhoneNumber.toString().length

        if (typeof newPhoneNumber == 'number' &&
            phoneLength >= 9 &&
            phoneLength <= 13) {

            this._phoneNumber = newPhoneNumber

        } else {
            console.log('Phone must be a number [9-13 char]')
        }
    }

    get name() {
        return this._name 
    }

    get phoneNumber() {
        return this._phoneNumber
    }
}


let newContact = new Contact()
newContact.name = 'Lucia'
newContact.phoneNumber = 123456789

console.log(newContact)