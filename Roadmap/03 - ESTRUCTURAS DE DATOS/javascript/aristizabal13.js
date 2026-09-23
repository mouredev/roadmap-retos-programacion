

/*
**Listas
*/

//Array

let myList = ["Emanuel","Aristizabal",18,16,2008]
console.log(myList)

myList.push("David") //Añade "David" al final
console.log(myList) 

myList.pop() // Elimina el ultimo indice
console.log(myList)

console.log(myList.shift()) // Elimina el primer indice
console.log(myList)

myList.unshift("Emanuel", "David") // Añade "Emanuel" & "David" al inicio
console.log(myList)


myList.splice(3, 3) // Se le indica una porcion(posicion) de la lista a eliminar
console.log(myList)

myList.splice(1, 1, 18) // Se le indica una porcion(posicion) de la lista a agregar 

let myNewList = myList.slice(0, 4) // Eliminar uno o mas elementos indicando su posicion
console.log(myNewList)

let listNumbers = [10, 5, 1, 0]
console.log(listNumbers.sort((a, b) => a - b )) // Ordena de manera ascendente


let listString = ["Emanuel","david", "aristizabal", "Gongora"]
console.log(listString.sort()) // Por defecto ordena de todas las mayusculas van antes de las minusculas 


//Sets

let mySet = new Set(["Ema", 18, "emanuelaristizabal7@gmail.com"])
console.log(mySet)

mySet.add("aristizabal13") // Insersion 
console.log(mySet)

mySet.delete(18) // Borrado
console.log(mySet)

// Ordenacion convirtiendo el set a un array y luego ordenando el array
let myNewSet = new Set([10, 5, 1, 0, 8]);
let myArray = Array.from(myNewSet).sort((a, b) => a - b); 
console.log(myArray)

// Convertimos el array ordenado a un set
mySecondSet = new Set(myArray)
console.log(mySecondSet)

//Maps

let myMap = new Map([
    ["name", "Emanuel"],
    ["age", 18],
    ["email", "emanuelaristizabal7@gmail.com"]
])

console.log(myMap)

myMap.set("name", "Emanuel David") // Insercion
console.log(myMap)

console.log(myMap.get("name")) // Acceso a un valor 

console.log(myMap.keys()) // Acceso a las llaves
console.log(myMap.values()) // Acceso a los valores
console.log(myMap.entries()) // Acceso a todo

console.log(myMap.delete("age")) // Borrado



//Objects

let person = {
    name : "Emanuel",
    age : 18,
    adress : "secundaria.cuenta.emanuel@gmail.com"
}

console.log(person.adress) // Acceso a un valor

person.age = "18" // Actualizacion
console.log(person.age)

delete person.age // Borrado
console.log(person)

/*
**Extra
*/

const readline = require('readline') 

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let contacts = []

const menu = () => {
    console.log(`
        1. Buscar contacto
        2. Agregar contacto
        3. Actualizar contacto
        4. Eliminar contacto
        5. Salir
    `);
    rl.question("Seleccion una opciion: ", chosenOption);
};

const chosenOption = (option) => {
    switch (option) {
        case "1":
            findContact();
            break;
        case "2":
            addContact();
            break;
        case "3":
            updateContact();
            break;
        case "4":
            deleteContact();
            break;
        case "5":
            console.log("Saliendo de la agenda...");
            break;
        default:
            console.log("Opcion invalida. Elige una opcion del 1 al 5.");
    };
};

const addContact = () => { 
    rl.question("Introduce el nombre del contacto: ", (name) => addContactTelephone(name));
};

const addContactTelephone = (name) => {
    rl.question("Introduce el telefono del contacto: ", (tlf) => {
        if (tlf.length > 11) {
            console.log("El telefono no puede ser mayor a 11 digitos");
            addContactTelephone();
        } else if (!/^\d{1,11}$/.test(tlf)) {
            console.log("El telefono solo puede incluir digitos numericos");
            addContactTelephone();
        } else {
            contacts.push({ nombre: name, telefono: tlf });
            console.log("Contacto agregado exitosamente");
            listContacts();
        }
    });
}; 

const listContacts = () => {
    contacts.map((contact) =>
        console.log(`
            Nombre: ${contact.nombre}
            Teléfono: ${contact.telefono}`)
        );
        menu();
};

const findContact = () => {
    rl.question("Introduce el nombre del contacto a buscar: ", (name) => {
        const contact = contacts.find((contact) => contact.nombre === name);
        if (contact) {
            console.log(`El numero de telefono de ${contact.nombre} es: ${contact.telefono}`);
        } else {
            console.log("Contacto no encontrado");
        }
        menu();
    });
};
const updateContact = () => {
    rl.question("Introduce el nombre del contacto a actualizar: ", (name) => { 
        const contact = contacts.find((contact) => contact.nombre === name);
        if (contact) {
            rl.question("Introduce el nuevo numero de telefono: ", (tlf) => {
                if (!/^\d{1,11}$/.test(tlf)) {
                    console.log("El telefono solo puede incluir digitos numericos");
                    updateContact();
                } else {
                    contact.telefono = tlf;
                    console.log("Contacto actualizado exitosamente");
                    listContacts();
                }
            });
        } else {
            console.log("Contacto no encontrado");
            menu();
        }
    });
};

const deleteContact = () => {
rl.question("Introduce el nombre del contacto a eliminar: ", (name) => {
    const contactIndex = contacts.findIndex((contact) => contact.nombre === name);
    if (contactIndex !== -1) {
            contacts.splice(contactIndex, 1);
            console.log("Contacto eliminado exitosamente");
    } else {
            console.log("El contacto no existe");
    }
    menu();
    });
};

menu();