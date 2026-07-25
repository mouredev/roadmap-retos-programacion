// const { get } = require('http');
const readline = require('readline');

/*
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/
// --- List ---
// Population, update operations
let fruitsList = ['Banana', 'Apple'];   // Creating an array
fruitsList[0] = 'Orange';               // Modifying an element based on its position
fruitsList.push('Banana');              // Adding an element to the end
fruitsList.unshift('Banana');           // Adding an element to the beginning
fruitsList.splice(1, 0, 'Strawberry')   // Adding an element on an specific position
fruitsList.splice(4, 1, 'Pear')         // Replacing an element on an specific position
fruitsList.splice(0, 0, 'Grapes', 'Watermelon') // Adding more than one element starting on an specific position
let groceryList = new Array();          // Creating an array
groceryList = fruitsList.concat(['Tomato', 'Pepper'])   // Adding another array to the first array

// Removing operations
groceryList = groceryList.slice(0,3);   // Slicing the array
groceryList.pop();                      // Removing the last element
groceryList.shift();                    // Removing the first element
groceryList.splice(1, 1);               // Removing an element of an specific position
groceryList.reverse();                  // Reversing the array

// Sorting operation
let numberList = [10, 2, 3, 5, 73];
numberList.sort((a, b) => a - b);       // Sorting the array ascending order
numberList.sort((a, b) => b - a);       // Sorting the array descending order

// --- Maps ---
const phoneCharacteristics = new Map();         // Creating a map
phoneCharacteristics.set('Battery', '100');     // Adding an element to the map
phoneCharacteristics.set('Portability', true);  // Adding an element to the map
phoneCharacteristics.set('Wireless', false);    // Adding an element to the map
phoneCharacteristics.set('PhoneNumber', 12321)  // Adding an element to the map
phoneCharacteristics.delete('Battery');         // Remove an element using it's key
let phonePortability = phoneCharacteristics.get('Portability'); // Get an element vßalue using it's key

// --- Set ---
const user = new Set(); // Creating a set
user.add('name');       // Adding an element to the set
user.add('age');        // Adding an element to the set
user.add('weight');     // Adding an element to the set
user.delete('weight');  // Removing an element of the set
user.clear();           // Clear all the set


// --- Objects ---
let newCar = {color: 'red', hasWindows: true, year: 2025};  // Creating an object
newCar.electric = false;    // Adding a new element to the object
newCar.color = 'Blue';      // Updating a value based on a key
delete newCar.hasWindows;   // Removing an element
isColorKeyAvailable = 'color' in newCar // Verifying that an object has a value

/*
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
(o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
*/
let agenda = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function getUserInput(questionText) {
    return new Promise((resolve) => {
        rl.question(questionText, (ans) => {
            resolve(ans);
        });
    });
}

async function registerContact() {
    let contact = {};
    const contactName = await getUserInput('Enter the contact name: ');
    const contactPhoneNumber = await getUserInput('Enter contact phone number: ');
    if (isNaN(contact.phoneNumber) || contact.phoneNumber.toString().split('').length > 11) {
        console.log('The entered value must be a number with less than 11 digits');
        showMenu();
    }
    else {
        contact = {name: contactName, phoneNumber: contactPhoneNumber};
        agenda.push(contact);
        console.log('---------------------------------');
        console.log('New entry registered successfully');
        console.log('Contact name: ' + contact.name);
        console.log('Contact phone number: ' + contact.phoneNumber);
        console.log('---------------------------------');
        showMenu();
    }
}

async function updateContact(nameToSearch) {
    const contact = agenda.find(contact => contact.name === nameToSearch);
    if (contact) {
        contact.phoneNumber = await getUserInput('Enter new phone number: ');
        if (isNaN(contact.phoneNumber) || contact.phoneNumber.toString().split('').length > 11) {
            console.log('The entered value must be a number with less than 11 digits');
            showMenu();
        }
        else {
            console.log('---------------------------------');
            console.log('New phone number registered successfully');
            console.log('Contact name: ' + contact.name);
            console.log('Contact phone number: ' + contact.phoneNumber);
            console.log('---------------------------------');
            showMenu();
        }
    }
    else {
        contactNotFoundMessage();
    }
}

async function removeContact(nameToSearch) {
    const contact = agenda.find(contact => contact.name === nameToSearch);
    if (contact) {
        console.log('---------------------------------');
        console.log('The contact was succesfully removed from the agenda');
        console.log('Contact name: ' + contact.name);
        console.log('Contact phone number: ' + contact.phoneNumber);
        const index = agenda.indexOf(contact);
        agenda.splice(index, 1);
        console.log('---------------------------------');
        showMenu();
    }
    else {
        contactNotFoundMessage();
    }
}

async function getPhoneNumberByName(nameToSearch) {
    // Find the contact with the matching name in the global 'agenda' list
    const contact = agenda.find(contact => contact.name === nameToSearch);
    if (contact) {
        console.log('---------------------------------');
        console.log('Contact "' + nameToSearch + '" found in the agenda');
        console.log(nameToSearch + ': ' + contact.phoneNumber);
        console.log('---------------------------------');
        showMenu()
    }
    else {
        contactNotFoundMessage();
    }
}

function isAgendaEmpty() {
    if (agenda.length === 0) {
        console.log('---------------------------------');
        console.log('Agenda is empty, try adding some contacts first');
        console.log('---------------------------------');
        showMenu();
    }
}

function contactNotFoundMessage() {
    console.log('---------------------------------');
    console.log('The contact was not found in the agenda');
    console.log('---------------------------------');
    showMenu();
}

async function showMenu() {
    console.log('Select an option');
    console.log('1. Register a new contact (Insert)');
    console.log('2. Update an existing contact');
    console.log('3. Remove an existing contact');
    console.log('4. Search a contact')
    console.log('5. Exit');
    const option = await getUserInput('Select your option (1-5): ');
    switch (option) {
        case '1':
            registerContact();
            break;
        case '2':
            isAgendaEmpty();
            const nameToUpdate = await getUserInput('Enter the contact name to update: ');
            updateContact(nameToUpdate);    
            break;
        case '3':
            isAgendaEmpty();
            const nameToRemove = await getUserInput('Enter the contact name to remove: ');
            removeContact(nameToRemove);
            break;
        case '4':
            isAgendaEmpty();
            const nameToSearch = await getUserInput('Enter the contact name to search: ');
            getPhoneNumberByName(nameToSearch);
            break;
        case '5':
            process.exit(0);
        default:
            console.log('---------------------------------');
            console.log('Invalid option. Please select a valid option (1-5)');
            console.log('---------------------------------');
            showMenu();
    }
}

showMenu();
