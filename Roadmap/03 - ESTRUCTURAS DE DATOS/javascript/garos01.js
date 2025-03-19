// Creación de un arreglo
let miArreglo = [1, 2, 3, 4, 5];

// Inserción
miArreglo.push(6);

// Borrado
miArreglo.splice(2, 1); // Elimina el elemento en el índice 2

// Actualización
miArreglo[0] = 10;

// Ordenación
miArreglo.sort();

console.log(miArreglo);

// Creación de un objeto
let miObjeto = {
  clave1: "valor1",
  clave2: "valor2",
  clave3: "valor3",
};

// Inserción
miObjeto.clave4 = "valor4";

// Borrado
delete miObjeto.clave2;

// Actualización
miObjeto.clave1 = "nuevo_valor";

// No hay ordenación en los objetos, ya que son estructuras basadas en claves

console.log(miObjeto);

// Creación de un conjunto
let miConjunto = new Set([1, 2, 3, 4, 5]);

// Inserción
miConjunto.add(6);

// Borrado
miConjunto.delete(3);

// No hay actualización en los conjuntos, ya que los elementos son únicos

// No hay ordenación en los conjuntos, ya que son desordenados por naturaleza

console.log(miConjunto);

// Creación de un mapa
let miMapa = new Map([
  ["clave1", "valor1"],
  ["clave2", "valor2"],
  ["clave3", "valor3"],
]);

// Inserción
miMapa.set("clave4", "valor4");

// Borrado
miMapa.delete("clave2");

// Actualización
miMapa.set("clave1", "nuevo_valor");

// No hay ordenación en los mapas, ya que son estructuras basadas en claves

console.log(miMapa);

// Ejercicio extra
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const usuarios = {};
const identificadores = [];

function new_user() {
  rl.question("Ingrese el nombre: ", function (nombre) {
    let numero_telefono;
    do {
      numero_telefono = readlineSync.question(
        "Ingrese el numero de telefono: "
      );
      if (!/^\d{10}$/.test(numero_telefono)) {
        console.log("Error: El numero debe contener 10 digitos");
      }
    } while (!/^\d{10}$/.test(numero_telefono));

    const identificador = identificadores.length + 1;
    identificadores.push(identificador);

    usuarios[identificador] = { nombre, numero_telefono };

    console.log(
      `Usuario guardado correctamente. Identificador: ${identificador}, nombre: ${nombre}`
    );

    startMenu();
  });
}

function show_user(id_usuario) {
  if (id_usuario in usuarios) {
    const usuario = usuarios[id_usuario];
    console.log(`Informacion del usuario con ID ${id_usuario}`);
    console.log(`Nombre: ${usuario.nombre}`);
    console.log(`Numero de telefono: ${usuario.numero_telefono}`);
  } else {
    console.log(`No se encontro el usuario con ID ${id_usuario}`);
  }

  startMenu();
}

// ... (resto de las funciones sin cambios)

// Menú Principal
function startMenu() {
  console.log("\nMenú:");
  console.log("A.- Registrar nuevos usuarios");
  console.log("B.- Listar usuarios");
  console.log("C.- Ver información de un usuario por ID");
  console.log("D.- Editar información de un usuario por ID");
  console.log("E.- Eliminar usuario por ID");
  console.log("F.- Finalizar el programa");

  rl.question("Seleccione una opción (A/B/C/D/E/F): ", function (opcion) {
    opcion = opcion.toUpperCase();

    if (opcion === "A") {
      new_user();
    } else if (opcion === "B") {
      list_user();
    } else if (opcion === "C") {
      rl.question(
        "Ingrese el ID del usuario que desea ver: ",
        function (id_usuario) {
          show_user(parseInt(id_usuario, 10));
        }
      );
    } else if (opcion === "D") {
      rl.question(
        "Ingrese el ID del usuario que desea editar: ",
        function (id_usuario) {
          edit_user(parseInt(id_usuario, 10));
        }
      );
    } else if (opcion === "E") {
      rl.question(
        "Ingrese el ID del usuario que desea eliminar: ",
        function (id_usuario) {
          delete_user(parseInt(id_usuario, 10));
        }
      );
    } else if (opcion === "F") {
      console.log("Programa finalizado.");
      rl.close();
    } else {
      console.log(
        "Opción no válida. Por favor, seleccione una opción correcta."
      );
      startMenu();
    }
  });
}

startMenu();
