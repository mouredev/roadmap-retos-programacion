// *** Arrays *** //
// Creation
let numbers: number[] = [5, 2, 1, 8, 3];

// Insertion
numbers.push(7);
numbers.splice(2, 0, 6)

// Erased
numbers.pop();
numbers.splice(2, 1);

// Update
numbers[1] = 9;

// Sort
numbers.sort((a, b) => a - b);
console.log(numbers);

// *** Objects *** //
// Creation
type Person = {name: string, age?: number, email? : string}
let person: Person = { name: "Isaac", age: 22 }; 

// Insertion
person.email = "isaac@gmail.com";

// Erased 
delete person.age;

// Update
person.name = "Geovanni";
console.log(person);

// *** Sets *** //
// Creation 
let numbersSet: Set<number> = new Set([1, 2, 3, 4]);

// Insertion
numbersSet.add(5);

// Erased
numbersSet.delete(2);

// Update
// There is no direct operation to update a value in a Set,
// the old one must be removed and the new one added.
numbersSet.delete(4);
numbersSet.add(0);

// Sort
let sortedNumbersSet = new Set([...numbersSet].sort((a, b) => a - b));
console.log(numbersSet);
console.log(sortedNumbersSet);

// *** Maps *** //
// Creation
let map: Map<string, number> = new Map([["a", 1], ["b", 2]]);

// Insertion
map.set("c", 3);

// Erased 
map.delete("b");

// Update 
map.set("a", 10);

// Sort
let sortedMap = new Map([...map.entries()].sort((a, b) => a[1] - b[1]));
console.log(map);
console.log(sortedMap);

// *** Extra Exercise *** //
import * as readline from 'readline';

interface Contact {
    name: string;
    phone: string;
}

const contacts: Contact[] = [];
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function prompt(question: string): Promise<string> {
    return new Promise((resolve) => rl.question(question, resolve));
}

function isValidPhone(phone: string): boolean {
    return /^\d{1,11}$/.test(phone);
}

async function main() {
    while (true) {
        console.log('\nContact book');
        console.log('1. Search contact');
        console.log('2. Add contact');
        console.log('3. Update contact');
        console.log('4. Delete contact');
        console.log('5. Exit');

        const choice = await prompt('Choose an option: ');

        switch (choice) {
            case '1':
                await searchContact();
                break;
            case '2':
                await addContact();
                break;
            case '3':
                await updateContact();
                break;
            case '4':
                await deleteContact();
                break;
            case '5':
                console.log('Leaving the program...');
                rl.close();
                return;
            default:
                console.log('Invalid option');
                break;
        }
    }
}

async function searchContact() {
    const name = await prompt("Enter the name of the contact to search: ");
    const contact = contacts.find(c => c.name === name);
    if (contact) {
        console.log(`Name: ${contact.name}, Phone: ${contact.phone}`);
    } else {
        console.log("Contact not found");
    }
}

async function addContact() {
    const name = await prompt("Enter the name of the new contact: ");
    const phone = await prompt("Enter the phone (max 11 digits): ");

    if (!isValidPhone(phone)) {
        console.log("Invalid phone number, please try again");
        return;
    }

    contacts.push({ name, phone });
    console.log("Contact added");
}

async function updateContact() {
    const name = await prompt("Enter the name of the contact to update: ");
    const contact = contacts.find(c => c.name === name);
    
    if (!contact) {
        console.log("Contact not found");
        return;
    }

    const newPhone = await prompt("Enter the new phone number (max 11 digits): ");

    if (!isValidPhone(newPhone)) {
        console.log("Invalid phone number, please try again");
        return;
    }

    contact.phone = newPhone;
    console.log("Contact updated");
}

async function deleteContact() {
    const name = await prompt("Enter the name of the contact to delete: ");
    const index = contacts.findIndex(c => c.name === name);

    if (index === -1) {
        console.log("Contact not found");
        return;
    }

    contacts.splice(index, 1);
    console.log("Contact deleted");
}

main().catch(err => console.error(err));