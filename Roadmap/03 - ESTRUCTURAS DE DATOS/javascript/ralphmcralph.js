// Estructuras por defecto

// ARRAYS

var myArray = ["Manolo", "Benito", "Kamelas"]
console.log(myArray);

// Operaciones de inserción

myArray.push("Alonso");

console.log(myArray);

// Operaciones de borrado

var newArray = myArray.filter(e => e !== 'Kamelas');

myArray = newArray;

console.log(myArray);

// Operaciones de actualización

myArray[myArray.indexOf("Alonso")] = "Fernando Alonso";

console.log(myArray);

// Operaciones de ordenación

myArray.sort()

console.log(myArray);

// Objetos

var myObject = {
    name: "Brais",
    surname: "Moure",
    username: "@mouredev",
    age: 36
}

console.log(typeof (myObject));

// Sets

const a = new Set([1, 2, 3]);

a.add("Hola");

console.log(a);
console.log(typeof (a));


// Map

const b = new Map([
    [1, "one"],
    [2, "two"],
    [3, "three"]
])

console.log(b);
console.log(typeof (b));


b.set(4, "four");
b.delete(3);
b.set(4, "cuatro");

console.log(b);


/* DIFICULTAD EXTRA(opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   * los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
* (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
*/

const readlineSync = require('readline-sync');

const contactos = new Map();

async function my_agenda() {

    while (true) {
        console.log("");
        console.log("1. Buscar contacto");
        console.log("2. Insertar contacto");
        console.log("3. Actualizar contacto");
        console.log("4. Eliminar contacto");
        console.log("5. Salir");


        let selected_option = parseInt(readlineSync.question("Selecciona una opción: "));

        switch (selected_option) {
            case 1:
                buscarContacto();
                break;
            case 2:
                insertarContacto();
                break;
            case 3:
                actualizarNumeroContacto();
                break;
            case 4:
                borrarContacto();
                break;
            case 5:
                console.log("Saliendo de la agenda");
                process.exit(0);
            default:
                console.log("Opción no válida. Elige una opción del 1 al 5");
                break;

        }
    }


}

function introducirNumero() {

    let numero;

    do {
        numero = readlineSync.question("Introduce el número del contacto: ");

        numero = parseInt(numero);
    } while (isNaN(numero) || numero.toString().length >= 11 || numero.toString().length <= 0);

    return numero;
}

function buscarContacto() {
    let nombre;

    do {
        nombre = readlineSync.question("Introduce el nombre del contacto: ");
    } while (!contactos.has(nombre))

    console.log(`Contacto encontrado: ${nombre} - ${contactos.get(nombre)}`);

    return nombre;
}

function insertarContacto() {
    let nombre = readlineSync.question("Introduce el nombre del contacto: ");
    let numero = introducirNumero();

    if (contactos.has(numero)) {
        console.log("El número ya está registrado");

    } else {
        contactos.set(nombre, numero);
        console.log(`Contacto guardado: ${nombre} - ${numero}`);
    }
}

function actualizarNumeroContacto() {
    let nombre = buscarContacto();

    let nuevoNumero = introducirNumero();

    contactos.set(nombre, nuevoNumero);

    console.log(`Contacto guardado: ${nombre} - ${nuevoNumero}`);

}

function borrarContacto() {
    let nombre = buscarContacto();

    contactos.delete(nombre);
    console.log(`Contacto eliminado: ${nombre}`);

}



my_agenda();



