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

// +++++++++ ARRAY +++++++++
var colores = ["Blanco", "Azul", "Naranja"];

colores.push("Verde"); // Añade un elemento al final.
colores.splice(2, 1); // Elimina el elemento en el índice 2.
colores[2] = "Rojo"; // Actualiza el elemento en el índice 2.
colores.sort(); // Ordena los elementos alfabéticamente.
console.log(colores);

// +++++++++ OBJECT +++++++++
var bountyHunter = {
  name: "-",
  height: "1.9m",
  specie: "Human",
}

bountyHunter.lastName = "Aran"; // Añade un nuevo elemento.
delete bountyHunter.specie; // Elimina una propiedad.
bountyHunter.name = "Samus"; // Modifica el valor de una propiedad existente.
Object.keys(bountyHunter).sort(); // Ordena las propiedad alfabéticamente, pero convierte el objeto en un arreglo.
console.log(bountyHunter);

// +++++++++ DIFICULTAD EXTRA +++++++++
var menu = "Por favor, ingrese el número de la opción que desea ejecutar:\n1) Agregar.\n2) Actualizar.\n3) Eliminar.\n4) Buscar.\n5) Salir."
var selectedOption = 0;
var directory = [];

function addContact() {
  var name = prompt("Por favor, ingrese el nombre del contacto:");
  var newContact = {Nombre: name};
  var stringPhone = prompt("Por favor, ingrese el teléfono del contacto con 10 dígitos:");
  var phoneNumber = parseInt(stringPhone, 10);

  if (/^[0-9.,]+$/.test(phoneNumber) && stringPhone.length === 10) {
    newContact.Telefono = phoneNumber;
    directory.push(newContact);
  } else {
    alert("Debe ingresar un número de teléfono conformado por 10 dígitos.");
  }
}

function updateContact() {
  var name = prompt("Por favor, ingrese el nombre del contacto a actualizar:");

  function searchContact(contact) {
    return contact.Nombre === name;
  }

  var results = directory.find(searchContact);
  var newName = prompt("Por favor, ingrese el nombre nuevo:");
  
  var stringnewPhone = prompt("Por favor, ingrese el teléfono nuevo con 10 dígitos:");
  var newPhoneNumber = parseInt(stringnewPhone, 10);

  if (/^[0-9.,]+$/.test(newPhoneNumber) && stringnewPhone.length === 10) {
    results.Nombre = newName;
    results.Telefono = newPhoneNumber;
  } else {
    alert("Debe ingresar un número de teléfono conformado por 10 dígitos.");
  }
}

function deleteContact() {
  var name = prompt("Por favor, ingrese el nombre del contacto que desea eliminar:");

  function searchContact(contact) {
    return contact.Nombre === name;
  }

  var results = directory.findIndex(searchContact);

  if (results >= 0) {
    directory.splice(results, 1);
  } else {
    alert("El contacto no pudo ser eliminado porque no existe.");
  }
}

function searchContact() {
  var name = prompt("Por favor, ingrese el nombre del contacto que desea buscar:");

  function searchContact(contact) {
    return contact.Nombre === name;
  }

  var results = directory.find(searchContact);

  if (results === undefined) {
    alert("El contacto no existe.");
  } else {
    alert("Nombre: " + results.Nombre + "\n" + "Teléfono: " + results.Telefono);
  }
}

do {
  selectedOption = parseInt(prompt(menu), 10);

  switch (selectedOption) {
    case 1:
      addContact();
      break;

    case 2:
      updateContact();
      break;

    case 3:
      deleteContact();
      break;

    case 4:
      searchContact();
      break;

    case 5:
      alert("Cerrando la agenda.");
      break;

    default:
      alert("Por favor, introduzca una opción del 1 al 5.");
      break;
  }
} while (selectedOption !== 5);
