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

// Arrays

// Crear un array
let elements = ["aire", "fuego", "tierra", "agua"];
console.log(elements);

// longitud
console.log(elements.length);

// pop sacar ultimo elemento
let water = elements.pop();
console.log(water);
console.log(elements);

// push agregar un elemento al final
elements.push(water);
console.log(elements);

// pop sacar primer elemento
let air = elements.shift();
console.log(air);
console.log(elements);

// push agregar un elemento al inicio
elements.unshift(air);
console.log(elements);

// Recorrer arreglo
elements.forEach((element) => {
  console.log(element);
});

for (const element of elements) {
  console.log(element);
}

// clear
elements = [];
elements.length = 0; // Alt
console.log(elements);

// slice
elements.push("aire", "fuego", "tierra", "agua");
console.log(elements);

let myNewArray = elements.slice(1, 3); // Permite extraer elemento indicando el indice incial y el final pero el ultimo indice no cuenta si no el anterior
console.log(myNewArray);

// splice

elements.splice(1, 2, "tierra"); // Elimina elementos en el rango y agrega un nuevo elemento en la posicion intermedia
console.log(elements);

// Copiar array

let otherArray = [...elements];
console.log(otherArray);

// Set

// Declaracion
let mySet = new Set();
console.log(mySet);

// Inicialización
mySet = new Set([
  "Elemento 1",
  "Elemento 2",
  "Elemento 3",
  "Elemento 4",
  "Elemento 5",
]);
console.log(mySet);

// Métodos comunes

// add & delete

mySet.add("Elemento 6"); // En Js el add añade el elemento al final, manteniendo el orden
console.log(mySet);

console.log(mySet.delete("Elemento 6")); // Elimina el elemento pero no utiliza el indice, debe ser con el valor del elemento que se quiere borrar
// Ademas retornara un true si existe el elemento y lo elimino, si no devuelve false.
console.log(mySet);

// NOTA: No hay acceso al indice a diferencia de los Array

// has
console.log(mySet.has("Elemento 6")); // Verifica si existe el elemento
console.log(mySet.has("Elemento 1"));

// Size
console.log(mySet.size); // Tamaño del set

// Convertir Set en Array
let myArray = Array.from(mySet);
console.log(myArray);

// Convertir Array en Set
mySet = new Set(myArray);
console.log(mySet);

// Map

// Map

// Declaración
let myMap = new Map();
console.log(myMap);

// Inicialización
myMap = new Map([
  ["key 1", "value 1"],
  ["key 2", "value 2"],
  ["key 3", "value 3"],
]);
console.log(myMap);

// Métodos y propiedades

// set
myMap.set("key 4", "value 4");
console.log(myMap);

myMap.set("key 2", "new value 2");
console.log(myMap);

// get
console.log(myMap.get("key 1"));
console.log(myMap.get("key 5"));

// has
console.log(myMap.has("key 1"));
console.log(myMap.has("key 5"));

// delete
myMap.delete("key 4");
console.log(myMap);

// keys
console.log(myMap.keys());

// values
console.log(myMap.values());

// entries
console.log(myMap.entries());

// size
console.log(myMap.size);

// clear
myMap.clear();
console.log(myMap);

// Objects

// Sintaxis
let person = {
  // Propiedades clave : valor
  name: "Diego",
  age: 27,
  alias: "DevsDav",
};

// Acceso a Propiedades

// Notacion por punto
console.log(person.name);

// Notación por corchetes
console.log(person["name"]);

// Modificar propiedades
person.name = "Diego Arenas";
console.log(person.name);

// Eliminación de propiedades
delete person.age;
console.log(person);

// Nueva propiedad
person["age"] = 27;
person.email = "devsdav@devsdav.dev";
console.log(person);

// Métodos (funciones) y Anidación

let person2 = {
  // Propiedades clave : valor
  name: "Diego",
  age: 27,
  alias: "DevsDav",
  // Métodos
  walk: function () {
    console.log("La persona camina.");
  },
  // Anidación de objeto
  job: {
    name: "Programador",
    exp: 4,
    work: function () {
      console.log("La persona trabaja.");
    },
  },
};

person2.walk();
person2.job.work();

// Igualdad de objetcs

let person4 = {
  // Propiedades clave : valor
  name: "Diego Arenas",
  age: 27,
  alias: "DevsDav",
};

// No se puede igualar asi
console.log(person == person4);
console.log(person === person4);

// Pero si por propiedades
console.log(person.name == person4.name);

// Iteración
for (let key in person4) {
  console.log(key + ": " + person4[key]);
}

// Interpolación de variables

let person3 = {
  // Propiedades clave : valor
  name: "Diego",
  age: 27,
  alias: "DevsDav",
  // Métodos
  walk: function () {
    console.log("La persona camina.");
  },
  // Anidación de objeto
  job: {
    name: "Programador",
    exp: 4,
    work: function () {
      // interpolacion con this
      console.log(`La persona tiene ${this.exp} años de experiencia`);
    },
  },
};

person3.job.work();

// Funciones como objects
// NOTA: Esto deberia ser una clase
function Person(name, age) {
  this.name = name;
  this.age = age;
}

let person5 = new Person("Diego", 27);
console.log(person5);

// console.clear();

/*
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

const Agenda = {
  contacts: {},
  find: function (name) {
    return Object.hasOwn(this.contacts, name)
      ? `${name}: ${this.contacts[name]}`
      : "Contacto no encontrado";
  },
  insert: function (name, phone) {
    let result = false;
    let phoneValidate = this.checkNumber(phone);
    let propsValidate = !Object.hasOwn(this.contacts, name);

    if (propsValidate && phoneValidate) {
      this.contacts[name] = Number(phone);
      result = true;
    }

    return result
      ? "Registro exitoso"
      : "Contacto no encontrado o numero invalido";
  },
  update: function (name, phone) {
    let phoneValidate = this.checkNumber(phone);
    let propsValidate = Object.hasOwn(this.contacts, name);

    if (propsValidate && phoneValidate) {
      (this.contacts[name] = Number(phone))
      return "Contacto Actualizado";
    }
    return "Contacto no encontrado o numero invalido";
  },
  delete: function (name) {
    if (Object.hasOwn(this.contacts, name)) {
      delete this.contacts[name];
      return "Contacto eliminado";
    }
    return "Contacto no encontrado";
  },
  show: function () {
    console.log(this.contacts);
  },

  checkNumber: function (number) {
    return number.length < 12 && !Number.isNaN(Number(number));
  },
};

const readline = require("readline");
const read = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const menu = () => {
  read.question(
    `Menu:
        1.Agregar
        2.Buscar
        3.Actualizar
        4.Eliminar
        5.Contactos
        6.Finalizar
        Ingrese la opcion:`,
    (option = (option) => {
      switch (option) {
        case "1":
          read.question(`Ingrese el nombre: `, (name) => {
            read.question(`Ingrese el numero de telfono: `, (phone) => {
              console.log(Agenda.insert(name, phone));
              menu();
            });
          });
          break;
        case "2":
          read.question(`Ingrese el nombre: `, (name) => {
            console.log(Agenda.find(name));
            menu();
          });
          break;
        case "3":
          read.question(`Ingrese el nombre: `, (name) => {
            read.question(`Ingrese el numero de telfono: `, (phone) => {
              console.log(Agenda.update(name, phone));
              menu();
            });
          });
          break;
        case "4":
          read.question(`Ingrese el nombre: `, (name) => {
            console.log(Agenda.delete(name));
            menu();
          });
          break;
        case "5":
          Agenda.show();
          menu();
          break;
        case "6":
          read.close();
          break;
        default:
          console.log("Operación no válida");
          menu();
          break;
      }
    })
  );
};

menu();
