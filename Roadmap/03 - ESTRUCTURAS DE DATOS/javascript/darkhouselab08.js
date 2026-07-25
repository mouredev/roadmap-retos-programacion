// NOTA; Este archivo es la version final del ejerccio Roadmap de JavaScript-darkHouseLab08.js  
/*
 * #03 ESTRUCTURAS DE DATOS
 */

// --- 1. ARRAYS (Listas) ---
let misFrutas = ["Manzana", "Pera"];
misFrutas.push("Uva");             // Inserción
misFrutas[1] = "Mango";            // Actualización
misFrutas.splice(0, 1);            // Borrado (elimina el primer elemento)
misFrutas.sort();                  // Ordenación
console.log("Array:", misFrutas);

// --- 2. OBJETOS (Diccionarios) ---
let programador = { nombre: "Jorge", lenguaje: "JS" };
programador.experiencia = "1 año"; // Inserción
programador.lenguaje = "JavaScript"; // Actualización
delete programador.experiencia;    // Borrado
console.log("Objeto:", programador);

// --- 3. SETS (Conjuntos de valores únicos) ---
let miSet = new Set(["a", "b", "c"]);
miSet.add("d");                    // Inserción
miSet.delete("a");                 // Borrado
console.log("Set (convertido a array):", Array.from(miSet));

// --- 4. MAPS (Diccionarios Clave-Valor dinámicos) ---
let miMapa = new Map();
miMapa.set("id", 1);               // Inserción
miMapa.set("id", 2);               // Actualización
miMapa.delete("id");               // Borrado

// ------------------------------------------------------------------
// DIFICULTAD EXTRA: AGENDA DE CONTACTOS
// ------------------------------------------------------------------

const readline = require('readline'); // Módulo para leer entrada desde la consola
const rl = readline.createInterface({ // Configuración de la interfaz
    input: process.stdin, 
    output: process.stdout 
});

let agenda = {};

function mostrarMenu() {
    console.log("\n--- AGENDA DE CONTACTOS ---"); // Menú de opciones
    console.log("1. Buscar");
    console.log("2. Insertar");
    console.log("3. Actualizar");
    console.log("4. Eliminar");
    console.log("5. Salir");
    
    rl.question("\nSelecciona una opción: ", (opcion) => {
        switch (opcion) {
            case "1": buscar(); break;  // Llama a la función correspondiente según la opción
            case "2": insertar(); break;
            case "3": actualizar(); break;
            case "4": eliminar(); break;
            case "5":
                console.log("Saliendo de la agenda..."); // Mensaje de salida
                rl.close();
                break;
            default:
                console.log("Opción no válida."); // Manejo de opción inválida
                mostrarMenu();
                break;
        }
    });
}

function validarTelefono(tel) {
    // Verifica que sea un número y que tenga entre 1 y 11 dígitos
    return !isNaN(tel) && tel.length > 0 && tel.length <= 11;
}

function insertar() {
    rl.question("Nombre del nuevo contacto: ", (nombre) => {
        rl.question("Número de teléfono (máx 11 dígitos): ", (tel) => {
            if (validarTelefono(tel)) {
                agenda[nombre] = tel;
                console.log("✅ Contacto guardado con éxito."); // Mensaje de éxito
            } else {
                console.log("❌ Error: El teléfono debe ser numérico y tener máximo 11 dígitos.");
            }
            mostrarMenu(); // Vuelve al menú principal
        });
    });
}

function buscar() {
    rl.question("Nombre a buscar: ", (nombre) => {
        if (agenda[nombre]) {
            console.log(`🔍 Resultado: ${nombre} -> Tel: ${agenda[nombre]}`);
        } else {
            console.log("⚠️ Contacto no encontrado."); // Mensaje si no se encuentra
        }
        mostrarMenu();
    });
}

function actualizar() {
    rl.question("Nombre del contacto a actualizar: ", (nombre) => {
        if (agenda[nombre]) {
            rl.question("Nuevo teléfono: ", (nuevoTel) => {
                if (validarTelefono(nuevoTel)) {
                    agenda[nombre] = nuevoTel;
                    console.log("✅ Contacto actualizado."); // Mensaje de éxito
                } else {
                    console.log("❌ Error en el formato del teléfono."); // Mensaje de error
                }
                mostrarMenu();
            });
        } else {
            console.log("⚠️ El contacto no existe.");
            mostrarMenu();
        }
    });
}

function eliminar() {
    rl.question("Nombre del contacto a eliminar: ", (nombre) => {
        if (agenda[nombre]) {
            delete agenda[nombre];
            console.log("🗑️ Contacto eliminado."); // Mensaje de éxito
        } else {
            console.log("⚠️ No se encontró el contacto."); // Mensaje si no se encuentra
        }
        mostrarMenu();
    });
}


mostrarMenu();
