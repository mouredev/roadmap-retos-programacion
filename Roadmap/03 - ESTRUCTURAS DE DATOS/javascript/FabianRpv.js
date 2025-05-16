// Estructura de Datos

// Arrays

let autos = ["BMW", "Audi", "Mercedes", "Nissan"];
console.log(autos);

// Inserción en Arrays

const agregarAdelante = () => {
  let array = autos.slice();
  array.unshift("Ford"); // Agrega un elemento al inicio del array
  console.log(array);
};

agregarAdelante();

const agregarAlFinal = () => {
  let array = autos.slice();
  array.push("Ford"); // Agrega un elemento al final del array
  console.log(array);
};

agregarAlFinal();

// Borrado en Arrays

const eliminarAdelante = () => {
  let array = autos.slice();
  array.shift(); // Elimina el primer elemento del array
  console.log(array);
};

eliminarAdelante();

const eliminarAlFinal = () => {
  let array = autos.slice();
  array.pop(); // Elimina el último elemento del array
  console.log(array);
};

eliminarAlFinal();

const eliminarYAgregar = () => {
  let array = autos.slice();
  array.splice(2, 1, "Ford"); // Elimina un elemento y agrega otro
  console.log(array);
};

eliminarYAgregar();

// Actualizacion en Arrays

const actualizarElemento = () => {
  let array = autos.slice();
  array[1] = "McLaren"; // Actualiza un elemento del array
  console.log(array);
};

actualizarElemento();

// Ordenacion en Arrays

const ordenarAlfabeticamente = () => {
  let array = autos.slice();
  array.sort(); // Ordena alfabéticamente
  console.log(array);
};

ordenarAlfabeticamente();

const invertirOrden = () => {
  let array = autos.slice();
  array.reverse(); // Invierte el orden
  console.log(array);
};

invertirOrden();

// Sets

let frutas = new Set(["Manzana", "Pera", "Naranja", "Fresa"]);
console.log(frutas);

// Inserción en Sets

const agregarElemento = () => {
  let set = new Set(frutas);
  set.add("Mora");
  console.log(set);
};

agregarElemento();

// Borrado en Sets

const eliminarElemento = () => {
  let set = new Set(frutas);
  set.delete("Pera");
  console.log(set);
};

eliminarElemento();

// Saber si existe un valor en Sets

const existeValor = () => {
  let set = new Set(frutas);
  console.log(set.has("Piña"));
};

existeValor();

// Maps

let personas = new Map([
  ["nombre", "Fabian"],
  ["apellido", "Petit"],
  ["edad", 20],
]);

console.log(personas);

// Inserción en Maps

const agregarElementoMap = () => {
  let map = new Map(personas);
  map.set("sexo", "Masculino");
  console.log(map);
};

agregarElementoMap();

// Borrado en Maps

const eliminarElementoMap = () => {
  let map = new Map(personas);
  map.delete("apellido");
  console.log(map);
};

eliminarElementoMap();

// Actualizacion en Maps

const actualizarElementoMap = () => {
  let map = new Map(personas);
  map.set("edad", 25);
  console.log(map);
};

actualizarElementoMap();

// Obtener un valor en Maps

const obtenerValorMap = () => {
  let map = new Map(personas);
  console.log(map.get("nombre"));
};

obtenerValorMap();

// Saber si existe una clave en Maps

const existeClaveMap = () => {
  let map = new Map(personas);
  console.log(map.has("Ciudad"));
};

existeClaveMap();

// Objetos

let persona = {
  nombre: "Fabian",
  apellido: "Petit",
  edad: 20,
};

console.log(persona);

// Inserción en Objetos

persona.sexo = "Masculino";
console.log(persona);

// Borrado en Objetos

delete persona.sexo;
console.log(persona);

// Actualizacion en Objetos

persona.edad = 25;
console.log(persona);

/*
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos
y con más de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.
*/


const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const mostrarMenu = () => {
  console.log("1. Buscar contacto");
  console.log("2. Insertar contacto");
  console.log("3. Actualizar contacto");
  console.log("4. Eliminar contacto");
  console.log("5. Salir");
};

const buscarContacto = (nombre) => {
  return agenda.find((contacto) => contacto.nombre === nombre);
};

const insertarContacto = (nombre, telefono) => {
  if (/^\d{1,11}$/.test(telefono)) {
    agenda.push({ nombre, telefono });
    console.log(`Contacto "${nombre}" insertado correctamente.`);
  } else {
    console.log(
      "Numero de telefono no valido. Debe ser numerico y tener maximo 11 digitos."
    );
  }
};

const actualizarContacto = (nombre, nuevoTelefono) => {
  if (/^\d{1,11}$/.test(nuevoTelefono)) {
    const contacto = buscarContacto(nombre);
    if (contacto) {
      contacto.telefono = nuevoTelefono;
      console.log(`Contacto "${nombre}" actualizado correctamente.`);
    } else {
      console.log(`Contacto "${nombre}" no encontrado.`);
    }
  } else {
    console.log(
      "Numero de telefono no valido. Debe ser numerico y tener maximo 11 digitos."
    );
  }
};

const eliminarContacto = (nombre) => {
  const indice = agenda.findIndex((contacto) => contacto.nombre === nombre);
  if (indice !== -1) {
    agenda.splice(indice, 1);
    console.log(`Contacto "${nombre}" eliminado correctamente.`);
  } else {
    console.log(`Contacto "${nombre}" no encontrado.`);
  }
};

let agenda = [];

const iniciarAgenda = () => {

  mostrarMenu();
  rl.question("Seleccione una Opcion: ", (menu) => {

    switch (menu) {

      case "1":
        rl.question("Ingrese el nombre del contacto a buscar: ", (nombre) => {
          const contacto = buscarContacto(nombre);
          if (contacto) {
            console.log(
              `Contacto encontrado: Nombre: ${contacto.nombre}, Telefono: ${contacto.telefono}`
            );
          } else {
            console.log(`Contacto "${nombre}" no encontrado.`);
          }
          iniciarAgenda();
        });

        break;

      case "2":
        rl.question("Ingrese el nombre del contacto: ", (nombre) => {
          rl.question("Ingrese el numero de telefono: ", (telefono) => {
            insertarContacto(nombre, telefono);
            iniciarAgenda();
          });
        });

        break;

      case "3":
        rl.question("Ingrese el nombre del contacto a actualizar: ", (nombre) => {
            rl.question("Ingrese el nuevo numero de telefono: ", (nuevoTelefono) => {
                actualizarContacto(nombre, nuevoTelefono);
                iniciarAgenda();
              });
          });

        break;

      case "4":
        rl.question("Ingrese el nombre del contacto a eliminar: ", (nombre) => {
          eliminarContacto(nombre);
          iniciarAgenda();
        });

        break;

      case "5":
        console.log("Saliendo del programa...");
        rl.close();
        break;

      default:
        console.log("Opcion no valida");
    }
  });
};

iniciarAgenda();
