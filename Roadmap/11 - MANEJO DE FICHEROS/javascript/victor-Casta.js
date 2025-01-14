const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

/*
  * Desarrolla un programa capaz de crear un archivo que se llame como
  * tu usuario de GitHub y tenga la extensión .txt.
  * Añade varias líneas en ese fichero:
  * - Tu nombre.
  * - Edad.
  * - Lenguaje de programación favorito.
  * Imprime el contenido.
  * Borra el fichero.
*/

fs.writeFile('victor-Casta.txt',
  'Victor\n21\nJavascript',
  (error) => {console.log(error)}
)

fs.readFile('victor-Casta.txt', 'utf-8', (error, data) => {
  console.log(data)
})

fs.unlink('victor-Casta.txt', (error) => {
  console.log(error)
})


/*
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

async function getMenu() {
  let option;
  do {
    console.log('1. Añadir producto');
    console.log('2. Consultar producto');
    console.log('3. Actualizar producto');
    console.log('4. Eliminar producto');
    console.log('5. Calcular venta total');
    console.log('6. Calcular venta por producto');
    console.log('7. Salir');

    option = await question('Ingresa una opción del menú: ');

    if (option === '1') {
      await addProducts();
    }
    if (option === '2') {
      await viewProducts();
    }
    if (option === '3') {
      await updateProducts();
    }
    if (option === '4') {
      await deleteProducts();
    }
    if (option === '5') {
      await totalSales();
    }
    if (option === '6') {
      await productSales();
    }
    if (option === '7') {
      fs.unlinkSync('sales.txt');
    }
  } while (option !== '7');

  rl.close();
}

function question(question) {
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      resolve(answer);
    });
  });
}

async function addProducts() {
  const nameProduct = await question('Ingresa el nombre del producto: ');
  const quantity = await question('Ingresa la cantidad vendida: ');
  const price = await question('Ingresa el precio del producto: ');

  const data = `${nameProduct}, ${quantity}, ${price}\n`;
  fs.appendFileSync('sales.txt', data, 'utf8');
}

async function viewProducts() {
  const userProductName = await question('Ingresa el nombre del producto: ');

  const fileStream = fs.createReadStream('sales.txt');
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let foundProduct = false;

  for await (const line of rl) {
    const [productName, quantity, price] = line.split(', ');

    if (productName === userProductName) {
      console.log(`Nombre: ${productName}`);
      console.log(`Cantidad: ${quantity}`);
      console.log(`Precio: ${price}`);
      foundProduct = true;
      break;
    }
  }

  if (!foundProduct) {
    console.log('No se encontró el producto');
  }
}

async function updateProducts() {
  const userNameProduct = await question('Nombre del producto: ');
  const userQuantity = await question('Ingresa la nueva cantidad vendida: ');
  const userPrice = await question('Ingresa el nuevo precio del producto: ');

  const fileStream = fs.createReadStream('sales.txt');
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let updatedLines = [];

  for await (const line of rl) {
    const [productName, quantity, price] = line.split(', ');

    if (productName === userNameProduct) {
      updatedLines.push(`${userNameProduct}, ${userQuantity}, ${userPrice}`);
    } else {
      updatedLines.push(line);
    }
  }

  rl.close();
  fs.writeFileSync('sales.txt', updatedLines.join('\n'));

  console.log('Producto actualizado correctamente');
}

async function deleteProducts() {
  const userNameProduct = await question('Nombre del producto: ');

  const fileStream = fs.createReadStream('sales.txt');
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let updatedLines = [];

  for await (const line of rl) {
    const [productName, quantity, price] = line.split(', ');

    if (productName!== userNameProduct) {
      updatedLines.push(line);
    }
  }

  rl.close();
  fs.writeFileSync('sales.txt', updatedLines.join('\n'));

  console.log('Producto eliminado correctamente');
}

async function totalSales() {
  const fileStream = fs.createReadStream('sales.txt');
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let total = 0;

  for await (const line of rl) {
    const [productName, quantity, price] = line.split(', ');
    total += parseInt(quantity) * parseInt(price);
  }

  console.log(`El total de ventas es: ${total}`);
  rl.close();
}

async function productSales() {
  const userNameProduct = await question('Nombre del producto: ');

  const fileStream = fs.createReadStream('sales.txt');
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let foundProduct = false;

  for await (const line of rl) {
    const [productName, quantity, price] = line.split(', ');

    if (productName === userNameProduct) {
      const totalByProduct = parseInt(quantity) * parseInt(price);
      console.log(`El total de ventas por ${userNameProduct} es: ${totalByProduct}`);
      foundProduct = true;
      break;
    }
  }

  if (!foundProduct) {
    console.log('No se encontró el producto');
  }

  rl.close();
}

getMenu();