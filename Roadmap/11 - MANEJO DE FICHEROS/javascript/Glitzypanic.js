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

// Ejercicio 1
const fs = require("fs");

const nombreArchivo = "Glitzypanic.txt";
const contenido = ["José Farías", "25", "javaScript"];
const contenidoFinal = contenido.join("\n");

function errorCrear(err) {
  if (err) {
    console.log("Error al crear el archivo");
    return;
  } else {
    console.log("Archivo creado");

    const datos = fs.readFileSync(nombreArchivo, { encoding: "utf-8" });
    console.log(datos);

    fs.unlink(nombreArchivo, errorBorrar);
  }
}

function errorBorrar(err) {
  if (err) {
    console.log("Error al borrar el archivo");
    return;
  } else {
    console.log("Archivo eliminado");
  }
}

function agregarProducto() {
  fs.writeFile(nombreArchivo, contenidoFinal, errorCrear);
}

agregarProducto();

//Ejercicio extra
const fs = require("fs");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const archivo = "inventario.txt";

function errorCrear(err) {
  if (err) {
    console.log("Error al crear el archivo");
    return;
  } else {
    console.log("Archivo creado");
  }
}

function errorBorrar(err) {
  if (err) {
    console.log("Error al borrar el archivo");
    return;
  } else {
    console.log("Archivo eliminado");
  }
}

function consultarProductos() {
  if (!fs.existsSync(archivo)) {
    console.log("No hay productos");
    menu();
    return;
  } else {
    const datos = fs.readFileSync(archivo, { encoding: "utf-8" });
    console.log(datos);
    menu();
  }
}

function agregarProducto() {
  if (!fs.existsSync(archivo)) {
    fs.writeFileSync(archivo, "", errorCrear);
  }
  rl.question("Nombre del producto: ", (nombre) => {
    rl.question("Cantidad vendida: ", (cantidad) => {
      rl.question("Precio: ", (precio) => {
        const cantidadNumero = Number(cantidad);
        const precioNumero = Number(precio);
        const producto = `${nombre}, ${cantidadNumero}, ${precioNumero}\n`;
        fs.appendFileSync(archivo, producto);
        menu();
      });
    });
  });
}

function actualizarProducto() {
  rl.question("Nombre del producto a actualizar: ", (nombre) => {
    const datos = fs.readFileSync(archivo, { encoding: "utf-8" });
    const productos = datos.split("\n");
    const producto = productos.find((p) => p.includes(nombre));
    if (producto) {
      rl.question("Nueva cantidad vendida: ", (cantidad) => {
        rl.question("Nuevo precio: ", (precio) => {
          const nuevoProducto = `${nombre}, ${cantidad}, ${precio}`;
          const nuevosProductos = productos.map((p) =>
            p.includes(nombre) ? nuevoProducto : p
          );
          fs.writeFileSync(archivo, nuevosProductos.join("\n"));
          menu();
        });
      });
    } else {
      console.log("Producto no encontrado");
      menu();
    }
  });
}

function eliminarProducto() {
  rl.question("Nombre del producto a eliminar: ", (nombre) => {
    const datos = fs.readFileSync(archivo, { encoding: "utf-8" });
    const productos = datos.split("\n");
    const producto = productos.find((p) => p.includes(nombre));
    if (producto) {
      const nuevosProductos = productos.filter((p) => !p.includes(nombre));
      fs.writeFileSync(archivo, nuevosProductos.join("\n"));
    } else {
      console.log("Producto no encontrado");
    }
    menu();
  });
}

function ventaTotal() {
  if (!fs.existsSync(archivo)) {
    console.log("No hay productos para calcular la venta total.");
    menu();
    return;
  }

  const datos = fs.readFileSync(archivo, { encoding: "utf-8" });
  const productos = datos.split("\n").filter((line) => line.trim() !== ""); // Filtrar líneas vacías
  let total = 0;

  productos.forEach((producto) => {
    const partes = producto.split(", ");
    if (partes.length === 3) {
      const precio = parseFloat(partes[2]); // Obtener el precio
      if (!isNaN(precio)) {
        total += precio; // Sumar el precio al total
      }
    }
  });

  console.log(`La venta total es: $${total.toFixed(2)}`);
  menu();
}

function salir() {
  fs.unlink(archivo, errorBorrar);
  rl.close();
}

function menu() {
  console.log("1. Consultar productos");
  console.log("2. Agregar producto");
  console.log("3. Actualizar producto");
  console.log("4. Eliminar producto");
  console.log("5. Venta total");
  console.log("6. Salir");
  rl.question("Opción: ", (opcion) => {
    switch (opcion) {
      case "1":
        consultarProductos();
        break;
      case "2":
        agregarProducto();
        break;
      case "3":
        actualizarProducto();
        break;
      case "4":
        eliminarProducto();
        break;
      case "5":
        ventaTotal();
        break;
      case "6":
        salir();
        break;
      default:
        console.log("Opción no válida");
        break;
    }
  });
}

menu();
