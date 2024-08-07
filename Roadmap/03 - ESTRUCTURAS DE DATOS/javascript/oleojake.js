/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */

// 1.- ARRAY
let frutas = ["manzana", "pera", "plátano", "fresa"];

// 1.1 INSERCIÓN EN ARRAY
frutas.push("melocotón"); // Inserción al final
frutas.unshift("albaricoque"); // Inserción al principio
frutas.splice(0,0,"palta"); // Añadiendo con splice en la posición 0

// 1.2 BORRADO EN ARRAY
frutas.pop(); // Borrado al final
frutas.shift(); // Borrado al principio
frutas.splice(0,1); // Eliminando con splice en la posición 0

// 1.3 ACTUALIZACIÓN EN ARRAY
frutas[0] = 'mango'; // Actualización
frutas.splice(2,1, "uva"); // Actualizando con splice

// Actualizando con MAP
// El método map crea un nuevo array de la misma longitud que el original, pero con los elementos transformados
let numbers = [1, 2, 3]
let doubleNumbers = numbers.map((number) => {
  return number * 2
})
console.log(doubleNumbers)

// Filtrado
numbers = [1, 2, 3, 4, 5, 6, 7]
let evenNumbers = numbers.filter(function (number) {
    return number % 2 === 0
})
console.log(evenNumbers)

// 1.4 ORDENACIÓN EN ARRAY
numbers = [3, 5, 22, 7, 2];
console.log(numbers.sort()); // Ordena los strings, no sirve para números

let numerosOrdenados = numbers.toSorted(function(a, b) { // Usamos toSorted y un nuevo array para no modificar el array original
    return a - b
    // Si quisieramos descendente return b - a
})
console.log(numerosOrdenados);

// Maatriz o array de arrays.
let matriz = [
    [1, 2, 3],
    [4, 5, 6,]
]

// 2. SET
// No acepta duplicados
let mySet = new Set(["Oleojake", 30]); 

// 2.1 INSERCCIÓN EN SET
mySet.add("Jijona");

// 2.2 BORRADO EN SET
mySet.delete("Oleojake");
mySet.clear(); // Borra todo el SET


// 3. MAPA
// No permite repetir claves
let myMap = new Map ([["Pablo", 30], ["Doly", 25]]);

// 3.1 INSERCCIÓN EN MAPA
myMap.set("Bonsito", 16);

// 3.2 BORRADO EN MAPA
myMap.delete("Bonsito");
myMap.clear(); // Borra todo el Mapa


// 4. OBJETOS
// Creación
let myObject = { nombre: 'Pabo', edad: 30, ciudad: 'Alicante' };
console.log(myObject);
// Inserción
myObject.trabajo = 'Dev';

// Actualización
myObject.edad = 26;

// Borrado
delete myObject.ciudad;
console.log(myObject.edad)


/* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */


// EJERCICIO HECHO CON ARRAYS DE OBJETOS

let contacts = [];
contacts.push({name:"Pablo", phone:"6000774503"});
contacts.push({name:"Doly", phone:"6521412514"});


// SEARCH CONTACT
function searchContact(name){
    let contacto = contacts.find(contacto => contacto.name.toLowerCase() === name.toLowerCase());
    if(contacto == undefined){
        return "Contacto no encontrado"
    }
    return contacto.phone;
    
}

// ADD CONTACT
function addContact(name, phone){
    if (phone.length > 11){
        console.log("\n --> El número es demasiado largo, debe tener 11 dígitos como máximo\n");
    } else {
        let contacto = contacts.find(contacto => contacto.name.toLowerCase() === name.toLowerCase());
        if(contacto == undefined){
            console.log("\n --> Inserción realizada con éxito\n");
            contacts.push({name,phone});
        } else {
            console.log("\n --> Ese contacto ya existe, guárdalo con un nombre diferente\n");
        }
    }
}

// DELETE CONTACT
function deleteContact(name){
    let contacto = contacts.find(contacto => contacto.name.toLowerCase() === name.toLowerCase());
    if (contacto == undefined){
        console.log("\n --> El nombre que has introducido no se encuentra en la agenda \n");
    } else {
        contacts = contacts.filter(contacto => contacto.name.toLowerCase() !== name.toLowerCase());
        console.log("\n Has eliminado el contacto: " + name + "\n");
    }
}

// UPDATE CONTACT
function updateContact(name, phone){
    let contactIndex = contacts.findIndex(contacto => contacto.name.toLowerCase() === name.toLowerCase());
    if (phone.length > 11){
        console.log("\n -->El número es demasiado largo, debe tener 11 dígitos como máximo \n");
    } else {
        if (contactIndex == -1){
            console.log("\n -->El nombre que has introducido no se encuentra en la agenda \n");
        } else {
            contacts[contactIndex].phone = phone;
            console.log("\n -->Has actualizado el número de teléfono de : " + name +" ("+phone+")");
        }
    }
}

// VER AGENDA
function verAgenda(){
    if(contacts.length > 0){
        console.log("TU AGENDA");
        console.log("------------------------------------");
        for(let i = 0; i< contacts.length; i++){
            console.log("* Nombre: " + contacts[i].name + " | Teléfono: " + contacts[i].phone);
        }
        console.log("------------------------------------");
        console.log("\n");
    } else {
        console.log("\n--> Tu agenda de contactos está vacía prueba a añadir algún contacto primero");
    }
}


const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function showMenu() {
console.log("¿Qué deseas hacer?");
console.log("1. Añadir Contacto");
console.log("2. Buscar Contacto");
console.log("3. Actualizar Contacto");
console.log("4. Eliminar Contacto");
console.log("5. Ver Agenda");
console.log("6. Salir\n");
}

function runAction(opcion) {

    switch (opcion){
        case "1":
            rl.question("\n --> Introduzca el nombre de contacto que quieres añadir \n", (newName) => {
                rl.question("\n --> y ahora su número de teléfono \n", (newPhone) => {
                    addContact(newName, newPhone);
                    run();
                });
            });  
            break;
        case "2":
            rl.question("\n --> Introduzca el nombre de contacto que quiere buscar \n", (opcion) => {
                console.log("\n --> El número de " + opcion + " es: " +searchContact(opcion) +"\n");
                run();
            });            
            break;
        case "3":
            rl.question("\n --> Introduzca el nombre de contacto que quieres actualizar \n", (newName) => {
                rl.question("\n --> y ahora su nuevo número de teléfono \n", (newPhone) => {
                    updateContact(newName, newPhone);
                    run();
                });
            });
            break;
        case "4":
            rl.question("\n --> Introduzca el nombre de contacto que deseas eliminar \n", (opcion) => {
                deleteContact(opcion);
                run();
            });
            break;
        case "5":
            verAgenda();
            run();
            break;
        case "6":
            console.log("\n --> Cerrando agenda \n");
            rl.close();
            break;
        default: 
            console.log("\n --> No le entiendo \n");
            run();
    }
}

function run() {
    showMenu();
    rl.question("Seleccione una opción (1-6): ", (opcion) => {
        runAction(opcion);
    });
}

run();