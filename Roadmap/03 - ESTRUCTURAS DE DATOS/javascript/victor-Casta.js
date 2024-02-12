/*
  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
*/

//Array: Coleccion ordenada de elemento
const arrayExample = [1, 2, 3, 4, 5];

//Objects: Colecciones de pares clave-valor
const objectExample = {
  name: "John",
  age: 30,
}

//sets: Estructuras que no permiten valores repetidos
let miSet = new Set([1, 2, 3, 4, 5]);

//maps: Estructuras clave-valor que pueden tener cualquier tipo de clave y valor
let myMap = new Map();
myMap.set("key1", "value1");
myMap.set({ a: 1, b: 2 }, "value2");

//Arrays Typed: permiten almacenar datos de un tipo específico, como enteros o flotantes.
let miArrayTyped = new Int32Array([1, 2, 3, 4]);

/*
   * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/
const numberList = [1, 2, 3, 4]

//Insertar datos
numberList.push(5); //Insertar datos al final de un array
numberList.unshift(0); //Insertar datos al principio de un array


//Borrar datos
numberList.pop(); //Eliminar el ultimo elemento del array
numberList.shift(); //Eliminar el primer elemento del array


//Actualizacion
numberList[1] = 9; //Modificar un dato en una posición
numberList.splice(3, 0, 7); // Agrega 4 en la posición 3


//Ordenación
numberList.sort((a, b) => a - b); // Ordenamiento ascendente

numberList.reverse(); // Cambia el sentido de los elementos (ascendente a descendente)
const { log } = require('console');
// guardarDato.js

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const contacts = [];

function searchContact(callback) {
  rl.question('Ingrese el Nombre del contacto: ', (dato) => {
    let searchedData = contacts.find(objeto => objeto.name === dato);
    if (searchedData) {
      console.log(`Nombre: ${searchedData.name} Telefono: ${searchedData.phone}`);
    } else {
      console.log('Contacto no encontrado');
    }
    if (callback) {
      callback(searchedData);
    }
  });
}

function realizarOperacion() {
  rl.question('Seleccione un numero: 1.Buscar, 2.Insertar, 3.Actualizar, 4.Borrar, 5.Salir: ', (data) => {
    const userData = data;
    switch (userData) {
      case '1':
        searchContact(() => {
          realizarOperacion();
        });
        break;
      case '2':
        let contactsItem = {};
        rl.question('nombre: ', (name) => {
          contactsItem['name'] = name;
          rl.question('telefono: ', (phone) => {
            contactsItem['phone'] = phone;
            if (!isNaN(phone) && phone.length >= 10) {
              contacts.push(contactsItem);
              console.log(`Datos Ingresados: ${contactsItem.name} ${contactsItem.phone}`);
            } else {
              console.log('Por favor ingrese un telefono de 10 caracteres (Incluya código de verificación)');
            }
            realizarOperacion();
          });
        });
        break;
      case '3':
        searchContact((searchedData) => {
          if (searchedData) {
            rl.question(`Ingrese el nuevo nombre para ${searchedData.name}: `, (newName) => {
              rl.question(`Ingrese el nuevo teléfono para ${searchedData.name}: `, (newPhone) => {
                searchedData.name = newName;
                searchedData.phone = newPhone;
                console.log(`Contacto actualizado: ${searchedData.name} ${searchedData.phone}`);
                realizarOperacion();
              });
            });
          } else {
            realizarOperacion();
          }
        });
        break;
      case '4':
        if (contacts.length > 0) {
          rl.question('Ingrese el nombre del contacto que desea eliminar: ', (contactDelete) => {
            let position = contacts.findIndex(objeto => objeto.name === contactDelete)
            if (position !== -1) {
              contacts.splice(position, 1);
              console.log(`Se ha eliminado al contacto: ${contactDelete}`);
            } else {
              console.log("No se encontró a este usuario");
            }
            realizarOperacion();  
          });
        } else {
          console.log("No hay contactos registrados");
          realizarOperacion(); 
        }
        break;
      case '5':
        console.log('Saliendo del programa');
        rl.close();
        break;
      default:
        console.log(`Ups! No se ha seleccionado correctamente`);
        realizarOperacion();
    }
  });
}

// Iniciar el programa
realizarOperacion();
