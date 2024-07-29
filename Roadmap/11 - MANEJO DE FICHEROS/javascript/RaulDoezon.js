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

const createTextFile = () => {
  let contenido = ["Raúl\n32\nJavaScript"];
  const link = document.createElement("a");
  let archivo = new Blob([contenido], { type: 'text/plain' });
  const url = URL.createObjectURL(archivo);
  const textFile = archivo.text();

  console.log("contenido del archivo:");
  console.log(textFile);
  link.href = url;
  link.download = "RaulDoezon.txt";

  console.log("Nombre del archivo:");
  console.log(link.download);
  // link.click();
  URL.revokeObjectURL(url);
}

createTextFile()
