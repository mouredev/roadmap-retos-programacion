// array
// Creation
let array = [1, 2, 3, 4];

// Insertion
array.push(5); // Appends to the end

// Deletion
array.splice(2, 1); // Removes the item at index 2

// Update
array[2] = 10; // Updates the item at index 2

// Sorting
array.sort((a, b) => a - b); // Sorts the array in ascending order

// object
// Creation
let object = { name: "Alice", age: 25 };

// Insertion
object.email = "alice@example.com"; // Adds a new property

// Deletion
delete object.age; // Deletes the age property

// Update
object.name = "Bob"; // Updates the name property

// set
// Creation
let set = new Set([1, 2, 3, 4]);

// Insertion
set.add(5); // Adds a new element

// Deletion
set.delete(2); // Removes the element 2

// map
// Creation
let map = new Map([
  ["a", 1],
  ["b", 2],
]);

// Insertion
map.set("c", 3); // Adds a new key-value pair

// Deletion
map.delete("b"); // Deletes the key-value pair with key 'b'

// Update
map.set("a", 100); // Updates the value for key 'a'

// Sorting - Maps are not directly sortable, but you can sort the entries
let mapSorted = new Map([...map.entries()].sort());

//EJERCICIO
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contacts = [];

const mainMenu = () => {
  rl.question(
    "Choose an operation: search (s), insert (i), update (u), delete (d), list (l), exit (e): ",
    (choice) => {
      switch (choice) {
        case "s":
          searchContact();
          break;
        case "i":
          insertContact();
          break;
        case "u":
          updateContact();
          break;
        case "d":
          deleteContact();
          break;
        case "l":
          listContacts();
          break;
        case "e":
          rl.close();
          break;
        default:
          console.log("Invalid choice.");
          mainMenu();
      }
    }
  );
};

const validatePhoneNumber = (number) => {
  const regex = /^\d{1,11}$/;
  return regex.test(number);
};

const findContactIndex = (name) =>
  contacts.findIndex((c) => c.name.toLowerCase() === name.toLowerCase());

const searchContact = () => {
  rl.question("Enter the name of the contact to search: ", (name) => {
    const index = findContactIndex(name);
    if (index !== -1) {
      console.log(
        `Contact found: ${contacts[index].name}, ${contacts[index].phone}`
      );
    } else {
      console.log("Contact not found.");
    }
    mainMenu();
  });
};

const insertContact = () => {
  rl.question("Enter the name of the new contact: ", (name) => {
    rl.question("Enter the phone number of the new contact: ", (phone) => {
      if (!validatePhoneNumber(phone)) {
        console.log("Invalid phone number.");
        insertContact();
      } else {
        contacts.push({ name, phone });
        console.log("Contact inserted.");
        mainMenu();
      }
    });
  });
};

const updateContact = () => {
  rl.question("Enter the name of the contact to update: ", (name) => {
    const index = findContactIndex(name);
    if (index !== -1) {
      rl.question("Enter the new phone number: ", (phone) => {
        if (!validatePhoneNumber(phone)) {
          console.log("Invalid phone number.");
          updateContact();
        } else {
          contacts[index].phone = phone;
          console.log("Contact updated.");
          mainMenu();
        }
      });
    } else {
      console.log("Contact not found.");
      mainMenu();
    }
  });
};

const deleteContact = () => {
  rl.question("Enter the name of the contact to delete: ", (name) => {
    const index = findContactIndex(name);
    if (index !== - 1) {
      contacts.splice(index, 1);
      console.log("Contact deleted.");
    } else {
      console.log("Contact not found.");
    }
    mainMenu();
  });
};

const listContacts = () => {
  if (contacts.length === 0) {
    console.log("No contacts to display.");
  } else {
    console.log("Contact List:");
    contacts.forEach((contact, index) => {
      console.log(
        `${index + 1}. Name: ${contact.name}, Phone: ${contact.phone}`
      );
    });
  }
  mainMenu();
};

mainMenu();

rl.on("close", () => {
  console.log("Exiting contact list application.");
  process.exit(0);
});
