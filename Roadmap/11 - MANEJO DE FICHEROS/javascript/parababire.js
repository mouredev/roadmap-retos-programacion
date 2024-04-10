const { File } = require('buffer');
const { log } = require('console');
const fs = require('fs');
const readline = require('readline');
const userName = "parababire";
const fileName = `${userName}.txt`;
const fileContent = "Nombre: Ángel Narváez.\nEdad: 44 años.\nLenguaje de programación: Javascript."

fs.open(fileName, "w", (err, fd) => {
  if (err) throw err;
  fs.appendFile(fileName, fileContent, (err) => {
    if (err) throw err;
    fs.readFile(fileName, "utf8", (err, data) => {
      if (err) throw err;
      console.log(data);
    })
    console.log("Datos agregados");
    const borrado = () => {
      fs.unlink(fileName, err => {
        if (err) throw err;
        console.log("Archivo borrado");
      });
      rl.close();
    };
    setTimeout(borrado, 5000);
  });
  console.log("archivo abierto");
});

//Extra
let rl = readline.createInterface(process.stdin, process.stdout);

const leerArchivo = () => {
  try {
    return fs.readFileSync(fileName, "utf8").split("\n");
  } catch (error) {
    console.log("Archivo no encontrado");
    return [];
  }
}

const crearProducto = () => {
  rl.question("Nombre del producto: ", nombre => {
    rl.question("Cantidad del producto: ", cantidad => {
      rl.question("Precio del producto: ", precio => {
        const producto = `${nombre}, ${cantidad}, ${precio}\n`;
        fs.appendFile(fileName, `${producto}`, err => {
          if (err) throw err;
          console.log("Producto creado");
          menu();
          selecionarOperacion();
        })
      });
    });
  });
}

const consultarProducto = () => {
  rl.question("Producto solicitado: ", (nombre) => {
    const data = leerArchivo();
      const productoBuscado = data.find((producto) => producto.split(",")[0] === nombre);
      if (productoBuscado) {
        console.log(productoBuscado);
        menu();
        selecionarOperacion();
      } else {
        console.log("Producto no encontrado");
        menu();
        selecionarOperacion();
      }
  });
}

const actualizarProducto = () => {
  rl.question("Nombre del producto: ", nombre => {
    rl.question("Cantidad del producto: ", cantidadNueva => {
      rl.question("Precio del producto: ", precioNuevo => {
        const inventario = leerArchivo();
        const productosActualizados = inventario.map(linea => {
          const [producto, cantidad, precio] = linea.split(", ");
          if (producto === nombre) {
            return `${nombre}, ${cantidadNueva}, ${precioNuevo}`;
          }
          return linea;
        });
        fs.writeFile(fileName, productosActualizados.join("\n"), err => {
          if (err) throw err;
          console.log("Producto actualizado");
          menu();
          selecionarOperacion();
        });
      });
    });
  });
}

const borrarProducto = () => {
  if (fs.existsSync(fileName)) {
    rl.question("Nombre del producto: ", nombre => {
      const inventario = leerArchivo();
      const productosActualizados = inventario.filter(linea => {
        const [producto, cantidad, precio] = linea.split(", ");
        if (producto !== nombre) {
          return `${linea}\n`;
        }
      });
      fs.writeFile(fileName, productosActualizados.join("\n"), err => {
        if (err) throw err;
        console.log("Producto borrado");
        menu();
        selecionarOperacion();
      });
    });
  } else {
    console.log("Archivo no existe");
    menu();
    selecionarOperacion();
  }
}

const mostrarProductos = () => {
  const producto = leerArchivo();
  console.log(producto.join("\n"));
  menu();
  selecionarOperacion();
}

const ventaTotal = () => {
  const ventas = leerArchivo();
  let total = 0;
  ventas.forEach((venta) => {
    const [_, cantidad, precio] = venta.split(", ");
    if (cantidad === undefined && precio === undefined) {
      return 0;
    } else {
      total += parseInt(cantidad) * parseFloat(precio);
    }
  });
  console.log(`Venta total: ${total}`);
  menu();
  selecionarOperacion();
}

const ventaPorProducto = () => {
  rl.question("Producto solicitado: ", (nombre) => {
    let total = 0;
    const data = leerArchivo();
    const productoBuscado = data.find((producto) => producto.split(",")[0] === nombre);
      if (productoBuscado) {
        total += parseInt(productoBuscado.split(",")[1]) * parseFloat(productoBuscado.split(",")[2]);
        console.log(`Total venta producto: ${total}`);
        menu();
        selecionarOperacion();
      } else {
        console.log("Producto no encontrado");
        menu();
        selecionarOperacion();
      }
  });
}

const cerrarPrograma = () => {
  fs.unlink(fileName, err => {
    if (err) console.log(err = "Archivo no creado");
    console.log("Saliste del programa");
  })
  rl.close();
}

const menu = () => {
  console.log("");
  console.log("1.- Anadir producto");
  console.log("2.- Consultar producto");
  console.log("3.- Actualizar producto");
  console.log("4.- Borrar producto");
  console.log("5.- Mostrar productos");
  console.log("6.- Calcular venta total");
  console.log("7.- Calcular venta por producto");
  console.log("8.- Salir");
  selecionarOperacion();
}

const selecionarOperacion = () => {
  rl.question("Elige una opción ", opcion => {
    switch (opcion) {
      case "1":
        crearProducto();
        break;
      case "2":
        consultarProducto();
        break;
      case "3":
        actualizarProducto();
        break;
      case "4":
        borrarProducto();
        break;
      case "5":
        mostrarProductos();
        break;
      case "6":
        ventaTotal();
        break;
      case "7":
        ventaPorProducto();
        break;
      case "8":
        cerrarPrograma();
        break;
    
      default:
        console.log("Ingresa una opción valida");
        menu();
        selecionarOperacion();
        break;
    }
  });
}
menu();
