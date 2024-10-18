//Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
// Arreglo
const array = [1, 2, 3, 4, 5];
console.log(array);

// Objeto
let persona = {
  nombre: "Juan",
  apellido: "Perez",
};

const { nombre, apellido } = persona;
console.log(nombre);
console.log(apellido);

// Set
let set = new Set([1, 2, 3, 4, 5]);
console.log(set);

// Map
let map = new Map();
map.set("nombre", "juan");
map.set("apellido", "Perez");
console.log(map);

// WeakSet
let mascota1 = { nombre: "Max" };
let mascota2 = { nombre: "Bruno" };
let weakSet = new WeakSet([mascota1, mascota2]);
console.log(weakSet);

// WeakMap
let weakMap = new WeakMap();
let obj = { id: 1 };
weakMap.set(obj, "Valor asociado");
console.log(weakMap);

// String
let cadenaDeTexto = "Hola JavaScript";

// Number
let vuelto = 2000;

// Boolean
let tieneTelefono = true;

// Funcion
function caminar() {
  console.log("caminando");
}
caminar();

//  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

// Arreglos
const tareas = ["entrenar", "trabajar", "estudiar", "descansar"];
console.log(tareas);

// Arreglos inserción
tareas[4] = "meditar";
console.log(tareas);

const leer = "leer";
tareas.push(leer);

console.log(tareas);
const socializar = "socializar";

tareas.unshift(socializar);
console.log(tareas);

// Arreglos borrado
tareas.shift();
console.log(tareas);

tareas.pop();
console.log(tareas);

let pos = 1;
let elementoEliminado = tareas.splice(pos, 1);
console.log(elementoEliminado);
console.log(tareas);

// Arreglos actualización
tareas[1] = "programar";
console.log(tareas);

// Arreglos ordenación
tareas.sort();
console.log(tareas);

//  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

// Objetos
const automovil = {
  marca: "Toyota",
  modelo: "rav4",
  tipo: "SUV",
};

console.log(automovil);

// Objetos inserción
automovil.motor = 2000;
console.log(automovil);

// Objetos borrado
delete automovil.motor;
console.log(automovil);

// Objetos actualización
automovil.modelo = "4Runner";
console.log(automovil);

/*
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

const contactos = [
  { nombre: "Juan", telefono: "12345678" },
  { nombre: "María", telefono: "87654321" },
  { nombre: "Lupe", telefono: "87654321" },
];

//console.log(typeof contactos);

function mostrarMenu() {
  process.stdout.write("1. Crear un usuario\n");
  process.stdout.write("2. Buscar un usuario\n");
  process.stdout.write("3. Actualizar un usuario\n");
  process.stdout.write("4. Eliminar un usuario\n");
  process.stdout.write("5. Salir\n");
  process.stdout.write("Selecciona una opción:\n");
}

mostrarMenu();

process.stdin.on("data", function (data) {
  const exp = data.toString().trim();
  console.log(exp);

  switch (exp) {
    // Crear un contacto
    case "1":
      process.stdout.write("Ingresa el nombre del contacto: \n");
      process.stdin.once("data", function (nombreData) {
        const nuevoNombre = nombreData.toString().trim();

        process.stdout.write("Ingresa el número de teléfono: \n");
        process.stdin.once("data", function (telefonoData) {
          const nuevoTelefono = telefonoData.toString().trim();

          if (
            !isNaN(nuevoTelefono) &&
            nuevoTelefono !== "" &&
            nuevoTelefono.length <= 11
          ) {
            const nuevoContacto = {
              nombre: nuevoNombre,
              telefono: nuevoTelefono,
            };
            contactos.push(nuevoContacto);
            console.log(
              `Nuevo contacto ${nuevoContacto.nombre} agregado exitósamente.\n`
            );
            console.log(contactos);
            mostrarMenu();
          } else {
            console.log(
              "El número de teléfono debe tener 11 dígitos o menos y solo contener números."
            );
          }
        });
      });
      break;
    // Buscar un contacto
    case "2":
      process.stdout.write("Ingresa el nombre del contacto a buscar: ");
      process.stdin.once("data", function (nombreContacto) {
        const buscarContacto = nombreContacto.toString().trim();
        const contactoEncontrado = contactos.find(
          (contacto) => contacto.nombre == buscarContacto
        );
        if (contactoEncontrado) {
          console.log("Contacto encontrado", contactoEncontrado);
        } else {
          console.log("Contacto no encontrado");
        }
      });
      break;
    // Actualizar un contacto
    case "3":
      process.stdout.write(
        "Ingresa el nombre del contacto que deseas actualizar: "
      );
      process.stdin.once("data", function (nombreContacto) {
        const buscarContacto = nombreContacto.toString().trim();
        const contactoEncontrado = contactos.find(
          (contacto) => contacto.nombre == buscarContacto
        );
        if (contactoEncontrado) {
          process.stdout.write("Ingresa el nuevo nombre: ");
          process.stdin.once("data", function (nombreContacto) {
            const nuevoNombreContacto = nombreContacto.toString().trim();
            contactoEncontrado.nombre = nuevoNombreContacto;
            console.log(contactos);
            process.stdout.write("Ingresa el nuevo número de teléfono: ");
            process.stdin.once("data", function (numeroContacto) {
              const nuevoNumeroContacto = numeroContacto.toString().trim();

              if (
                !isNaN(nuevoNumeroContacto) &&
                nuevoNumeroContacto !== "" &&
                nuevoNumeroContacto.length <= 11
              ) {
                contactoEncontrado.telefono = nuevoNumeroContacto;
                console.log(contactos);
                mostrarMenu();
              } else {
                console.log(
                  "El número de teléfono debe tener 11 dígitos o menos y solo contener números."
                );
              }
            });
          });
        } else {
          console.log("Contacto no encontrado");
        }
      });
      break;
    // Eliminar un contacto
    case "4":
      process.stdout.write(
        "Ingresa el nombre del contacto que deseas eliminar: "
      );
      process.stdin.once("data", function (nombreContacto) {
        const nombreContactoAEliminar = nombreContacto.toString().trim();
        const indice = contactos.findIndex(
          (contacto) => contacto.nombre == nombreContactoAEliminar
        );
        if (indice !== -1) {
          contactos.splice(indice, 1);
          console.log(`Contacto ${nombreContactoAEliminar} eliminado`);
          console.log(contactos);
          mostrarMenu();
        } else {
          console.log("Contacto no encontrado");
        }
      });
      break;
    // Salir
    case "5":
      process.stdout.write("Gracias por visitarnos.\n");
      process.exit();
      break;
    default:
      process.stdout.write(
        "Opción no válida. Selecciona una opción correcta.\n"
      );
      mostrarMenu();
  }
});
