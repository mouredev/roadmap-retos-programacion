/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
// 🔥 Arrays
let array = [3, 1, 4, 1, 5, 9];
array.push(2); // Inserción
//		[3, 1, 4, 1, 5, 9, 2]
array.splice(1, 1); // Borrado
//		[3, 4, 1, 5, 9, 2]
array[0] = 8; // Actualización
//		[8, 4, 1, 5, 9, 2]
array.sort(); // Ordenación
//		[1, 2, 4, 5, 8, 9]
console.log("Array:", array);

// 🔥 Objetos
let objeto = { nombre: "Anderson", edad: 20 };
objeto.apellido = "Mancilla"; // Inserción
//		{nombre: 'Anderson', edad: 20, apellido: 'Mancilla'}
delete objeto.edad; // Borrado
//		{nombre: 'Anderson', apellido: 'Mancilla'}
objeto.nombre = "Alfonso"; // Actualización
//		{nombre: 'Alfonso', apellido: 'Mancilla'}
console.log("Objeto:", objeto);

// 🔥 Conjuntos (Set)
let conjunto = new Set([1, 2, 3, 4]);
conjunto.add(5); // Inserción
//		{1, 2, 3, 4, 5}
conjunto.delete(2); // Borrado
//		{1, 3, 4, 5}
console.log("Conjunto:", conjunto);

// 🔥 Mapas (Map)
let mapa = new Map();
mapa.set("clave1", "valor1"); // Inserción
//		{'clave1' => 'valor1'}
mapa.delete("clave1"); // Borrado
//		{size: 0}
mapa.set("clave2", "valor2 actualizado"); // Actualización
//		{'clave2' => 'valor2 actualizado'}
console.log("Mapa:", mapa);

// 🔥 Extra: Agenda de Contactos
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let agenda = {};

function mostrarMenu() {
    console.log("\n1. Buscar contacto");
    console.log("2. Insertar contacto");
    console.log("3. Actualizar contacto");
    console.log("4. Eliminar contacto");
    console.log("5. Mostrar todos los contactos");
    console.log("6. Salir");
}

function buscarContacto(nombre) {
    if (agenda[nombre]) {
        console.log(`Contacto encontrado: ${nombre} - ${agenda[nombre]}`);
    } else {
        console.log("Contacto no encontrado.");
    }
}

function insertarContacto(nombre, telefono) {
    if (/^\d{1,11}$/.test(telefono)) {
        agenda[nombre] = telefono;
        console.log("Contacto insertado correctamente.");
    } else {
        console.log("Número de teléfono no válido. Debe ser numérico y tener máximo 11 dígitos.");
    }
}

function actualizarContacto(nombre, telefono) {
    if (agenda[nombre]) {
        if (/^\d{1,11}$/.test(telefono)) {
            agenda[nombre] = telefono;
            console.log("Contacto actualizado correctamente.");
        } else {
            console.log("Número de teléfono no válido. Debe ser numérico y tener máximo 11 dígitos.");
        }
    } else {
        console.log("Contacto no encontrado.");
    }
}

function eliminarContacto(nombre) {
    if (agenda[nombre]) {
        delete agenda[nombre];
        console.log("Contacto eliminado correctamente.");
    } else {
        console.log("Contacto no encontrado.");
    }
}

function mostrarTodosLosContactos() {
    console.log("\nLista de contactos:");
    for (let nombre in agenda) {
        console.log(`${nombre} - ${agenda[nombre]}`);
    }
}

function iniciarAgenda() {
    mostrarMenu();
    readline.question("Seleccione una opción: ", opcion => {
        switch (opcion) {
            case '1':
                readline.question("Nombre del contacto a buscar: ", nombre => {
                    buscarContacto(nombre);
                    iniciarAgenda();
                });
                break;
            case '2':
                readline.question("Nombre del contacto: ", nombre => {
                    readline.question("Número de teléfono: ", telefono => {
                        insertarContacto(nombre, telefono);
                        iniciarAgenda();
                    });
                });
                break;
            case '3':
                readline.question("Nombre del contacto a actualizar: ", nombre => {
                    readline.question("Nuevo número de teléfono: ", telefono => {
                        actualizarContacto(nombre, telefono);
                        iniciarAgenda();
                    });
                });
                break;
            case '4':
                readline.question("Nombre del contacto a eliminar: ", nombre => {
                    eliminarContacto(nombre);
                    iniciarAgenda();
                });
                break;
            case '5':
                mostrarTodosLosContactos();
                iniciarAgenda();
                break;
            case '6':
                console.log("Saliendo de la agenda...");
                readline.close();
                break;
            default:
                console.log("Opción no válida.");
                iniciarAgenda();
                break;
        }
    });
}

iniciarAgenda();