//  Data Structure
//  Array
let arrayOfNumbers = [0, 1, 2, 3, 4];

arrayOfNumbers.push(5); //  Add an element to the end of the array
arrayOfNumbers.unshift(-1); // Add an element to the beginning of the array

arrayOfNumbers.pop(); // Removes the last element of the array
arrayOfNumbers.shift(); //  Removes the first element of the array

arrayOfNumbers[0] = -1; //  Updates an element of the array

arrayOfNumbers.sort((a, b) => a - b); //  Sort the elementos of the array

//  Object
let me = {
  name: "Isaac",
  age: 20,
};

me.language = "Spanish"; //  Add a key to the object

delete me.language; //  Removes a key of the object

me.age = 25; //  Update a key of the object

let sortedKeys = Object.keys(me).sort(); //  Sort the keys of the object

//  Set
let set = new Set([6, 7, 8, 9, 1]);

set.add(1); //  Add an element to the set

set.delete(9); //   Delete an element of the set

let sortedArray = Array.from(set).sort((a, b) => a - b); //  Sort the elements of the set in an array

//  Map
let map = new Map();
map.set("name", "Isaac");
map.set("age", 25);

map.set("language", "Spanish"); //  Add an element to the map

map.set("age", 30); //  Update the value of 'age'

map.delete("language"); //Delete the key 'language'

let sortedMap = new Map([...map.entries()].sort()); //  Sort the map by keys

//  Extra difficulty
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contactList = [];

const searchContact = (name) => {
  const contact = contactList.find(
    (c) => c.name.toLowerCase() === name.toLowerCase()
  );
  if (contact) {
    console.log(`Contact found: ${contact.name} - ${contact.phone}`);
  } else {
    console.log(`No contact found with the name ${name}.`);
  }
};

const insertContact = (name, phone) => {
  contactList.push({ name, phone });
  console.log(`Contact ${name} added successfully.`);
};

const updateContact = (name, newPhone) => {
  const index = contactList.findIndex(
    (c) => c.name.toLowerCase() === name.toLowerCase()
  );
  if (index !== -1) {
    contactList[index].phone = newPhone;
    console.log(`Contact ${name} updated successfully.`);
  } else {
    console.log(`No contact found with the name ${name}.`);
  }
};

const deleteContact = (name) => {
  const initialLength = contactList.length;
  contactList = contactList.filter(
    (c) => c.name.toLowerCase() !== name.toLowerCase()
  );
  if (contactList.length < initialLength) {
    console.log(`Contact ${name} deleted successfully.`);
  } else {
    console.log(`No contact found with the name ${name}.`);
  }
};

const validatePhone = (phone) => {
  const phoneRegex = /^[0-9]{1,11}$/;
  return phoneRegex.test(phone);
};

const showMenu = () => {
  rl.question(
    "Select the option to do in the contact list: search / add / update / delete / exit\n",
    (option) => handleOption(option)
  );
};

const handleOption = (option) => {
  switch (option) {
    case "search":
      rl.question("Write the name of the contact to find: ", (name) => {
        searchContact(name);
        showMenu();
      });
      break;

    case "add":
      rl.question("Write the name of the contact to add: ", (name) => {
        rl.question("Write the phone number of the contact: ", (phone) => {
          if (validatePhone(phone)) {
            insertContact(name, phone);
          } else {
            console.log("Invalid phone number, failed to add the contact.");
          }
          showMenu();
        });
      });
      break;

    case "update":
      rl.question("Write the name of the contact to update: ", (name) => {
        rl.question("Write the new phone number: ", (newPhone) => {
          if (validatePhone(newPhone)) {
            updateContact(name, newPhone);
          } else {
            console.log("Invalid phone number, failed to update the contact.");
          }
          showMenu();
        });
      });
      break;

    case "delete":
      rl.question("Write the name of the contact to delete: ", (name) => {
        rl.question(
          `Are you sure to delete ${name} contact? true / false: `,
          (confirmation) => {
            if (confirmation !== "true") {
              console.log(`The contact ${name} has not been deleted.`);
            } else {
              deleteContact(name);
              console.log(`The contact ${name} has been deleted.`);
            }
            showMenu();
          }
        );
      });
      break;

    case "exit":
      console.log("Thanks for using Contact List 3000!");
      rl.close();
      break;

    default:
      console.log("Invalid option, please try again.");
      showMenu();
      break;
  }
};

showMenu();
