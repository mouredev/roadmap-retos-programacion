// Ejemplos de creación de estructuras soportadas por defecto en JavaScript

// 1. Arrays
let array = [1, 2, 3, 4, 5];
console.log('Array:', array);

// Operaciones con arrays
array.push(6); // Inserción
console.log('Array después de inserción:', array);

array.splice(2, 1); // Borrado
console.log('Array después de borrado:', array);

array[1] = 10; // Actualización
console.log('Array después de actualización:', array);

array.sort((a, b) => a - b); // Ordenación
console.log('Array después de ordenación:', array);

// 2. Objetos
let objeto = { nombre: 'Juan', edad: 30 };
console.log('Objeto:', objeto);

// Operaciones con objetos
objeto.direccion = 'Calle Falsa 123'; // Inserción
console.log('Objeto después de inserción:', objeto);

delete objeto.edad; // Borrado
console.log('Objeto después de borrado:', objeto);

objeto.nombre = 'Pedro'; // Actualización
console.log('Objeto después de actualización:', objeto);

// 3. Mapas
let mapa = new Map();
mapa.set('clave1', 'valor1');
mapa.set('clave2', 'valor2');
console.log('Mapa:', mapa);

// Operaciones con mapas
mapa.set('clave3', 'valor3'); // Inserción
console.log('Mapa después de inserción:', mapa);

mapa.delete('clave2'); // Borrado
console.log('Mapa después de borrado:', mapa);

mapa.set('clave1', 'nuevoValor1'); // Actualización
console.log('Mapa después de actualización:', mapa);

// 4. Conjuntos
let conjunto = new Set([1, 2, 3, 4, 5]);
console.log('Conjunto:', conjunto);

// Operaciones con conjuntos
conjunto.add(6); // Inserción
console.log('Conjunto después de inserción:', conjunto);

conjunto.delete(3); // Borrado
console.log('Conjunto después de borrado:', conjunto);

conjunto = new Set([...conjunto].map(x => x * 2)); // Actualización
console.log('Conjunto después de actualización:', conjunto);

// Ejercicio extra: Agenda de contactos por terminal

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let contactos = [];

function mostrarMenu() {
    console.log('\nAgenda de Contactos');
    console.log('1. Insertar contacto');
    console.log('2. Buscar contacto');
    console.log('3. Actualizar contacto');
    console.log('4. Eliminar contacto');
    console.log('5. Salir');
    rl.question('Selecciona una opción: ', (opcion) => {
        switch (opcion) {
            case '1':
                insertarContacto();
                break;
            case '2':
                buscarContacto();
                break;
            case '3':
                actualizarContacto();
                break;
            case '4':
                eliminarContacto();
                break;
            case '5':
                rl.close();
                break;
            default:
                console.log('Opción no válida');
                mostrarMenu();
                break;
        }
    });
}

function insertarContacto() {
    rl.question('Nombre: ', (nombre) => {
        rl.question('Número de teléfono: ', (telefono) => {
            if (!/^\d{1,11}$/.test(telefono)) {
                console.log('Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.');
                mostrarMenu();
            } else {
                contactos.push({ nombre, telefono });
                console.log('Contacto insertado.');
                mostrarMenu();
            }
        });
    });
}

function buscarContacto() {
    rl.question('Nombre del contacto a buscar: ', (nombre) => {
        const contacto = contactos.find(c => c.nombre === nombre);
        if (contacto) {
            console.log(`Contacto encontrado: ${contacto.nombre} - ${contacto.telefono}`);
        } else {
            console.log('Contacto no encontrado.');
        }
        mostrarMenu();
    });
}

function actualizarContacto() {
    rl.question('Nombre del contacto a actualizar: ', (nombre) => {
        const contacto = contactos.find(c => c.nombre === nombre);
        if (contacto) {
            rl.question('Nuevo número de teléfono: ', (telefono) => {
                if (!/^\d{1,11}$/.test(telefono)) {
                    console.log('Número de teléfono no válido. Debe ser numérico y tener hasta 11 dígitos.');
                } else {
                    contacto.telefono = telefono;
                    console.log('Contacto actualizado.');
                }
                mostrarMenu();
            });
        } else {
            console.log('Contacto no encontrado.');
            mostrarMenu();
        }
    });
}

function eliminarContacto() {
    rl.question('Nombre del contacto a eliminar: ', (nombre) => {
        const index = contactos.findIndex(c => c.nombre === nombre);
        if (index !== -1) {
            contactos.splice(index, 1);
            console.log('Contacto eliminado.');
        } else {
            console.log('Contacto no encontrado.');
        }
        mostrarMenu();
    });
}

mostrarMenu();