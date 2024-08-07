//#03 Ejercicio: Estructura de Datos.
// Retos de Programación con MoureDev.
// Creador: César Biliškov.
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
// Desarrollo:

// Ejemplos de estructuras de datos:

let arrayEjemplo = [10, 20, 30, 40, 50]; 
let objetoEjemplo = { nombre: "César Biliškov", edad: 33, ciudad: "ConCon, Valparaiso" };
let setEjemplo = new Set([60, 70, 80, 90, 100]); 

console.log("Array:", arrayEjemplo);
console.log("Objeto:", objetoEjemplo);
console.log("Set:", Array.from(setEjemplo));

arrayEjemplo.push(60); 
console.log("Array después de la inserción:", arrayEjemplo);

objetoEjemplo.edad = 33; 
console.log("Objeto después de la actualización:", objetoEjemplo);

setEjemplo.add(70); 
console.log("Set después de la inserción:", Array.from(setEjemplo));

arrayEjemplo.pop();
console.log("Array después del borrado:", arrayEjemplo);

delete objetoEjemplo.ciudad;
console.log("Objeto después del borrado:", objetoEjemplo);


setEjemplo.delete(60);
console.log("Set después del borrado:", Array.from(setEjemplo));

arrayEjemplo.sort((a, b) => b - a);
console.log("Array después de la ordenación:", arrayEjemplo);

// Dificultad extra de ejercicio:

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let agenda = [
  { nombre: "Aquiles Dpic", telefono: "1212121212" },
  { nombre: "María Jose Radic", telefono: "17771117771" },
  { nombre: "Vicente Novak", telefono: "5555544441" }
];

function mostrarContactos() {
  console.log("Lista de contactos:");
  agenda.forEach((contacto, index) => {
    console.log(`${index + 1}. Nombre: ${contacto.nombre}, Teléfono: ${contacto.telefono}`);
  });
}

function agregarContacto() {
  rl.question("Ingrese el nombre del contacto: ", (nombre) => {
    rl.question("Ingrese el número de teléfono: ", (telefono) => {
      if (/^\d+$/.test(telefono) && telefono.length <= 11) {
        agenda.push({ nombre, telefono });
        console.log("Contacto agregado con éxito.");
        mostrarContactos();
      } else {
        console.log("Número de teléfono no válido.");
      }
      mostrarMenu();
    });
  });
}

function buscarContacto() {
  rl.question("Ingrese el nombre del contacto a buscar: ", (nombre) => {
    const contactoEncontrado = agenda.find(contacto => contacto.nombre.toLowerCase() === nombre.toLowerCase());
    if (contactoEncontrado) {
      console.log(`Contacto encontrado - Nombre: ${contactoEncontrado.nombre}, Teléfono: ${contactoEncontrado.telefono}`);
    } else {
      console.log("Contacto no encontrado.");
    }
    mostrarMenu();
  });
}

function actualizarContacto() {
  rl.question("Ingrese el nombre del contacto a actualizar: ", (nombre) => {
    const indiceContacto = agenda.findIndex(contacto => contacto.nombre.toLowerCase() === nombre.toLowerCase());
    if (indiceContacto !== -1) {
      rl.question("Ingrese el nuevo número de teléfono: ", (nuevoTelefono) => {
        if (/^\d+$/.test(nuevoTelefono) && nuevoTelefono.length <= 11) {
          agenda[indiceContacto].telefono = nuevoTelefono;
          console.log("Contacto actualizado con éxito.");
          mostrarContactos();
        } else {
          console.log("Número de teléfono no válido.");
        }
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
    const indiceContacto = agenda.findIndex(contacto => contacto.nombre.toLowerCase() === nombre.toLowerCase());
    if (indiceContacto !== -1) {
      agenda.splice(indiceContacto, 1);
      console.log("Contacto eliminado con éxito.");
    } else {
      console.log("Contacto no encontrado.");
    }
    mostrarMenu();
  });
}

function mostrarMenu() {
  console.log("\nSeleccione una operación:");
  console.log("1. Mostrar contactos");
  console.log("2. Agregar contacto");
  console.log("3. Buscar contacto");
  console.log("4. Actualizar contacto");
  console.log("5. Eliminar contacto");
  console.log("6. Salir");

  rl.question("Ingrese el número de la operación deseada: ", (opcion) => {
    switch (opcion) {
      case '1':
        mostrarContactos();
        mostrarMenu();
        break;
      case '2':
        agregarContacto();
        break;
      case '3':
        buscarContacto();
        break;
      case '4':
        actualizarContacto();
        break;
      case '5':
        eliminarContacto();
        break;
      case '6':
        rl.close();
        break;
      default:
        console.log("Opción no válida. Intente nuevamente.");
        mostrarMenu();
    }
  });
}

mostrarMenu();

