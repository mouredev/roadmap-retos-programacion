//const prompt = require('prompt-sync')();
const fsPromises = require('fs').promises;
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
      const borrado = () => {
        fs.unlink(fileName, err => {
          if (err) throw err;
          console.log("Archivo borrado");
        });
      } 
      setTimeout(borrado, 5000);
    })
    console.log("Datos agregados");
  });
  console.log("archivo abierto");
});

//Extra
/* let rl = readline.createInterface(process.stdin, process.stdout);

const leerArchivo = (archivo) => {
  fs.readFile(archivo, 'utf8', (err, data) => {
    if (err) throw err;
    return data.split("\n");
  });
}

const crearProducto = () => {
  rl.question("Nombre del producto: ", nombre => {
    rl.question("Cantidad del producto: ", cantidad => {
      rl.question("Precio del producto: ", precio => {
        const producto = `${nombre}, ${cantidad}, ${precio}\n`;
        fs.appendFile("producto.txt", `${producto}`, err => {
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
    const data = fs.readFileSync("producto.txt", "utf8");
      const productos = data.split("\n");
      const productoBuscado = productos.find((producto) => producto.split(",")[0] === nombre);
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
    rl.question("Cantidad del producto: ", cantidad => {
      rl.question("Precio del producto: ", precio => {
        //const productoActualizado = `${nombre}, ${cantidad}, ${precio}`;
        fs.open("producto.txt", "r", (err, data) => {
          if (err) throw err;
          console.log(data.toLocaleString());
          menu();
          selecionarOperacion();
        })
      });
    });
  });
}

const mostrarProductos = () => {
  fs.readFile("producto.txt", "utf8", (err, data) => {
    if (err) throw err;
    console.log(data);
    menu();
    selecionarOperacion();
  });
}

const cerrarPrograma = () => {
  fs.unlink("producto.txt", err => {
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
        
        break;
      case "5":
        mostrarProductos();
        break;
      case "6":
        
        break;
      case "7":
        
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
menu(); */

