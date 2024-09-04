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

// Creación de estructuras de datos en JavaScript
// Array
const array = [1, 2, 3, 4, 5];
console.log(array);

// Operaciones de inserción
array.push(6);
console.log(array);

// Operaciones de borrado
array.pop();
console.log(array);

// Operaciones de actualización
array[0] = 0;
console.log(array);

// Operaciones de ordenación
array.sort();
console.log(array);

// Object
const object = {
  name: 'Elianis',
  age: 25,
  country: 'Colombia'
};
console.log(object);

// Operaciones de inserción
object.email = '';
console.log(object);



// Creación de una agenda de contactos
const contacts = [];

function addContact(name, phone) {
  contacts.push({ name, phone });

  console.log('Contact added successfully');

}

function searchContact(name) {
  const contact = contacts.find(contact => contact.name === name);

  if (contact) {
    console.log(contact);
  } else {
    console.log('Contact not found');
  }
}

function updateContact(name, phone) {
  const contact = contacts.find(contact => contact.name === name);

  if (contact) {
    contact.phone = phone;
    console.log('Contact updated successfully');
  } else {
    console.log('Contact not found');
  }
}

function deleteContact(name) {
  const index = contacts.findIndex(contact => contact.name === name);

  if (index !== -1) {
    contacts.splice(index, 1);
    console.log('Contact deleted successfully');
  } else {
    console.log('Contact not found');
  }
}

function isPhoneNumber(phone) {
  return /^\d{11}$/.test(phone);
}

function main() {
  let option;

  do {
    console.log('1. Add contact');
    console.log('2. Search contact');
    console.log('3. Update contact');
    console.log('4. Delete contact');
    console.log('5. Exit');

    option = prompt('Choose an option: ');

    switch (option) {
      case '1':
        const name = prompt('Enter the name: ');
        let phone;

        do {
          phone = prompt('Enter the phone number: ');
        } while (!isPhoneNumber(phone));

        addContact(name, phone);
        break;
      case '2':
        const search = prompt('Enter the name to search: ');
        searchContact(search);
        break;
      case '3':
        const update = prompt('Enter the name to update: ');
        let newPhone;

        do {
          newPhone = prompt('Enter the new phone number: ');
        } while (!isPhoneNumber(newPhone));

        updateContact(update, newPhone);
        break;
      case '4':
        const del = prompt('Enter the name to delete: ');
        deleteContact(del);
        break;
      case '5':
        console.log('Goodbye!');
        break;
      default:
        console.log('Invalid option');
        break;
    }
  } while (option !== '5');
}

main();

