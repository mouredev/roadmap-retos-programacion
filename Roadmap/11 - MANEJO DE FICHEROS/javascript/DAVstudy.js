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
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

// // Importar modulo

const fs = require("fs");

// // Crear archivo
// fs.writeFile("DAVstudy.txt", "", (err) => {
//   if (err) throw err;
//   console.log("Archivo creado o sobreescrito exitosamente.");
// });

// // Escribir en archivo
// fs.writeFile("DAVstudy.txt", "Diego Arenas\n27\nJavaScript", (err) => {
//   if (err) throw err;
//   console.log("Archivo creado o sobreescrito exitosamente.");
// });

// // Leer archivo completo
// fs.readFile("DAVstudy.txt", "utf8", (err, data) => {
//   if (err) throw err;
//   console.log("Contenido del archivo:");
//   console.log(data);
// });

// // Eliminar un archivo
// fs.unlink("DAVstudy.txt", (err) => {
//   if (err) throw err;
//   console.log("Archivo eliminado.");
// });

/*
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

const myEcommerce = {
  nameFile: "",
  indexCurrentProduct: 0,
  currentProduct: "",
  currentQuantitySold: 0,
  currentPrice: 0,
  lastLineAdd: "",
  app: function (params) {},
  createFile: function (nameFile) {
    this.nameFile = `${nameFile}.txt`;
    fs.writeFileSync(
      this.nameFile,
      "nombre_producto,cantidad_vendida,precio\n"
    );
  },
  saveNewProduct: function (newLine) {
    fs.appendFileSync(this.nameFile, newLine);
  },
  updateProduct: function (product) {},
  findProduct: function (product) {
    const data = fs.readFileSync(this.nameFile, "utf8");
    const lines = data.split("\n");
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].split(",");
      if (line[0] === product) {
        this.currentProduct = line[0];
        this.currentQuantitySold = line[1];
        this.currentPrice = line[2];
        this.indexCurrentProduct = i;
      }
    }
  },
};



console.log(myEcommerce.createFile('product-solds-price'))
console.log(myEcommerce.saveNewProduct('toalla,2000,100\n'))
console.log(myEcommerce.saveNewProduct('cartas,400,100\n'))
