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

// Arrays
let array = [3, 1, 4, 1, 5, 9];
array.push(2); // Inserción
array.splice(1, 1); // Borrado
array[0] = 8; // Actualización
array.sort(); // Ordenación
console.log("Array:", array);

// Objetos
let objeto = { nombre: "Juan", edad: 30 };
objeto.apellido = "Pérez"; // Inserción
delete objeto.edad; // Borrado
objeto.nombre = "Carlos"; // Actualización
console.log("Objeto:", objeto);

// Conjuntos (Set)
let conjunto = new Set([1, 2, 3, 4]);
conjunto.add(5); // Inserción
conjunto.delete(2); // Borrado
console.log("Conjunto:", conjunto);

// Mapas (Map)
let mapa = new Map();
mapa.set("clave1", "valor1"); // Inserción
mapa.delete("clave1"); // Borrado
mapa.set("clave2", "valor2 actualizado"); // Actualización
console.log("Mapa:", mapa);

// DIFICULTAD EXTRA: Agenda de Contactos
class Agenda {
    constructor() {
        this.contactos = new Map();
    }

    agregarContacto(nombre, telefono) {
        if (!/^[0-9]{1,11}$/.test(telefono)) {
            console.log("Número de teléfono no válido.");
            return;
        }
        this.contactos.set(nombre, telefono);
        console.log(`Contacto agregado: ${nombre} - ${telefono}`);
    }

    actualizarContacto(nombre, nuevoTelefono) {
        if (this.contactos.has(nombre)) {
            this.contactos.set(nombre, nuevoTelefono);
            console.log(`Contacto actualizado: ${nombre} - ${nuevoTelefono}`);
        } else {
            console.log("Contacto no encontrado.");
        }
    }

    eliminarContacto(nombre) {
        if (this.contactos.delete(nombre)) {
            console.log(`Contacto eliminado: ${nombre}`);
        } else {
            console.log("Contacto no encontrado.");
        }
    }

    buscarContacto(nombre) {
        if (this.contactos.has(nombre)) {
            console.log(`Contacto encontrado: ${nombre} - ${this.contactos.get(nombre)}`);
        } else {
            console.log("Contacto no encontrado.");
        }
    }

    mostrarAgenda() {
        console.log("Agenda de Contactos:");
        this.contactos.forEach((telefono, nombre) => {
            console.log(`${nombre}: ${telefono}`);
        });
    }
}

const agenda = new Agenda();
agenda.agregarContacto("Juan", "123456789");
agenda.agregarContacto("María", "987654321");
agenda.actualizarContacto("Juan", "111222333");
agenda.buscarContacto("María");
agenda.eliminarContacto("Juan");
agenda.mostrarAgenda();