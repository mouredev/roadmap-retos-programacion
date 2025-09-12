// CREACIÓN DE LAS ESTRUCTURAS SOPORTADAS

// Datos primitivos (no pueden ser manipuladas por las distintas operaciones)

let numero = 4;
let float = 4.0;
let cadena = "jeje";
let booleano = true;

// Array
const array = ["Hola", "moure", "soy", "Vixis"];    // Creación
const array_2 = new Array;
console.log(array);
console.log(array.push("zzz"));                     // Operación de inserción
console.log(array.unshift(1));
console.log(array.pop());                           // Operación de borrado
console.log(array.shift());
console.log(array[1]="Moure");                      // Operación de actualización
console.log(array.sort());                          // Operación de ordenación ascendente
console.log(array.sort((a, b) => {                  // Operación de ordenación descendente
    if (a > b) return -1;
}));

// Map

let mapa = new Map();   // Creación
mapa.set({ z: 1, x: 2, y: 3 }, "zzz");
mapa.set("a", 1);
mapa.set("b", 2);
mapa.set("c", 3);       // Operación de inserción
mapa.delete("a");       // Operación de borrado
mapa.set("b", 20)       // Operación de actualización
console.log(mapa + "\n");

// Object

const objeto = {                // Creación
    nombre: "Vixito",
    edad: "22",
    país: "Colombia"
}; console.log(objeto);
objeto.profesion = "Ingeniero"; // Operación de inserción
delete objeto.país;             // Operación de borrado
objeto.nombre = "Carlos";       // Operación de actualización
console.log(objeto);

// Set

let conjunto = new Set([1, 2, 3, 4, 5]);    // Creación
conjunto.add(6);                            // Operación de inserción
conjunto.delete(3);                         // Operación de borrado
// No hay operación de actualización porque no exite un comando como tal, se tiene que hacer manualmente.



// DIFICULTAD EXTRA

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let contacto = [];

function Menu(){
    console.log("AGENDA DE DATOS \n Pulsa los números para explorar las opciones: \n 1. Buscar contacto \n 2. Insertar contacto \n 3. Actualizar contacto \n 4. Eliminar contacto \n 5. Cerrar");
    rl.question("Selecciona: ", (opcion) => {
        switch (opcion.trim()) {
            case '1':
                rl.question("Nombre del contacto a buscar: ", (nombre) => {
                    const busqueda = contacto.find(c => c.nombre.toLowerCase() === nombre.trim().toLowerCase());
                    if(busqueda){
                        console.log(`✅ Contacto encontrado: ${busqueda.nombre} - ${busqueda.telefono}\n`);
                    }else{
                        console.log("❌ Contacto no encontrado.\n");
                    }
                    Menu();
                })
                break;
            case '2':
                rl.question("Inserte el nombre: ", (nombre) => {
                    rl.question("Inserte el teléfono: ", (telefono) => {
                        if(/^\d{1,11}$/.test(telefono)){
                            contacto.push({nombre: nombre.trim(), telefono: telefono.trim()});
                            console.log("✅ Contacto añadido.\n");
                        }else{
                            console.log("❌ Número de teléfono no válido.\nDebe ser numérico y no más de 11 dígitos.\n");
                        }
                        Menu();
                    });
                });
                break;
            case '3':
                rl.question("Nombre del contacto a actualizar: ", (nombre) => {
                    const indice = contacto.findIndex(c => c.nombre.toLowerCase() === nombre.trim().toLowerCase());
                    if (indice !== -1) {
                        rl.question("Inserte el nuevo nombre: ", (nuevoNombre) => {
                            rl.question("Inserte el nuevo número de teléfono: ", (nuevoTelefono) => {
                                if (/^\d{1,11}$/.test(nuevoTelefono)) {
                                    contacto[indice] = { nombre: nuevoNombre.trim(), telefono: nuevoTelefono.trim() };
                                    console.log("✅ Contacto actualizado.\n");
                                } else {
                                    console.log("❌ Número de teléfono no válido.\nDebe ser numérico y no más de 11 dígitos.\n");
                                }
                                Menu();
                            });
                        });
                    } else {
                        console.log("❌ Contacto no encontrado.\n");
                        Menu();
                    }
                });
                break;
            case '4':
                rl.question("Nombre del contacto a eliminar: ", (nombre) => {
                    const indice = contacto.findIndex(c => c.nombre.toLowerCase() === nombre.trim().toLowerCase());
                    if(indice !== -1){
                        contacto.splice(indice, 1)
                        console.log("✅ Contacto eliminado.\n");
                    }else{
                        console.log("❌ Contacto no encontrado.\n")
                    }
                    Menu();
                });
                break;
            case '5':
                rl.close();
                break;
            default:
                console.log("\nOpción no válida...");
                Menu();
                break;
        }
    });
}

Menu();