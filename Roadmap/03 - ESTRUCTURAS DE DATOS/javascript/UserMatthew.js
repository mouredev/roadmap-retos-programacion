/*# #03 ESTRUCTURAS DE DATOS 
  ## Ejercicio
*/

// 1. Arrays
let array = [3, 1, 4, 1, 5, 9, 7, 15, 11, 8, 35];
// ---- Inserción ----
array.push(2); // Inserción al final
console.log("Mi array:", array);
array.unshift(6); // Inserción al inicio
console.log("Mi array:", array);
// ---- Eliminación -----
array.pop(); // Eliminación del último
console.log("Mi array:", array);
array.shift(); // Eliminación del primero
console.log("Mi array:", array);
array.splice(0, 3); // Elimina elementos especificos, 3 elementeos desde el indice 0
console.log("Mi array:", array);
array.length = 5; // Elimina los elementos de una array hasta dejar solo indice especificado
console.log("Mi array:", array);
// ---- Actualización -----
array[1] = 10; // Actualización segun el indice
console.log("Mi array:", array);
// ---- Ordenación ----
array.sort((a, b) => a - b); // Ordenación de forma ascendente 
console.log("Mi array:", array);
// ---- Array Vacio -----
array = []
console.log("Mi array:", array);

// 2. Objetos 
let objeto = { Nombre: 'Juan', edad: 25, profesión: 'Abogado ' };
console.log(objeto)
// ---- Inserción ----
objeto.apellidos = 'Diaz'
objeto.email = 'Juan@gmail.com';
console.log(objeto)
// ---- Actualización -----
objeto.Nombre = 'Bruno'
console.log(objeto)
// ---- Eliminación -----
delete objeto.edad
console.log(objeto)
// ---- LLamar solo una clave valor
console.log(objeto.Nombre) //

// 3. Maps
let map = new Map([['Nombre', 'Luffy'], ['edad', 17]]);
// ---- Inserción ----
map.set('rango', 'capitan'); // Añade un nuevo dato debido a que no existe la clave
console.log(map)
// ---- Actualización -----
map.set('edad', 19); // Actualiza el valor debido a que existe la clave
console.log(map)
// ---- Eliminación -----
map.delete('rango'); //
console.log(map)

// 4. Sets 
let set = new Set([1, 2, 3, 4, 5]);
// ---- Inserción ----
set.add(6); // Al no existir se añade
set.add(1); // Al existir no se añade
console.log(set)
// ---- Eliminación -----
set.delete(2); // Al existir se elimina
console.log(set)


// Dificultad Extra

let agenda = function () {
  let agendaDB = [
    { Nombre: 'Juan', Telefono: 123456789 },
    { Nombre: 'Tony', Telefono: 987456312 },
    { Nombre: 'Alberto', Telefono: 521364789 },
    { Nombre: 'Viego', Telefono: 456123987 }
  ];
  let bucle = true;

  while (bucle) {
    let decision = prompt(`Elije una opción del menú:
        1 - Buscar contacto
        2 - Añadir contacto
        3 - Actualizar contacto
        4 - Eliminar contacto
        5 - Salir`);

    switch (decision) {
      case '1':
        let nombreBuscado = prompt("Ingrese el nombre del contacto a buscar: ");
        let contactoEncontrado = agendaDB.find(contacto => contacto.Nombre === nombreBuscado);
        if (contactoEncontrado) {
          console.log(`Contacto encontrado: ${contactoEncontrado.Nombre} - ${contactoEncontrado.Telefono}`);
        } else {
          console.log(`No se encontró el contacto.`);
        }
        break;
      case '2':
        let nombre = prompt("Ingrese el nombre del nuevo contacto: ");
        let telefono = prompt("Ingrese el número del nuevo teléfono: ");
        if (telefono.length <= 11) {
          agendaDB.push({ Nombre: nombre, Telefono: telefono });
          console.log(`Contacto añadido: ${nombre} ${telefono}`);
        } else {
          console.log("El número de teléfono es demasiado largo.");
        }
        break;
      case '3':
        let nombreActualizar = prompt("Ingrese el nombre del contacto a actualizar: ");
        let contactoActualizado = agendaDB.find(contacto => contacto.Nombre === nombreActualizar);
        if (contactoActualizado) {
          let nuevoTelefono = prompt("Ingrese el nuevo número de teléfono: ");
          if (nuevoTelefono.length <= 11) {
            contactoActualizado.Telefono = nuevoTelefono;
            console.log(`Contacto actualizado: ${nombreActualizar} ${nuevoTelefono}`);
          } else {
            console.log("El número de teléfono es demasiado largo.");
          }
        } else {
          console.log(`No se encontró el contacto.`);
        }
        break;
      case '4':
        let nombreEliminar = prompt("Ingrese el nombre del contacto a eliminar: ");
        contactoEncontrado = agendaDB.find(contacto => contacto.Nombre === nombreEliminar);
        if (contactoEncontrado) {
          agendaDB = agendaDB.filter(contacto => contacto.Nombre !== nombreEliminar);
          console.log(`Contacto eliminado: ${nombreEliminar}`);
        } else {
          console.log(`No se encontró el contacto.`);
        }
        break;
      case '5':
        bucle = false;
        break;
      default:
        console.log('Opción no existente, por favor ingrese una opción válida');
    }
  }
}

agenda();



/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un Nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */