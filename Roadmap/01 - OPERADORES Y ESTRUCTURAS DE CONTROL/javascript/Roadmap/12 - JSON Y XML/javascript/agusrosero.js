/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

// EJERCICIO:

const fs = require("node:fs");

const content = {
  nombre: "Hernan",
  edad: 23,
  fechaNacimiento: "03-08-00",
  lenguajes: "Python, Javascript",
};

// XML
fs.writeFile("test.xml", JSON.stringify(content), (err) => {
  if (err) {
    console.error(err);
  }
  console.log("El archivo fue guardado..");

  fs.readFile("test.xml", "utf-8", (error, data) => {
    if (error) {
      console.log("Error al leer el archivo.");
      return;
    }
    console.log("Contenido del archivo:", data);
  });

  fs.unlink("test.xml", (error) => {
    if (error) {
      console.log("Error al borrar el archivo", error);
    }
    console.log("Archivo borrado correctamente");
  });
});

// JSON
fs.writeFile("test.json", JSON.stringify(content), (err) => {
  if (err) {
    console.error(err);
  }
  console.log("El archivo fue guardado..");

  fs.readFile("test.json", "utf-8", (error, data) => {
    if (error) {
      console.log("Error al leer el archivo.");
      return;
    }
    console.log("Contenido del archivo:", data);
  });

  fs.unlink("test.json", (error) => {
    if (error) {
      console.log("Error al borrar el archivo", error);
    }
    console.log("Archivo borrado correctamente");
  });
});
