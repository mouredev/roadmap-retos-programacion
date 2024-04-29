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

/* USANDO ES MODULES DE NODE */

import { writeFileSync, readFileSync, unlinkSync, existsSync, appendFile } from "fs";

const txt = "Pancratzia.txt";
const content = ["Pancratzia", "24", "JavaScript"];

writeFileSync(txt, content.join("\n"));

const datos = readFileSync(txt, "utf-8");

console.log(`Datos del archivo ${txt}:`);
console.log(datos);

unlinkSync(txt);

/** SEGUNDA PARTE **/

import readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const fileName = "ventas.txt";

function agregarProductos() {
  rl.question("Ingrese el nombre del producto: ", (nombre) => {
    rl.question("Ingrese la cantidad vendida: ", (cantidad) => {
      rl.question("Ingrese el precio del producto: ", (precio) => {
        const data = `${nombre}, ${cantidad}, ${precio}\n`;
        appendFile(fileName, data, (err) => {
          if (err) {
            console.log(err);
            return;
          }
        })
        console.log("--------------------------------");
        console.log("Se agregó el producto: ", data);
        console.log("--------------------------------");
        mostrarMenu();
      });
    });
  });
}

function mostrarTotal() {
  const data = readFileSync(fileName, "utf8");
  let lines = data.split("\n");
  lines = lines.filter((line) => line !== "");
  let total = 0;
  for (const line of lines) {
    const [, cantidad, precio] = line.split(", ");
    total += parseInt(cantidad) * parseFloat(precio);
  }
  console.log(`Venta total: $${total.toFixed(2)}`);
  mostrarMenu();
}

function mostrarProductos() {
  const data = readFileSync(fileName, "utf8");
  let lines = data.split("\n");
  lines = lines.filter((line) => line !== "");
  for (const line of lines) {
    const [nombre, cantidad, precio] = line.split(", ");
    console.log(
      `Se han vendido ${cantidad} unidades de ${nombre} a ${precio}$. Por lo tanto, el total de la venta es ${parseFloat(
        (parseInt(cantidad) * parseFloat(precio)).toFixed(2)
      )}$`
    );
  }
  mostrarMenu();
}

function borrarProducto() {
  rl.question("Ingrese el nombre del producto a eliminar: ", (nombre) => {
    let newData = "";
    const data = readFileSync(fileName, "utf8");
    const lines = data.split("\n");
    for (const line of lines) {
      if (!line.startsWith(nombre)) {
        newData += line + "\n";
      }
    }
    writeFileSync(fileName, newData);
    console.log("--------------------------------");
    console.log("Se elimino el producto");
    console.log("--------------------------------");
    mostrarMenu();
  });
}

function eliminarArchivo() {
  unlinkSync(fileName);

  console.log("--------------------------------");
  console.log(`Se ha eliminado el archivo ${fileName}`);
  console.log("--------------------------------");
  console.log("¡HASTA PRONTO!")
  console.log("--------------------------------");
}

function mostrarMenu() {
  console.log("\n--- MENÚ ---");
  console.log("1. Añadir producto");
  console.log("2. Consultar venta total");
  console.log("3. Consultar venta por producto");
  console.log("4. Eliminar producto");
  console.log("5. Salir");

  rl.question("Seleccione una opción: ", (option) => {
    switch (option) {
      case "1":
        agregarProductos();
        break;
      case "2":
        mostrarTotal();
        break;
      case "3":
        mostrarProductos();
        break;
      case "4":
        borrarProducto();
        break;
      case "5":
        eliminarArchivo();
        rl.close();
        break;
      default:
        console.log("--------------------------------");
        console.log("Opción no válida. Seleccione una opción válida.");
        console.log("--------------------------------");
        mostrarMenu();
        break;
    }
  });
}

function inicio() {
  if (!existsSync(fileName)) {
    writeFileSync(fileName, "");
  }

  mostrarMenu();
}

inicio();
