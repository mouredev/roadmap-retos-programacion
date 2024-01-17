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



/* Soluciones */

// Arrays

// Creación
let miArray = [1, 2, 3, 4, 5];

// Inserción
miArray.push(6); // Añade un elemento al final
miArray.unshift(0); // Añade un elemento al principio

// Borrado
miArray.pop(); // Elimina el último elemento
miArray.shift(); // Elimina el primer elemento
miArray.splice(2, 1); // Elimina un elemento en la posición 2

// Actualización
miArray[1] = 10; // Actualiza el valor en la posición 1

// Ordenación
miArray.sort(); // Ordena el array

// Objetos 

// Creación
let miObjeto = { nombre: 'Juan', edad: 25, ciudad: 'Montevideo' };

// Actualización
miObjeto.edad = 26;

// Inserción
miObjeto.trabajo = 'Desarrollador';

// Borrado
delete miObjeto.ciudad;

// No hay operación de ordenación para objetos

// Mapas

// Creación
let miMapa = new Map();

// Inserción
miMapa.set('clave1', 'valor1');
miMapa.set('clave2', 'valor2');

// Borrado
miMapa.delete('clave1');

// Actualización
miMapa.set('clave2', 'nuevoValor');

// No hay operación de ordenación específica para Mapas

// Sets

// Creación
let miSet = new Set([1, 2, 3]);

// Inserción
miSet.add(4);

// Borrado
miSet.delete(2);

// No hay operación de actualización específica para Sets
// No hay operación de ordenación específica para Sets

// Extra/Opcional

let lista = [];

function validarTelefono(numero) {
    return /^\d{10,11}$/.test(numero);
}

function buscarContacto(nombre) {
    return lista.find(contacto => contacto.Nombre === nombre);
}

function contactos() {
    console.log("Para agregar un contacto presiona 1, para borrarlo presiona 2, para volver presiona 3.");
    let numeros = prompt("Por favor, presiona un número: "); 

    switch (numeros) {
        case '1':
            let nombre = prompt("Ingresa el nombre de tu contacto: ");
            let numero = prompt("Ingresa el número de tu contacto: ");

            if (validarTelefono(numero)) {
                lista.push({ Nombre: nombre, Numero: numero });
                console.log("Contacto guardado.");
            } else {
                console.error("Número de teléfono inválido. Debe tener 10 o 11 dígitos como máximo y no tener caracteres incorrectos.");
            }
            break;

        case '2':
            let nombreBorrar = prompt("Ingresa el nombre del contacto que quieres borrar: ");
            let contactoBorrar = buscarContacto(nombreBorrar);

            if (contactoBorrar) {
                lista = lista.filter(contacto => contacto !== contactoBorrar);
                console.log("Contacto borrado.");
            } else {
                console.error("Contacto no encontrado.");
            }
            break;

        case '3':
            return panel();

        default:
            console.error("Operación cancelada. Número no reconocido.");
    }
    return panel();
}

function agenda() {
    console.log("Bienvenido a la lista de contactos.");
    if (lista.length === 0) {
        console.log("No hay contactos registrados.");
    } else {
        console.log(lista);
    }
    return panel();
}

function buscarYMostrarContacto() {
    let nombre = prompt("Ingresa el nombre del contacto que quieres buscar: ");
    let contacto = buscarContacto(nombre);

    if (contacto) {
        console.log("Contacto encontrado: ", contacto);
    } else {
        console.error("Contacto no encontrado.");
    }
    return panel();
}

function panel() {
    console.log("Bienvenido al panel de contactos: Presiona 1 para agregar o borrar un contacto, presiona 2 para ver todos los contactos, presiona 3 para buscar un contacto, presiona 4 para salir.");
    let numero = prompt("Por favor, presiona un número: ");

    switch (numero) {
        case '1':
            return contactos();

        case '2':
            return agenda();

        case '3':
            buscarYMostrarContacto();
            break;

        case '4':
            console.log("Ha salido del programa.");
            break;

        default:
            console.error("Número incorrecto.");
            return panel();
    }
}

panel();
