////////////////////////////////
// Arrays
////////////////////////////////

let macedonia = ["apple", "orange", "banana", "grapes", "lemon"]
console.log(macedonia)

// Añadir al final
macedonia.push("strawberries")
console.log(macedonia)

// Añadir al principio
macedonia.unshift("pear")
console.log(macedonia)

// Eliminar del final
macedonia.pop()
console.log(macedonia)

// Eliminar del principio
macedonia.shift()
console.log(macedonia)

// Eliminar una cantidad concreta desde un punto
macedonia.splice(3, 1)
console.log(macedonia)

// Mostrar el último elemento
console.log(macedonia[macedonia.length-1])

// Ordenar alfabéticamente
macedonia.sort()
console.log(macedonia)


////////////////////////////////
// Objects
////////////////////////////////

let user = {
  name: "d4-n1",
  age: 28,
  favouriteFood: "pizza"
}
console.log(user)

// Añadir un elemento
user.gender = "male"
console.log(user)

// Actualizar un elemento
user.favouriteFood = "pasta"
console.log(user)

// Eliminar un elemento
delete user.gender
console.log(user)

// .sort() no se puede utilizar en objetos


////////////////////////////////
// Extra
////////////////////////////////
let phoneBook = []
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

////////////////////////////////
// Functions
////////////////////////////////

// Validate phone number
const validatePhoneNumber = (number) => {
  const format = /^\d{1,11}$/;
  return format.test(number);
}

// Add a contact
const addContact = () => {
  rl.question("Enter a name ", (userInput) => {
    let userName = userInput;

    rl.question("Enter a phone number ", (userInput) => {
      let numberValidation = validatePhoneNumber(userInput)
      if (numberValidation == true) {
        let phoneNumber = userInput;
        phoneBook.push({ userName, phoneNumber });
        console.log("\n✅ Contact added")
        menu();
      } else {
        console.log("Invalid number format")
        addContact()
      }
    });
  });
};

// Display all contacts
const displayContacts = () => {
  for(i = 0; i <= phoneBook.length - 1; i++) {
    console.log(`· ${phoneBook[i].userName} - ${phoneBook[i].phoneNumber}`)
  }
  menu()
}

// Edit a contact
const editContact = () => {
  rl.question("Search a name ", (userName) => {
    index = findContact(userName)
    if (index != -1) {
      rl.question("Enter a new name ", (userName) => {
        phoneBook[index].userName = userName
    
        rl.question("Enter a new phone number ", (userNumber) => {
          phoneBook[index].phoneNumber = userNumber
          console.log("\n✅ Contact updated")
          menu()
        });
      });
    } else {
      console.log("\n😥 There are no results with that name")
    }
    menu()
  });
}

// Remove a contact
const removeContact = () => {
  rl.question("Search a name ", (userName) => {
    index = findContact(userName)
    if (index != -1) {
      phoneBook.splice([index], 1)
      console.log("\n✅ Contact removed")
    } else {
      console.log("\n😥 There are no results with that name")
    }
    menu()
  });
}

// Find matches in phoneBook
const findContact = (name) => {
  let contact = phoneBook.findIndex((contact) => contact.userName == name)
  return contact
}

// Search a contact
const searchContact = () => {
  rl.question("Search a name ", (userName) => {
    index = findContact(userName)
    if (index != -1) {
      console.log(
`
Name: ${phoneBook[index].userName}
Phone number: ${phoneBook[index].phoneNumber}
`)
    } else {
      console.log("\n😥 There are no results with that name")
    }
    menu()
  });
};

// Run Phone book
const menu = () => {
  rl.question(
`a   Add a new contact
c   Close the phone book
d   Display all the contacts
e   Edit an existing contact
r   Remove a contact
s   Search for a contact
What do you want to do?
`,
  (userInput) => {
    userInput = userInput.toLowerCase()

    switch(userInput) {
      // Add
      case "a":
        addContact()
        break;

      // Close  
      case "c":
        rl.close();
        break;

       // Display
      case "d":
        displayContacts()
        break;
        
      // Edit  
      case "e":
        editContact()
        break;

      // Remove
      case "r":
        removeContact()
        break;

      // Search  
      case "s":
        searchContact()
        break;
        
      default:
        console.log("Please, choose an valid option")
        menu()
    }
  })
}

console.log("Welcome to Console Book")
menu()