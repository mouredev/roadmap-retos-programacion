//* EJERCICIO:- Ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
//  Utiliza operaciones de inserción, borrado, actualización y ordenación.

// objetos de JavaScript: Array, Set, Map
let usuario = {
    nombre: "Franco",
    apellido: "Jorge",
};
console.log(usuario);

// --- ARRAY (Lista. 
let lista = ["Zelda", "Franco", "Jorge"];
lista.push("Peach");          // Inserción
lista.splice(1, 1);           // Borrado (Franco)
lista[0] = "Ganondorf";       // Actualización
lista.sort();                 // ORDENACIÓN 
console.log("Array ordenado:", lista);

// --- SET  ---

let conjunto = new Set(["A", "B", "C"]);
conjunto.add("D");            // Inserción
conjunto.delete("A");         // Borrado
// Para actualizar en un Set, borras el viejo y metes el nuevo.
console.log("Set:", conjunto);

// --- MAP (Diccionario Clave-Valor) ---
let mapa = new Map();
mapa.set("nombre", "Franco"); // Inserción
mapa.set("edad", 34);
mapa.set("nombre", "Jorge");  // Actualización.
mapa.delete("edad");          // Borrado
console.log("Map:", mapa);


// Dificultad EXTRA: AGENDA DE CONTACTOS


const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let agenda = []; // Aquí guardaremos los contactos

function mostrarMenu() {
    console.log("\n--- AGENDA ---");
    console.log("1. Buscar contacto");
    console.log("2. Insertar contacto");
    console.log("3. Actualizar contacto");
    console.log("4. Eliminar contacto");
    console.log("5. Salir");
    
    rl.question("\nElige una opción: ", function(opcion) {
        switch(opcion) {
            case "1": buscarContacto(); break;
            case "2": insertarContacto(); break;
            case "3": actualizarContacto(); break;
            case "4": eliminarContacto(); break;
            case "5": 
                console.log("¡Adiós!");
                rl.close(); // Cerramos el programa
                break;
            default:
                console.log("Opción no válida.");
                mostrarMenu();
        }
    });
}

function buscarContacto() {
    rl.question("Nombre a buscar: ", (nombre) => {
        const contacto = agenda.find(c => c.nombre === nombre);
        if (contacto) {
            console.log(`Encontrado: ${contacto.nombre} - Tel: ${contacto.telefono}`);
        } else {
            console.log("No existe ese contacto.");
        }
        mostrarMenu();
    });
}

function insertarContacto() {
    rl.question("Nombre: ", (nombre) => {
        rl.question("Teléfono: ", (telefono) => {
            // VALIDACIÓN: Debe ser numérico y <= 11 dígitos
            if (!isNaN(telefono) && telefono.length > 0 && telefono.length <= 11) {
                agenda.push({ nombre: nombre, telefono: telefono });
                console.log("Contacto guardado.");
            } else {
                console.log("ERROR: El teléfono debe ser numérico y tener máx 11 dígitos.");
            }
            mostrarMenu();
        });
    });
}

function actualizarContacto() {
    rl.question("Nombre del contacto a actualizar: ", (nombre) => {
        // Buscamos el índice (posición) en el array
        const index = agenda.findIndex(c => c.nombre === nombre);
        
        if (index !== -1) {
            rl.question("Nuevo teléfono: ", (nuevoTel) => {
                if (!isNaN(nuevoTel) && nuevoTel.length <= 11) {
                    agenda[index].telefono = nuevoTel;
                    console.log("Actualizado correctamente.");
                } else {
                    console.log("Teléfono inválido.");
                }
                mostrarMenu();
            });
        } else {
            console.log("Contacto no encontrado.");
            mostrarMenu();
        }
    });
}

function eliminarContacto() {
    rl.question("Nombre a eliminar: ", (nombre) => {
        const cantidadInicial = agenda.length;
        // Filtramos: Nos quedamos con todos LOS QUE NO sean ese nombre
        agenda = agenda.filter(c => c.nombre !== nombre);
        
        if (agenda.length < cantidadInicial) {
            console.log("Contacto eliminado.");
        } else {
            console.log("No se encontró el contacto.");
        }
        mostrarMenu();
    });
}


mostrarMenu();