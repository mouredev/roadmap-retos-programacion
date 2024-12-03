/* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
*/

/*const fs = require('fs');// Importamos el módulo fs para trabajar con ficheros. 
const fileName = 'wapastorv.txt';// Nombre del archivo que vamos a crear. 
const content = 'Nombre: William Pastor\nEdad: 26\nLenguaje de programación favorito: JavaScript'; // Contenido del archivo que vamos a crear. 

fs.writeFile(fileName, content, (err) => { // Creamos el archivo con el contenido. 
  if (err) {
    console.error('Error al crear el archivo:', err); // Si hay un error, lo mostramos por consola. 
    return;
  }
  console.log('Archivo creado correctamente con el contenido:', content);  // Si no hay errores, mostramos un mensaje de éxito.
    fs.readFile(fileName, 'utf8', (err, data) => { // Leemos el archivo creado. 
        if (err) {
        console.error('Error al leer el archivo:', err); // Si hay un error, lo mostramos por consola.
        return;
        }
        console.log('Contenido del archivo:', data);// Si no hay errores, mostramos el contenido del archivo. 
        fs.unlink(fileName, (err) => {// Borramos el archivo creado. 
        if (err) {
            console.error('Error al borrar el archivo:', err);
            return;
        }
        console.log('Archivo borrado correctamente');
        });
   
    });
});*/

/* DIFICULTAD EXTRA (opcional):
* Desarrolla un programa de gestión de ventas que almacena sus datos en un 
* archivo .txt.
* - Cada producto se guarda en una línea del archivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
*/

// Código extra aquí...
const fs = require('fs'); // Importamos el módulo fs para trabajar con ficheros.
const readline = require('readline'); // Importamos el módulo readline para leer la entrada por consola.
const rl = readline.createInterface({ // Creamos una interfaz de lectura.
  input: process.stdin, // Establecemos la entrada estándar.
  output: process.stdout // Establecemos la salida estándar.
});

const fileNameVentas = 'ventas.txt'; // Nombre del archivo que vamos a crear.
const menu = `Menú:
    1. Añadir producto.
    2. Consultar productos.
    3. Actualizar producto.
    4. Eliminar producto.
    5. Calcular venta total.
    6. Calcular venta por producto.
    7. Salir.`; // Menú de opciones.
const productos = []; // Array donde almacenaremos los productos

function addProduct() { // Función para añadir un producto.
    rl.question('Introduce el nombre del producto, la cantidad vendida y el precio (separados por comas): ', (answer) => {
        const [nombre, cantidad, precio] = answer.split(','); // Dividimos la respuesta en un array.
        productos.push({ nombre, cantidad: parseInt(cantidad), precio: parseFloat(precio) }); // Añadimos el producto al array.
        rl.question('Producto añadido correctamente. Pulsa cualquier tecla para continuar.', () => showMenu());}); // Mostramos el menú.
}

function showProducts() { // Función para mostrar los productos.
    console.log('Productos:');
    productos.forEach((producto) => console.log(`${producto.nombre}, ${producto.cantidad}, ${producto.precio}`)); // Mostramos los productos.
    rl.question('Pulsa cualquier tecla para continuar.', () => showMenu());
}

function updateProduct() { // Función para actualizar un producto.
    rl.question('Introduce el nombre del producto a actualizar: ', (nombre) => {
        const producto = productos.find((producto) => producto.nombre === nombre); // Buscamos el producto.
        if (!producto) { // Si no existe, mostramos un mensaje de error.
            console.log('Producto no encontrado.');
            return rl.question('Pulsa cualquier tecla para continuar.', () => showMenu());
        }
        rl.question('Introduce la nueva cantidad vendida y el nuevo precio (separados por comas): ', (answer) => {
            const [cantidad, precio] = answer.split(','); // Dividimos la respuesta en un array.
            producto.cantidad = parseInt(cantidad); // Actualizamos la cantidad.
            producto.precio = parseFloat(precio); // Actualizamos el precio.
            rl.question('Producto actualizado correctamente. Pulsa cualquier tecla para continuar.', () => showMenu());
        });
    });
}

function deleteProduct() { // Función para eliminar un producto.
    rl.question('Introduce el nombre del producto a eliminar: ', (nombre) => {
        const index = productos.findIndex((producto) => producto.nombre === nombre); // Buscamos el índice del producto.
        if (index === -1) { // Si no existe, mostramos un mensaje de error.
            console.log('Producto no encontrado.');
            return rl.question('Pulsa cualquier tecla para continuar.', () => showMenu());
        }
        productos.splice(index, 1); // Eliminamos el producto.
        rl.question('Producto eliminado correctamente. Pulsa cualquier tecla para continuar.', () => showMenu());
    });
}

function totalSale() { // Función para calcular la venta total.
    const total = productos.reduce((acc, producto) => acc + producto.cantidad * producto.precio, 0); // Calculamos el total.
    console.log(`Venta total: ${total}`); // Mostramos el total.
    rl.question('Pulsa cualquier tecla para continuar.', () => showMenu());
}

function saleByProduct() { // Función para calcular la venta por producto.
    rl.question('Introduce el nombre del producto: ', (nombre) => {
        const producto = productos.find((producto) => producto.nombre === nombre); // Buscamos el producto.
        if (!producto) { // Si no existe, mostramos un mensaje de error.
            console.log('Producto no encontrado.');
            return rl.question('Pulsa cualquier tecla para continuar.', () => showMenu());
        }
        console.log(`Venta por ${producto.nombre}: ${producto.cantidad * producto.precio}`); // Mostramos la venta por producto.
        rl.question('Pulsa cualquier tecla para continuar.', () => showMenu());
    });
}

function showMenu() { // Función para mostrar el menú.
    rl.question(menu, (option) => {
        switch (option) { // Según la opción seleccionada, llamamos a la función correspondiente.
            case '1':
                addProduct();
                break;
            case '2':
                showProducts();
                break;
            case '3':
                updateProduct();
                break;
            case '4':
                deleteProduct();
                break;
            case '5':
                totalSale();
                break;
            case '6':
                saleByProduct();
                break;
            case '7':
                fs.unlink(fileNameVentas, (err) => { // Borramos el archivo creado.
                    if (err) {
                        console.error('Error al borrar el archivo:', err);
                        return;
                    }
                    console.log('Archivo borrado correctamente.');
                    rl.close();
                });
                break;
            default:
                console.log('Opción no válida.'); // Si la opción no es válida, mostramos un mensaje de error.
                showMenu();
        }
    });
}

fs.writeFile(fileNameVentas, '', (err) => { // Creamos el archivo.
    if (err) {
        console.error('Error al crear el archivo:', err);
        return;
    }
    console.log('Archivo creado correctamente.');
    showMenu();
})

rl.on('close', () => console.log('¡Hasta luego!')); // Cuando se cierra la interfaz, mostramos un mensaje

