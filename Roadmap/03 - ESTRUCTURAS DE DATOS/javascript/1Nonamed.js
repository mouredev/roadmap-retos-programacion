// DATA STRUCTURES

console.log("----- ARRAYS -----");
const fruitsArr = ["Banana", "Pear", "Apple", "Apricot", "Banana"];
console.log("Fruits:", fruitsArr, "\n");

console.log("Array length:", fruitsArr.length);

// Acceder a las posiciones de un Array
console.log("fruitsArr[2] =>", fruitsArr[2]);
console.log("fruitsArr[3] =>", fruitsArr[3]);

console.log("\nMétodos de los Arrays:");

// Push -- Añadir (Modifica el array original)
fruitsArr.push(["Pear", "Apple"]);
console.log("- Push =>", fruitsArr);

// Unshift
fruitsArr.unshift("Watermelon");
console.log("- Unshift =>", fruitsArr);

// Filter
const bananasArr = fruitsArr.filter((fruit) => fruit === "Banana");
console.log("- Filter =>", bananasArr);

// Find
const foundFruit = fruitsArr.find((fruit) => fruit.startsWith("Apr"));
console.log("- Find =>", foundFruit);

// Sort
const numbers = [2, 3, 10, 2, 4];
console.log(
  "- Sort =>",
  numbers.sort((a, b) => a - b)
);

// Splice
console.log("- Splice =>", fruitsArr.splice(1, fruitsArr.length));

// Reverse
console.log("- Reverse =>", fruitsArr.reverse());

// Flat
console.log("- Flat =>", fruitsArr.flat());

console.log("----- OBJECTS -----");
const person = {
  id: 15,
  name: "Marcos",
  age: 20,
  knowledge: {
    javascript: false,
    go: false,
  },
};
console.log("Person: ", person);

person.name = "Lucas";
person.knowledge = { ...person.knowledge, python: true };

console.log("\nModified Person Obj: ", person);

console.log("----- MAPS -----");
// The Map object holds key-value pairs and remembers the original insertion order of the keys. Any value (both objects and primitive values) may be used as either a key or a value.

const people = new Map();
people.set("Poncho", { phone: "2347651029" });
people.set("Vicky", { phone: "2347654449", address: "9 Fow Ave" });

console.log(people);

// Extra Challenge
// Agenda de Contactos
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
import { SERVFAIL } from "node:dns";
const rl = readline.createInterface({ input, output });

const contacts = [
  { id: 1, name: "Juan", phone: 1234560987 },
  { id: 1, name: "Pedro", phone: 1234560987 },
];

const ops = [
  { id: 1, name: "Search" },
  { id: 2, name: "Add" },
  { id: 3, name: "Update" },
  { id: 4, name: "Delete" },
];

const searchContact = async () => {
  console.log(`
    *****************************************************
    *                  SEARCH CONTACT                   *
    *****************************************************
    `);
  const contactInput = await rl.question("Contact name? ");

  const contact = contacts.find((contact) => {
    return contact.name === contactInput;
  });

  if (!contact) {
    console.log("Contact not found, please try again");
    searchContact();
  } else {
    console.log(contact);
  }

  agenda();
};

const addContact = () => {
  console.log("Add");
};
const updateContact = () => {
  console.log("Update");
};
const deleteContact = () => {
  console.log("Delete");
};

async function agenda() {
  const op = await rl.question(
    `
    *****************************************************
    *                        AGENDA                     *
    *****************************************************
    *                                                   * 
    * What do you want to do today?                     *
    *                                                   *
    * 1: Search Contact                                 *
    * 2: Add Contact                                    *
    * 3: Update Contact                                 *
    * 4: Delete Contact                                 *
    *                                                   *
    * 0: Exit program                                   *
    *****************************************************
    
    * Insert the operation number or 0 to exit: `
  );
  switch (+op) {
    case 1:
      searchContact();
      break;
    case 2:
      addContact();
      break;
    case 3:
      updateContact();
      break;
    case 4:
      deleteContact();
      break;
    case 0:
      rl.close();
      break;
    default:
      console.log("Operation not valid");
      break;
  }
}

agenda();
