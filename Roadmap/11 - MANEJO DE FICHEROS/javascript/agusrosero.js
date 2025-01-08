/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

// EJERCICIO:
const fs = require("node:fs");

// Contenido
const nombre = "Hernan";
const edad = 23;
const lenguajeFavorito = "Python";
const content = `-${nombre}\n-${edad}\n-${lenguajeFavorito}`;

fs.writeFile("./agusrosero.txt", content, (err) => {
  if (err) {
    console.log(err);
  }
  console.log(content);

  // Eliminamos el archivo
  fs.unlink("./agusrosero.txt", function (err) {
    if (err) return console.log(err);
    console.log("Archivo eliminado con exito!");
  });
});
