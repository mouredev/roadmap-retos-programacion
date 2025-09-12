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

// Array
let array = [1, "Hola", [1, "Azul"], 4, true];
console.log(array);
console.log(array[2][0]);

// Object
let object = {
  name: "Cristian",
  surname: "Gómez",
  age: 21,
};
console.log(object);

// Map
var map = new Map();
map.set("name", "Cristian");
map.set("surname", "Gómez");
map.set("age", 21);
console.log(map);

// Set
var set = new Set();
set.add(1);
set.add(2);
console.log(set);

// Utiliza operaciones de inserción, borrado, actualización y ordenación.

// Inserción
array.push("Adiós");
console.log(array);

object["city"] = "Neiva";
console.log(object);

map.set("city", "Neiva");
console.log(map);

set.add(3);
console.log(set);

// Borrado
array.pop();
console.log(array);

delete object.city;
console.log(object);

map.delete("city");
console.log(map);

set.delete(3);
console.log(set);

// Actualización
array[0] = 2;
console.log(array);

object.name = "Cristian";
console.log(object);

map.set("name", "Cristian");
console.log(map);

// Ordenación
array.sort();
console.log(array);

// Dificultad extra

class contacto {
  constructor(nombre, numero) {
    this.nombre = nombre;
    this.numero = numero;
  }
}
agenda = [];

salir = false;

while (salir === false) {
  console.log("Menu de opciones");
  console.log("1. Buscar contacto");
  console.log("2. Insertar contacto");
  console.log("3. Actualizar contacto");
  console.log("4. Eliminar contacto");
  console.log("5. Salir");

  let opción = Number(prompt("Ingrese el número de la opción deseada:"));
  let nombre = null;
  let numero = null;

  switch (opción) {
    case 1:
      if (agenda.length === 0) {
        console.log("No hay contactos en la agenda.");
        break;
      }
      nombre = prompt("Ingrese el nombre del contacto:");
      for (let i = 0; i < agenda.length; i++) {
        if (agenda[i].nombre === nombre) {
          console.log(
            "Nombre: " + agenda[i].nombre,
            "Número: " + agenda[i].numero
          );
        } else {
          console.log("El contacto no existe en la agenda.");
        }
      }
      break;
    case 2:
      nombre = prompt("Ingrese el nombre del contacto:");
      for (let i = 0; i < agenda.length; i++) {
        while (agenda[i].nombre === nombre) {
          console.log(
            "El contacto ya existe en la agenda, ingrese otro nombre."
          );
          nombre = prompt("Ingrese el nombre del contacto:");
        }
      }
      numero = prompt("Ingrese el número del contacto:");
      verificarNumero(numero);
      agenda.push(new contacto(nombre, numero));
      break;
    case 3:
      if (agenda.length === 0) {
        console.log("No hay contactos en la agenda.");
        break;
      }
      mostrarContactos();
      let nombreContacto = prompt(
        "Ingrese el nombre del contacto que desea actualizar:"
      );
      for (let i = 0; i < agenda.length; i++) {
        if (agenda[i].nombre === nombreContacto) {
          nombre = prompt("Ingrese el nuevo nombre del contacto:");
          numero = prompt("Ingrese el nuevo número del contacto:");
          verificarNumero(numero);
          agenda[i].nombre = nombre;
          agenda[i].numero = numero;
        }
      }
      mostrarContactos();
      break;
    case 4:
      if (agenda.length === 0) {
        console.log("No hay contactos en la agenda.");
        break;
      }
      mostrarContactos();
      let nombreContactoEliminar = prompt("Ingrese el nombre del contacto:");
      for (let i = 0; i < agenda.length; i++) {
        if (agenda[i].nombre === nombreContactoEliminar) {
          agenda.splice(i, 1);
        }
      }
      mostrarContactos();
      break;
    case 5:
      salir = true;
      break;
  }
  function mostrarContactos() {
    for (let i = 0; i < agenda.length; i++) {
      console.log("Nombre: " + agenda[i].nombre, "Número: " + agenda[i].numero);
    }
  }
  function verificarNumero(numero) {
    while (isNaN(numero) || numero.length <= 10) {
      console.log("El número ingresado no es válido.");
      numero = prompt("Ingrese el número del contacto:");
    }
  }
}
