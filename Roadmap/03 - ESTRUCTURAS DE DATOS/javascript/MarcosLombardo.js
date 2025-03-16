/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

// Estructuras soportadas

// Array: Colección de datos que pueden ser números, strings, objetos, otros arrays, entre otros.
console.log("Array:");

// Creación de Array
let myArray = [3, 6, 5, 1, 4, 2]; // [3, 6, 5, 1, 4, 2]

// Métodos
myArray.push(0); // [3, 6, 5, 1, 4, 2, 0] => Agrega uno o más elementos al final del array
myArray.unshift(7); // [7, 3, 6, 5, 1, 4, 2, 0] => Agrega uno o más elementos al principio del array
myArray.pop(); // [7, 3, 6, 5, 1, 4, 2] => Elimina el último elemento del array
myArray.shift(); // [3, 6, 5, 1, 4, 2] => Elimina el primer elemento del array
myArray.splice(4, 0, 0); // [3, 6, 5, 1, 8, 4, 2] => Cambia uno o más elementos según la especificación
myArray[4] = 8; // [3, 6, 5, 1, 0, 4, 2] => Cambia el elemento del índice indicado por el nuevo asignado
myArray.sort(); // [0, 1, 2, 3, 4, 5, 6] => Ordena el Array de menor a mayor

console.log(myArray);

// Object: Colección de variables y funciones agrupadas de manera estructural. Las variables definidas dentro de un objeto se las denomina propiedades y las funciones métodos. Las propiedades son pares clave-valor.
console.log("Object:");

// Creación de Objeto
let myObject = { name: "Marcos", age: 32, country: "Argentina" };

// Métodos
myObject.mail = "marcos@mail.com"; // { name: "Marcos", age: 32, country: "Argentina", mail: "marcos@mail.com" } => Agrega una nueva colección clave valor
myObject.age = 33; // { name: "Marcos", age: 33, country: "Argentina", mail: "marcos@mail.com" } => Modifica un valor de una clave existente
delete myObject.country; // { name: "Marcos", age: 33, mail: "marcos@mail.com" } => Elimina una colección específica

console.log(myObject);

// Map: Colección de pares clave-valor donde tanto las claves como los valores, pueden ser de cualquier tipo.
console.log("Map:");

// Creación de Map
let myMap = new Map([
  ["name", "Marcos"],
  ["age", 32],
  ["country", "Argentina"],
]);

// Métodos
myMap.set("mail", "marcos@mail.com"); // { "name" => "Marcos", "age" => 32, "country" => "Argentina", "mail" => "marcos@mail.com" } => Agrega una nueva colección al map
myMap.set("age", 33); // { "name" => "Marcos", "age" => 33, "country" => "Argentina", "mail" => "marcos@mail.com" } => Actualiza el valor cuya clave se especifica
myMap.get("name"); // Marcos => Accede al valor cuya clave se especifique
myMap.delete("country"); // { "name" => "Marcos", "age" => 33, "mail" => "marcos@mail.com" } => Elimina la colección con la clave especificada

console.log(myMap);

// Set: Colección de valores únicos.
console.log("Set:");

// Creación de Set
let mySet = new Set(["Marcos", "Lombardo", 33, true]);

// Métodos
mySet.add("Hola"); // { "Marcos", "Lombardo", 33, true, "Hola" } => Agrega uno o más elementos al final del set
mySet.delete(true); // { "Marcos", "Lombardo", 33, "Hola" } => Elimina el elemento asignado
mySet.has("Lombardo"); // true => Corrobora si un elemento puntual se encuentra dentro del set y devuelve un booleano
mySet.has(true); // false => Corrobora si un elemento puntual se encuentra dentro del set y devuelve un booleano
mySet.size; // 4 => Devuelve la longitud del set

console.log(mySet);

const { constants } = require("buffer");

// Dificultad extra

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contacts = [];

const mainMenu = () => {
  rl.question(
    "Choose an option: (s)Search, (i)Insert, (u)Update, (d)Delete, (l)List, (e)Exit",
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
          console.log("Invalid option.");
          mainMenu();
      }
    }
  );
};

const findContactIndex = (name) =>
  contacts.findIndex((c) => c.name.toLowerCase() === name.toLowerCase());

const searchContact = () => {
  rl.question("Enter the name of the contact to search: ", (name) => {
    const index = findContactIndex(name);
    if (index !== -1) {
      console.log(
        `Name: ${contacts[index].name} - Phone: ${contacts[index].phone}`
      );
    } else {
      console.log("Contact not found");
    }
    mainMenu();
  });
};

const insertContact = () => {
  rl.question("Enter the name of the new contact: ", (name) => {
    rl.question("Enter the phone number of the new contact: ", (phone) => {
      if (!/^\d{8,11}$/.test(phone)) {
        console.log("The phone number is not valid");
        insertContact();
      } else {
        contacts.push({ name, phone });
        console.log("Contact inserted");
        mainMenu();
      }
    });
  });
};

const updateContact = () => {
  rl.question("Enter the name of the contact to update: ", (name) => {
    const index = findContactIndex(name);
    if (index !== -1) {
      rl.question("Enter the phone number to update: ", (phone) => {
        if (!/^\d{8,11}$/.test(phone)) {
          console.log("The phone number is not valid");
          mainMenu();
        } else {
          contacts[index].phone = phone;
          console.log("Contact updated");
          mainMenu();
        }
      });
    } else {
      console.log("Contact not found");
      mainMenu();
    }
  });
};

const deleteContact = () => {
  rl.question("Enter the name of the contact to delete: ", (name) => {
    const index = findContactIndex(name);
    if (index !== -1) {
      contacts.splice(index, 1);
      console.log("Contact deleted");
    } else {
      console.log("Contact not found");
    }
    mainMenu();
  });
};

const listContacts = () => {
  if (contacts.length === 0) {
    console.log("No contacts yet");
  } else {
    console.log("Contacts: ");
    contacts.forEach((contact, index) => {
      console.log(
        `${index + 1}. Name: ${contact.name} - Phone: ${contact.phone}`
      );
    });
  }
  mainMenu();
};

mainMenu();

rl.on("close", () => {
  process.exit(0);
});
