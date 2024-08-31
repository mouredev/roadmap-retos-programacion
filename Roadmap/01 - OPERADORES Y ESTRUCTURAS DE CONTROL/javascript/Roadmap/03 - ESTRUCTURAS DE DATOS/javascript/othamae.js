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

// Array 
console.log('** ARRAY **')
let array = new Array([1,2,3,4,5,6,7,8,9]) // creation
console.log(`This is the initial array: ${array}`)
array.push(10) // insert at the end
console.log(`Adding an element at the end: ${array}`)
array.unshift(0) // insert at the beginning
console.log(`Inserting an element at the beginning: ${array}`)
array.splice(2,0,55) // insert the element 3 at index 2
console.log(`Inserting an element at index 2: ${array}`)
array.splice(2,1) // delete one element starting at index 2
console.log(`Deleting an element at index 2: ${array}`)
array.pop() // delete the last element
console.log(`Deleting the last element: ${array}`)
array.shift() // delete the first element
console.log(`Deleting the first element: ${array}`)
array[2]= 0 // update the element at index 2
console.log(`Updating the element at index 2: ${array}`)
array.reverse() // reverse the array
console.log(`Reversing the array: ${array}`)
array.sort() // sort the array
console.log(`Sorting the array: ${array}`)

// Object
console.log('** OBJECT **')
let object = new Object({one: 1, two: 2, three: 3, four: 4}) // creation
console.log(`This is the initial object:`)
console.log(object)
object.five = 7 // insert at the end
console.log(`Adding an element at the end:`)
console.log(object)
object['six']= 6 // insert at the end
console.log(`Different way to add an element at the end:`)
console.log(object)
delete object.six // delete the element with key 'six' (Also working with: object['six'])
console.log(`Deleting the element with key 'six':`)
console.log(object)
object.five = 5 // update the element with key 'five' (Also working with: object['five'])
console.log(`Updating the element with key 'five':`)
console.log(object)


// Map
console.log('** MAP **')
let map = new Map([
    ['one', 1],
    ['two', 2],
    ['three', 3],
    ['four', 4],  
]) // creation
console.log(`This is the initial map: `)
console.log(map)
map.set('five', 6) // insert at the end
console.log(`Adding an element at the end:`)
console.log(map)
map.delete('two') // delete the element with key 'two' 
console.log(`Deleting the element with key 'two':`)
console.log(map)
map.set('five', 5) // update the element with key 'five'
console.log(`Updating the element with key 'five':`)
console.log(map)
map.clear() // delete all elements
console.log(`Deleting all elements:`)
console.log(map)

// Set
console.log('** SET **')
let set = new Set([1,2,3,4]) // creation
console.log(`This is the initial set: `)
console.log(set)
set.add(5) // insert at the end
console.log(`Adding an element at the end:`)
console.log(set)
set.delete(2) // delete the element with value 'two' 
console.log(`Deleting the element with value 'two':`)
console.log(set)
set.clear() // delete all elements
console.log(`Deleting all elements:`)
console.log(set)

// EXTRA TASK:

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function addressBook(book){       
    console.log('** Welcome to your address book **')
    console.log('This is your address book:')
    console.log(book)
    showOptions()
    rl.on('line', (input)=>{
        if (input == 1) addContact(book)
        if (input == 2) searchContact(book)
        if (input == 3) updateContact(book)
        if (input == 4) deleteContact(book)
        if (input == 5) rl.close()
        if (input > 5) console.log('Invalid option, please try again')
    })
  
}

function showOptions(){
    console.log('Please select an option')
    console.log('1. Add a new contact')
    console.log('2. Search a contact')
    console.log('3. Update a contact')
    console.log('4. Delete a contact')
    console.log('5. Exit')
}

function addContact(book){
    rl.question('Enter the name of the contact: ', (name)=>{
        rl.question('Enter the phone number of the contact: ', (phone)=>{
            if (!validatePhone(phone)){
                console.log('Invalid phone number, please try again')
                addContact(book)
                return
            }
            book.set(name, phone)
            console.log('Contact added successfully')
            console.log(book)
            showOptions()
        })
    })
}

function searchContact(book){
    rl.question('Enter the name of the contact to search: ', (name)=>{
        if (book.has(name))console.log(`The phone number of ${name} is ${book.get(name)}`)
        else console.log('Contact not found')
        showOptions()
    })
}

function updateContact(book){
    rl.question('Enter the name of the contact to update: ', (name)=>{
        if (book.has(name)){
            rl.question('Enter the new phone number of the contact: ', (phone)=>{
                if (!validatePhone(phone)){
                    console.log('Invalid phone number, please try again')
                    updateContact(book)
                    return
                }
                book.set(name, phone)
                console.log('Contact updated successfully')
                console.log(book)
                showOptions()
            })
        }
        else {
            console.log('Contact not found')
            showOptions()
        }
    })
}

function deleteContact(book){
    rl.question('Enter the name of the contact to delete: ', (name)=>{
        if (book.has(name)){
            book.delete(name)
            console.log('Contact deleted successfully')
            console.log(book)
            showOptions()
        }
        else {
            console.log('Contact not found')
            showOptions()
        }
    })
}

function validatePhone(phone){
    const regex = /^\d{1,11}$/;
    return regex.test(phone);
}


const book = new Map([
    ['Moure', '123456789'],
    ['Mario', '987654312'] 
])

addressBook(book)