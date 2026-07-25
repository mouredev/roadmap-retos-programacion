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
const rl = readline.createInterface({ input, output });

const contacts = [
  { id: 1, name: "Juan", phone: 1234560987 },
  { id: 2, name: "Juan", phone: 1222543388 },
  { id: 3, name: "Pedro", phone: 1255566427 },
];

const ops = [
  { id: 1, name: "Search" },
  { id: 2, name: "Add" },
  { id: 3, name: "Update" },
  { id: 4, name: "Delete" },
];

const showAgenda = (arr) => {
  console.log(`
    *****************************************************
    *                    CONTACT LIST                   *
    *****************************************************`);
  arr.map((contact) =>
    console.log(`    * Name: ${contact.name}
    *   Phone: ${contact.phone}
    -----------------------------------------------------`)
  );
  isExit();
};

const isExit = async (op) => {
  const answer = await rl.question(`
    *****************************************************
    *                                                   *
    * Please select one of the following options:       *
    *                                                   *
    * 1: Go back and try again                          *
    * 2: Go to the Main Menu                            *
    * 3: Show contact list                              *
    * 0: Exit                                           *
    *                                                   *
    *****************************************************
    * `);

  if (+answer === 1) return op();
  if (+answer === 2) return agenda();
  if (+answer === 3) return showAgenda(contacts);

  rl.close();
};

const searchContact = async () => {
  console.log(`
    *****************************************************
    *                  SEARCH CONTACT                   *
    *****************************************************`);
  const contactInput =
    await rl.question(`    * Contact name?                                     *
    * `);

  const contactsFound = contacts.filter((contact) => {
    return contact.name.toLowerCase() === contactInput.toLowerCase();
  });

  if (contactsFound.length === 0) {
    console.log(`    *                                                   *
    * Contact not found.                                *`);
    return isExit(searchContact);
  }

  showAgenda(contactsFound);
  isExit(searchContact);
};

const addContact = async () => {
  console.log(`
    *****************************************************
    *                     ADD CONTACT                   *
    *****************************************************`);
  const contactInputName =
    await rl.question(`    * Contact name?                                     *
    * `);
  const contactInputPhone =
    await rl.question(`    *                                                   *
    * Phone number?                                     *
    * `);

  const nameHasNumbers = /\d/.test(contactInputName);
  const phoneHasLetters = /[a-zA-Z]/g.test(contactInputPhone);

  if (contactInputName === "" || nameHasNumbers) {
    console.log(`
    * Contact name is not valid.                        *
    * Only letters allowed.                             *`);
    return isExit(addContact);
  }

  if (
    contactInputPhone === "" ||
    phoneHasLetters ||
    contactInputPhone.length > 10
  ) {
    console.log(`
    * Contact phone number is not valid.                *
    * Only numbers allowed, has to be 10 digits         *`);
    return isExit(addContact);
  }

  const newContact = {
    id: contacts.length + 1,
    name: contactInputName,
    phone: +contactInputPhone,
  };

  contacts.push(newContact);
  console.log(`    *
    * The contact ${newContact.name} has been added sucessfully     *`);
  isExit(addContact);
};

const updateContact = async () => {
  console.log(`
    *****************************************************
    *                   UPDATE CONTACT                  *
    *****************************************************`);
  const contactInputData =
    await rl.question(`    * Contact to update? Type name or phone number      *
    * `);

  const foundContactIndex = contacts.findIndex(
    (contact) =>
      contact.name.toLowerCase() === contactInputData.toLowerCase() ||
      contact.phone === +contactInputData
  );

  if (foundContactIndex === -1) {
    console.log(`    * Contact ${contactInputData} not found`);
    return isExit(updateContact);
  }

  const contact = contacts[foundContactIndex];
  console.log(`    *                                                   *   
    * Updating contact ${contact.name}
    *                                                   *
    * Name: ${contact.name}
    *   Phone: ${contact.phone}
    -----------------------------------------------------`);

  const option =
    await rl.question(`    *                                                   *
    * What would you like to update?                    *
    * 1: Name                                           *
    * 2: Phone                                          *
    * `);

  if (+option !== 1 && +option !== 2) {
    console.log(`    *                                                   *
    * Please select a valid option                      *`);
  }

  if (+option === 1) {
    const newContactName =
      await rl.question(`    *                                                   *
    * Type the new name for ${contact.name} 
    * `);
    console.log(`    *                                                   *
    * Contact name was successfully updated to ${newContactName}`);
    contact.name = newContactName;
  }

  if (+option === 2) {
    const newContactPhone =
      await rl.question(`    *                                                   *
    * Type the new phone number for ${contact.name} 
    * `);

    const phoneHasLetters = /[a-zA-Z]/g.test(newContactPhone);
    if (phoneHasLetters) {
      console.log(`    *                                                   * 
    * Phone number must be a number, please try again   *`);
      return isExit(updateContact);
    }

    console.log(`    *                                                   *
    * Contact phone number was successfully updated to ${newContactPhone}`);
    contact.phone = newContactPhone;
  }

  isExit(updateContact);
};

const deleteContact = async () => {
  console.log(`
    *****************************************************
    *                   UPDATE CONTACT                  *
    *****************************************************`);
  const contactInputData =
    await rl.question(`    * Contact to delete? Type name or phone number      *
    * `);

  const foundContactIndex = contacts.findIndex(
    (contact) =>
      contact.name.toLowerCase() === contactInputData.toLowerCase() ||
      contact.phone === +contactInputData
  );

  if (foundContactIndex === -1) {
    console.log(`    * Contact ${contactInputData} not found`);
    return isExit(updateContact);
  }

  const contact = contacts[foundContactIndex];
  console.log(`    *                                                   *   
    * Deleting contact ${contact.name}
    *                                                   *
    * Name: ${contact.name}
    *   Phone: ${contact.phone}
    -----------------------------------------------------`);
  console.log(`
    * Contact ${contact.name} was successfully deleted`);
  contacts.splice(foundContactIndex, 1);

  isExit(deleteContact);
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
    * 5: Show contact list                              *
    *                                                   *
    * 0: Exit program                                   *
    *                                                   *
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
    case 5:
      showAgenda(contacts);
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
