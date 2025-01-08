import { createInterface } from "readline";

/* -- exercise */
let fruits = ["Apple", "Banana", "Cherry"];

fruits.push("Date");
console.log("Array after insertion:", fruits);
fruits.pop();
console.log("Array after deletion:", fruits);
fruits[1] = "Blueberry";
console.log("Array after update:", fruits);
fruits.sort();
console.log("Sorted array:", fruits);

let colors = new Set(["red", "green", "blue"]);
colors.add("yellow");
console.log("Set after insertion:", colors);
colors.delete("green");
console.log("Set after deletion:", colors);

let fruitsMap = new Map([
  ["apple", 5],
  ["banana", 10],
  ["cherry", 15],
]);
fruitsMap.set("date", 20);
console.log("Map after insertion:", fruitsMap);
fruitsMap.delete("banana");
console.log("Map after deletion:", fruitsMap);
fruitsMap.set("cherry", 18);
console.log("Map after update:", fruitsMap);

let sentence = "Hello, world!";
let newSentence = sentence.replace("world", "JavaScript");
console.log("String after replacement:", newSentence);
let modifiedSentence = "Hey " + sentence + " Have a nice day!";
console.log("String after insertion:", modifiedSentence);
let removedText = sentence.replace(", world", "");
console.log("String after deletion:", removedText);

/* -- extra challenge */
const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contacts = [];
const isNumeric = (str) => {
  return /^\d+$/.test(str);
};

const addContact = (name, phoneNumber) => {
  contacts.push({ name, phoneNumber });
  console.log(`Contact ${name} added successfully.`);
};

const searchContact = (name) => {
  let foundContacts = contacts.filter((contact) => contact.name.toLowerCase() === name.toLowerCase());
  if (foundContacts.length > 0) {
    console.log(`Found ${foundContacts.length} contacts:`);
    foundContacts.forEach((contact) => console.log(`Name: ${contact.name}, Phone Number: ${contact.phoneNumber}`));
  } else console.log(`No contacts found with name '${name}'.`);
};

const updateContact = (name, newPhoneNumber) => {
  let foundContact = contacts.find((contact) => contact.name.toLowerCase() === name.toLowerCase());
  if (foundContact) {
    foundContact.phoneNumber = newPhoneNumber;
    console.log(`Phone number updated for contact '${name}'.`);
  } else console.log(`Contact '${name}' not found.`);
};

const deleteContact = (name) => {
  let initialLength = contacts.length;
  contacts = contacts.filter((contact) => contact.name.toLowerCase() !== name.toLowerCase());
  if (contacts.length < initialLength) console.log(`Contact '${name}' deleted successfully.`);
  else console.log(`Contact '${name}' not found.`);
};

const handleUserInput = () => {
  rl.question(`\nChoose an operation:\n1. Add contact\n2. Search contact\n3. Update contact\n4. Delete contact\n5. Exit\n`, function (option) {
    switch (option.trim()) {
      case "1":
        rl.question(`Enter name: `, function (name) {
          rl.question(`Enter phone number: `, function (phoneNumber) {
            if (isNumeric(phoneNumber) && phoneNumber.length <= 11) addContact(name, phoneNumber);
            else console.log(`Invalid phone number format.`);

            handleUserInput();
          });
        });
        break;
      case "2":
        rl.question(`Enter name to search: `, function (name) {
          searchContact(name);
          handleUserInput();
        });
        break;
      case "3":
        rl.question(`Enter name to update: `, function (name) {
          rl.question(`Enter new phone number: `, function (phoneNumber) {
            if (isNumeric(phoneNumber) && phoneNumber.length <= 11) updateContact(name, phoneNumber);
            else console.log(`Invalid phone number format.`);

            handleUserInput();
          });
        });
        break;
      case "4":
        rl.question(`Enter name to delete: `, function (name) {
          deleteContact(name);
          handleUserInput();
        });
        break;
      case "5":
        rl.close();
        break;
      default:
        console.log(`Invalid option. Please choose a valid operation.`);
        handleUserInput();
    }
  });
};

console.log("Welcome to the Contact Agenda!");

handleUserInput();

rl.on("close", () => {
  console.log("Exiting the Contact Agenda. Goodbye!");
  process.exit(0);
});
