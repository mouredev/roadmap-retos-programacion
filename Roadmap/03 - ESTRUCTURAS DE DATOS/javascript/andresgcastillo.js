// Arrays
let miArray = [1, 2, 3, 4, 5];
miArray.push(6); // Inserción
miArray.splice(0, 1); // Borrado
miArray[0] = 7; // Actualización
miArray.sort(); // Ordenación

// Sets
let miSet = new Set([1, 2, 3, 4, 5]);
miSet.add(6); // Inserción
miSet.delete(1); // Borrado
// Los Sets no soportan la actualización de un elemento específico o la ordenación debido a su naturaleza

// Objects
let miObjeto = {uno: 1, dos: 2, tres: 3};
miObjeto["cuatro"] = 4; // Inserción
delete miObjeto["uno"]; // Borrado
miObjeto["dos"] = 22; // Actualización
// Los Objects no soportan la ordenación debido a su naturaleza

// Maps
let miMapa = new Map([
  ["uno", 1],
  ["dos", 2],
  ["tres", 3],
]);
miMapa.set("cuatro", 4); // Inserción
miMapa.delete("uno"); // Borrado
miMapa.set("dos", 22); // Actualización
// Los Maps no soportan la ordenación debido a su naturaleza

//Dificultad Extra
//se ejecuta con node.js

const readline = require("readline");

let contactos = {};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function iniciarPrograma() {
  rl.question("¿Qué operación quieres realizar? (buscar, insertar, actualizar, eliminar, salir): ", (operacion) => {
    switch (operacion) {
      case "buscar":
        buscarContacto();
        break;
      case "insertar":
        insertarContacto();
        break;
      case "actualizar":
        actualizarContacto();
        break;
      case "eliminar":
        eliminarContacto();
        break;
      case "salir":
        rl.close();
        break;
      default:
        console.log("Operación no reconocida.");
        iniciarPrograma();
    }
  });
}

function buscarContacto() {
  rl.question("Introduce el nombre del contacto que quieres buscar: ", (nombre) => {
    if (contactos[nombre]) {
      console.log(`Nombre: ${nombre}, Teléfono: ${contactos[nombre]}`);
    } else {
      console.log("Contacto no encontrado.");
    }
    iniciarPrograma();
  });
}

function insertarContacto() {
  rl.question("Introduce el nombre del nuevo contacto: ", (nombre) => {
    rl.question("Introduce el número de teléfono del nuevo contacto: ", (telefono) => {
      if (validarTelefono(telefono)) {
        contactos[nombre] = telefono;
        console.log("Contacto insertado correctamente.");
      } else {
        console.log("Número de teléfono no válido.");
      }
      iniciarPrograma();
    });
  });
}

function actualizarContacto() {
  rl.question("Introduce el nombre del contacto que quieres actualizar: ", (nombre) => {
    if (contactos[nombre]) {
      rl.question("Introduce el nuevo número de teléfono: ", (telefono) => {
        if (validarTelefono(telefono)) {
          contactos[nombre] = telefono;
          console.log("Contacto actualizado correctamente.");
        } else {
          console.log("Número de teléfono no válido.");
        }
      });
    } else {
      console.log("Contacto no encontrado.");
    }
    iniciarPrograma();
  });
}

function eliminarContacto() {
  rl.question("Introduce el nombre del contacto que quieres eliminar: ", (nombre) => {
    if (contactos[nombre]) {
      delete contactos[nombre];
      console.log("Contacto eliminado correctamente.");
    } else {
      console.log("Contacto no encontrado.");
    }
    iniciarPrograma();
  });
}

function validarTelefono(telefono) {
  const regex = /^\d{1,11}$/;
  return regex.test(telefono);
}

iniciarPrograma();
