// ********* Array *********
let array = [1, 2, 3, 4]

array.push(5) // Add
array.pop() // Delete
array = [5, 6, 2, 8] // Update
array.sort() // Sort


// ********* Set *********
let mySet = new Set([1, 2, 3, 4])

mySet.add('Hellooo') // Add
mySet.delete(1) // Delete
mySet = [2, 8, 7] // Update
mySet.sort() // Sort


// ********* Map *********
let myMap = new Map([
    ['name', 'Lia'],
    ['color', 'blue']
])

myMap.set('alias', 'li') // Add
myMap.delete('alias') // Delete
myMap.set('name', 'Mirko') // Update


// ********* Object *********
let person = {
    name: 'Matias',
    age: 10,
    walk: function () {
        console.log('Walking')
    }
}

person.color = 'red' // Add
delete person.color // Delete
person.name = 'Brais' // Update


//  DIFICULTAD EXTRA (opcional):
//  Crea una agenda de contactos por terminal.
//  - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  - Cada contacto debe tener un nombre y un número de teléfono.
//  - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//    los datos necesarios para llevarla a cabo.
//  - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
//    (o el número de dígitos que quieras)
//  - También se debe proponer una operación de finalización del programa.
// 

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


class Agenda {

    constructor() {
        this.contacts = []
    }

    createContact(name, phoneNumber) {
        console.log('I can create a contact')

        let validation = correctPhoneNumber(phoneNumber)
        if (validation !== 'Valid phone number') {
            console.log(validation)
            return
        }

        let contactFound = this.contacts.find(contact => contact.name === name) ||
            this.contacts.find(contact => contact.phoneNumber === phoneNumber)

        if (contactFound) {
            console.log('Contact already exists')
        } else {
            let contact = new Contact(name, phoneNumber)
            this.contacts.push(contact)
        }
    }

    searchContact(name) {
        console.log('I can search contact', name)
        let contactFound = this.contacts.find(contact => contact.name === name)
        if (contactFound) {
            console.log(`Name: ${contactFound.name}, Phone number: ${contactFound.phoneNumber}`)
        } else {
            console.log('Contact not found')
        }
    }

    updateContact(name, phoneNumber) {
        console.log('I can update contact')
        const index = this.contacts.findIndex(contact => contact.name === name);
        this.contacts.splice(index, 1, {name}, {phoneNumber})
    }

    deleteContact(name) {
        console.log('I can delete contact')
        const index = this.contacts.findIndex(contact => contact.name === name);
        if (index !== -1) {
            this.contacts.splice(index, 1)
            console.log('Contact deleted')
        }
        else {
            console.log('Contact does not exist')
        }
    }

    showContactList() {
        console.log(this.contacts)

    }

}

class Contact {

    constructor(name, phoneNumber) {
        this.name = name
        this.phoneNumber = phoneNumber
    }

    showContactData(name) {
        console.log(`Name: ${this.name}`)
        console.log(`Phone number: ${this.phoneNumber}`)
    }
}

function correctPhoneNumber(phoneNumber) {
    phoneNumber = phoneNumber.toString();
    let validDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

    if (phoneNumber.length !== 13) {
        return 'Invalid number. It must contain 13 digits';
    }

    for (let i = 0; i < phoneNumber.length; i++) {
        if (!validDigits.includes(phoneNumber[i])) {
            return 'Contains non-numeric values';
        }
    }

    return 'Valid phone number';
}


function showMenu(agenda) {

    console.log('-----------------------')
    console.log('1. Search contact')
    console.log('2. Create contact')
    console.log('3. Update contact')
    console.log('4. Delete contact')
    console.log('5. Show contact list')
    console.log('6. Exit')


    rl.question('Choose an option: ', (option) => {
        console.log('-----------------------')

        switch (option) {

            case '1':
                rl.question('Name of contact to search: ', (name) => {
                    agenda.searchContact(name)
                    showMenu(agenda)
                })
                break

            case '2':
                rl.question('Name of contact to create: ', (name) => {
                    rl.question(`Phone of ${name} `, (phoneNumber) => {
                        agenda.createContact(name, phoneNumber)
                        showMenu(agenda)
                    })
                })
                break

            case '3':
                rl.question('Name of contact to update: ', (name) => {
                    rl.question(`New phone of ${name} `, (phoneNumber) => {
                        agenda.updateContact(name, phoneNumber)
                        showMenu(agenda)
                    })
                })
                break

            case '4':
                rl.question('Name of contact to delete: ', (name) => {
                    agenda.deleteContact(name)
                    showMenu(agenda)
                })
                break

            case '5':
                agenda.showContactList()
                showMenu(agenda)
                break

            case '6':
                console.log('Bye!')
                rl.close()
                break

            default:
                console.log('Value is not correct')
                showMenu(agenda)
        }
    })

}

function main() {
    let agenda = new Agenda()
    showMenu(agenda)
}

main()
