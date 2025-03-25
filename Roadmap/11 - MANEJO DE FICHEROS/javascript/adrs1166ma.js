/*
IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:
- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.

DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
[nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
*/

// 🔥 Crear, escribir, leer y borrar un archivo
const fs = require('fs'); // Para el manerjo de archivos


const fileName1 = "adrs1166ma.txt"; // Nombre del archivo

function crearArchivo() {
    const contenido = `Nombre: Anderson\nEdad: 20\nLenguaje favorito: JavaScript`;
    fs.writeFile(fileName1, contenido, (e) => {
        if (e) {
            console.error("Error al crear el archivo:", e);
            return;
        }
        console.log(`Archivo "${fileName1}" creado con éxito.`);
        leerArchivo();
    });
}

function leerArchivo() {
    fs.readFile(fileName1, 'utf8', (e, data) => {
        if (e) {
            console.error("Error al leer el archivo:", e);
            return;
        }
        console.log(`Contenido del archivo:\n${data}`);
        borrarArchivo();
    });
}

function borrarArchivo() {
    fs.unlink(fileName1, (e) => {
        if (e) {
            console.error("Error al borrar el archivo:", e);
            return;
        }
        console.log(`Archivo "${fileName1}" borrado con éxito.`);
    });
}

crearArchivo();


// 🔥 Extra ------------------------------------------------------------------------------------------------------------------------


const fs = require('fs');
const readline = require('readline');

const fileName = "ventas.txt";

// Para leer entrada del usuario
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Preguntar algo al usuario
function preguntar(pregunta) {
    return new Promise((resolve) => {
        rl.question(pregunta, (respuesta) => resolve(respuesta));
    });
}

async function menu() {
    while (true) {
        console.log("\n--- MENÚ DE GESTIÓN DE VENTAS ---");
        console.log("1. Añadir producto");
        console.log("2. Consultar productos");
        console.log("3. Actualizar producto");
        console.log("4. Eliminar producto");
        console.log("5. Calcular venta total");
        console.log("6. Calcular venta por producto");
        console.log("7. Salir");

        const opcion = await preguntar("Seleccione una opción: ");

        switch (opcion) {
            case "1":
                await añadirProducto();
                break;
            case "2":
                await consultarProductos();
                break;
            case "3":
                await actualizarProducto();
                break;
            case "4":
                await eliminarProducto();
                break;
            case "5":
                await calcularVentaTotal();
                break;
            case "6":
                await calcularVentaPorProducto();
                break;
            case "7":
                await salir();
                return;
            default:
                console.log("Opción no válida. Intente de nuevo.");
        }
    }
}

async function añadirProducto() {
    const nombre = await preguntar("Nombre del producto: ");
    const cantidad = await preguntar("Cantidad vendida: ");
    const precio = await preguntar("Precio unitario: ");
    const linea = `${nombre}, ${cantidad}, ${precio}\n`;

    fs.appendFile(fileName, linea, (err) => {
        if (err) {
            console.error("Error al añadir el producto:", err);
        } else {
            console.log("Producto añadido con éxito.");
        }
    });
}

async function consultarProductos() {
    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer los productos:", err);
            return;
        }
        if (!data.trim()) {
            console.log("No hay productos registrados.");
            return;
        }
        console.log("Productos registrados:");
        console.log(data);
    });
}

async function actualizarProducto() {
    const nombre = await preguntar("Nombre del producto a actualizar: ");
    const cantidad = await preguntar("Nueva cantidad vendida: ");
    const precio = await preguntar("Nuevo precio unitario: ");

    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer los productos:", err);
            return;
        }

        const lineas = data.split('\n').filter(linea => linea.trim());
        let encontrado = false;

        for (let i = 0; i < lineas.length; i++) {
            const [producto] = lineas[i].split(',');
            if (producto.trim() === nombre.trim()) {
                lineas[i] = `${nombre}, ${cantidad}, ${precio}`;
                encontrado = true;
                break;
            }
        }

        if (!encontrado) {
            console.log("Producto no encontrado.");
            return;
        }

        fs.writeFile(fileName, lineas.join('\n'), (err) => {
            if (err) {
                console.error("Error al actualizar el producto:", err);
            } else {
                console.log("Producto actualizado con éxito.");
            }
        });
    });
}

async function eliminarProducto() {
    const nombre = await preguntar("Nombre del producto a eliminar: ");

    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer los productos:", err);
            return;
        }

        const lineas = data.split('\n').filter(linea => linea.trim());
        const nuevasLineas = lineas.filter(linea => {
            const [producto] = linea.split(',');
            return producto.trim() !== nombre.trim();
        });

        if (lineas.length === nuevasLineas.length) {
            console.log("Producto no encontrado.");
            return;
        }

        fs.writeFile(fileName, nuevasLineas.join('\n'), (err) => {
            if (err) {
                console.error("Error al eliminar el producto:", err);
            } else {
                console.log("Producto eliminado con éxito.");
            }
        });
    });
}

async function calcularVentaTotal() {
    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer los productos:", err);
            return;
        }

        const lineas = data.split('\n').filter(linea => linea.trim());
        let total = 0;

        for (const linea of lineas) {
            const [, cantidad, precio] = linea.split(',').map(valor => parseFloat(valor.trim()));
            total += cantidad * precio;
        }

        console.log(`Venta total: $${total.toFixed(2)}`);
    });
}

async function calcularVentaPorProducto() {
    const nombre = await preguntar("Nombre del producto: ");

    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) {
            console.error("Error al leer los productos:", err);
            return;
        }

        const lineas = data.split('\n').filter(linea => linea.trim());
        let encontrado = false;

        for (const linea of lineas) {
            const [producto, cantidad, precio] = linea.split(',').map(valor => valor.trim());
            if (producto === nombre) {
                const venta = parseFloat(cantidad) * parseFloat(precio);
                console.log(`Venta del producto "${nombre}": $${venta.toFixed(2)}`);
                encontrado = true;
                break;
            }
        }

        if (!encontrado) {
            console.log("Producto no encontrado.");
        }
    });
}

async function salir() {
    fs.unlink(fileName, (err) => {
        if (err && err.code !== 'ENOENT') {
            console.error("Error al borrar el archivo:", err);
        } else {
            console.log("Archivo borrado. ¡Hasta luego!");
        }
        rl.close();
    });
}

menu();