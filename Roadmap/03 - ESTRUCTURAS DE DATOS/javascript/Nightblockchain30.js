/* 
  * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
*/

// >>> listas
let lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]; // TYPE OF "Object"
// Inserción
lista.push("ten");
// Borrado
lista.pop();
console.log(lista);
// Actualización
lista[0] = "One";
console.log(lista);
// Ordenación
lista.sort();
console.log(lista);

 
// >>> Diccionarios Objeto 

/*
IMPORTANTE 
-> las claves SIEMPRE DEBEB ser strings
-> los objetos en JS están pernsado para tener informacion estática
-> Métodos propios del tipo de structura
*/

let diccionario = { // constructor: ƒ Object()
    nombre: "Night",
    apellido: "BlockChain",
    edad: 26
};
// Inserción
diccionario["nacionalidad"]="Español";
console.log(diccionario);
// Borrado
delete diccionario["nacionalidad"];
console.log(diccionario);
// Actualización
diccionario["nombre"]="ALP";
console.log(diccionario);
// Ordenación
// > No aplica


// >>> Conjuntos
myset = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9,9,9,9]); // No permite elementos repetidos
console.log(myset);
// Inserción
myset.add(10);
console.log(myset);
// Borrado
myset.delete(9);
console.log(myset);
// Actualización && Ordenación 
// >No aplica porque no permite acceso por índice


// >>> Diccionario con Constructor MAP. 
/*
IMPORTANTE 
-> las claves PUEDEN de ser cualquier tipo
-> Permite agregar datos de forma dinámica
-> Métodos propios del tipo de dato
*/

let diccionarioMap = new Map([ // constructor: Map()
    [1, "Night"], // clave INT
    ["apellido", "Blockchain"], // clave STRING
    [true, 26], // clave BOOL
]);
// Busqueda 
diccionarioMap.get("apellido");
console.log(diccionarioMap);
//  Inserción
diccionarioMap.set("nacionalidad","español");
console.log(diccionarioMap);
// Borrado
diccionarioMap.delete(true);
console.log(diccionarioMap);
// Actualización
diccionarioMap.set(1,"Alonso");
console.log(diccionarioMap);
// Ordenación
// >No aplica porque no tiene índice


// >>> Pilas // LIFO - last In First Out
let pila = [1,2,3,4,5]
// Inserción
pila.push("6");
console.log(pila);
// Borrado
pila.pop();
console.log(pila);
// Actualización
pila[0] = "1";
console.log(pila);
// Ordenación
pila.sort();
console.log(pila);


// >>> Colas // FIFO - FIRST In FIRST Out
let cola = [1,2,3];
// Inserción
cola.push("ultimo");
console.log(cola);
// Borrado
cola.shift(); 
console.log(cola);
// Actualización
cola[0]="dos";
console.log(cola);
// Ordenación
cola.sort();
console.log(cola);

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
