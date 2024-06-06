/*#03 ESTRUCTURAS DE DATOS*/

// 1. Arrays

let arrayNumerico = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; // Array de números
let arrayString = ["Hola", "Mundo", "en", "Array", "!"]; // Array de strings
let arrayMixto = [1, "Hola", 2, "Mundo", 3, "en", 4, "Array", 5, "!"]; // Array mixto

// Insertando valores

arrayNumerico.push(11); // Inserta el valor 11 al final del array
//console.log(arrayNumerico); -> // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
arrayNumerico.unshift(0); // Inserta el valor 0 al inicio del array
//console.log(arrayNumerico); -> // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

// Eliminando valores

arrayNumerico.pop(); // Elimina el último valor del array
//console.log(arrayNumerico); -> // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arrayNumerico.shift(); // Elimina el primer valor del array
//console.log(arrayNumerico); -> // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arrayNumerico.splice(0, 5); // Elimina los primeros 5 valores del array
//console.log(arrayNumerico); -> // [6, 7, 8, 9, 10]

// Actualizando valores

arrayAlCuadrado = arrayNumerico.map((num) => Math.pow(num, 2)); // Eleva al cuadrado cada valor del array
// console.log(arrayAlCuadrado); // -> [36, 49, 64, 81, 100]

// Ordenando valores

arrayNumerico.sort((a, b) => b - a); // Ordena los valores de forma descendente
//console.log(arrayNumerico); // -> [10, 9, 8, 7, 6]

arrayNumerico.reverse(); // Invierte el orden de los valores del array
//console.log(arrayNumerico); // -> [6, 7, 8, 9, 10]

// 2. Objetos

let Programmer = {
  dev: "RobMxz",
  edad: 18,
  nacionalidad: "Peruana",
  lenguajes: ["JavaScript", "Python", "Java", "C++"],
};

let Gato = {
  nombre: "Yoko",
  raza: "Bengala",
  edad: 4,
};

// Array de Objetos

let arrayObjetos = [Programmer, Gato];

// Añadir un valor

Programmer["sexo"] = "Masculino";
//console.log(Programmer); // -> {dev: "RobMxz", edad: 18, nacionalidad: "Peruana", [ 'JavaScript', 'Python', 'Java', 'C++' ], sexo: "Masculino"}

// Actualizar un valor

Programmer["edad"] = 19;
//console.log(Programmer); // -> {dev: "RobMxz", edad: 19, nacionalidad: "Peruana", [ 'JavaScript', 'Python', 'Java', 'C++' ], sexo: "Masculino"}

// Eliminar un valor

delete Programmer["nacionalidad"];
//console.log(Programmer); // -> {dev: "RobMxz", edad: 19, [ 'JavaScript', 'Python', 'Java', 'C++' ], sexo: "Masculino"}

// Dificultad extra :)

/*
    DIFICULTAD EXTRA (opcional):
    Crea una agenda de contactos por terminal.
    Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
    Cada contacto debe tener un nombre y un número de teléfono.
    El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
    El programa no puede dejar introducir números de teléfono no númericos y con más
    de 11 dígitos (o el número de dígitos que quieras).
    También se debe proponer una operación de finalización del programa.
*/

const readline = require("readline");

let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let usuario = "RobMxz";

let contactos = [];

function agenda() {
  rl.question(options(), (respuesta) => {
    switch (respuesta) {
      case "1":
        añadirContacto();
        break;
      case "2":
        buscarContacto();
        break;
      case "3":
        actualizarContacto();
        break;
      case "4":
        eliminarContacto();
        break;
      case "5":
        console.log("\nAdios muchas gracias por usar la agenda ٩(◕‿◕｡)۶\n");
        rl.close();
        break;
      default:
        agenda();
        break;
    }
  });
}

function options() {
  return (
    `Hola ${usuario} !!!` +
    "\nEliga una opción ◑﹏◐ ( 1 - 5 )\n" +
    "1.Agrega un contacto 📱\n" +
    "2.Buscar un contacto\n" +
    "3.Actualizar un contacto\n" +
    "4.Eliminar un contacto\n" +
    "5.Salir\n" +
    "Opción: "
  );
}

function añadirContacto() {
  rl.question("Nombre: ", (nombre) => {
    if (contactos.find((contacto) => contacto.nombre === nombre)) {
      console.log("\nEl contacto ya existe\n");
      return agenda();
    }
    rl.question("Número: ", (numero) => {
      if (!verificacion(numero)) {
        console.log("\nNúmero no válido\n");
        return agenda();
      }
      if (contactos.find((contacto) => contacto.numero === numero)) {
        console.log("\nEl número ya existe\n");
        return agenda();
      }
      contactos.push({ nombre, numero });
      console.log("\nContacto añadido\n");
      agenda();
    });
  });
}

function buscarContacto() {
  if (contactos.length === 0) {
    console.log("\nNo hay contactos\n");
    return agenda();
  }
  rl.question("Indique el nombre del contacto ლ(╹◡╹ლ): ", (nombre) => {
    let contacto = contactos.find((contacto) => contacto.nombre === nombre);
    if (contacto) {
      console.log(`\nNombre: ${contacto.nombre}, Número: ${contacto.numero}\n`);
    } else {
      console.log("\nContacto no encontrado\n");
    }
    agenda();
  });
}

function actualizarContacto() {
  if (contactos.length === 0) {
    console.log("\nNo hay contactos\n");
    return agenda();
  }
  rl.question("Indique el nombre del contacto: ", (nombre) => {
    let contacto = contactos.find((contacto) => contacto.nombre === nombre);
    if (contacto) {
      rl.question("Nuevo número: ", (numero) => {
        if (!verificacion(numero)) {
          console.log("\nNúmero no válido\n");
          return agenda();
        }
        contacto.numero = numero;
        console.log("\nContacto actualizado\n");
        return agenda();
      });
    } else {
      console.log("\nContacto no encontrado\n");
      agenda();
    }
  });
}

function eliminarContacto() {
  if (contactos.length === 0) {
    console.log("\nNo hay contactos\n");
    return agenda();
  }
  rl.question("Indique el nombre del contacto: ", (nombre) => {
    let contacto = contactos.find((contacto) => contacto.nombre === nombre);
    if (contacto) {
      contactos = contactos.filter((contacto) => contacto.nombre !== nombre);
      console.log("\nContacto eliminado\n");
    } else {
      console.log("\nContacto no encontrado\n");
    }
    1;
    agenda();
  });
}

function verificacion(numero) {
  let regex = /^\d{9}$/;
  return regex.test(numero);
}
agenda();
