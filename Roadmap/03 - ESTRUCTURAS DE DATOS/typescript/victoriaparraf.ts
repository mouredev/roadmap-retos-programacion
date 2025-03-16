//ARRAYS
//Creacion de un array
let numeros: number[] = [5,3,4,6,7,1];
//insertar en un array
numeros.push(10); // Agregar al final
numeros.unshift(0); // Agregar al inicio
console.log(numeros);
//borrar elementos de un array
numeros.pop(); // Eliminar el último elemento
numeros.shift(); // Eliminar el primer elemento
console.log(numeros);
//actualizar elementos
numeros[2] = 7; // Actualizar el tercer elemento
console.log(numeros);
//ordenar
numeros.sort((a, b) => a - b); // Ordenar en orden ascendente
console.log(numeros); 

//TUPLAS
//Creacion de tuplas
let persona: [string, number] = ["Victoria", 23];
//Insercion y actualizacion (no se pueden insertar nuevos elementos)
persona[0] = "Vanessa";
persona[1] = 24;
console.log(persona);

//CONJUNTOS(sets)
//creacion
let conjunto: Set<number> = new Set([1,2,3,4]);
//Insercion
conjunto.add(5);
conjunto.add(3); // No se agregará ya que 3 ya está presente
console.log(conjunto); // Set { 1, 2, 3, 4, 5 }
//borrar
conjunto.delete(2);
console.log(conjunto); // Set { 1, 3, 4, 5 }
//verificar y tamano
console.log(conjunto.has(3)); // true
console.log(conjunto.size); // 4

//MAPAS 
//creacion
let mapa: Map<string, number> = new Map([
    ["uno", 1],
    ["dos", 2]
]);
//insertar
mapa.set("tres", 3);
console.log(mapa); // Map { 'uno' => 1, 'dos' => 2, 'tres' => 3 }
//borrar
mapa.delete("dos");
console.log(mapa); // Map { 'uno' => 1, 'tres' => 3 }
//actualizar
mapa.set("uno", 10);
console.log(mapa); // Map { 'uno' => 10, 'tres' => 3 }
//iterar
mapa.forEach((valor, clave) => {
    console.log(`${clave}: ${valor}`);
});
// uno: 10
// tres: 3

//OPERADORES
//Crear objeto
let personaObj = {
    nombre: "Victoria",
    edad: 23
};
//Insertar y actualizar
personaObj["profesion"] = "Ingeniera"; // Inserción
personaObj.edad = 22; // Actualización
console.log(personaObj); // { nombre: 'Alice', edad: 31, profesion: 'Ingeniera' }
//borrar
//delete personaObj.profesion;
console.log(personaObj); // { nombre: 'Alice', edad: 31 }
//iteracion
for (let clave in personaObj) {
    if (personaObj.hasOwnProperty(clave)) {
        console.log(`${clave}: ${personaObj[clave]}`);
    }
}
// nombre: Alice
// edad: 31

/**************************************************************/

/*EXTRAAA */
import * as readline from 'readline';

// Crear una interfaz para leer datos desde la consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Estructura de datos para almacenar los contactos
interface Contacto {
    nombre: string;
    telefono: string;
}

let contactos: Contacto[] = [];

// Función para mostrar el menú
function mostrarMenu(): void {
    console.clear();
    console.log("Bienvenido a tus Contactos");
    console.log("1. Agregar un nuevo contacto");
    console.log("2. Editar un contacto");
    console.log("3. Buscar un contacto");
    console.log("4. Eliminar un contacto");
    console.log("5. Salir");
}

// Función para agregar un nuevo contacto
function agregarContacto(): void {
    rl.question("Ingrese el nombre del contacto: ", (nombre: string) => {
        rl.question("Ingrese el número de teléfono: ", (telefono: string) => {
            if (telefono.match(/^\d{1,11}$/)) {
                contactos.push({ nombre, telefono });
                console.log("Contacto agregado exitosamente.");
            } else {
                console.log("Número de teléfono inválido. Debe ser numérico y tener hasta 11 dígitos.");
            }
            setTimeout(myAgenda, 1000); // Volver al menú principal
        });
    });
}

// Función para editar un contacto
function editarContacto(): void {
    rl.question("Ingrese el nombre del contacto a editar: ", (nombre: string) => {
        let contacto = contactos.find(c => c.nombre === nombre);
        if (contacto) {
            rl.question("Ingrese el nuevo número de teléfono: ", (telefono: string) => {
                if (telefono.match(/^\d{1,11}$/)) {
                    contacto.telefono = telefono;
                    console.log("Contacto actualizado exitosamente.");
                } else {
                    console.log("Número de teléfono inválido. Debe ser numérico y tener hasta 11 dígitos.");
                }
                setTimeout(myAgenda, 1000); // Volver al menú principal
            });
        } else {
            console.log("Contacto no encontrado.");
            setTimeout(myAgenda, 1000); // Volver al menú principal
        }
    });
}

// Función para buscar un contacto
function buscarContacto(): void {
    rl.question("Ingrese el nombre del contacto a buscar: ", (nombre: string) => {
        let contacto = contactos.find(c => c.nombre === nombre);
        if (contacto) {
            console.log(`Nombre: ${contacto.nombre}, Teléfono: ${contacto.telefono}`);
        } else {
            console.log("Contacto no encontrado.");
        }
        setTimeout(myAgenda, 1000); // Volver al menú principal
    });
}

// Función para eliminar un contacto
function eliminarContacto(): void {
    rl.question("Ingrese el nombre del contacto a eliminar: ", (nombre: string) => {
        let indice = contactos.findIndex(c => c.nombre === nombre);
        if (indice !== -1) {
            contactos.splice(indice, 1);
            console.log("Contacto eliminado exitosamente.");
        } else {
            console.log("Contacto no encontrado.");
        }
        setTimeout(myAgenda, 1000); // Volver al menú principal
    });
}

// Función principal para manejar el menú y las opciones
function myAgenda(): void {
    mostrarMenu();
    rl.question("Ingrese una opción: ", (respuesta: string) => {
        let opcion: number = parseInt(respuesta);

        switch (opcion) {
            case 1:
                agregarContacto();
                break;
            case 2:
                editarContacto();
                break;
            case 3:
                buscarContacto();
                break;
            case 4:
                eliminarContacto();
                break;
            case 5:
                console.log("Salir");
                rl.close(); // Cerrar la interfaz después de recibir la entrada
                return; // Salir de la función para evitar que se vuelva a mostrar el menú
            default:
                console.log("Opción no válida. Intente de nuevo.");
                setTimeout(myAgenda, 1000); // Volver al menú principal
                break;
        }
    });
}

myAgenda();




