const fs = require("fs");

// Obtener el nombre de usuario de GitHub
const username = "GAROS01";

// Crear el nombre del archivo con extensión .txt
const filename = `${username}.txt`;

// Contenido a escribir en el archivo
const content = `Nombre: Oscar Garzon\nEdad: 29\nLenguaje de programación favorito: Python y JavaScript\n`;

// Escribir en el archivo
fs.writeFile(filename, content, (err) => {
  if (err) {
    console.error("Error al escribir en el archivo:", err);
    return;
  }
  console.log("Archivo creado y contenido agregado correctamente.");

  // Leer el contenido del archivo y mostrarlo
  fs.readFile(filename, "utf8", (err, data) => {
    if (err) {
      console.error("Error al leer el archivo:", err);
      return;
    }
    console.log("Contenido del archivo:");
    console.log(data);

    // Borrar el archivo
    fs.unlink(filename, (err) => {
      if (err) {
        console.error("Error al borrar el archivo:", err);
        return;
      }
      console.log(`El archivo ${filename} ha sido borrado.`);
    });
  });
});

// Ejercicio estra

const readline = require("readline");

const archivo = "ventas.txt";

function leerArchivo() {
  try {
    return fs.readFileSync(archivo, "utf8").split("\n");
  } catch (error) {
    console.log("No hay ventas registradas.");
    return [];
  }
}

function guardarVenta(nombreProducto, cantidad, precio) {
  fs.appendFileSync(archivo, `${nombreProducto}, ${cantidad}, ${precio}\n`);
}

function mostrarVentas() {
  const ventas = leerArchivo();
  if (ventas.length > 0) {
    console.log("Ventas realizadas:");
    ventas.forEach((venta) => console.log(venta.trim()));
  } else {
    console.log("No hay ventas registradas.");
  }
}

function actualizarVenta(nombreProducto, nuevaCantidad, nuevoPrecio) {
  const ventas = leerArchivo();
  const nuevasVentas = ventas.map((venta) => {
    const [producto, cantidad, precio] = venta.split(", ");
    if (producto === nombreProducto) {
      return `${nombreProducto}, ${nuevaCantidad}, ${nuevoPrecio}`;
    }
    return venta;
  });
  fs.writeFileSync(archivo, nuevasVentas.join("\n"));
}

function eliminarVenta(nombreProducto) {
  const ventas = leerArchivo();
  const nuevasVentas = ventas.filter((venta) => {
    const [producto] = venta.split(", ");
    return producto !== nombreProducto;
  });
  fs.writeFileSync(archivo, nuevasVentas.join("\n"));
}

function calcularVentaTotal() {
  const ventas = leerArchivo();
  let total = 0;
  ventas.forEach((venta) => {
    const [_, cantidad, precio] = venta.split(", ");
    total += parseInt(cantidad) * parseFloat(precio);
  });
  console.log(`Venta total: ${total}`);
}

function calcularVentaProducto(nombreProducto) {
  const ventas = leerArchivo();
  const ventaProducto = ventas.find((venta) => {
    const [producto, _, __] = venta.split(", ");
    return producto === nombreProducto;
  });
  if (ventaProducto) {
    const [_, cantidad, precio] = ventaProducto.split(", ");
    console.log(
      `Venta de ${nombreProducto}: ${parseInt(cantidad) * parseFloat(precio)}`
    );
  } else {
    console.log(`No se encontró la venta del producto ${nombreProducto}`);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function menu() {
  console.log("\nMenú:");
  console.log("1. Añadir venta");
  console.log("2. Consultar ventas");
  console.log("3. Actualizar venta");
  console.log("4. Eliminar venta");
  console.log("5. Calcular venta total");
  console.log("6. Calcular venta por producto");
  console.log("7. Salir y borrar archivo");
  rl.question("Seleccione una opción: ", function (opcion) {
    switch (opcion) {
      case "1":
        rl.question(
          "Ingrese el nombre del producto: ",
          function (nombreProducto) {
            rl.question("Ingrese la cantidad vendida: ", function (cantidad) {
              rl.question("Ingrese el precio unitario: ", function (precio) {
                guardarVenta(nombreProducto, cantidad, precio);
                menu();
              });
            });
          }
        );
        break;
      case "2":
        mostrarVentas();
        menu();
        break;
      case "3":
        rl.question(
          "Ingrese el nombre del producto a actualizar: ",
          function (nombreProducto) {
            rl.question(
              "Ingrese la nueva cantidad vendida: ",
              function (nuevaCantidad) {
                rl.question(
                  "Ingrese el nuevo precio unitario: ",
                  function (nuevoPrecio) {
                    actualizarVenta(nombreProducto, nuevaCantidad, nuevoPrecio);
                    menu();
                  }
                );
              }
            );
          }
        );
        break;
      case "4":
        rl.question(
          "Ingrese el nombre del producto a eliminar: ",
          function (nombreProducto) {
            eliminarVenta(nombreProducto);
            menu();
          }
        );
        break;
      case "5":
        calcularVentaTotal();
        menu();
        break;
      case "6":
        rl.question(
          "Ingrese el nombre del producto para calcular su venta: ",
          function (nombreProducto) {
            calcularVentaProducto(nombreProducto);
            menu();
          }
        );
        break;
      case "7":
        fs.unlinkSync(archivo);
        console.log("Archivo borrado. Saliendo del programa.");
        rl.close();
        break;
      default:
        console.log("Opción no válida. Inténtelo de nuevo.");
        menu();
        break;
    }
  });
}

menu();
