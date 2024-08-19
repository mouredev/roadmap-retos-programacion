/** #03 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Dentro de los ejemplos de estructura de soporte tenemos:
 * Arrays
 * Objetos
 * Maps
 * Sets
 */



//-----ARRAYS-----
//  Esto es ejemplo de un Array
var frutas = ["Manzana", "Pera", "Plátano", "Durazno", "Kiwi", "Fresa"];

//  INSERCIÓN
frutas.push("Uva"); // Agrega al final
console.log(frutas); //[ 'Manzana', 'Pera', 'Plátano', 'Durazno', 'Kiwi', 'Fresa', 'Uva' ]

frutas.unshift("Pasas"); // Agrega al principio
console.log(frutas); //[ 'Pasas', 'Manzana', 'Pera', 'Plátano', 'Durazno', 'Kiwi', 'Fresa', 'Uva' ]

frutas.splice(3, 0, "Naranja"); // Agrega en alguna parte del array, siempre y cuando se explique que se va agregar
console.log(frutas); //[ 'Pasas', 'Manzana', 'Pera', 'Naranja', 'Plátano', 'Durazno', 'Kiwi', 'Fresa', 'Uva' ]


//  BORRADO
frutas.pop(); // Elimina al final
console.log(frutas); //[ 'Manzana', 'Pera', 'Naranja', 'Plátano', 'Durazno', 'Kiwi', 'Fresa' ]

frutas.shift(); // Elimina al principio
console.log(frutas);

frutas.splice(2, 1); // Elimina una parte especifica en la cual le demos los parámetros
console.log(frutas);


//  ACTUALIZACIÓN
frutas[3] = "Cereza"; // Se actualiza el elemento en una posición especifica
console.log(frutas);


//  ORDENAMIENTO
frutas.sort(); // Esta es la forma simple de ordenamiento en menor a mayor ó bien de a - z
console.log(frutas);



//-----OBJETO-----
var persona = {
    nombre: "Jesus Antonio",
    edad: 23,
    país: "Mexico",
};

//  INSERCIÓN
persona.altura = 1.70; // Agrega una nueva propiedad
console.log(persona);


//  BORRADO
delete persona.altura; // Elimina una propiedad especifica
console.log(persona);


//  ACTUALIZACIÓN
persona.edad = 24; // Se actualiza el valor de la piedad
console.log(persona);


//  ORDENAMIENTO
// No existe una forma de ordenamiento para las propiedades
// sin embargo se puede utilizar los valores de las propiedades
// para hacer el ordenamiento



//-----MAPS-----
var agendaTelefonica = new Map([
    ["Fatima", { teléfono: "953-123-4567", email:"fatima@example.com"}],
    ["Rosa", { teléfono: "953-123-4567", email:"rosa@example.com"}],
]);

//  INSERCIÓN
agendaTelefonica.set("JesusAntonio", { teléfono: "953-000-0000", email:"jesus@example.com"}); // Agrega un nuevo valor al map
console.log(agendaTelefonica);


//  BORRADO
agendaTelefonica.delete("Rosa"); // Elimina un valor especifico del map
console.log(agendaTelefonica);


//  ACTUALIZACIÓN
agendaTelefonica.set("JesusAntonio",  { teléfono: "953-123-4567", email:"jesusantonio@example.com"}); // Se actualiza el valor especifica del map
console.log(agendaTelefonica);


//  ORDENAMIENTO
// No existe una forma de ordenamiento para los maps



//-----SETS-----
var etiquetaArticulo = new Set([
    "Hogar",
    "Ropa",
    "Electrodomésticos"
]);

//  INSERCIÓN
etiquetaArticulo.add("Juguetes"); // Agrega un nuevo valor al set
console.log(etiquetaArticulo);


//  BORRADO
etiquetaArticulo.delete("Ropa"); // Elimina un valor especifico del set
console.log(etiquetaArticulo);


//  ACTUALIZACIÓN
etiquetaArticulo.delete("Juguetes"); // Se elimina el ultimo valor del set
etiquetaArticulo.add("Jardín"); // Se agrega el nuevo valor al final del set
console.log(etiquetaArticulo);


//  ORDENAMIENTO
var sortArray = [...etiquetaArticulo].sort(); // Se hace el ordenamiento manera alfabética
console.log(sortArray);



/**-----DIFICULTAD EXTRA-----*/

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let contacts = [];

const mainMenu = () => {
rl.question("Choose an operation: search (s), insert (i), update (u), delete (d), list (l), exit (e): ",
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

/**-----DIFICULTAD EXTRA-----*/
