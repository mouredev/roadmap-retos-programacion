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


let numeros = [0,1,2,3,4,5,6,7,8,9];

// 📌 Insertar
numeros.push(7); // Agrega al final
numeros.unshift(3); // Agrega al inicio

// 📌 Borrar
numeros.pop(); // Elimina el último
numeros.shift(); // Elimina el primero

// 📌 Actualizar
numeros[1] = 10; // Cambia el segundo elemento

// 📌 Ordenar
numeros.sort((a, b) => a - b); // Orden ascendente

console.log(numeros);


let persona = {
    nombre : "Juan" ,
    edad: 10,
    profesion: "programador",
    equipo: "",
}
// 🔹 Inserción
//persona[equipo] = "pikachu";
persona.edad = 11
// borrar
delete persona[edad];

//actualizacion


console.log (persona);


let user = {
    name: "John",
    age: 30
};

  Object.keys(user) = ["name", "age"]
  Object.values(user) = ["John", 30]
  Object.entries(user) = [ ["name","John"], ["age",30] ]


  //  * DIFICULTAD EXTRA (opcional):
//  * Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.


const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contactos = {}; // Diccionario para almacenar contactos

// Validar número de teléfono
const validarTelefono = (telefono) => {
  return /^\d{1,11}$/.test(telefono); // Solo números y máximo 11 dígitos
};

// Menú de opciones
const mostrarMenu = () => {
  console.log("\n📞 AGENDA DE CONTACTOS");
  console.log("1️⃣ Agregar contacto");
  console.log("2️⃣ Buscar contacto");
  console.log("3️⃣ Actualizar contacto");
  console.log("4️⃣ Eliminar contacto");
  console.log("5️⃣ Listar contactos");
  console.log("6️⃣ Salir\n");
  rl.question("Elige una opción: ", manejarOpcion);
};

// Manejar opción del usuario
const manejarOpcion = (opcion) => {
  switch (opcion) {
    case "1":
      agregarContacto();
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
      listarContactos();
      break;
    case "6":
      console.log("📴 Saliendo del programa...");
      rl.close();
      break;
    default:
      console.log("❌ Opción inválida, intenta de nuevo.");
      mostrarMenu();
  }
};

// Función para agregar un contacto
const agregarContacto = () => {
  rl.question("Nombre: ", (nombre) => {
    if (!nombre) {
      console.log("❌ El nombre no puede estar vacío.");
      return mostrarMenu();
    }

    rl.question("Teléfono: ", (telefono) => {
      if (!validarTelefono(telefono)) {
        console.log("❌ Teléfono inválido (máximo 11 dígitos, solo números).");
        return mostrarMenu();
      }

      contactos[nombre] = telefono;
      console.log(`✅ Contacto ${nombre} agregado.`);
      mostrarMenu();
    });
  });
};

// Función para buscar un contacto
const buscarContacto = () => {
  rl.question("Nombre del contacto a buscar: ", (nombre) => {
    if (contactos[nombre]) {
      console.log(`📞 ${nombre}: ${contactos[nombre]}`);
    } else {
      console.log("❌ Contacto no encontrado.");
    }
    mostrarMenu();
  });
};

// Función para actualizar un contacto
const actualizarContacto = () => {
  rl.question("Nombre del contacto a actualizar: ", (nombre) => {
    if (!contactos[nombre]) {
      console.log("❌ Contacto no encontrado.");
      return mostrarMenu();
    }

    rl.question("Nuevo teléfono: ", (telefono) => {
      if (!validarTelefono(telefono)) {
        console.log("❌ Teléfono inválido.");
        return mostrarMenu();
      }

      contactos[nombre] = telefono;
      console.log(`✅ Contacto ${nombre} actualizado.`);
      mostrarMenu();
    });
  });
};

// Función para eliminar un contacto
const eliminarContacto = () => {
  rl.question("Nombre del contacto a eliminar: ", (nombre) => {
    if (contactos[nombre]) {
      delete contactos[nombre];
      console.log(`🗑️ Contacto ${nombre} eliminado.`);
    } else {
      console.log("❌ Contacto no encontrado.");
    }
    mostrarMenu();
  });
};

// Función para listar todos los contactos
const listarContactos = () => {
  console.log("\n📋 Lista de contactos:");
  if (Object.keys(contactos).length === 0) {
    console.log("⚠️ No hay contactos guardados.");
  } else {
    for (let nombre in contactos) {
      console.log(`📞 ${nombre}: ${contactos[nombre]}`);
    }
  }
  mostrarMenu();
};

// Iniciar el programa
mostrarMenu();
