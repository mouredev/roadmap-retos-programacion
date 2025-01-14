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

const fruits = ['apple', 'orange', 'pear', 'banana'];

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
const orderedFruits = fruits.toSorted();    // Order without modifying the original
console.log(fruits);    // [ 'apple', 'peach', 'melon', 'banana' ]
console.log(orderedFruits); // [ 'apple', 'banana', 'melon', 'peach' ]

const numbers = [1, 4, 2, 8, 11];
let orderedNumbers = numbers.toSorted((a, b) => a - b);   // to order numbers in ascending
console.log(orderedNumbers);    // [ 1, 2, 4, 8, 11 ]
orderedNumbers = numbers.toSorted((a, b) => b - a);   // to order numbers in descending
console.log(orderedNumbers);    // [ 11, 8, 4, 2, 1 ]


// SET -> removes duplicates

const fruitsSet = new Set(['apple', 'orange', 'pear', 'banana', 'banana']);
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

const person = {
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


/* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const contactList = [];

const printMenu = () => {
    console.log('\nWhat do you want to do?');
    console.log('1. Add');
    console.log('2. Find');
    console.log('3. Update');
    console.log('4. Remove');
    console.log('5. View list');
    console.log('6. Exit');
};


const printContactData = ({ name, number }, printMessage=true) => {
    if (printMessage) {
        console.log('\nHere is the contact data:');
    }

    console.log(` - Name: ${name}`);
    console.log(` - Phone: ${number}`);
};


const checkCorrectPhone = (number) => {
    if (number.length > 11) {
        console.log('\nThe phone number must be less than 11 characters length.');
    } else if (isNaN(number)) {
        console.log('\nThe phone number must be a number');
    } else {
        return true;
    }

    return false;
}


const addContact = ({ name, number }) => {
    const isCorrectNumber = checkCorrectPhone(number);
    
    if (!isCorrectNumber) {
        return false;
    }

    if (findContactByName(name)) {
        console.log('\nThe introduced contact already exists.');
        return false;
    } else {
        contactList.push({ name, number });
        console.log('\nThe new contact has been created.');
        printContactData({ name, number });
        return true;
    }
};

const findContactByName = (nameToFind) => {
    return contactList.find(({ name }) => nameToFind === name);
}

const findContactIndex = ({ name: nameToFind, number: numberToFind }) => {
    return contactList.findIndex(({ name, number }) => (
        nameToFind === name && numberToFind === number
    ));
};

const updateContact = (oldData, newData) => {
    const contactIndex = findContactIndex(oldData);

    if (contactIndex === -1) {
        console.log('\nThe contact doesn\'t exist.');
        return false;
    }

    contactList[contactIndex] = {...newData};
    printContactData(newData);
    return true;
};

const removeContact = ({ name, number }) => {
    const contactIndex = findContactIndex({ name, number });

    if (contactIndex === -1) {
        console.log('\nThe contact doesn\'t exist.');
        return false;
    }

    contactList.splice(contactIndex, 1);
    return true;
};

const printContactList = () => {
    if (contactList.length === 0) {
        console.log('\nThere are not contacts yet.');
        return;
    }

    console.log('\nThese are the stored contacts:');
    for (let contact of contactList) {
        printContactData(contact, false);
        console.log('\n');
    }
};


function run() {
    printMenu();
    rl.question('Select your option (1-6): ', (option) => {
        if (option === '1') {
            // ADD NEW CONTACT

            rl.question('\nEnter the new name:\n> ', (newName) => {
                const contact = findContactByName(newName);

                if (contact) {
                    console.log('\nThe contact already exists. Use another name instead.');
                    run();
                }

                rl.question('Enter the new phone number:\n> ', (newNumber) => {
                    const newContact = {
                        name: newName,
                        number: newNumber
                    };
                    
                    addContact(newContact);
                    run();
                });
            });

        } else if (option === '2') {
            // FIND CONTACT

            rl.question('\nEnter the name to find:\n> ', (name) => {
                const contact = findContactByName(name);

                if (!contact) {
                    console.log('\nNo contact has been found.');
                } else {
                    printContactData(contact);
                }

                run();
            });

        } else if (option === '3') {
            // UPDATE CONTACT

            rl.question('\nEnter the name of the contact to update:\n> ', (oldName) => {
                const contact = findContactByName(oldName);

                if (!contact) {
                    console.log('\nThe contact doesn\'t exist. You can not update it.');
                    run();
                }

                console.log('\nWhat do you want to update?');
                console.log('1. Contact name');
                console.log('2. Contact phone number');
                rl.question('Select (1-2): ', (modifier) => {
                    const newData = {...contact};

                    if (modifier === '1') {
                        rl.question('Enter the new name: ', (newName) => {
                            newData.name = newName
                            updateContact(contact, newData);
                            run();
                        });
                    } else if (modifier === '2') {
                        rl.question('Enter the new phone number: ', (newNumber) => {
                            const isCorrectNumber = checkCorrectPhone(newNumber);

                            if (!isCorrectNumber) {
                                run();
                            }

                            newData.number = newNumber
                            updateContact(contact, newData);
                            run();
                        });
                    } else {
                        console.log('\nNot correct option.');
                    }
                });
            });

        } else if (option === '4') {
            // REMOVE CONTACT

            rl.question('\nEnter the name of the contact to remove:\n> ', cName => {
                const contact = findContactByName(cName);

                if (!contact) {
                    console.log('\nThe contact doesn\'t exist.');
                    run();
                }

                removeContact(contact);
                run();
            });

        } else if (option === '5') {
            printContactList();
            run();
        } else if (option === '6') {
            rl.close();
            return;
        } else {
            console.log('\nOption not allowed.');
            run();
        }
    })
}

run();