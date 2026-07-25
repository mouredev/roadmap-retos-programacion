// Importamos el módulo readline para manejar la entrada del usuario
const readline = require('readline');

// Creamos una interfaz de readline
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para ejemplificar las estructuras de datos en JavaScript
function ejemplosEstructurasDatos() {
    // Array: equivalente a ArrayList en Java
    let array = ['Java', 'Python', 'JavaScript'];
    console.log('Array:', array);

    // Set: conjunto sin duplicados
    let set = new Set([1, 2, 2, 3, 4]);
    console.log('Set:', set);

    // Map: equivalente a HashMap en Java
    let map = new Map();
    map.set('Uno', 1);
    map.set('Dos', 2);
    map.set('Tres', 3);
    console.log('Map:', map);

    // Operaciones
    array.splice(1, 1); // Borrado (elimina 'Python')
    array[1] = 'TypeScript'; // Actualización
    array.sort(); // Ordenación

    console.log('Array después de operaciones:', array);
}

// Función principal para la agenda de contactos
function agendaContactos() {
    let agenda = new Map();

    function mostrarMenu() {
        console.log("\n--- Agenda de Contactos ---");
        console.log("1. Buscar contacto");
        console.log("2. Añadir contacto");
        console.log("3. Actualizar contacto");
        console.log("4. Eliminar contacto");
        console.log("5. Mostrar todos los contactos");
        console.log("6. Salir");
        rl.question("Seleccione una opción: ", manejarOpcion);
    }

    function manejarOpcion(opcion) {
        switch (opcion) {
            case '1':
                buscarContacto();
                break;
            case '2':
                anadirContacto();
                break;
            case '3':
                actualizarContacto();
                break;
            case '4':
                eliminarContacto();
                break;
            case '5':
                mostrarContactos();
                break;
            case '6':
                console.log("¡Hasta luego!");
                rl.close();
                return;
            default:
                console.log("Opción no válida.");
                mostrarMenu();
        }
    }

    function buscarContacto() {
        rl.question("Ingrese el nombre del contacto: ", (nombre) => {
            if (agenda.has(nombre)) {
                console.log(`Teléfono de ${nombre}: ${agenda.get(nombre)}`);
            } else {
                console.log("Contacto no encontrado.");
            }
            mostrarMenu();
        });
    }

    function anadirContacto() {
        rl.question("Ingrese el nombre del contacto: ", (nombre) => {
            solicitarTelefono((telefono) => {
                agenda.set(nombre, telefono);
                console.log("Contacto añadido con éxito.");
                mostrarMenu();
            });
        });
    }

    function actualizarContacto() {
        rl.question("Ingrese el nombre del contacto a actualizar: ", (nombre) => {
            if (agenda.has(nombre)) {
                solicitarTelefono((telefono) => {
                    agenda.set(nombre, telefono);
                    console.log("Contacto actualizado con éxito.");
                    mostrarMenu();
                });
            } else {
                console.log("Contacto no encontrado.");
                mostrarMenu();
            }
        });
    }

    function eliminarContacto() {
        rl.question("Ingrese el nombre del contacto a eliminar: ", (nombre) => {
            if (agenda.delete(nombre)) {
                console.log("Contacto eliminado con éxito.");
            } else {
                console.log("Contacto no encontrado.");
            }
            mostrarMenu();
        });
    }

    function mostrarContactos() {
        if (agenda.size === 0) {
            console.log("La agenda está vacía.");
        } else {
            agenda.forEach((telefono, nombre) => {
                console.log(`${nombre}: ${telefono}`);
            });
        }
        mostrarMenu();
    }

    function solicitarTelefono(callback) {
        rl.question("Ingrese el número de teléfono (máximo 11 dígitos): ", (telefono) => {
            if (/^\d{1,11}$/.test(telefono)) {
                callback(telefono);
            } else {
                console.log("Número no válido. Debe ser numérico y tener máximo 11 dígitos.");
                solicitarTelefono(callback);
            }
        });
    }

    mostrarMenu();
}

// Ejecutamos los ejemplos y la agenda
console.log("Ejemplos de estructuras de datos en JavaScript:");
ejemplosEstructurasDatos();

console.log("\nIniciando la agenda de contactos...");
agendaContactos();