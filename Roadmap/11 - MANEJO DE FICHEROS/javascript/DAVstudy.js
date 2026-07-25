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
const readline = require("readline");
const read = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
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
  createFile: function (nameFile) {
    this.nameFile = `${nameFile}.txt`;
    fs.writeFileSync(this.nameFile, "nombre_producto,cantidad_vendida,precio");
    return "Archivo Creado";
  },
  addProduct: function (newLine) {
    fs.appendFileSync(this.nameFile, "\n" + newLine);
    return "Nuevo producto agregado";
  },
  updateProduct: function (
    product,
    newProduct = "",
    quantitySold = "",
    price = ""
  ) {
    const dataUpdate = [];
    const data = fs.readFileSync(this.nameFile, "utf8");
    const lines = data.split("\n");
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].split(",");
      if (line[0] === product) {
        if (newProduct !== "") {
          line[0] = newProduct;
        }
        if (quantitySold !== "") {
          line[1] = quantitySold;
        }
        if (price !== "") {
          line[2] = price;
        }
        dataUpdate.push(line.join(","));
      } else {
        dataUpdate.push(lines[i]);
      }
    }
    fs.writeFileSync(this.nameFile, dataUpdate.join("\n"));
    return "Archivo actualizado";
  },
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
        return "Producto encontrado";
      }
    }
    return "El producto no existe";
  },
  deleteProduct: function (product) {
    const dataUpdate = [];
    const data = fs.readFileSync(this.nameFile, "utf8");
    const lines = data.split("\n");
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].split(",");
      if (line[0] === product) {
        continue;
      } else {
        dataUpdate.push(lines[i]);
      }
    }
    fs.writeFileSync(this.nameFile, dataUpdate.join("\n"));
    return "Producto eliminado";
  },
  calculateSells: function (product) {
    this.findProduct(product);
    return Number(this.currentQuantitySold) * Number(this.currentPrice);
  },
};

// console.log(myEcommerce.createFile("product-solds-price"));
// console.log(myEcommerce.addProduct("\nToalla,2000,100"));
// console.log(myEcommerce.addProduct("\nCartas,400,100"));
// console.log(myEcommerce.findProduct("toalla"));
// console.log(myEcommerce.currentProduct);
// console.log(myEcommerce.updateProduct("Toalla", "Toallas", "10", "100"));
// console.log(myEcommerce.deleteProduct("Cartas"));
// console.log(myEcommerce.calculateSells("Toallas"));


myEcommerce.createFile('data');
app = () => {
  
  read.question(
    `Ecommerce: 
      1. Agregar producto
      2. Actualizar producto
      3. Buscar producto
      4. Cantidad de ventas de un producto 
      5. Eliminar producto
      0. Cerrar (elimina el archivo)
      Ingrese su opcion: `,
    (option = (option) => {
      switch (option) {
        case "1":
          read.question(`Ingrese el nombre del producto: `, (name) => {
            read.question(`Ingrese la cantidad de ventas: `, (quantitySold) => {
              read.question(`Ingrese el precio: `, (price) => {
                const line = [name, quantitySold, price]
                console.log(myEcommerce.addProduct(line.join(',')))
                app();
              });
            });
          });
          break;
        case "2":
          read.question(
            `Ingrese el nombre del producto a modificar`,
            (name) => {
              read.question(`Desea cambiar el nombre? `, (answer) => {
                answer.toLowerCase() === "si"
                  ? read.question(`Ingrese el nuevo nombre: `, (newName) =>
                      read.question(
                        `Desea cambiar la cantidad de ventas? `,
                        (answer) => {
                          answer.toLowerCase() === "si"
                            ? read.question(
                                `Ingrese la cantidad de ventas: `,
                                (newQuantity) =>
                                  read.question(
                                    `Desea cambiar el precio? `,
                                    (answer) => {
                                      answer.toLowerCase() === "si"
                                        ? read.question(
                                            `Ingrese el precio: `,
                                            (newPrice) => {
                                              console.log(
                                                myEcommerce.updateProduct(
                                                  name,
                                                  newName,
                                                  newQuantity,
                                                  newPrice
                                                )
                                              )
                                            })
                                        : console.log(
                                            myEcommerce.updateProduct(
                                              name,
                                              newName,
                                              newQuantity
                                            )
                                          );
                                    }
                                  )
                              )
                            : read.question(
                                `Desea cambiar el precio? `,
                                (answer) => {
                                  answer.toLowerCase() === "si"
                                    ? read.question(
                                        `Ingrese el precio: `,
                                        (newPrice) =>
                                          console.log(
                                            myEcommerce.updateProduct(
                                              name,
                                              newName,
                                              "",
                                              newPrice
                                            )
                                          )
                                      )
                                    : console.log(
                                        myEcommerce.updateProduct(
                                          name,
                                          newName,
                                          "",
                                          ""
                                        )
                                      );
                                }
                              );
                        }
                      )
                    )
                  : read.question(
                      `Desea cambiar la cantidad de ventas? `,
                      (answer) => {
                        answer.toLowerCase() === "si"
                          ? read.question(
                              `Ingrese la cantidad de ventas: `,
                              (newQuantity) =>
                                read.question(
                                  `Desea cambiar el precio? `,
                                  (answer) => {
                                    answer.toLowerCase() === "si"
                                      ? read.question(
                                          `Ingrese el precio: `,
                                          (newPrice) =>
                                            console.log(
                                              myEcommerce.updateProduct(
                                                name,
                                                "",
                                                newQuantity,
                                                newPrice
                                              )
                                            )
                                        )
                                      : console.log(
                                          myEcommerce.updateProduct(
                                            name,
                                            "",
                                            newQuantity
                                          )
                                        );
                                  }
                                )
                            )
                          : read.question(
                              `Desea cambiar el precio? `,
                              (answer) => {
                                answer.toLowerCase() === "si"
                                  ? read.question(
                                      `Ingrese el precio: `,
                                      (newPrice) =>
                                        console.log(
                                          myEcommerce.updateProduct(
                                            name,
                                            "",
                                            "",
                                            newPrice
                                          )
                                        )
                                    )
                                  : console.log("No hubo ningun cambio");
                              }
                            );
                      }
                    );
              });
            }
          );
          app();
          break;
        case '3':
          read.question(`Ingrese el nombre del producto: `, (name) => {
            console.log(myEcommerce.findProduct(name))
            app();
          });
          break;
        case '4':
            read.question(`Ingrese el nombre del producto: `, (name) => {
              console.log(myEcommerce.calculateSells(name))
              app();
            });
            break;  
        case '5':
          read.question(`Ingrese el nombre del producto: `, (name) => {
            console.log(myEcommerce.deleteProduct(name))
            app();
          });
          break;
        case '0':
            fs.unlinkSync(myEcommerce.nameFile)
            read.close()
            break;
        default:
          app();      
          break;
      }
    })
  );
};

app();
