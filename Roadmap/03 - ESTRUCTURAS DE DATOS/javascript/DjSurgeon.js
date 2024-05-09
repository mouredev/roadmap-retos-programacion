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
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

/* === ESTRUCTURAS DE DATOS EN JAVASCRIPT === */
/*
 * Las estructuras de datos en JavaScript son un aspecto crucial de la programación eficiente.
 * Proporcionan una forma de organizar, gestionar y almacenar datos que facilita su acceso y trabajo.
 * Comprender los diferentes tipos de estructuras de datos y sus aplicaciones puede mejorar
 * significativamente tus habilidades de programación.
 *
 * JavaScript admite una serie de estructuras de datos, incluyendo Arreglos (Arrays),
 * Objetos (Objects), Datasets (Sets), Mapas (Maps),
 * Pilas (Stacks), Colas (Queues), Listas Enlazadas (Linked Lists),
 * Árboles (Trees), Grafos (Graphs), Tablas Hash (Hash Tables), y otras.
 * Cada una de estas estructuras de datos tiene sus propias fortalezas y debilidades,
 * y se utilizan en diferentes situaciones dependiendo de los requisitos de la tarea en cuestión.
 */
// ARRAYS
/* El arreglo es la estructura de datos más simple en JavaScript.
 * Se utiliza para almacenar múltiples valores en una sola variable.
 */

let ids = [1, 2, 3, 4, 5];
console.log(ids);

let nombres = ["Marc", "Noa", "Sergio", "Verónica"];

// Accedes a un elemento del array mediante su indice
console.log(nombres[2]);

// Adición de elementos al final de un array

nombres.push("Leonidas");
console.log(nombres);

// Eliminar el último elemento de un array

nombres.pop();
console.log(nombres);

// Añadir un elemento al principio de un array

nombres.unshift("Nala");
console.log(nombres);

// Eliminar el primer elemento de un array

nombres.shift();
console.log(nombres);

// Encontrar el índice de un elemento del array

let position = nombres.indexOf("Sergio");
console.log(position);

// Eliminar elemento de un array y crear un array nuevo (Modifica el array original)

let hijos = nombres.splice(0, 2);
console.log(hijos);
console.log(nombres);

// Copiar un array (No modifica el array original)

let padres = nombres.slice();
console.log(padres);
console.log(nombres);

// OBJETOS
/*
 * Un objeto es una colección de propiedades, y una propiedad es una asociación
 * entre un nombre (o clave) y un valor. El valor de una propiedad puede ser una función,
 * en cuyo caso la propiedad es conocida como un método.
 */

let miCoche = {
  color: "rojo",
  ruedas: 4,
  descapotable: false,
};

console.log(miCoche);
console.log(miCoche.color);

// Añadir una propiedad al objeto.

miCoche.volante = false;

console.log(miCoche);

// Iterar sobre las propiedades de los objetos.
// For...in
for (let piezas in miCoche) {
  console.log(
    `Estas son mis claves: ${piezas} y estos sus valores: ${miCoche[piezas]}`
  );
}
//Devuelve un array con las claves Object.keys()
console.log(Object.keys(miCoche));
// Object.getOwnPropertyNames()
console.log(Object.getOwnPropertyNames(miCoche));

// SET
/*
 * Set es una colección de valores en la que cada valor debe ser único.
 * Los valores duplicados son automáticamente eliminados.
 * Set es ideal para situaciones donde los valores deben ser únicos,
 * y se manejan datos que no requieren un orden específico o indexación.
 */
// Creamos un nuevo set
let consolas = new Set();
// Agregar elementos
consolas.add("NES");
consolas.add("Mega Drive");
console.log(consolas);
// Eliminar elementos
consolas.delete("NES");
console.log(consolas);
// Verificar Existencia
console.log(consolas.has("Mega Drive"));
// Tamaño
console.log(consolas.size);
// Eleminar todos los datos
consolas.clear();
// Algunos usos de los set
// Eliminar duplicados
const nuevas = ["360", "PS3", "PS4", "XboxOne", "PS3"];
console.log(nuevas);
const newGen = new Set(nuevas);
console.log(newGen);
// Unir conjuntos
const oldGen = new Set(["NES", "MegaDrive"]);
consolas = new Set([...newGen, ...oldGen]);
console.log(consolas);

// MAP
/*
 * Map es una colección de pares clave-valor donde cada clave es única.
 * A diferencia de los objetos, las claves en Map pueden ser de cualquier tipo,
 * y mantiene el orden de inserción de los elementos
 */
// Creamos un nuevo Map
let juegos = new Map();
// Agregar elementos
juegos.set(1, "Gears of War");
juegos.set(2, "Jak & Daxter");
console.log(juegos);
// Tamaño del mapa
console.log(juegos.size);
// Valor de la clave
console.log(juegos.get(1));
console.log(juegos.get(4));
// Saber si existe la clave o no
console.log(juegos.has(1));
console.log(juegos.has(4));
// Eliminar una clave
juegos.delete(2);
console.log(juegos);
// Eliminar el mapa completo
juegos.clear();
console.log(juegos);
// Diferentes maneras de reccorrer un map
juegos.set(1, "Gears of War");
juegos.set(2, "Jak & Daxter");
juegos.set(3, "Halo");
//.keys() devuelve un iterable con las claves.
console.log(juegos.keys());
// .values() devuelve un iterable con los valores.
console.log(juegos.values());
// .entries() devuelve un iteracle con la entradas clave y valor.
console.log(juegos.entries());

// AGENDA DE CONTACTOS

const agenda = new Map();
agenda.set(1, { name: "Juan", phone: "123456789" });
agenda.set(2, { name: "María", phone: "987654321" });

// Añadir un contacto
/* Creamos una función con los parametros nombre y telefono
 * comprobamos si tanto nombre y telefono son strings
 * y si es asi, añadimos el contacto a la agenda en la siguiente posición disponible.
 */
function addContact(nombre, telefono) {
  if (
    typeof nombre === "string" &&
    typeof telefono === "string" &&
    telefono.length === 9
  ) {
    agenda.set(agenda.size + 1, { name: nombre, phone: telefono });
    console.log(
      `El contacto: ${nombre} y el telefono: ${telefono} han sido correctamente introducidos.`
    );
  } else {
    console.log("Introduce los datos correctos");
  }
}
// Eliminar un contacto
/*
 * Creamos una función con el numero de clave como argumento
 * comprobamos si esa clave esta en el set de la agenda
 * si está se procede al borrado de esa clave
 */
function deleteContact(clave) {
  if (agenda.has(clave) === true) {
    console.log(`El contacto ${agenda.get(clave).name} ha sido eliminado.`);
    agenda.delete(clave);
  } else {
    console.log("El contacto seleccionado no existe.");
  }
}
// Busqueda de un contacto
/*
 * Creamos una función con el numero de clave como argumento
 * comprobamos que esa clave este dentro del set y si esta
 * devuelve por consola los datos de la clave.
 */
function getContact(clave) {
  if (agenda.has(clave) === true) {
    console.log(
      `El contacto seleccionado es: ${
        agenda.get(clave).name
      } y su telefono es: ${agenda.get(clave).phone}`
    );
  } else {
    console.log("Ese contacto no se encuentra en la agenda.");
  }
}
// Actualización de un contacto
/*
 * Creamos una función que toma como argumentos un clave
 * un nombre y un telefono, comprueba si esa clave es valida
 * y luego toma los argumentos para actualizar el contacto
 */
function actContact(clave, nombre, telefono) {
  if (agenda.has(clave) === true && typeof clave === "number") {
    if (
      typeof nombre === "string" &&
      typeof telefono === "string" &&
      telefono.length === 9
    ) {
      agenda.set(clave, { name: nombre, phone: telefono });
      console.log(`El contacto: ${agenda.get(clave).name} ha sido actualizado`);
    } else {
      console.log("Los datos introducidos son incorrectos.");
    }
  } else {
    console.log("Ese contacto no esta en la agenda.");
  }
}
