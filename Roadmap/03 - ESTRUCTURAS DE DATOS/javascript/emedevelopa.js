// ESTRUCUTRAS DE DATOS

// Arrays
let myArray = [1, 2, 3 ,4];
console.log(myArray);

//Insercción
myArray.push(5); //Inserta 5 en el último lugar.
console.log(myArray);

myArray.unshift(0); //Inserta 0 en primer lugar.
console.log(myArray);

//Borrado
myArray.shift(0); //Borra el primer dato.
console.log(myArray);

myArray.pop(5); //Borra el último dato.
console.log(myArray); 

//Actualización
myArray[1] = 13; // La posición 1 se actualiza.
console.log(myArray);


//Objetos
let user = {
    name: "María",
    age: 33,
    town: "Madrid",
    "number of kids": 2,
};
console.log(user);

//Actualiza
user.name = "Paca";
console.log(user);

//Inserta nueva propiedad
user["favourite color"] = "green";
console.log(user);

//Borrado
delete user.age;
console.log(user);

// Creación
let miMapa = new Map();

// Inserción
miMapa.set('clave1', 'valor1');
miMapa.set('clave2', 'valor2');

// Borrado
miMapa.delete('clave1');

// Actualización
miMapa.set('clave2', 'nuevoValor');


// Sets

// Creación
let miSet = new Set([1, 2, 3]);

// Inserción
miSet.add(4);

// Borrado
miSet.delete(2);

//EXTRA
const readline = require ("readline"); //Importa el módulo readline de node.js que proporciona una interfaz para leer ddatos desde un flujo de entrada (terminal)

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}); // Se crea una interfaz de comandos q utiliza el módulo "readline". process.stdin representa la entrada estandar (teclado) y process.stdout la salida (pantalla).

const agenda = new Map(); //Aquí se almacenan los datos. Un map es una estructura de datos que asocia claves con valores.

function mostrarMenu () {
    console.log("\n1. Mostrar contactos");  //n1 salto de linea.
    console.log("2. Añadir contacto");
    console.log("3. Actualizar contacto");
    console.log("Eliminar contacto");
    console.log("Salir");
}

function mostrarContactos () {
    console.log("\n---Contactos---");
    if (agenda.size === 0) {
        console.log("La agenda está vacía");
    } else {
        agenda.forEach((telefono, nombre) => {
            console.log(`${nombre}: ${telefono}`);
        });
    }
}

function agregarContacto () {
    rl.question("Nombre del contacto", (nombre) => {
        rl.question("Número de teléfono: ", (telefono) => {
            if (/^\d{1,11}$/.test(telefono)) {   ///^\d{1,11}$/ significa que la cadena debe consistir en entre 1 y 11 dígitos y no debe contener ningún otro carácter.
                agenda.set(nombre, telefono);
                console.log("Contacto añadido");
            } else {
                console.log("Número no válido");
            }
            mostrarMenu();
        });
    });
}  

function actualizarContacto () {
    rl.question("Nombre del contacto a actualizar: ", (nombre) => {
        if (agenda.has(nombre)) {
            rl.question("Nuevo número de teléfono ", (telefono) => {
                if(/^\d{1,11}$/.test(telefono)) {
                    agenda.set(nombre, telefono);
                    console.log("Contacto actualizado");
                } else {
                    console.log("Número no válido");
                }
                mostrarMenu();
            });
        } else {
            console.log("Contacto no encontrado");
            mostrarMenu();
        }
    });
}

function eliminarContacto () {
    rl.question("Nombre del contacto a elimiar ", (nombre) => {
        if (agenda.has(nombre)) {
            agenda.delete(nombre);
            console.log("Contacto eliminado");
        } else {
            console.log("Contacto no encontrado");
        }
        mostrarMenu();
    })
}

function opcionUser (opcion) {
    switch (opcion) {
        case "1":
            mostrarContactos();
            break;
        case "2":
            agregarContacto ();
            break;
        case "3":
            actualizarContacto ();
            break;
        case "4":
            eliminarContacto ();
            break;
        case "5":
            console.log("Saliendo del programa");
            rl.close();
            break;
        default:
            console.log("Opción no válida. Introduce un número del 1 al 5");
    }
}




