// Arrays 
const arr1 = [1, 30, 20, "13", 50, true];
console.log(arr1);

// pop(). Remueve el último elemento del Array en el que se use y lo regresa.
let arr1LastIndex = arr1.pop();
console.log(arr1);
console.log(arr1LastIndex);

// unshift(). Añade elementos al inicio del Array en que se use y regresa el nuevo número de elementos en dicho Array.
const newArr1 = arr1.unshift(arr1LastIndex);
console.log(newArr1)
console.log(arr1);

// shift(). Remueve el primer elemento de un Array y lo regresa.
let arr1FirstIndex = arr1.shift();
console.log(arr1FirstIndex);
console.log(arr1);

// push(). Añade un elemento al final de un Array y regresa el nuevo número de elementos en dicho Array.
let oldArr1 = arr1.push(arr1FirstIndex);
console.log(oldArr1);
console.log(arr1);

// reverse(). Invierte el orden los elementos de un Array.
arr1.reverse();
console.log(arr1);


// Objetos
const miGata = {
    nombre: "Estrellita",
    edad: 4
}
console.log(miGata);

// Añadir propiedades a objetos
miGata.color = "Carey";
console.log(miGata);

// Eliminar propiedades de objetos
delete miGata.edad;
console.log(miGata);


// Ejercicio Extra


import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

const rl = readline.createInterface({ input, output });




let fulfilled = false;
let searchSuccessful = false;
let addSuccessful = false;
let updateSuccessful = false;
let deleteSuccessful = false;
let nameFound = false;
let actionChosen = false;


const directorio = [
    {
        name: "John",
        number: 933741390
    },
    {
        name: "Jane",
    }
];



function searchContact(str) {

    for(const persons of directorio) {
        if (persons.name === str.toString()) {
            fulfilled = true;
            searchSuccessful = true;
            console.log(persons);
            backToMenu();
            return;
        }
    }
    console.log("The person you are looking for is not in your contacts. Try Again.");
}


async function backToMenu() {
    let mainMenu = false;
    while (mainMenu != true) {
        let action = await rl.question("Would you like to go back to the main menu?. Please type 'yes' or 'no'. ");
        if (action === "yes") {
            mainMenu = true;
            fulfilled = false;
            searchSuccessful = false;
            addSuccessful = false;
            updateSuccessful = false;
            deleteSuccessful = false;
            directory();
        } else if (action === "no") {
            mainMenu = true;
            rl.close();
        } else {
            console.log("Wrong command.");
            continue;
        }
    }
}


function addContact(str, num) {

    const newContact = {};
    newContact.name = str.toString();
    newContact.number = Number(num);
    directorio.push(newContact);

    fulfilled = true;
    addSuccessful = true;
    console.log("New Contact added.");
    console.log(directorio);
    backToMenu();
    return directorio;
}


async function updateContact(str) {
    for(const persons of directorio) {
        if (persons.name === str.toString()) {
            nameFound = true;
            fulfilled = true;
            while (updateSuccessful != true) {
                let newNumber = await rl.question('What is the new number for the contact?. It must be exactly of 9 digits. ');
                Number(newNumber.trim());
                if (newNumber.length === 9 && newNumber !== "" && !isNaN(newNumber)) {
                    persons.number = Number(newNumber);
                    updateSuccessful = true;
                    console.log("Contact number updated.")
                    console.log(directorio);
                    backToMenu();
                    return;
                } else {
                    console.log("Contact number must be of exactly 9 digits.");
                }
            }
        }
    }
    console.log("That name is not in your contacts.");
}


function deleteContact(str) {
    for(const persons of directorio) {
        if (persons.name === str) {
            const index = directorio.indexOf(persons);
            directorio.splice(index, 1);
            fulfilled = true;
            deleteSuccessful = true;
            console.log("Contact deleted!")
            console.log(directorio);
            backToMenu();
            return;
        }
    }
    console.log("That name is not in your contacts, try again.");
}




async function directory() {


    while (fulfilled != true) {

    let action = await rl.question('What do you want to do? Type "search", "add", "update" or "delete" depending of what you are trying to do. ');
    if (action === "search") {
        while (searchSuccessful != true) {
            let action = await rl.question('Who are you searching for? ');
            searchContact(action);
        }
    } else if (action === "add") {
        let newName = await rl.question('What is the name of the new contact? ');
        while (addSuccessful != true){
            let newNumber = await rl.question('What is the number of the new contact?. It must be of exactly 9 digits. ');
            Number(newNumber.trim());
            if (newNumber.length === 9 && newNumber !== "" && !isNaN(newNumber)){
                addContact(newName, newNumber);
            } else {
                fulfilled = true;
                console.log("The phone number must be of exactly 9 numbers. Try again.");
            }
        }
    } else if (action === "update") {
        while (nameFound != true) {
            let newName = await rl.question('What is the name of the contact you want to update? ');
            updateContact(newName);
        }
    } else if (action === "delete") {
        while (deleteSuccessful != true) {
            let newName = await rl.question('What is the name of the contact you want to delete? ');
            deleteContact(newName);
        }
    } else {
            console.log("Wrong command, try again");
            continue;
        }
    }
}

directory();