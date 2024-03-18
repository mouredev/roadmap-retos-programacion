/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/

const { opendirSync } = require("fs");

// #########################
// ### GESTIÓN DE ARRAYS ###
// #########################

// Arrays
let carBrands = ["Mercedez","Ferrari","Peugeot", "Citroën","Wolsvagen", "McLaren","Toyota","Daewoo","Porshe","Rolls-Royce" ]
console.log( "Brand Cards >>> ", carBrands );

//Insertando elementos en el array en la ultima posición del array:
carBrands.push("Malibu");
console.log("Elemento añadido en la ultima posición >>>", carBrands );

// Insertando elemento el en la primera posición del array:
carBrands.unshift("Seat");
console.log("Añadido en primera posición >>> ", carBrands );

// Eliminando elemento del array en la ultima posición:
carBrands.pop();
console.log("Ultimo elemento eliminado >>>", carBrands );

// Eliminando el primer elemento del array:
carBrands.shift();
console.log("Primer elemento eliminado >>>", carBrands );

// Actualizando un elemento especifico del array:
carBrands[1] = "Hummer";
console.log(">>> Elemento [1] actualizado: ", carBrands);
 
// Copiando el array integro
let newCarBrands = carBrands.slice();
console.log( "Copiado: ", newCarBrands );

// Ver longitud de un array:
console.log( "Longitud del array es: ", carBrands.length );

// Ordenamiento de los elementos de un array de forma ascendente:
carBrands.sort();
console.log( "ordenados de la A a la Z: ", carBrands );


// ##########################
// ### GESTIÓN DE OBJETOS ###
// ##########################

// Objeto
let heroe = {
    nombre    : "Iron man",
    poder     : "volar",
    profesion : "Filantropo heroe",
    fuerza    : 5,
}
console.log("Objeto: ", heroe );

// Añadiendo un elemento nuevo al objeto Heroe:
heroe.debilidad = "Martinis";
console.log( " Elemento añadido al objeto >>>", heroe );

// Eliminando un elemento de un objeto:
delete heroe.profesion;
console.log("Eliminando elemento del objeto: >>>", heroe);

// Actualizando elemento de un objeto:
heroe.poder = "Super Fuerza";
console.log( "Poder actualizado: ", heroe );

console.log(" ");
console.log(" ");

console.log("#####################################");
console.log("#####################################");
console.log("#####################################");
console.log(" ");

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
*/

let contacts = [];
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

//Validando el numero de telefono ingresado
const validatePhonenumer = (number) => {
  const format = /^\d{1,11}$/;
  return format.test(number);
};

// Inserción de datos
const insertContact = () => {
  rl.question("Ingresa nombre de contacto: ", (userInput) => {
    let userName = userInput;

    rl.question("Ingresa numero de telefono: ", (userInput) => {
      let numberValidation = validatePhonenumer(userInput);
      if (numberValidation == true) {
        let phoneNumber = userInput;
        contacts.push({ userName, phoneNumber });
        console.log("\n Contacto agregado");
        comenzarPrograma();
      } else {
        console.log("Formato de numero invalido");
        insertContact();
      }
    });
  });
};

// Eliminando contacto
const deleteContact = () => {
  rl.question("DIme que usuario deseas borrar del registro", (userName) => {
    index = findContact(userName);
    if (index != -1) {
      contacts.splice([index], 1);
      console.log("\n Contacto borrado");
    } else {
      console.log(
        "\n No hemos encontrados coincidencias con el dato ingresado",
      );
    }
  });
};

// Actualizando un contacto
const updateContact = () => {
  rl.question("Indique el usuario a actualizar:", (userName) => {
    index = findContact(userName);
    if (index != -1) {
      rl.question("Ingrese el nuevo nombre de contacto:", (userName) => {
        contacts[index].userName = userName;
        rl.question("Ingrese el nuevo numero de telefono:", (phoneNumber) => {
          contacts[index].phoneNumber = phoneNumber;
          console.log("\n Contacto actualizado");
          comenzarPrograma();
        });
      });
    } else {
      console.log("\n No logro encontrar el contacto indicado o no existe.");
    }
    comenzarPrograma();
  });
};

//Encontrar coincidencias
const findContact = (name) => {
  let contact = contacts.findIndex((contact) => contact.userName == name);
  return contact;
};

// Buscando un contacto
const searchContact = () => {
  rl.question("Ingresa nombre de contacto: ", (userName) => {
    index = findContact(userName);
    if (index != -1) {
      console.log(
        `
          Nombre: ${contacts[index].userName}
          Numero: ${contacts[index].phoneNumber}
        `,
      );
    } else {
      console.log("\n No se encontraron coincidencias");
    }
    comenzarPrograma();
  });
};

// Muestra todos los contactos
const showAllContacts = () => {
  for (i = 0; i <= contacts.length - 1; i++) {
    console.log(`
   Nombre: ${contacts[i].userName} - Numero: ${contacts[i].phoneNumber}`);
  }
  comenzarPrograma();
};

// Menu principal
const comenzarPrograma = () => {
  // Pregunta al usuario y espera la respuesta
  rl.question(
    `
      #### - Agenda de Contactos 1.0 - ####
      Pulse 1 -> Para Insertar nuevo contacto
      Pulse 2 -> Para Eliminar un contacto
      Pulse 3 -> Para Actualizar un contacto
      Pulse 4 -> Para Buscar contacto
      Pulse 5 -> Mostrar todos los contactos
      Pulse 6 -> Para Salir
    `,
    (userInput) => {
      const selectedOption = parseInt(userInput);
      switch (selectedOption) {
        case 1:
          insertContact();
          break;

        case 2:
          deleteContact();
          break;

        case 3:
          updateContact();
          break;

        case 4:
          searchContact();
          break;

        case 5:
          showAllContacts();
          break;

        case 6:
          console.log("Gracias por usar la agenda 1.0. ¡Hasta luego!");
          rl.close();
          break;

        default:
          console.log("No ha ingresado una opción válida.");
          comenzarPrograma();
      }
    },
  );
};

comenzarPrograma();

