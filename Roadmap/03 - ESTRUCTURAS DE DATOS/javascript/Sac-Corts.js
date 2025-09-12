// Exercise //

// Arrays
let array = [1, 2, 3, 4, 5];

array.push(6);
array.unshift(0);
array.splice(3, 0, 2.5);
console.log(array);

array.pop();
array.shift();
array.splice(3, 1);
console.log(array);

array[2] = 9;
console.log(array);

array.sort((a, b) => a - b);
console.log(array);

// Objects
let obj = {
    name: 'Isaac',
    age: 22,
    city: 'Reynosa'
};

obj.country = "México";
console.log(obj);

delete obj.city;
console.log(obj);

obj.age = 23;
console.log(obj);

let sortedKeys = Object.keys(obj).sort();
let sortedObj = {};
for (let key of sortedKeys) {
    sortedObj[key] = obj[key];
}
console.log(sortedObj);

// Sets
let set = new Set([2, 3, 5, 1, 4]); 

set.add(6);
console.log(set);

set.delete(3);
console.log(set);

let sortedSet = new Set([...set].sort((a, b) => a - b));
console.log(sortedSet);

// Maps
let map = new Map([
    ["name", "Isaac"],
    ["age", 22],
    ["city", "Reynosa"]
]);

map.set("country", "México");
console.log(map);

map.delete("city");
console.log(map);

map.set("age", 23);
console.log(map);

let sortedMapArray = [...map.entries()].sort();
let sortedMap = new Map(sortedMapArray);
console.log(sortedMap);

// WeakSets
let weakSet = new WeakSet();
let obj1 = { a: 1 };
let obj2 = { b: 2 };

weakSet.add(obj1);
weakSet.add(obj2);

weakSet.delete(obj1);
console.log(weakSet);

// WeakMaps
let weakMap = new WeakMap();
let key1 = {};
let key2 = {};

weakMap.set(key1, "value1");
weakMap.set(key2, "value2")

weakMap.delete(key1);

weakMap.set(key2, "newValue2");
console.log(weakMap);

// Extra Exercise //

const readline = require('readline');

const rl = readline.createInterface(
    process.stdin, process.stdout);


let contactBook = [];

function menu() {
    console.log(`
        1. Search contact
        2. Add contact
        3. Update contact
        4. Delete contact
        5. Exit
        `);
        rl.question('Select an option: ', handleUserInput);
}

function handleUserInput(option) {
    switch(option) {
        case '1':
            searchContact();
            break;
        case '2':
            addContact();
            break;
        case '3':
            updateContact();
            break;
        case '4':
            deleteContact();
            break;
        case '5':
            rl.close();
            break;
        default:
            console.log('Invalid option');
            menu();
    }
}

function searchContact() {
    rl.question("Enter the contact's username: ", (name) => {
        const contact = contactBook.find(c => c.name.toLowerCase() === name.toLowerCase());
        if (contact) {
            console.log(`Contact found: ${contact.name} - ${contact.phone}`);
        } else {
            console.log('Contact not found');
        }
        menu();
    });
}

function addContact() {
    rl.question("Enter the contact's username: ", (name) => {
        rl.question("Enter the contact's phone number: ", (phone) => {
            if (/^\d{1,11}$/.test(phone)) {
                contactBook.push({name, phone});
                console.log('Contact added');
            } else {
                console.log('Invalid phone number');
            }
            menu();
        });
    });
}

function updateContact() {
    rl.question("Enter the name of the contact to update: ", (name) => {
        const contact = contactBook.find(c => c.name.toLowerCase() === name.toLowerCase());
        if (contact) {
            rl.question("Enter the new phone number: ", (phone) => {
                if (/^\d{1,11}$/.test(phone)) {
                    contact.phone = phone;
                    console.log('Contact updated');
                } else {
                    console.log('Invalid phone number');
                }
                menu();
            });
        } else {
            console.log('Contact not found');
            menu();
        }
    });
}

function deleteContact() {
    rl.question("Enter the name of the contact to delete: ", (name) => {
        const index = contactBook.findIndex(c => c.name.toLowerCase() === name.toLowerCase());
        if (index !== -1) {
            contactBook.splice(index, 1);
            console.log('Contact deleted');
        } else {
            console.log('Contact not found');
        }
        menu();
    });
}

rl.on('close', () => {
    console.log('Finished program')
    process.exit(0);
});

menu();