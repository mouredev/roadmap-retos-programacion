// Ejercicio 1: Crear un archivo con datos personales y leerlo
import * as fs from "fs";

const userName = "ialmontedr0";
const fileName = `${userName}.txt`;

let myData: {
  nombre: string;
  edad: number;
  lenguajeFavorito: string;
} = {
  nombre: "Anthony Almonte",
  edad: 26,
  lenguajeFavorito: "TypeScript",
};

// Escribimos en el archivo
fs.writeFile(
  fileName,
  `Nombre: ${myData.nombre}\nEdad: ${myData.edad}\nLenguaje Favorito: ${myData.lenguajeFavorito}`,
  (err) => {
    if (err) throw err;
    console.log(`El archivo "${fileName}" ha sido creado con éxito.`);

    // Lectura del archivo
    fs.readFile(fileName, "utf8", (err, data) => {
      if (err) throw err;
      console.log(`Contenido del archivo "${fileName}":\n${data}`);
      console.log(data);

      // Eliminar el archivo
      fs.unlink(fileName, (err) => {
        if (err) throw err;
        console.log(`El archivo "${fileName}" ha sido eliminado con éxito.`);
      });
    });
  }
);

// Ejercio 2: Crear archivo archivo.txt

import * as fs from "fs"; // Importa el módulo fs para operaciones de sistema de archivos
import * as readline from "readline"; // Importa el módulo readline para manejo de entrada y salida en la terminal

const salesFileName: string = "sales.txt"; // Nombre del archivo que almacenará los datos de ventas

// Crea una interfaz de readline para la entrada y salida de terminal
const rl: readline.Interface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para añadir un producto al archivo
function addProduct(): void {
  rl.question("Nombre del producto: ", (name: string) => {
    rl.question("Cantidad vendida: ", (quantity: string) => {
      rl.question("Precio: ", (price: string) => {
        const productLine: string = `${name}, ${quantity}, ${price}\n`; // Formato de la línea del producto
        fs.appendFileSync(salesFileName, productLine); // Añade la línea al archivo
        console.log("Producto añadido.");
        mainMenu(); // Regresa al menú principal
      });
    });
  });
}

// Función para consultar productos en el archivo
function viewProducts(): void {
  if (fs.existsSync(salesFileName)) {
    // Verifica si el archivo existe
    const data: string = fs.readFileSync(salesFileName, "utf8"); // Lee el contenido del archivo
    console.log("Productos:\n" + data); // Imprime los productos
  } else {
    console.log("No hay productos para mostrar.");
  }
  mainMenu(); // Regresa al menú principal
}

// Función para actualizar un producto en el archivo
function updateProduct(): void {
  if (!fs.existsSync(salesFileName)) {
    // Verifica si el archivo existe
    console.log("No hay productos para actualizar.");
    return mainMenu(); // Regresa al menú principal si no hay productos
  }

  const data: string[] = fs.readFileSync(salesFileName, "utf8").split("\n"); // Lee y divide el contenido del archivo en líneas

  rl.question("Nombre del producto a actualizar: ", (name: string) => {
    const index: number = data.findIndex((line) => line.startsWith(`${name},`)); // Encuentra el índice del producto
    if (index === -1) {
      console.log("Producto no encontrado.");
      return mainMenu(); // Regresa al menú principal si el producto no se encuentra
    }

    rl.question("Nueva cantidad vendida: ", (newQuantity: string) => {
      rl.question("Nuevo precio: ", (newPrice: string) => {
        data[index] = `${name}, ${newQuantity}, ${newPrice}`; // Actualiza la línea del producto
        fs.writeFileSync(salesFileName, data.join("\n")); // Escribe los cambios en el archivo
        console.log("Producto actualizado.");
        mainMenu(); // Regresa al menú principal
      });
    });
  });
}

// Función para eliminar un producto del archivo
function deleteProduct(): void {
  if (!fs.existsSync(salesFileName)) {
    // Verifica si el archivo existe
    console.log("No hay productos para eliminar.");
    return mainMenu(); // Regresa al menú principal si no hay productos
  }

  const data: string[] = fs.readFileSync(salesFileName, "utf8").split("\n"); // Lee y divide el contenido del archivo en líneas

  rl.question("Nombre del producto a eliminar: ", (name: string) => {
    const index: number = data.findIndex((line) => line.startsWith(`${name},`)); // Encuentra el índice del producto
    if (index === -1) {
      console.log("Producto no encontrado.");
      return mainMenu(); // Regresa al menú principal si el producto no se encuentra
    }

    data.splice(index, 1); // Elimina la línea del producto
    fs.writeFileSync(salesFileName, data.join("\n")); // Escribe los cambios en el archivo
    console.log("Producto eliminado.");
    mainMenu(); // Regresa al menú principal
  });
}

// Función para calcular la venta total y por producto
function calculateSales(): void {
  if (!fs.existsSync(salesFileName)) {
    // Verifica si el archivo existe
    console.log("No hay productos para calcular.");
    return mainMenu(); // Regresa al menú principal si no hay productos
  }

  const data: string[] = fs.readFileSync(salesFileName, "utf8").split("\n"); // Lee y divide el contenido del archivo en líneas

  let totalSales: number = 0;
  const salesByProduct: Record<string, number> = {};

  data.forEach((line) => {
    if (line.trim() === "") return; // Ignora líneas vacías
    const [name, quantity, price] = line.split(", ");
    const sale: number = parseInt(quantity) * parseFloat(price); // Calcula la venta de cada producto
    totalSales += sale;
    if (!salesByProduct[name]) {
      salesByProduct[name] = 0;
    }
    salesByProduct[name] += sale; // Acumula la venta por producto
  });

  console.log("Venta total:", totalSales.toFixed(2)); // Imprime la venta total
  console.log("Venta por producto:");
  for (const [name, sale] of Object.entries(salesByProduct)) {
    console.log(`${name}: ${sale.toFixed(2)}`); // Imprime la venta por cada producto
  }

  mainMenu(); // Regresa al menú principal
}

// Función para salir y borrar el archivo
function exitProgram(): void {
  if (fs.existsSync(salesFileName)) {
    fs.unlinkSync(salesFileName); // Elimina el archivo si existe
    console.log(`Archivo ${salesFileName} borrado.`);
  }
  rl.close(); // Cierra la interfaz de readline
}

// Menú principal
function mainMenu(): void {
  console.log(`
    1. Añadir producto
    2. Consultar productos
    3. Actualizar producto
    4. Eliminar producto
    5. Calcular ventas
    6. Salir
    `);

  rl.question("Elige una opción: ", (option: string) => {
    switch (option) {
      case "1":
        addProduct();
        break;
      case "2":
        viewProducts();
        break;
      case "3":
        updateProduct();
        break;
      case "4":
        deleteProduct();
        break;
      case "5":
        calculateSales();
        break;
      case "6":
        exitProgram();
        break;
      default:
        console.log("Opción no válida.");
        mainMenu();
        break;
    }
  });
}

// Inicia el programa mostrando el menú principal
mainMenu();
