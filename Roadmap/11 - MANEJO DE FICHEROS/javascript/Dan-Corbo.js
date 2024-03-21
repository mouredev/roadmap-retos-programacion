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


/* Soluciones */


const fs = require('fs');

// Nombre del usuario de GitHub
const nombre = "Dan-Corbo";

// Nombre del archivo
const nombreDelArchivo = `${nombre}.txt`;

// Contenido del archivo
const datos = [
    "Nombre: Daniel Corbo",
    "Edad: 24",
    "Lenguaje de programación favorito: JavaScript"
].join("\n");

// Escribir el contenido en el archivo
fs.writeFileSync(nombreDelArchivo, datos);

// Leer el contenido del archivo
console.log("Contenido del archivo:");
console.log(fs.readFileSync(nombreDelArchivo, 'utf8'));

// Borrar el archivo
fs.unlinkSync(nombreDelArchivo);
console.log(`El archivo ${nombreDelArchivo} ha sido eliminado.`);



/* Extra - Opcional */


const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const fileName = "ventas.txt";

function agregarProductos() {
  rl.question('Ingrese el nombre del producto: ', (nombre) => {
    rl.question('Ingrese la cantidad vendida: ', (cantidad) => {
      rl.question('Ingrese el precio del producto: ', (precio) => {
        const data = `${nombre}, ${cantidad}, ${precio}\n`;
        fs.appendFileSync(fileName, data);
        console.log('Producto agregado correctamente.');
        mostrarMenu();
      });
    });
  });
}

function mostrarTotal() {
  const data = fs.readFileSync(fileName, 'utf8');
  const lines = data.split('\n');
  let total = 0;
  for (const line of lines) {
    const [, cantidad, precio] = line.split(', ');
    total += parseInt(cantidad) * parseFloat(precio);
  }
  console.log(`Venta total: $${total.toFixed(2)}`);
  mostrarMenu();
}

function mostrarProductos() {
  const data = fs.readFileSync(fileName, 'utf8');
  const lines = data.split('\n');
  for (const line of lines) {
    const [nombre, cantidad, precio] = line.split(', ');
    console.log(`${nombre}: ${cantidad} unidades vendidas a $${precio} c/u`);
  }
  mostrarMenu();
}

function borrarProducto() {
  rl.question('Ingrese el nombre del producto a eliminar: ', (nombre) => {
    let newData = '';
    const data = fs.readFileSync(fileName, 'utf8');
    const lines = data.split('\n');
    for (const line of lines) {
      if (!line.startsWith(nombre)) {
        newData += line + '\n';
      }
    }
    fs.writeFileSync(fileName, newData);
    console.log('Producto eliminado correctamente.');
    mostrarMenu();
  });
}

function mostrarMenu() {
  console.log("\n--- MENÚ ---");
  console.log("1. Añadir producto");
  console.log("2. Consultar venta total");
  console.log("3. Consultar venta por producto");
  console.log("4. Eliminar producto");
  console.log("5. Salir");

  rl.question('Seleccione una opción: ', (option) => {
    switch (option) {
      case '1':
        agregarProductos();
        break;
      case '2':
        mostrarTotal();
        break;
      case '3':
        mostrarProductos();
        break;
      case '4':
        borrarProducto();
        break;
      case '5':
        fs.unlinkSync(fileName);
        console.log(`El archivo ${fileName} ha sido eliminado.`);
        rl.close();
        break;
      default:
        console.log('Opción no válida. Por favor, seleccione una opción del menú.');
        mostrarMenu();
        break;
    }
  });
}

// Comprobar si el archivo existe
if (!fs.existsSync(fileName)) {
  // Si el archivo no existe, crearlo
  fs.writeFileSync(fileName, '');
}

mostrarMenu();
