/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * 

- Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

// Arrays sin Elementos;
let arrays = [] //array 
console.log(arrays);
console.log("..... ")

// Arrays con Elementos
const superHeroes = ['Batman', 'Super Man', 'Deadpool', 'Hulk'];

// Arrays Metodo pop() y push();
const pop_element = superHeroes.pop()
console.log(superHeroes);
console.log("..... ")

// push();
const push_element = superHeroes.push('Spider Man');
console.log(superHeroes);
console.log(".... ")

// Arraus Metodo shift y unshift;
const unshift_elment = superHeroes.unshift('Profesor X', 'Aquaman');
console.log(superHeroes);
console.log(".... ")

// shift;
const shift_element = superHeroes.shift();
console.log(superHeroes);
console.log(".... ")

// Arrays Mapeo
const notas = [2, 3, 4, 5, 9];

const notaPor2 = notas.map((Notas) => {
  return Notas * 2;
})
console.log(notaPor2);
console.log(".... ")

// filter
const notas_1 = [4, 6, 8, 9, 10, 2, 3, 5]
const notasPar = notas_1.filter((unaNotaPar) => {
  return unaNotaPar % 2 === 0;
});
if (notasPar.length === 0) {
  console.log('Ninguna nota cumple con la condicion');
} else {
  console.log(notasPar);
};

// ordenación
const fruta = ['Manzana', 'Banana', 'Pera', 'Naranja'];

fruta.sort();
console.log(fruta);
console.log("..... ")

// Actualizacio
const juegos = ['Pacman', 'Call of Duty ', 'Fortnite'];
juegos[0] = 'Pokemon';
console.log(juegos);
console.log("..... ")

// Eliminacio
delete juegos[0];
console.log(juegos);
console.log("......")

// Busqueda del indexOf();

console.log("....  indexOf()... ")
const index_elemento = juegos.indexOf('Fortnite');
console.log(index_elemento);
console.log(".... ")

// Objeto
let objeto = {
  nombre: "Mario",
  edad: 33,
  altura: 1.80
};
console.log(objeto);
console.log(".... ")

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * 

- Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
console.log("Bienvenidos ala Agenda de Contactos");

const agenda_contacto = function () {
  let agenda = [
    { nombre: "Matteo", numero: "3123113498" },
    { nombre: "Laura", numero: "3138434573" }
  ];

  let leave = false;

  while (!leave) {
    let opcion = prompt(`¿Qué desea hacer? 
        1 - Búsqueda de contacto 
        2 - Añadir contacto 
        3 - Actualizar contacto
        4 - Eliminar contacto
        5 - Salir`);

    switch (opcion) {
      case '1':
        let search_contacto = prompt("Ingrese el nombre del contacto que deseas buscar: ");
        let contactoEncontrado = agenda.find(contacto => contacto.nombre === search_contacto);
        if (contactoEncontrado) {
          console.log(`Nombre: ${contactoEncontrado.nombre}, Número: ${contactoEncontrado.numero}`);
        } else {
          console.log("Contacto no encontrado");
        }
        break;

      case '2':
        let nombre = prompt("Ingrese el Nombre del contacto que quieres agregar: ");
        let telefono = prompt("Ingrese el Número del contacto que quieres agregar: ");
        if (telefono.length <= 11) {
          agenda.push({ nombre: nombre, numero: telefono });
          console.log("Contacto agregado");
        } else {
          console.log("Error: El número de teléfono debe tener 11 dígitos o menos");
        }
        break;

      case '3':
        let nombreAntiguo = prompt("Ingrese el nombre del contacto que deseas actualizar: ");
        let nombreNuevo = prompt("Ingrese el nuevo nombre del contacto: ");
        let nuevoTelefono = prompt("Ingrese el nuevo número de teléfono para este contacto: ");
        let contactoParaActualizar = agenda.find(contacto => contacto.nombre === nombreAntiguo);
        if (contactoParaActualizar) {
          contactoParaActualizar.nombre = nombreNuevo;
          contactoParaActualizar.numero = nuevoTelefono;
          console.log("Contacto actualizado");
        } else {
          console.log("Contacto no encontrado");
        }
        break;

      case '4':
        let eliminar_contacto = prompt("Ingrese el nombre del contacto que desea eliminar: ");
        let index = agenda.findIndex(contacto => contacto.nombre === eliminar_contacto);
        if (index !== -1) {
          agenda.splice(index, 1);
          console.log("Contacto eliminado");
        } else {
          console.log("Contacto no encontrado");
        }
        break;

      case '5':
        leave = true;
        console.log('Saliendo de la agenda...');
        break;

      default:
        console.log('Opción no válida, por favor intente de nuevo');
    }
  }
}

agenda_contacto();
