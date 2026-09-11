//Estructuras de datos

//Arrays

//Añadir elementos

const frutas = ["manzana", "pera"];

// Al final
frutas.push("uva");         // ["manzana", "pera", "uva"]

// Al inicio
frutas.unshift("fresa");    // ["fresa", "manzana", "pera", "uva"]

// En una posición específica (splice)
frutas.splice(2, 0, "kiwi"); // En índice 2, borrar 0, insertar "kiwi"
// ["fresa", "manzana", "kiwi", "pera", "uva"]

//Eliminar elementos
const numeros = [10, 20, 30, 40, 50];

// Del final
numeros.pop();              // Elimina 50 → [10, 20, 30, 40]

// Del inicio
numeros.shift();            // Elimina 10 → [20, 30, 40]

// En una posición específica (splice)
numeros.splice(1, 2);       // Desde índice 1, elimina 2 elementos
// Elimina 30 y 40 → [20]

// Por valor (usando indexOf + splice)
const colores = ["rojo", "azul", "verde", "azul"];
const indice = colores.indexOf("azul"); // Encuentra el primero
colores.splice(indice, 1);             // Elimina ese → ["rojo", "verde", "azul"]

// Filtrando (crea nuevo array sin el elemento)
const sinVerde = colores.filter(color => color !== "verde");
// ["rojo", "azul"]

//Actualizar elementos
const animales = ["perro", "gato", "conejo"];

// Por índice
animales[1] = "hamster";    // ["perro", "hamster", "conejo"]

// Con map (crea nuevo array transformado)
const enMayusculas = animales.map(animal => animal.toUpperCase());
// ["PERRO", "HAMSTER", "CONEJO"]

//ordenacion
// sort() - Ordena alfabéticamente (por defecto)
const letras = ["c", "a", "b", "d"];
letras.sort();              // ["a", "b", "c", "d"]

// ⚠️ Cuidado con números (los trata como strings)
const numeros2 = [100, 25, 3, 1];
numeros2.sort();            // [1, 100, 25, 3] ❌ (orden lexicográfico)

// Para números, hay que pasar una función de comparación
numeros2.sort((a, b) => a - b);  // [1, 3, 25, 100] ✅ ascendente
numeros2.sort((a, b) => b - a);  // [100, 25, 3, 1] ✅ descendente

// reverse() - Invierte el orden
letras.reverse();           // ["d", "c", "b", "a"]

//Objetos
const persona = {
    nombre: "Ana",
    edad: 25,
    ciudad: "Bogotá"
};

// Inserción (añadir nueva propiedad)
persona.telefono = "3001234567";
persona["email"] = "ana@email.com";

// Borrado
delete persona.ciudad;

// Actualización
persona.edad = 26;
persona["nombre"] = "Ana María";

// Listar claves, valores y entradas
console.log(Object.keys(persona));    // ["nombre", "edad", "telefono", "email"]
console.log(Object.values(persona));  // ["Ana María", 26, "3001234567", "ana@email.com"]
console.log(Object.entries(persona)); // [["nombre","Ana María"], ["edad",26], ...]

//Sets
const numerosSet = new Set();

// Inserción
numerosSet.add(1);
numerosSet.add(2);
numerosSet.add(3);
numerosSet.add(2);  // No se añade (duplicado)
console.log(numerosSet); // Set(3) {1, 2, 3}

// Borrado
numerosSet.delete(2);
console.log(numerosSet); // Set(2) {1, 3}

// Verificar existencia
console.log(numerosSet.has(3)); // true

// Tamaño
console.log(numerosSet.size); // 2

// Recorrer
numerosSet.forEach(num => console.log(num));

// Los Sets no tienen actualización directa (borras y añades)
// ni ordenación (no tiene sentido, no son indexados)

//Maps
const agendaMap = new Map();

// Inserción
agendaMap.set("Ana", "3001234567");
agendaMap.set("Carlos", "3109876543");
agendaMap.set("Beatriz", "3205554433");

// Borrado
agendaMap.delete("Carlos");

// Actualización (sobrescribir con set)
agendaMap.set("Ana", "3009999999"); // Cambia el número de Ana

// Búsqueda
console.log(agendaMap.get("Beatriz")); // "3205554433"
console.log(agendaMap.has("Carlos"));  // false

// Tamaño
console.log(agendaMap.size); // 2

// Recorrer
agendaMap.forEach((telefono, nombre) => {
    console.log(nombre + ": " + telefono);
});

//Dificultad extra
const contactos = new Map();
contactos.set("Juan", "3001234567");
function menu() {
    console.log("--- AGENDA DE CONTACTOS ---");
    console.log("1. Ver lista de contactos");
    console.log("2. Buscar un contacto");
    console.log("3. Añadir un contacto");
    console.log("4. Actualizar un contacto");
    console.log("5. Eliminar un contacto");
    console.log("6. Salir de la agenda");
}
function listarContactos() {
    if (contactos.size === 0) {
        console.log("La agenda está vacía.");
        return;
    }
    console.log("\n--- LISTA DE CONTACTOS ---");
    contactos.forEach((telefono, nombre) => {
        console.log(nombre + ": " + telefono);
    });
}
function busquedaContacto(){
    busqueda = prompt("Ingresa el nombre del contacto que deseas buscar: ");
    if(contactos.has(busqueda)){
        console.log("Teléfono de " + busqueda + ": " + contactos.get(busqueda));
    }
    else{
        console.log("Contacto no encontrado")
    }
}

function añadirContacto(){
    const nuevoNombre = prompt("Ingresa el nombre del nuevo contacto: ")
    // Verificar si ya existe
    if (contactos.has(nuevoNombre)) {
        console.log("Ya existe un contacto con ese nombre. Usa la opción 4 para actualizarlo.");
        return;
    }
    const nuevoTelefono = prompt("Ingresa el telefono del nuevo contacto: ")
    if(isNaN(entrada) || nuevoTelefono.length > 11 || nuevoTelefono == ""){
        console.log("El telefono no puede ser un caracter, ni ser mayor a 11 digitos")
    }
    else {
        contactos.set(nuevoNombre, nuevoTelefono);
    }
}
//Apoyo de IA para la creación de esta funcion
function actualizarContacto() {
    const nombreBuscado = prompt("Ingresa el nombre del contacto a actualizar: ");
    
    if (!contactos.has(nombreBuscado)) {
        console.log("Contacto '" + nombreBuscado + "' no encontrado.");
        return;
    }
    
    // Preguntar si quiere cambiar el nombre o solo el teléfono
    const opcion = prompt("¿Deseas cambiar el nombre? (s/n): ").toLowerCase();
    
    let nuevoNombre = nombreBuscado;
    if (opcion === "s" || opcion === "si") {
        nuevoNombre = prompt("Ingresa el nuevo nombre: ");
    }
    
    const nuevoTelefono = prompt("Ingresa el nuevo teléfono para " + nuevoNombre + ": ");
    
    // Validación del teléfono
    if (isNaN(nuevoTelefono) || nuevoTelefono.length > 11 || nuevoTelefono === "") {
        console.log("Error: El teléfono debe ser numérico y tener máximo 11 dígitos.");
        return;
    }
    
    // Si cambió el nombre, eliminar el viejo y crear el nuevo
    if (nuevoNombre !== nombreBuscado) {
        contactos.delete(nombreBuscado);
    }
    
    contactos.set(nuevoNombre, nuevoTelefono);
    console.log("Contacto actualizado con éxito.");
}

function eliminacionContacto(){
        eliminar = prompt("Ingrese el nombre del contacto que desea eliminar: ")
        if(contactos.has(eliminar)){
            contactos.delete(eliminar);
        }
        else {
            console.log("contacto no encontrado")
        }       
    }

let ejecutando = true;

while (ejecutando) {
    menu();
    const entrada = prompt("Ingrese un número según la operación que desea realizar: ");
    const opcion = parseInt(entrada);
    
    // Validar entrada
    if (isNaN(opcion)) {
        console.log("Error: Debe ingresar un número válido del 1 al 6.");
        continue; // Vuelve al inicio del bucle
    }    
    switch (opcion) {
        case 1:
            listarContactos();
            break;
        case 2:
            busquedaContacto();
            break;
        case 3:
            añadirContacto();
            break;
        case 4:
            actualizarContacto();
            break;
        case 5:
            eliminacionContacto();
            break;
        case 6:
            console.log("¡Hasta luego! Cerrando agenda...");
            ejecutando = false; // Termina el bucle
            break;
        default:
            console.log("Opción no válida. Ingrese un número del 1 al 6.");
    }
}