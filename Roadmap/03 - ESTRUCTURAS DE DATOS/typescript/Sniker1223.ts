/**


//Array
let numbers: number[] = [5, 3, 9, 1];
console.log(numbers);
numbers.push(7); // Insert
console.log(numbers);
numbers.splice(1, 1);//Delete
console.log(numbers);
numbers[2] = 10;//update
console.log(numbers);
numbers.sort((a, b) => a - b);//sort
console.log(numbers);

//Tuples
let person: [String, number] = ['Alice', 25];
console.log(person);
person = ['Bob', 30]; //Not possible, only assign
console.log(person);
person[1] = 35; //Update
console.log(person);
// Detele is not permitted and sort is not common

//Sets
let uniqueNumbers: Set<number> = new Set([3, 1, 4]);
console.log(uniqueNumbers);
uniqueNumbers.add(2); //Insert
console.log(uniqueNumbers);
uniqueNumbers.delete(3); //Delete
console.log(uniqueNumbers);
uniqueNumbers.delete(4);// There's not update directly, first delete and then add.
uniqueNumbers.add(5);
console.log(uniqueNumbers);

//Maps
let userAge: Map<String, number> = new Map([
  ['Richard', 50],
  ['Alice', 25],
  ['Bob', 25]
]);
console.log(userAge);
userAge.set('Charlie', 35); //Insert
console.log(userAge);
userAge.delete('Bob'); //Delete
console.log(userAge);
userAge.set('Alice', 26); //Update
console.log(userAge);
let sortedUsers = Array.from(userAge.entries()).sort((a, b) => a[1] - b[1]);// Convert to Array then sort by age
console.log(sortedUsers);

//Objects
let personInfo: { [key: string]: any } = {
  name: 'Alice',
  age: 25
};
console.log(personInfo);
personInfo.city = 'New York'; //Insert
console.log(personInfo);
delete personInfo.age; //Delete
console.log(personInfo);
personInfo.name = 'Bob'; //Update
console.log(personInfo);
let sortedKeys = Object.keys(personInfo).sort(); //Convert to Array then sort 
console.log(sortedKeys);

//Readonly Arrays
let readonlyNumbers: readonly number[] = [1, 2, 3];
console.log(readonlyNumbers);
//Try to update, insert, delete can generate an error

//Readonly Tuples
let readonlyPerson: readonly [String, number] = ['Alice', 25];
console.log(readonlyPerson);
//Try to update, insert, delete can generate an error

//Enums
enum Color {
  Red = 1,
  Green,
  Blue
}
console.log(Color);
let c: Color = Color.Green; //Access
console.log(c);
//Try to update, insert, delete, sort can generate an error
 

*/

// Extra
import * as readline from 'readline';

type Contact = {
  name: string,
  phone: string
};

class ContactAgenda {
  private contacts: Contact[] = [];

  validatePhone(phone: string): boolean {
    const phoneRegex = /^\d{1,11}$/;
    return phoneRegex.test(phone);
  }

  addContact(name: string, phone: string): void {
    if (this.validatePhone(phone)) {
      this.contacts.push({ name, phone });
      console.log("Added successfully.");
    } else {
      console.log("Phone is not valid. Phone must contain only numbers and have 11 digits.");
    }
  }

  searchContact(name: string): void {
    const result = this.contacts.filter(contact => contact.name.toLowerCase() === name.toLowerCase());
    if (result.length > 0) {
      console.log("Contacts found.");
      result.forEach(contact => console.log(`Name: ${contact.name}, Phone: ${contact.phone}`));
    } else {
      console.log("Contacts not found.")
    }
  }

  updateContact(name: string, newPhone: string): void {
    const contact = this.contacts.find(contact => contact.name.toLowerCase() === name.toLowerCase());
    if (contact) {
      if (this.validatePhone(newPhone)) {
        contact.phone = newPhone;
        console.log("Phone updated successfully.");
      } else {
        console.log("Phone is not valid.");
      }
    } else {
      console.log("Contact not found.")
    }
  }

  deleteContact(name: string): void {
    const initialLeng = this.contacts.length;
    this.contacts = this.contacts.filter(contact => contact.name.toLowerCase() !== name.toLowerCase());
    if (this.contacts.length < initialLeng) {
      console.log("Contact delete successfully.");
    } else {
      console.log("Contact not found.");
    }
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const agenda = new ContactAgenda();

function showMenu() {
  console.log("\nOptions:");
  console.log("1. Add contact");
  console.log("2. Search contact");
  console.log("3. Update contact");
  console.log("4. Delete contact");
  console.log("5. Exit");

  rl.question("Select an option: ", (option) => {
    switch (option) {
      case '1':
        rl.question("Type the name: ", (nameToAdd) => {
          rl.question("Type the phone: ", (phoneToAdd) => {
            agenda.addContact(nameToAdd, phoneToAdd);
            showMenu();
          });
        });
        break;
      case '2':
        rl.question("Type the name to search: ", (nameToSearch) => {
          agenda.searchContact(nameToSearch);
          showMenu();
        });
        break;
      case '3':
        rl.question("Type the contact to update: ", (nameToUpdate) => {
          rl.question("Type the new phone", (newPhone) => {
            agenda.updateContact(nameToUpdate, newPhone);
            showMenu();
          });
        });
        break;
      case '4':
        rl.question("Type the contact to delete: ", (nameToDelete) => {
          agenda.deleteContact(nameToDelete);
          showMenu();
        });
        break;
      case '5':
        console.log("Quit... ");
        rl.close();
        break;
      default:
        console.log("Invalid choice. Try again. ");
        showMenu();
    }
  });
}
showMenu();