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
/*
const fs = require('fs');
const path = require('path');

const githubUsername = 'giovanyosorio';
const filename = `${githubUsername}.txt`;
const filePath = path.join(__dirname, filename);

// Crear y escribir en el archivo
fs.writeFileSync(filePath, 'Tu nombre\nEdad\nLenguaje de programación favorito');

// Leer e imprimir el contenido del archivo
const content = fs.readFileSync(filePath, 'utf8');
console.log(content);

// Borrar el archivo
fs.unlinkSync(filePath);


const fs = require('fs');
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
*/
const fs = require('fs');
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const filename = 'ventas.txt';

const addProduct = () => {
  rl.question('Introduce el nombre del producto: ', (name) => {
    rl.question('Introduce la cantidad vendida: ', (quantity) => {
      rl.question('Introduce el precio: ', (price) => {
        const newProduct = `${name}, ${quantity}, ${price}\n`;
        fs.appendFileSync(filename, newProduct);
        console.log('Producto añadido correctamente.');
        mainMenu();
      });
    });
  });
};

const viewProducts = () => {
  const data = fs.readFileSync(filename, 'utf8');
  console.log('\nProductos:\n' + data);
  mainMenu();
};

const updateProduct = () => {
  rl.question('Introduce el nombre del producto a actualizar: ', (name) => {
    const data = fs.readFileSync(filename, 'utf8');
    const lines = data.split('\n');
    let found = false;

    for (let i = 0; i < lines.length; i++) {
      if (lines[i].startsWith(name + ',')) {
        found = true;
        rl.question('Introduce la nueva cantidad vendida: ', (quantity) => {
          rl.question('Introduce el nuevo precio: ', (price) => {
            lines[i] = `${name}, ${quantity}, ${price}`;
            fs.writeFileSync(filename, lines.join('\n'));
            console.log('Producto actualizado correctamente.');
            mainMenu();
          });
        });
        break;
      }
    }

    if (!found) {
      console.log('Producto no encontrado.');
      mainMenu();
    }
  });
};

const deleteProduct = () => {
  rl.question('Introduce el nombre del producto a eliminar: ', (name) => {
    const data = fs.readFileSync(filename, 'utf8');
    const lines = data.split('\n');
    const filteredLines = lines.filter(line => !line.startsWith(name + ','));

    if (lines.length !== filteredLines.length) {
      fs.writeFileSync(filename, filteredLines.join('\n'));
      console.log('Producto eliminado correctamente.');
    } else {
      console.log('Producto no encontrado.');
    }
    mainMenu();
  });
};

const calculateTotalSales = () => {
  const data = fs.readFileSync(filename, 'utf8');
  const lines = data.split('\n');
  let total = 0;

  lines.forEach(line => {
    const parts = line.split(', ');
    if (parts.length === 3) {
      total += parseInt(parts[1]) * parseFloat(parts[2]);
    }
  });

  console.log(`Venta total: ${total}`);
  mainMenu();
};

const calculateSalesByProduct = () => {
  rl.question('Introduce el nombre del producto: ', (name) => {
    const data = fs.readFileSync(filename, 'utf8');
    const lines = data.split('\n');
    let found = false;

    lines.forEach(line => {
      const parts = line.split(', ');
      if (parts.length === 3 && parts[0] === name) {
        found = true;
        const total = parseInt(parts[1]) * parseFloat(parts[2]);
        console.log(`Venta total para ${name}: ${total}`);
      }
    });

    if (!found) {
      console.log('Producto no encontrado.');
    }
    mainMenu();
  });
};

const mainMenu = () => {
  console.log('\nGestión de ventas:');
  console.log('1. Añadir producto');
  console.log('2. Consultar productos');
  console.log('3. Actualizar producto');
  console.log('4. Eliminar producto');
  console.log('5. Calcular venta total');
  console.log('6. Calcular venta por producto');
  console.log('7. Salir');
  rl.question('Elige una opción: ', (option) => {
    switch (option) {
      case '1':
        addProduct();
        break;
      case '2':
        viewProducts();
        break;
      case '3':
        updateProduct();
        break;
      case '4':
        deleteProduct();
        break;
      case '5':
        calculateTotalSales();
        break;
      case '6':
        calculateSalesByProduct();
        break;
      case '7':
        fs.unlinkSync(filename);
        rl.close();
        break;
      default:
        console.log('Opción no válida. Inténtalo de nuevo.');
        mainMenu();
    }
  });
};

mainMenu();
