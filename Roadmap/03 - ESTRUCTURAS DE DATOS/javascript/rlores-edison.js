/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */


/*KIND OF OBJECTS:

ARRAYS:

An array can hold many values under a single name.*/
const capitals = ["Madrid", "Paris", "London", "Rome"];
console.log(capitals);

const cars = ["Saab", "Volvo", "BMW", "Seat", "Ford"];
// Access the full array and print it in the Terminal:
console.log(cars); 


//ARRAY PROPERTIES AND METHODS:

// Access the values by referring ALWAYS to an index NUMBER (Arrays use numbered indexes):
console.log(cars[0]); // Saab in position 0

// Change the value of a specific index:
cars[0]= "Audi";
console.log(cars); // Changed element 0, now Audi

// Access the last element in the array:
console.log(cars[cars.length - 1]); // Ford in position 4

// Print the length of an array:
const movies = ["Alice in Wonderland", "The Lion King", "Aladdin", "Dumbo"];
let length = movies.length;
console.log(length); // 4

// Add a new element to the end of an array:
cars[cars.length] = "Mercedes"; // Using the .length property or the Array.push() method.
console.log(cars); // Mercedes in position 5
cars.push("BMW"); // Add a new element to the end of an array
console.log(cars); // BMW in position 6

//Add a new element to the beginning of an array:
cars.unshift("Volvo"); // Add a new element to the beginning of an array
console.log(cars); // Volvo in position 0

// Remove an element from an array:
cars.pop(); // Remove the last element from an array
console.log(cars); // ["Saab", "Volvo", "BMW", "Seat"]
cars.shift(); // Remove the first element from an array
console.log(cars); // ["Volvo", "BMW", "Seat"]

// Flat the array:
const myArr = [[1,2],[3,4],[5,6]];
const newArr = myArr.flat();
console.log(newArr); // [1, 2, 3, 4, 5, 6]  

// Array.at() method to find out which elements are in an array position:
console.log(cars.at(0)); 
console.log(cars.at(2));

// Sort an array:
let sort = movies.sort();
console.log(sort) // ["Aladdin", "Alice in Wonderland", "Dumbo", "The Lion King"]

// Looping through an array:
for (let i = 0; i < movies.length; i++) {
  console.log(movies[i]);
}

// We can also create de array and provide the elements:
const fruits = [];
fruits[0]= "pear";
fruits[1]= "apple";
fruits[2]= "banana";

console.log(fruits);

// Converting an Array to String or text, using .toString() method:
const pets = ["dog", "cat", "bird", "mouse", "fish"];
console.log(pets.toString());


/*OBJECTS: 

Objects use NAMES to Access its values (Objects use named indexes):*/ 
const person = {firstName:"Alf",  lastName:"Brown", age:"53"};
console.log(person);


/*NESTED ARRAYS AND OBJECTS:
Values in objects can be arrays, and values in arrays can be objects, variables of different types, functions and arrays:*/

const obj = {
  fruits: ["apple", "banana", "orange"]
};

const arr = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25 }
];

let mixedVar = "Hello"; // string
mixedVar = 42; // number
mixedVar = true; // boolean

const functionsArray = [
  function() { console.log("Function 1"); },
  () => { console.log("Arrow Function"); }
];

const nestedArr = ["outer", [1, 2, [3, 4]]];


/*
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

const contacts = [
  { name: "John Doe", phoneNumber: "+1234567890" },
  { name: "Jane Smith", phoneNumber: "+9876543210" },
  { name: "Mike Johnson", phoneNumber: "+1122334455" },
  { name: "Emily Brown", phoneNumber: "+5667788999" },
  { name: "David Lee", phoneNumber: "+4444555566" },
  { name: "Sarah Taylor", phoneNumber: "+7777888899" },
  { name: "Kevin White", phoneNumber: "+2223334444" },
  { name: "Lisa Nguyen", phoneNumber: "+5556667777" },
  { name: "Tom Harris", phoneNumber: "+8889990000" },
  { name: "Amy Martin", phoneNumber: "+1112223333" }
];   

//Funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.

const prompt = require("prompt-sync")({sigint: true});

console.log("Select the operation you want to perform:");
console.log("1. Search contact");
console.log("2. Insert contact");
console.log("3. Update contact");
console.log("4. Delete contact");
console.log("5. Exit");

let operationSelected = false;

while (!operationSelected) {
  let input = prompt("Enter the number of the operation you want to perform (1-5): ");

  if (input === null) {
    console.log("Operation cancelled.");
    break;
  }
  let selectedNumber = parseInt(input, 10);

  switch (selectedNumber) {
    case 1:
      console.log("Search contact selected");
      searchContacts();
      operationSelected = true;
      break;
    case 2:
      console.log("Insert contact selected");
      insertContact();
      operationSelected = true;
      break;
    case 3:
      console.log("Update contact selected");
      updateContact();
      operationSelected = true;
      break;
    case 4:
      console.log("Delete contact selected");
      deleteContact();
      operationSelected = true;
      break;
    case 5:
      console.log("Exiting...");
      operationSelected = true;
      break;
    default:
      console.log("Invalid input. Please enter a number between 1 and 5.");
  }
}

function searchContacts() {
  let searchTerm = prompt("Enter the name of the contact you want to search for: ");
  const foundContacts = contacts.filter((contact) => 
    contact.name.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  if (foundContacts.length > 0) {
    console.log(`Found ${foundContacts.length} matching contact(s):`);
    foundContacts.forEach((contact, index) => {
      console.log(`${index + 1}. Name: ${contact.name}, Phone: ${contact.phoneNumber}`);
    });
  } else {
    console.log("No contacts found.");
  }
}

function insertContact() {
  let name = prompt("Enter the name of the contact: ");
  let phoneNumber = prompt("Enter the phone number of the contact: ");
  
  if (!validatePhoneNumber(phoneNumber)) {
    console.log("Invalid phone number format. Please use XXX-XXX-XXXX");
    return;
  }
  
  contacts.push({ name, phoneNumber });
  console.log(`Contact ${contacts.length} added.`);
  console.log(contacts);
}

function validatePhoneNumber(phone) {
  const regex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
  return phone.match(regex);
}


function findContactIndex(name) {
  return contacts.findIndex((contact) => contact.name.toLowerCase() === name.toLowerCase());
}

function updateContact() {
  const name = prompt("Enter the name of the contact to update: ");
  const index = findContactIndex(name);
  if (index !== -1) {
    const phone = prompt("Enter the new phone number: ");
    if (!validatePhoneNumber(phone)) {
      console.log("Invalid phone number.");
      updateContact();
    } else {
      contacts[index].phoneNumber = phone;
      console.log("Contact updated.");
      console.log(contacts);
    }
  } else {
    console.log("Contact not found.");
    mainMenu();
  }
}

function deleteContact() {
  let name = prompt("Enter the name of the contact you want to delete: "); 
  const index = findContactIndex(name);
  if (index !== -1) {
    const deletedContact = contacts.splice(index, 1)[0];
    console.log(`Contact deleted: Name - ${deletedContact.name}, Phone - ${deletedContact.phoneNumber}`);
  } else {
    console.log("Contact not found.");
  }
  console.log(contacts);
}