/*
_____________________________________
https://github.com/EliTeDev-44
2025 - JavaScript
_______________________________________
03 ESTRUCTURAS DE DATOS
---------------------------------------
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
// _______________________
// Referencias:
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Indexed_collections

// _______________________
// Creando Arrays (Arreglos, Listas...)
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/Array

// Muestra ejemplos de creación de todas las estructuras soportadas por defecto
let miArray = [] // Array vacío
let numeros = [14, 22, 36, 44, 59] // Array con números
let frutas = ["Melón", "Plátano", "Pera"] // Array con cadenas de texto
let mixto = [44, "Texto", true, null, undefined, 99.99] // Array con datos mixtos

console.log("===============================")
console.log("Arrays:\n")
console.log("✅ Array vacío:", miArray)
console.log("✅ Array de números:", numeros)
console.log("✅ Array de frutas:", frutas)
console.log("✅ Array mixto:", mixto)


// _______________________
// Utiliza operaciones de inserción, borrado, actualización y ordenación.

// Métodos:
// _______________________

console.log("================================")
console.log("Métodos del Array:\n")

// Creando Array
let arrayJugon = ["Hola", "soy un Array."]
console.log("😎 Resultado:", arrayJugon)

// Acceder a un elemento mediante su índice
console.log("✅ Búsqueda índice:", arrayJugon[1])

// ForEach - Recorrer un Array
let ingredientes = ["Harina", "Levadura", "Huevos", "Yogurt", "Azúcar"];

ingredientes.forEach(function (ing) {
  console.log("🧁 Ingrediente:", ing)
})

// Push - Agrega elemento al final del Array
arrayJugon.push("✅ Me acaban de insertar al final.")
console.log("😎 Push:" ,arrayJugon)

// Pop - Elimina un elemento del final del Array
arrayJugon.pop()
console.log("😎 Pop:", arrayJugon)

// Unshift - Añade un elemento al principo del Array
arrayJugon.unshift("👋🏼")
console.log("😎 Unshift:", arrayJugon)

// Shift - Elimina el primer elemento de un Array
arrayJugon.shift()
console.log("❌ Shift:", arrayJugon)

// IndexOf - Encontrar el índice de un elemento del Array
console.log("🔍 Índice del Array:", arrayJugon.indexOf("Hola"))

// Borrado del Array Completo:
arrayJugon = []
console.log("❌ Array borrado:", arrayJugon)

// Redefieniendo el Array
arrayJugon = ["Hola,", "soy un array", "Jugón"]
console.log("🧠 Actualizando:", arrayJugon)

// Length - Mostrando el número de elemento del array.
console.log("🧠 Length:", arrayJugon.length)

// Slice(x, x) - Muestra los elementos seleccionados en RANGO
console.log("😎 Slice:", arrayJugon.slice(0, 2))

// Splice (x, x) - Elimina los elementos deleccionados en RANGO
console.log("❌ Splice:", arrayJugon.splice("Hola", 1))

// Copiar un Array
let copiaArrayJugon = arrayJugon.slice()
console.log("🙌🏼 Array copiado:", copiaArrayJugon)


/*  * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa. */

// 🧭 Agenda de contactos por terminal
// Autor: EliTeDev-44
// Ejecútalo con: node agenda.js

const readline = require("readline")

// Creamos la interfaz para leer desde la terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

// Base de datos temporal en memoria
let agenda = [
    { nombre: "Jose", telefono: "600123456" },
    { nombre: "Lucia", telefono: "699654321" }
]

// Función principal del menú
function mostrarMenu() {
    console.log("\n📒  AGENDA DE CONTACTOS")
    console.log("1️⃣  Ver contactos")
    console.log("2️⃣  Buscar contacto")
    console.log("3️⃣  Añadir contacto");
    console.log("4️⃣  Actualizar contacto")
    console.log("5️⃣  Eliminar contacto")
    console.log("6️⃣  Salir\n")

    rl.question("✅ Selecciona una opción (1-6): ", (opcion) => {
        switch (opcion) {
            case "1": verContactos(); break;
            case "2": buscarContacto(); break;
            case "3": agregarContacto(); break;
            case "4": actualizarContacto(); break;
            case "5": eliminarContacto(); break;
            case "6": salir(); break;
            default:
                console.log("❌ Opción no válida.");
                mostrarMenu();
        }
    });
}

// 📖 Ver todos los contactos
function verContactos() {
    console.log("\n📇 Contactos guardados:");
    agenda.forEach((c, i) => console.log(`${i + 1}. ${c.nombre} - ${c.telefono}`));
    mostrarMenu();
}

// 🔍 Buscar contacto por nombre
function buscarContacto() {
    rl.question("Introduce el nombre del contacto: ", (nombre) => {
        const contacto = agenda.find(c => c.nombre.toLowerCase() === nombre.toLowerCase());
        if (contacto) {
            console.log(`✅ Encontrado: ${contacto.nombre} - ${contacto.telefono}`);
        } else {
            console.log("❌ No se encontró el contacto.");
        }
        mostrarMenu();
    });
}

// ➕ Agregar nuevo contacto
function agregarContacto() {
    rl.question("Nombre del nuevo contacto: ", (nombre) => {
        rl.question("Teléfono: ", (telefono) => {
            if (!/^\d{1,11}$/.test(telefono)) {
                console.log("❌ Teléfono inválido. Debe tener solo números y máximo 11 dígitos.");
                mostrarMenu();
                return;
            }

            agenda.push({ nombre, telefono });
            console.log(`✅ Contacto añadido: ${nombre} - ${telefono}`);
            mostrarMenu();
        });
    });
}

// ✏️ Actualizar un contacto
function actualizarContacto() {
    rl.question("Nombre del contacto a actualizar: ", (nombre) => {
        const contacto = agenda.find(c => c.nombre.toLowerCase() === nombre.toLowerCase());
        if (!contacto) {
            console.log("❌ No se encontró el contacto.");
            mostrarMenu();
            return;
        }

        rl.question("Nuevo número de teléfono: ", (nuevoTelefono) => {
            if (!/^\d{1,11}$/.test(nuevoTelefono)) {
                console.log("❌ Teléfono inválido. Debe tener solo números y máximo 11 dígitos.");
                mostrarMenu();
                return;
            }

            contacto.telefono = nuevoTelefono;
            console.log(`✅ Contacto actualizado: ${contacto.nombre} - ${contacto.telefono}`);
            mostrarMenu();
        });
    });
}

// ❌ Eliminar un contacto
function eliminarContacto() {
    rl.question("Nombre del contacto a eliminar: ", (nombre) => {
        const indice = agenda.findIndex(c => c.nombre.toLowerCase() === nombre.toLowerCase());
        if (indice === -1) {
            console.log("❌ No se encontró el contacto.");
        } else {
            console.log(`🗑️ Contacto eliminado: ${agenda[indice].nombre}`);
            agenda.splice(indice, 1);
        }
        mostrarMenu();
    });
}

// 🚪 Salir del programa
function salir() {
    console.log("\n👋 ¡Hasta pronto!");
    rl.close();
}

// 🏁 Iniciar programa
mostrarMenu();