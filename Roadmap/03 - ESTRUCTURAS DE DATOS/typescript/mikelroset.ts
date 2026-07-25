
// --------------------------------- ARRAYS --------------------------------- //
/* Un array es una colección ordenada de elementos. Puede contener cualquier 
 * tipo de dato, incluyendo otros arrays. Los arrays se pueden declarar de 
 * varias maneras, como en la siguiente línea:
 */
const myArray: number[] = [1, 2, 3, 4, 5];

// Accediendo a elementos
myArray[0]; // 1
myArray[1]; // 2
myArray[2]; // 3
myArray[3]; // 4
myArray[4]; // 5

// Longitud
myArray.length; // 5

// Añadiendo elementos
myArray.push(6); // [1, 2, 3, 4, 5, 6]

// Eliminando el último elemento
myArray.pop(); // [1, 2, 3, 4, 5]

// Eliminando el primer elemento
myArray.shift(); // [2, 3, 4, 5]

// Añadiendo elementos al inicio
myArray.unshift(0); // [0, 2, 3, 4, 5]

// Cortando elementos
myArray.splice(2, 2); // [2, 3]

// Uniendo arrays
let otherArray: number[] = [1, 2, 3];
myArray.concat(otherArray); // [1, 2, 3, 1, 2, 3]

// Invirtiendo el array
myArray.reverse(); // [5, 4, 3, 2, 1]

// Ordenando el array
myArray.sort(); // [1, 2, 3, 4, 5]

// Buscando elementos
myArray.indexOf(3); // 2
myArray.lastIndexOf(3); // 4

// Copiando array
let copyArray: number[] = myArray.slice(); // [1, 2, 3, 4, 5]

// Copiando array con inicio y final
let copyArray2: number[] = myArray.slice(1, 4); // [2, 3, 4]

// Copiando array con inicio y final negativos
let copyArray3: number[] = myArray.slice(-3, -1); // [3, 4]

// Copiando array con inicio y final negativos
let copyArray5: number[] = myArray.slice(-3, -1); // (Error corrected) should be [3, 4]


// --------------------------------- OBJECTS -------------------------------- //
/* Un objeto es una colección de pares clave-valor, donde las claves son cadenas 
 * de texto y los valores pueden ser cualquier tipo de dato. Los objetos se 
 * pueden declarar de varias maneras, como en la siguiente línea:
 */
type PersonInfo = {
  name: string;
  age: number;
  city?: string;
};
const myObject: PersonInfo = { name: "John", age: 25 };

// Accediendo a propiedades
myObject.name; // "John"
myObject.age; // 25

// Longitud
Object.keys(myObject).length; // 2

// Añadiendo propiedades
myObject.city = "New York"; // { name: "John", age: 25, city: "New York" }

// Eliminando propiedades
delete myObject.city; // { name: "John", age: 25 }

/* Cortando propiedades: Hacer que 'age' sea opcional en la definición del 
tipo para usar delete */
const { age, ...rest } = myObject; // { name: "John" }
const myObjectWithoutAge = { ...rest };

// Uniendo objetos
let otherObject: PersonInfo = { name: "Jane", age: 30 };
let combinedObject: PersonInfo = { 
  ...myObject, 
  ...otherObject 
}; // { name: "Jane", age: 30 }

// Copiando objeto
let copyObject: object = myObject; // { name: "John", age: 25 }

// Copiando objeto con propiedades
let copyObject2: object = Object.assign(
  {}, 
  myObject
); // { name: "John", age: 25 }

// Copiando objeto con propiedades y métodos
class Person {
  name: string;
  age: number;
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
  sayHello() {
    console.log(`Hello, my name is ${this.name}`);
  }
}
let person = new Person("John", 25);
let copyObject3: object = Object.assign(
  { sayHello: person.sayHello.bind(person) }, 
  person
); // { name: "John", age: 25, sayHello: [Function: sayHello] }


// ---------------------------------- MAPAS --------------------------------- //
/* Un Map es una colección de pares clave-valor, pero a diferencia de un objeto,
 * las claves pueden ser de cualquier tipo, no solo cadenas.
 * Los mapas preservan el orden de inserción.
 */
const myMap: Map<string, number> = new Map();

// Accediendo a elementos
myMap.get("key"); // undefined

// Añadiendo elementos
myMap.set("key", 10); // Map { "key" => 10 }

// Accediendo a elementos
myMap.get("key"); // 10

// Eliminando elementos
myMap.delete("key"); // Map {}

// Copiando mapa
let copyMap: Map<string, number> = myMap; // Map { "key" => 10 }

// Copiando mapa con elementos
let copyMap2: Map<string, number> = new Map(myMap); // Map { "key" => 10 }

// Copiando mapa con elementos y valores
let copyMap3: Map<string, number> = new Map(
  myMap.entries()
);


// ---------------------------------- SETS ---------------------------------- //
/* Un Set es una colección de valores únicos. No permite duplicados y, como los 
 * mapas, preserva el orden de inserción.
 */
const mySet: Set<number> = new Set();

// Accediendo a elementos
mySet.has(10); // false

// Añadiendo elementos
mySet.add(10); // Set { 10 }

// Eliminando elementos
mySet.delete(10); // Set {}

// Copiando set
let copySet: Set<number> = mySet; // Set { 10 }

// Copiando set con elementos
let copySet2: Set<number> = new Set(mySet); // Set { 10 }

// Copiando set con elementos y valores
let copySet3: Set<number> = new Set(
  mySet.values()
);


// --------------------------------- WEAKMAP -------------------------------- //
/* Un WeakMap es similar a un Map, pero sus claves deben ser objetos. Además, 
 * no previene que los objetos claves sean recolectados por el recolector de 
 * basura si no tienen más referencias.
 */

const myWeakMap: WeakMap<object, string> = new WeakMap();

// Accediendo a elementos
myWeakMap.get(myObject); // undefined

// Añadiendo elementos
myWeakMap.set(myObject, "Hola"); // WeakMap { { [object Object]] => "Hola" }

// Eliminando elementos
myWeakMap.delete(myObject); // WeakMap {}

// Copiando mapa
let copyWeakMap: WeakMap<object, string> = myWeakMap; 
// WeakMap { { [object Object]] => "Hola" }


// --------------------------------- WEAKSET -------------------------------- //
/* Un WeakSet es como un Set, pero solo admite objetos como valores. Al igual 
 * que el WeakMap, los objetos dentro del WeakSet pueden ser recolectados si ya 
 * no hay otras referencias hacia ellos.
 */
const myWeakSet: WeakSet<object> = new WeakSet();

// Accediendo a elementos
myWeakSet.has(myObject); // false

// Añadiendo elementos
myWeakSet.add(myObject); // WeakSet { { [object Object] } }

// Eliminando elementos
myWeakSet.delete(myObject); // WeakSet {}

// Copiando set
let copyWeakSet: WeakSet<object> = myWeakSet; 
// WeakSet { { [object Object] } }


// --------------------------------- ENUMS ---------------------------------- //
/* Los enums permiten definir un conjunto de valores constantes con nombres 
 * asociados a un valor (pueden ser numéricos o de cadena).
 */
enum MyEnum {
    FIRST = "FIRST",
    SECOND = "SECOND"
}

const myEnum: MyEnum = MyEnum.FIRST;

// Accediendo a elementos
MyEnum.FIRST; // "FIRST"
MyEnum.SECOND; // "SECOND"

// Copiando enum
let copyEnum: MyEnum = myEnum; 
// "FIRST"

// Copiando enum con elementos
let copyEnum2: MyEnum = MyEnum.FIRST; 
// "FIRST"


// -------------------------- BONUS EJERCICIO ------------------------------- //
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

type Contact = {
  name: string;
  phone: number;
};

class Agenda {
  contacts: Contact[];

  constructor() {
    this.contacts = [];
  }

  addContact(contact: Contact) {
    this.contacts.push(contact);
  }

  findContact(name: string): Contact | undefined {
    return this.contacts.find((contact) => contact.name === name);
  }

  updateContact(contact: Contact) {
    const index = this.contacts.findIndex((c) => c.name === contact.name);
    if (index !== -1) {
      this.contacts[index] = contact;
    } else {
      this.addContact(contact);
    }
  }

  deleteContact(name: string) {
    const index = this.contacts.findIndex((c) => c.name === name);
    if (index !== -1) {
      this.contacts.splice(index, 1);
    } else {
      console.log(`${name} no existe`);
    }
  }

  listContacts() {
    console.log(this.contacts);
  }
}

const agenda = new Agenda();
const options: string[] = [
  "[1] Añadir contacto",
  "[2] Buscar contacto",
  "[3] Actualizar contacto",
  "[4] Eliminar contacto",
  "[5] Listar contactos",
  "[6] Salir",
];

const runContactApp = (): void => {
  const option = prompt(
    "Elige una opción:\n" +
      options.map((o) => `  ${o}`).join("\n")
  );

  switch (option) {
    case "1":
      const addName = prompt("Ingrese el nombre: ");
      if (!addName) {
        console.log("Por favor ingrese un nombre válido.");
        break;
      }

      const addPhone = prompt("Ingrese el número de teléfono: ");
      if (!addPhone) {
        console.log("Por favor ingrese un número de teléfono válido.");
        break;
      }
      if (addPhone.length > 11) {
        console.log("El número de teléfono debe tener 11 dígitos.");
        break;
      }
      if (!/^\d+$/.test(addPhone)) {
        console.log("El número de teléfono debe ser numérico.");
        break;
      }
      const addContact: Contact = { name: addName, phone: parseInt(addPhone) };
      agenda.addContact(addContact);
      break;
      
    case "2": 
      const findName = prompt("Ingrese el nombre del contacto a buscar: ");
      if (!findName) {
        console.log("Por favor ingrese un nombre válido.");
        break;
      }
      const findContact = agenda.findContact(findName);
      if (findContact) {
        console.log(findContact);
      }
      else {
        console.log(`${findContact} no existe`);
        break;
      }
      break;

    case "3":
      const updateName = prompt("Ingrese el nombre del contacto a actualizar: ");
      if (!updateName) {
        console.log("Por favor ingrese un nombre válido.");
        break;
      }
      const updatePhone = prompt("Ingrese el número de teléfono del contacto a actualizar: ");
      if (!updatePhone) {
        console.log("Por favor ingrese un número de teléfono válido.");
        break;
      }
      if (updatePhone.length > 11) {
        console.log("El número de teléfono debe tener 11 dígitos.");
        break;
      }
      if (!/^\d+$/.test(updatePhone)) {
        console.log("El número de teléfono debe ser numérico.");
        break;
      }
      const updateContact: Contact = { name: updateName, phone: parseInt(updatePhone) };
      agenda.updateContact(updateContact);
      break;

    case "4":
      const deleteName = prompt("Ingrese el nombre del contacto a eliminar: ");
      if (!deleteName) {
        console.log("Por favor ingrese un nombre válido.");
        break;
      }
      agenda.deleteContact(deleteName);
      break;

    case "5":
      agenda.listContacts();
      break;

    case "6":
      break;

    default:
      console.log("Opción no válida. Inténtalo de nuevo.");
      break;
  }
}

runContactApp();
