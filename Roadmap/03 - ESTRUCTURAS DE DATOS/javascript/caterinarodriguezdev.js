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

console.log("--------------ESTRUCTURAS DE DATOS----------------");
console.log("---------------------ARRAY------------------------");

const arr = [1, 2, 3];
console.log("array: ", arr);
arr.push(4);
console.log("Inserción en el array de un 4. Resultado: ", arr);
arr.pop();
console.log("Borrado en el array", arr);
arr.shift();
console.log("Borrado del primer elemento en el array", arr);

let arrDesordenado = [2, 1, 0];
console.log("array desordenando", arrDesordenado);
arrDesordenado.sort();
console.log("array ordenado", arrDesordenado);

arrDesordenado[0] = 10;
console.log("actualizamos array desordenado", arrDesordenado);

console.log("---------------------SET------------------------");
// Los sets solo permiten datos únicos, no puede haber dos elementos repetidos
const miSet = new Set([1, 2, 3]);
console.log("mi set es", miSet);
miSet.add(4);
console.log(".add() añade un elemento a mi", miSet);
miSet.delete(3);
console.log("borrando el elemento 3", miSet);
console.log("el set tiene el elemento 4?", miSet.has(4));
miSet.clear();
console.log("hacemos un clear del set", miSet);

console.log("---------------------WEAKSET------------------------");
const obj1 = { nombre: "obj1" };
const obj2 = { nombre: "obj2" };
const obj3 = { nombre: "obj3" };

const miWeakSet = new WeakSet();
miWeakSet.add(obj1);
miWeakSet.add(obj2);
console.log("my weak set", miWeakSet);
miWeakSet.add(obj3);
console.log("add obj3", miWeakSet);
miWeakSet.delete(obj2);
console.log("delete 3", miWeakSet);
console.log("my weak set has obj1?", miWeakSet.has(obj1));

console.log("---------------------WEAKMAP------------------------");
let weakMap = new WeakMap();
let key1 = {};
let key2 = {};

weakMap.set(key1, "value1");
weakMap.set(key2, "value2");

weakMap.delete(key1);

weakMap.set(key2, "newValue2");
console.log(weakMap);

console.log("---------------------OBJETO------------------------");
const persona = {
  nombre: "Caterina",
  edad: 24,
  genero: "f",
};

persona.edad = 25;
console.log(persona);

delete persona.genero;
console.log(persona);

const sortedKeys = Object.keys(persona).sort();

let sortedObj = {};
sortedKeys.map((key) => (sortedObj[key] = persona[key]));
console.log("objeto ordenado", sortedObj);

console.log("---------------------MAP------------------------");

let map = new Map([
  ["nombre", "Caterina"],
  ["edad", 22],
  ["genero", "f"],
]);

map.set("casa", "Mallorca");

map.delete("genero");
console.log(map);

let sortedMapArray = [...map.entries()].sort();
let sortedMap = new Map(sortedMapArray);
console.log(sortedMap);

console.log("--------------------EJERCICIO EXTRA------------------");

/* DIFICULTAD EXTRA (opcional):
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
const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

let contacts = [];

const menu = () => {
  console.log(`
        ------------------
        1. Añadir contacto
        2. Borrar contacto
        3. Opción sorpresa
        4. Ver contactos
        -----------------

        `);
  rl.question("Elije mortal :) -> ", chooseOption);
};

const chooseOption = (option) => {
  switch (option) {
    case "1":
      addContact();
      break;
    case "2":
      deleteContact();
      break;
    case "3":
      console.log("testim Grace, princeseta");
    case "4":
      listContacts();
      break;
    default:
      menu();
  }
};

const addContact = () => {
  rl.question("Nombre pls -> ", (name) => addContactTelephone(name));
};

const addContactTelephone = (name) => {
  rl.question("Teléfono porfa pls -> ", (tlf) => {
    if (tlf.length > 11) {
      console.log("El teléfono no puede ser mayor a 11 dígitos");
      addContactTelephone();
    } else if (!/^\d{1,11}$/.test(tlf)) {
      console.log("El teléfono solo puede incluir dígitos numéricos");
      addContact();
    } else {
      contacts.push({ nombre: name, telefono: tlf });
      console.log("siuuuu, contacto añadido");
      listContacts();
    }
  });
};

const listContacts = () => {
  console.log("                  ");
  console.log("------------------");
  console.log("                  ");
  console.log("TUS CONTACTOS, REINA:");
  console.log("                  ");
  contacts.map((contact) =>
    console.log(`Nombre: ${contact.nombre} - Teléfono: ${contact.telefono}`)
  );
  menu();
};

const deleteContact = () => {
  rl.question("A quien hacemos la cruz? -> ", (contact) => {
    contacts = contacts.filter((contact) => contact.nombre === contact);
    console.log("eliminao >:)");
    menu();
  });
  menu();
};

menu();
