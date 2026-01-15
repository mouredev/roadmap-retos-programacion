//  * EJERCICIO:
//  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
//  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

// Arrays
const estudiantes = ["ant000o", "7R0N1X", "dieswae"];
estudiantes.push("Reaien"); // Inserción
console.log(estudiantes); 
estudiantes.splice(2, 1, "C-BLSKV", "d4-n1"); // Borrado/Inserción (usando splice). En la posición 2, borra 1 item, agrega "C-BLSKV" y "d4-n1".
console.log(estudiantes);
estudiantes.pop(); // Borrado (usando pop, borra el último del array)
console.log(estudiantes);
estudiantes[2] = "TofeDev"; // Actualización
console.log(estudiantes);
estudiantes.sort(); // Ordenación
console.log(estudiantes);


console.log("---------------------------------------------------------------")


// Objects
let perro = {
    raza: "Shiba Inu", 
    edad: "2 años", 
    nombre: "Moonie"
}
perro.sexo = "Hembra"; // Inserción
perro.color = "Blanco"
console.log(perro);
delete perro.color; // Borrado
console.log(perro);
Object.defineProperty(perro, "edad", {value: "18 meses"}); // Actualización
console.log(perro);
// No se puede ordenar un Object, para ordenarlo hay que convertir valores en array. --Se omitirá por ahora--


console.log("---------------------------------------------------------------")

// Maps
let autos = new Map(); // map creado vacío
autos.set("Kia", 600); // Inserción
autos.set("Toyota", 200);
autos.set("Lamborghini", 350);
console.log(autos);
console.log("---------------------------------------------------------------")
autos.set("frutas",[   // Inserción de un Array (map acepta cualquier tipo de dato).
    ["uva", 20],
    ["piña", 15],
    ["kiwi", 10],
]);
console.log(autos.get("frutas"));
console.log("---------------------------------------------------------------")
autos.get("frutas").push(["mango", 7]);  // Inserción al Array dentro del Map
console.log(autos);
console.log("---------------------------------------------------------------")
autos.delete("frutas"); // Borrado
console.log(autos);
console.log("---------------------------------------------------------------")
autos.set("Kia", 40); // Actualizado
console.log(autos);
// Para ordenarlo hay que convertir valores en array. --Se omitirá por ahora--


console.log("---------------------------------------------------------------")


// Set
let letras = new Set(["h", "o", "l", "a"]);
letras.add("d"); // Inserción
console.log(letras);
letras.delete("d"); // Borrado
console.log(letras);
// Actualizado como tal no existe, habría que borrar uno y crear uno nuevo.
let palabra = "";   // Listar  los elementos, se puede hacer con un for...of.
for (const x of letras){
    palabra += x
}
console.log(palabra);


console.log("---------------------------------------------------------------");
console.log("---------------------------------------------------------------");
console.log("---------------------------------------------------------------");
console.log("---------------------------------------------------------------");
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let contactos = new Map();
contactos.set("Joaquin", "56923467680");
contactos.set("Alonso", "56986749614");
contactos.set("Ignacio", "56973960467");
contactos.set("Josefa", "56934684569");


function menu(){
    console.log(
            "--- MENÚ PRINCIPAL ---\n" +
            "1. Buscar contacto\n" +
            "2. Añadir nuevo contacto\n" +
            "3. Editar un contacto\n" +
            "4. Eliminar un contacto\n" +
            "0. Salir"
        );
        rl.question("\nSelecciona una opción: ", (opcion) => {
        switch(opcion){
            case "1":
                console.log("\nBuscar contacto");
                buscarContact();
            break;
            case "2": 
                console.log("\nAñadir contacto")
                addContact();
            break;
            case "3":
                console.log("\nEditar contacto")
                editContact();
            break;
            case "4":
                console.log("\nEliminar contacto")
                deleteContact();
            break;
            case "0":
                rl.close();
            break;
            default:
                console.log("Error");
                menu();
        }
        });
}
menu();

function buscarContact(){
    rl.question("\nNombre del contacto: ", (nombre) => {
        if (contactos.has(nombre)){
            const value = contactos.get(nombre);
            console.log(`${nombre} - ${value}`);
        }else{
            console.log("Contacto no existente")
            buscarContact();
        }
        rl.question('\n1. Buscar otro contacto\n0. Volver al menú\n', (opcion) => {
            if (opcion === "1"){
                buscarContact();
            }else{
                menu();
            }
        });
    });
}


function addContact(){
    rl.question("\nNúmero: ", (numero) => {
        if (numero.length <= 11 && !isNaN(numero)){
            rl.question('\nNombre: ', (nombre) => {
                contactos.set(nombre, numero);
                console.log(`Se agregó a ${nombre}`)
                rl.question('\n1. Añadir otro contacto\n0. Volver al menú\n', (opcion) => {
                    if (opcion === "1"){
                        addContact();
                    }else{
                        menu();
                    }
                });
            });
        }else{
            console.log("Número no válido, intente otra vez");
            addContact();
        }
    });
}

function editContact(){
    for (const [key, value] of contactos){
    console.log(key, value);
};
    rl.question("\nNombre del contacto a editar: ", (nombre) => {
        if (contactos.has(nombre)){
            rl.question("\n¿Qué quieres editar?\n1. Nombre\n2. Número\n", (opcion) => {
                if (opcion === "1"){
                    rl.question("\nNuevo nombre: ", (newName) => {
                        const newNombre = newName; 
                        const numActual = contactos.get(nombre);
                        contactos.delete(nombre);
                        contactos.set(newNombre, numActual);
                        console.log("Contacto editado con exito.")
                        rl.question('\n1. Editar otro contacto\n0. Volver al menú\n', (opcion) => {
                            if (opcion === "1"){
                                editContact();
                            }else{
                                menu();
                            }
                        });
                    });
                }else if (opcion === "2"){
                    rl.question("Nuevo número: ", (newNum) => {
                        if (newNum.length <= 11 && !isNaN(newNum)){
                            const newNumero = newNum;
                            contactos.set(nombre, newNumero);
                        console.log("Contacto editado con exito.")
                        }else{
                            console.log("Número no válido, intente otra vez");
                            editContact();
                        }
                        rl.question('\n1. Editar otro contacto\n0. Volver al menú\n', (opcion) => {
                            if (opcion === "1"){
                                editContact();
                            }else{
                                menu();
                            }
                        });
                    });
                }else{
                    console.log("Opción inválida");
                    editContact();
                }
            });
        }else{
            console.log("Contacto no existente")
            editContact();
        }
    });
}


function deleteContact(){
    for (const [key, value] of contactos){
    console.log(key, value);
};
    rl.question("\nNombre del contacto a eliminar: ", (nombre) => {
        if (contactos.has(nombre)){
            contactos.delete(nombre);    
            console.log(`Se eliminó a ${nombre}`)
            rl.question('\n1. Eliminar otro contacto\n0. Volver al menú\n', (opcion) => {
                    if (opcion === "1"){
                        deleteContact();
                    }else{
                        menu();
                    }
                });
        }else{
            console.log("Contacto no existente")
            deleteContact();
        }
    });
}













