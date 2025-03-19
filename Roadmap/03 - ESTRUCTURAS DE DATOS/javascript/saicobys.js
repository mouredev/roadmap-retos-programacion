/* Creación */
/* Arrays */

// Ejemplo de array de numeros
const numeros = [1, 2, 3, 4, 5];

// Ejemplo de array de strings
const nombres = ["Juan", "Maria", "Pedro"];

// Ejemplo de array mixto
const datos = [1, "Hola", true, { nombre: "Pedro" }];

/* Operaciones basicas */
/* Insercion */

// Agregar un numero al final del array "numeros"
numeros.push(6);
console.log(numeros);

// Agregar un nombre al inicio del array "nombres"
nombres.unshift("Ana");
console.log(nombres);

// Insertar el string "Hola" en el indice 2 del array "datos"
datos.splice(2, 0, "Hola");
console.log(datos);

/* Borrar */

// Eliminar el ultimo numero del array "numeros" y guardarlo en una variable
const numeroEliminado = numeros.pop();
console.log(numeroEliminado);
console.log(numeros);

// Eliminar el primer nombre del array "nombres" y guardarlo en una variable
const nombreEliminado = nombres.shift();
console.log(nombreEliminado);
console.log(nombres);

// Eliminar dos elementos a partir del indice 2 del array "datos"
datos.splice(2, 2);
console.log(datos);

/* Actualización */

// Actualizar el nombre de la segunda fruta en el array "frutas"
frutas[1] = "Uva";
console.log(frutas);

/* Ordenación */

// Ordenar alfabeticamente el array "nombres"
nombres.sort();
console.log(nombres);

// Ordenar el array "productos" por precio de menor a mayor
productos.sort((a, b) => a.precio - b.precio);
console.log(productos);

/* Objects */

// Ejemplo de objeto con propiedades de tipo string
const persona = {
  nombre: "Juan",
  edad: 30,
  ciudad: "Madrid",
};

// Ejemplo de objeto con propiedades de diferentes tipos
const producto = {
  id: 1,
  nombre: "Producto X",
  precio: 12.5,
  disponible: true,
};

/* Acceso a propiedades */

// Acceder al nombre del usuario en el objeto "usuario"
const nombreUsuario = usuario.nombre;
console.log;

/* DIFICULTAD EXTRA */

const contactos = []; // Array para almacenar los contactos

function validarTelefono(telefono) {
  // Validación del número de teléfono (puedes ajustar los criterios)
  return /^\d{10}$/.test(telefono); // Ejemplo: 10 dígitos numéricos
}

while (true) {
  const opcion = prompt(
    "Elija una opción:\n" +
      "1. Agregar contacto\n" +
      "2. Buscar contacto\n" +
      "3. Actualizar contacto\n" +
      "4. Eliminar contacto\n" +
      "5. Mostrar todos los contactos\n" +
      "6. Salir"
  );

  switch (opcion) {
    case "1":
      const nombre = prompt("Ingrese el nombre del contacto:");
      let telefono;
      do {
        telefono = prompt("Ingrese el número de teléfono (10 dígitos):");
      } while (!validarTelefono(telefono));
      contactos.push({ nombre, telefono });
      alert("Contacto agregado exitosamente!");
      break;

    case "2":
      const terminoBusqueda = prompt("Ingrese el nombre o teléfono a buscar:");
      const resultados = contactos.filter(
        (c) =>
          c.nombre.includes(terminoBusqueda) ||
          c.telefono.includes(terminoBusqueda)
      );
      if (resultados.length > 0) {
        alert(
          resultados
            .map((c) => `Nombre: ${c.nombre}, Teléfono: ${c.telefono}`)
            .join("\n")
        );
      } else {
        alert("No se encontraron contactos.");
      }
      break;

    // ... (Casos 3, 4, 5 para actualizar, eliminar y mostrar todos los contactos)

    case "6":
      alert("Saliendo del programa...");
      process.exit(0);
      break;

    default:
      alert("Opción inválida.");
  }
}
