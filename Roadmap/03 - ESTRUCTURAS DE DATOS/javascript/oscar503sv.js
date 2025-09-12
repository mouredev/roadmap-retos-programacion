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

/* ************************************** ARRAYS ************************************** */
/*Una colección ordenada de elementos que pueden ser de cualquier tipo, y están indexados numéricamente, comenzando desde 0.*/
var miArray = [1, "dos", { clave: "valor" }, true];
console.log(miArray); //[1, "dos", { clave: "valor" }, true]
console.log(miArray[1]); //"dos"

miArray.push("tres"); // agrega un elemento al final de la colección
console.log(miArray); 
miArray.pop(); // elimina el último elemento de la colección
console.log(miArray); 
miArray.shift(); // elimina el primer elemento de la colección
console.log(miArray);
miArray.unshift("uno"); // agrega un elemento al principio de la colección
console.log(miArray); 

miArray.splice(1, 1); // elimina el elemento en la posición 1 de la colección
console.log(miArray); 
miArray.splice(1, 0, "dos"); // agrega un elemento en la posición 1 de la colección
console.log(miArray); 

/* ************************************** OBJETOS ************************************** */
/*Un objeto es una colección de propiedades, que se pueden acceder a mediante el operador de acceso de objetos.*/
var miObjeto = {
    propiedad1: "valor1",
    propiedad2: "valor2",
    propiedad3: "valor3"
};
console.log(miObjeto.propiedad1); //"valor1"
miObjeto.propiedad2 = "nuevo valor"; //cambia el valor de la propiedad propiedad2
console.log(miObjeto.propiedad2); //"nuevo valor"
miObjeto.nuevaPropiedad = "Esta es una nueva propiedad"; //agrega una nueva propiedad a miObjeto
console.log(miObjeto.nuevaPropiedad); //"Esta es una nueva propiedad"
delete miObjeto.nuevaPropiedad; //elimina la propiedad nuevaPropiedad de miObjeto
console.log(miObjeto); //{ propiedad1: "valor1", propiedad2: "nuevo valor" }

/* ************************************** MATRICES ************************************** */
/*Una matriz es una colección de elementos del mismo tipo, indexados por un entero numérico.*/
var miMatriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Obtener elementos de la matriz
console.log(miMatriz[0][0]); // Output: 1
console.log(miMatriz[1][2]); // Output: 6
console.log(miMatriz[2][1]); // Output: 8

// Iterar sobre la matriz
for (var i = 0; i < miMatriz.length; i++) {
    for (var j = 0; j < miMatriz[i].length; j++) {
        console.log(miMatriz[i][j]);
    }
}

// Agregar un elemento a la matriz
miMatriz[0][0] = 10;
console.log(miMatriz); // Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

// Eliminar un elemento de la matriz
delete miMatriz[1][2];
console.log(miMatriz); // Output: [[10, 2, 3], [4, 5], [7, 8, 9]]

// Cambiar el valor de un elemento de la matriz
miMatriz[1][1] = 20;
console.log(miMatriz); // Output: [[10, 2, 3], [4, 20], [7, 8, 9]]

// Agregar una nueva fila a la matriz
miMatriz.push([10, 20, 30]);
console.log(miMatriz); // Output: [[10, 2, 3], [4, 20], [7, 8, 9], [10, 20, 30]]

// Eliminar una fila de la matriz    
miMatriz.pop();
console.log(miMatriz); // Output: [[10, 2, 3], [4, 20], [7, 8, 9]]

// Cambiar el valor de una fila de la matriz
miMatriz[1][1] = 30;
console.log(miMatriz); // Output: [[10, 2, 3], [4, 30], [7, 8, 9]]

miMatriz[1][2] = 6;
console.log(miMatriz); // Output: [[10, 2, 3], [4, 30, 6], [7, 8, 9]]

// Sumar dos matrices
var otraMatriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
];

var resultadoSuma = [];
for (var i = 0; i < miMatriz.length; i++) {
    resultadoSuma[i] = [];
    for (var j = 0; j < miMatriz[i].length; j++) {
        resultadoSuma[i][j] = miMatriz[i][j] + otraMatriz[i][j];
    }
}
console.log(resultadoSuma);

// Multiplicar una matriz por un escalar
var escalar = 2;
var resultadoMultiplicacion = [];
for (var i = 0; i < miMatriz.length; i++) {
    resultadoMultiplicacion[i] = [];
    for (var j = 0; j < miMatriz[i].length; j++) {
        resultadoMultiplicacion[i][j] = miMatriz[i][j] * escalar;
    }
}
console.log(resultadoMultiplicacion);

/* ************************************** SETS ************************************** */
/*Un conjunto es una colección de elementos que no tiene repeticiones, y que se pueden acceder a mediante el operador de acceso de objetos.*/
var miSet = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
console.log(miSet); //Set { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
console.log(miSet.has(1)); //true
console.log(miSet.has(10)); //false
console.log(miSet.add(10)); //Set { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
console.log(miSet.size); //10
console.log(miSet.delete(1)); //true
console.log(miSet); //Set { 2, 3, 4, 5, 6, 7, 8, 9, 10 }

/* ************************************** MAPS ************************************** */
/*Un map es una colección de elementos que se pueden acceder a mediante el operador de acceso de objetos.*/
var miMap = new Map();
miMap.set("nombre", "Juan");
miMap.set("edad", 25);
miMap.set("apellido", "Perez"); //Agrega un elemento a miMap
console.log(miMap); //Map { "nombre" => "Juan", "edad" => 25, "apellido" => "Perez" }
console.log(miMap.get("nombre")); //"Juan"
console.log(miMap.get("apellido")); //"Perez"
console.log(miMap.has("nombre")); //true
console.log(miMap.has("apellido")); //true  
console.log(miMap.delete("apellido")); //true
console.log(miMap); //Map { "nombre" => "Juan", "edad" => 25 }

/* ************************************** EJERCICIO EXTRA ************************************** */
// Importar la librería readline-sync para leer la entrada del usuario desde la terminal
// Crea una agenda de contactos por terminal
const readline = require("readline");

function agregarContacto(nombre, telefono) {
    if (!/^\d{1,11}$/.test(telefono)) {
        console.log("El número de teléfono debe ser numérico y no tener más de 11 dígitos.");
        return;
    }
    miAgenda.set(nombre, telefono);
    console.log("Contacto agregado.");
}

function buscarContacto(nombre) {
    if (miAgenda.has(nombre)) {
        console.log("El contacto de " + nombre + " es " + miAgenda.get(nombre));
    } else {
        console.log("No existe un contacto con el nombre " + nombre);
    }
}

function actualizarContacto(nombre, telefono) {
    if (miAgenda.has(nombre)) {
        miAgenda.set(nombre, telefono);
        console.log("El contacto " + nombre + " ha sido actualizado");
    } else {
        console.log("No existe un contacto con el nombre " + nombre);
    }
}

function eliminarContacto(nombre) {
    if (miAgenda.has(nombre)) {
        miAgenda.delete(nombre);
        console.log("El contacto " + nombre + " ha sido eliminado");
    } else {
        console.log("No existe un contacto con el nombre " + nombre);
    }
}

function mostrarAgenda() {
    console.log("La agenda de contactos es:");
    miAgenda.forEach((nombre, telefono) => {
        console.log(nombre + " - " + telefono);
    });
}

function menuAgenda() {
    console.log("\nBienvenido al sistema de agenda de contactos");
    console.log("1. Agregar un contacto");
    console.log("2. Buscar un contacto");
    console.log("3. Actualizar un contacto");
    console.log("4. Eliminar un contacto");
    console.log("5. Mostrar la agenda");
    console.log("6. Salir");
}

async function preguntar(question) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    return new Promise(resolve => rl.question(question, ans => {
        rl.close();
        resolve(ans);
    }));
}

async function main() {
    miAgenda = new Map();
    let salir = false;

    while (!salir) {
        menuAgenda();
        const opcion = await preguntar("Introduzca la opción: ");
        
        switch (opcion) {
            case "1":
                const nombreAgregar = await preguntar("Introduzca el nombre del contacto: ");
                const telefonoAgregar = await preguntar("Introduzca el número de teléfono: ");
                agregarContacto(nombreAgregar, telefonoAgregar);
                break;
            case "2":
                const nombreBuscar = await preguntar("Introduzca el nombre del contacto: ");
                buscarContacto(nombreBuscar);
                break;
            case "3":
                const nombreActualizar = await preguntar("Introduzca el nombre del contacto: ");
                const telefonoActualizar = await preguntar("Introduzca el número de teléfono: ");
                actualizarContacto(nombreActualizar, telefonoActualizar);
                break;
            case "4":
                const nombreEliminar = await preguntar("Introduzca el nombre del contacto: ");
                eliminarContacto(nombreEliminar);
                break;
            case "5":
                mostrarAgenda();
                break;
            case "6":
                console.log("Saliendo del sistema");
                salir = true;
                break;
            default:
                console.log("Opción inválida");
                break;
        }
    }
}

main();
