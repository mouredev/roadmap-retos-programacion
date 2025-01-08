//! Arreglos
//* Creacion
let array = [1, 2, 3, 4, 5];
console.log(array); // [1, 2, 3, 4, 5]

//* Insersion
array.push(6); // Inserta al final
console.log(array); // [1, 2, 3, 4, 5, 6]

array.unshift(0); // Inserta al inicio
console.log(array); // [0, 1, 2, 3, 4, 5, 6]

//* Borrado
array.pop(); // Elimina el último elemento
console.log(array); // [0, 1, 2, 3, 4, 5]

array.shift(); // Elimina el primer elemento
console.log(array); // [1, 2, 3, 4, 5]

//* Actualizacion
array[2] = 10; // Actualiza el tercer elemento
console.log(array); // [1, 2, 10, 4, 5]

//* Ordenacion
array.sort((a, b) => a - b); // Ordena de menor a mayor
console.log(array); // [1, 2, 4, 5, 10]

//! Objetos
//* Creacion
let obj = { a: 1, b: 2, c: 3 };
console.log(obj); // {a: 1, b: 2, c: 3}

//* Insersion
obj.d = 4;
console.log(obj); // {a: 1, b: 2, c: 3, d: 4}

//* Borrado
delete obj.b;
console.log(obj); // {a: 1, c: 3, d: 4}

//* Actualizacion
obj.a = 10;
console.log(obj); // {a: 10, c: 3, d: 4}

//* Ordenacion
let sortedKeys = Object.keys(obj).sort();
let sortedObj = {};
sortedKeys.forEach((key) => {
  sortedObj[key] = obj[key];
});
console.log(sortedObj); // {a: 10, c: 3, d: 4}

//! Conjuntos (sets)
//* Creacion
let set = new Set([1, 2, 3, 4, 5]);
console.log(set); // Set {1, 2, 3, 4, 5}

//* Insersion
set.add(6);
console.log(set); // Set {1, 2, 3, 4, 5, 6}

//* Borrado
set.delete(4);
console.log(set); // Set {1, 2, 3, 5, 6}

//* Actualizacion (no hay una operacion directa, se puede hacer borrando e insertando)
if (set.has(3)) {
  set.delete(3);
  set.add(10);
}
console.log(set); // Set {1, 2, 5, 6, 10}

//* Ordenacion (no aplica a Stes ya que son desordenados, pero se puede convertir a array y ordenar)
let sortedSetArray = Array.from(set).sort((a, b) => a - b);
console.log(sortedSetArray); // [1, 2, 5, 6, 10]

//! Mapas (maps)
//* Creacion
let map = new Map([
  ["a", 1],
  ["b", 2],
  ["c", 3],
]);
console.log(map); // Map {'a' => 1, 'b' => 2, 'c' => 3}

//* Insercion
map.set("d", 4);
console.log(map); // Map {'a' => 1, 'b' => 2, 'c' => 3, 'd' => 4}

//* Borrado
map.delete("b");
console.log(map); // Map {'a' => 1, 'c' => 3, 'd' => 4}

//* Actualizacion
map.set("a", 10);
console.log(map); // Map {'a' => 10, 'c' => 3, 'd' => 4}

//* Ordenacion (por clave)
let sortedMapKeys = new Map([...map.entries()].sort());
console.log(sortedMapKeys); // Map {'a' => 10, 'c' => 3, 'd' => 4}

//! Extra Ejercicio
// * Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.

const readline = require("readline");

let schedule = [
  {
    name: "Daniel",
    phone: 123456789,
  },
  {
    name: "Juan",
    phone: 987654321,
  },
  {
    name: "Pedro",
    phone: 123456789,
  },
  {
    name: "Maria",
    phone: 987654321,
  },
  {
    name: "Luis",
    phone: 123456789,
  },
];
function addContact(name, phone) {
  if (phone.length > 11) {
    console.log("El numero de telefono no puede ser mayor a 11 digitos");
    return;
  } else if (isNaN(phone)) {
    console.log("El numero de telefono debe ser numerico");
    return;
  }
  let contact = {
    name: name,
    phone: phone,
  };
  console.log("Contacto anadido");
  schedule.push(contact);
  return contact;
}

function findContact(name) {
  const lowerCaseName = name.toLowerCase();
  const contact = schedule.find(
    (contact) => contact.name.toLowerCase() === lowerCaseName
  );
  if (contact) {
    return contact;
  } else {
    return "El contacto no fue encontrado";
  }
}

function deleteContact(name) {
  const lowerCaseName = name.toLowerCase();
  const index = schedule.findIndex(
    (contact) => contact.name.toLocaleLowerCase() === lowerCaseName
  );
  if (index !== -1) {
    schedule.splice(index, 1);
    return "El contacto fue eliminado con exito";
  } else {
    return "El contacto no fue encontrado";
  }
}

function updateContact(currentName, newName = null, newPhone = null) {
  const lowerCaseCurrentName = currentName.toLowerCase();
  const contact = schedule.find(
    (contact) => contact.name.toLocaleLowerCase() === lowerCaseCurrentName
  );
  if (contact) {
    if (newName) {
      contact.name = newName;
    }
    if (newPhone) {
      contact.phone = newPhone;
    }
    return "El contacto fue actualizado con exito";
  } else {
    return "El contacto no fue encontrado";
  }
}

function sortContactByName() {
  schedule.sort((a, b) => {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  });
}

function sortContactByPhone() {
  schedule.sort((a, b) => a.phone - b.phone);
}

function promptUser() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  function askOperarion() {
    rl.question(
      "\n ¿Que operacion deseas realizar? \n 1 - Agregar Contacto, \n 2 - Buscar Contacto, \n 3 - Actualizar Contacto, \n 4 - Eliminar Contacto, \n 5 - Ordenar Contactos, \n 6 - Ver Agenda \n 7 - Salir \n",
      function (operation) {
        switch (operation) {
          case "1":
            rl.question("Ingresa el nombre del contacto: ", function (name) {
              rl.question(
                "Ingresa el telefono del contacto: ",
                function (phone) {
                  addContact(name, phone);
                  askOperarion();
                }
              );
            });
            break;

          case "2":
            rl.question("Ingresa el nombre del contacto: ", function (name) {
              console.log(findContact(name));
              askOperarion();
            });
            break;

          case "3":
            rl.question(
              "Ingresa el nombre actual del contacto: ",
              function (currentName) {
                rl.question(
                  "Ingresa el nuevo nombre del contacto o presiona enter para no modificarlo: ",
                  function (newName) {
                    rl.question(
                      "Ingresa el nuevo telefono del contacto o presiona enter para no modificarlo: ",
                      function (newPhone) {
                        console.log(
                          updateContact(
                            currentName,
                            newName || null,
                            newPhone || null
                          )
                        );
                        askOperarion();
                      }
                    );
                  }
                );
              }
            );
            break;

          case "4":
            rl.question(
              "Ingresa el nombre del contacto a eliminar: ",
              function (name) {
                console.log(deleteContact(name));
                askOperarion();
              }
            );
            break;

          case "5":
            rl.question(
              "Como desea ordenar los contactos? \n 1 - Por nombre \n 2 - Por telefono \n",
              function (sortOption) {
                if (sortOption === "1") {
                  sortContactByName();
                } else if (sortOption === "2") {
                  sortContactByPhone();
                } else {
                  console.log("Operacion no valida");
                }
                askOperarion();
              }
            );
            break;

          case "6":
            console.log(schedule);
            askOperarion();
            break;

          case "7":
            rl.close();
            break;
          default:
            console.log("Operacion no valida");
            askOperarion();
            break;
        }
      }
    );
  }
  askOperarion();
}

promptUser();
