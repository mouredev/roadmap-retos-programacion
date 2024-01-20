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

/***ESTRUCTURAS DE DATOS EN JS - PT1***/

//Arrays

let arrayStructure = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arrayStructure.push(10); //Inserción
arrayStructure.splice(7, 1); //Borrado
arrayStructure.pop(); //Borrado - Elimina el útlimo elemento del array
arrayStructure.shift(); //Borrado - Elimina el primer elemento del array
arrayStructure[6] = 8; //Actualización
let index = arrayStructure.findIndex((element) => element === 6); //Busqueda
arrayStructure = arrayStructure.sort((a, b) => b - a); //Ordenación

//Sets

let setStructure = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]); //Representan un conjunto de elementos
setStructure.add(10); //Inserción
setStructure.delete(1); //Borrado
setStructure.has(3); //Busqueda - En este caso particular retorna un boolean de valor true
setStructure.clear(); //Borrado - Elimina todos los elementos

//Los sets no tienen update o sort

//Maps - Es una colección de pares clave-valor

let mapStructure = new Map([
  ["uno", 1],
  ["dos", 2],
  ["tres", 3],
  ["cuatro", 4],
  ["cinco", 8],
]);

mapStructure.set("seis", 6); //Inserción
mapStructure.delete("seis"); //Borrado
mapStructure.get("cinco"); //Busqueda
mapStructure.set("cinco", 5); //Actualización
mapStructure.clear(); //Borrado - Elimina todos los elementos

//Objects

let objectStructure = {
  nombre: "Carmen",
  apellido: "Pérez",
  edad: 25,
  dni: 12345678,
  fechaNacimiento: "01/01/2000",
};

objectStructure["Ciudad"] = "Madrid"; //Inserción
delete objectStructure["Ciudad"]; //Borrado
objectStructure["edad"] = 26; //Actualización
let edad = objectStructure["edad"]; //Busqueda

/***ESTRUCTURAS DE DATOS EN JS - PT2***/
/**ACTIVIDAD EXTRA**/

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contactos = [];

function mostrarMenu() {
  console.log("\nAgenda de Contactos\n");
  console.log("1. Mostrar Contactos");
  console.log("2. Buscar Contacto");
  console.log("3. Agregar Contacto");
  console.log("4. Actualizar Contacto");
  console.log("5. Eliminar Contacto");
  console.log("6. Salir\n");
}

function mostrarContactos() {
  console.log("\nLista de Contactos:");
  contactos.forEach((contacto) =>
    console.log(`${contacto.nombre}: ${contacto.telefono}`)
  );
  volverAlMenu();
}

function buscarContacto(nombre) {
  const contactoEncontrado = contactos.find(
    (contacto) => contacto.nombre === nombre
  );
  if (contactoEncontrado) {
    console.log(
      `\n${contactoEncontrado.nombre}: ${contactoEncontrado.telefono}`
    );
  } else {
    console.log(`\nContacto "${nombre}" no encontrado.`);
  }
  volverAlMenu();
}

function agregarContacto(nombre, telefono) {
  contactos.push({ nombre, telefono });
  console.log(`\nContacto ${nombre} agregado.`);
  volverAlMenu();
}

function actualizarContacto(nombre, nuevoTelefono) {
  const contactoIndex = contactos.findIndex(
    (contacto) => contacto.nombre === nombre
  );
  if (contactoIndex !== -1) {
    contactos[contactoIndex].telefono = nuevoTelefono;
    console.log(`\nContacto ${nombre} actualizado.`);
  } else {
    console.log(`\nContacto "${nombre}" no encontrado.`);
  }
  volverAlMenu();
}

function eliminarContacto(nombre) {
  contactos = contactos.filter((contacto) => contacto.nombre !== nombre);
  console.log(`\nContacto ${nombre} eliminado.`);
  volverAlMenu();
}

function validarTelefono(telefono) {
  return /^\d{1,11}$/.test(telefono);
}

function volverAlMenu() {
  setTimeout(() => {
    mostrarMenu();
    rl.question("Seleccione una opción (1-6): ", (opcion) => {
      ejecutarOperacion(opcion);
    });
  }, 1000);
}

function ejecutarOperacion(opcion) {
  switch (opcion) {
    case "1":
      mostrarContactos();
      break;
    case "2":
      rl.question("Nombre del contacto a buscar: ", (nombre) =>
        buscarContacto(nombre)
      );
      break;
    case "3":
      rl.question("Nombre del contacto: ", (nombre) => {
        rl.question("Número de teléfono: ", (telefono) => {
          if (validarTelefono(telefono)) {
            agregarContacto(nombre, telefono);
          } else {
            console.log("Número de teléfono no válido.");
            volverAlMenu();
          }
        });
      });
      break;
    case "4":
      rl.question("Nombre del contacto a actualizar: ", (nombre) => {
        rl.question("Nuevo número de teléfono: ", (nuevoTelefono) => {
          if (validarTelefono(nuevoTelefono)) {
            actualizarContacto(nombre, nuevoTelefono);
          } else {
            console.log("Número de teléfono no válido.");
          }
        });
      });
      break;
    case "5":
      rl.question("Nombre del contacto a eliminar: ", (nombre) =>
        eliminarContacto(nombre)
      );
      break;
    case "6":
      console.log("Saliendo del programa.");
      rl.close();
      break;
    default:
      console.log("Opción no válida.");
      volverAlMenu();
  }
}

function iniciarPrograma() {
  mostrarMenu();
  rl.question("Seleccione una opción (1-6): ", (opcion) => {
    ejecutarOperacion(opcion);
  });
}

iniciarPrograma();
