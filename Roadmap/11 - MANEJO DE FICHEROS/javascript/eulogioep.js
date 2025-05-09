const fs = require('fs').promises;
const readline = require('readline');

// Constantes para los nombres de archivo
const FILENAME = 'info_personal.txt';
const SALES_FILENAME = 'ventas.txt';

// Configuración de la interfaz de lectura
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para preguntar al usuario
const pregunta = (pregunta) => {
    return new Promise((resolve) => {
        rl.question(pregunta, resolve);
    });
};

// Función principal
async function main() {
    await crearArchivoPersonal();
    await gestionVentas();
}

// Función para crear y manipular el archivo personal
async function crearArchivoPersonal() {
    try {
        // Crear y escribir en el archivo
        await fs.writeFile(FILENAME, 'Nombre: Juan\nEdad: 30\nLenguaje de programación favorito: JavaScript');
        console.log('Archivo creado y escrito con éxito.');

        // Leer y mostrar el contenido
        const contenido = await fs.readFile(FILENAME, 'utf8');
        console.log('Contenido del archivo:');
        console.log(contenido);

        // Borrar el archivo
        await fs.unlink(FILENAME);
        console.log('Archivo borrado con éxito.');
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// Función para la gestión de ventas
async function gestionVentas() {
    let salir = false;

    while (!salir) {
        console.log('\n--- Gestión de Ventas ---');
        console.log('1. Añadir producto');
        console.log('2. Consultar productos');
        console.log('3. Actualizar producto');
        console.log('4. Eliminar producto');
        console.log('5. Calcular venta total');
        console.log('6. Calcular venta por producto');
        console.log('7. Salir');

        const opcion = await pregunta('Seleccione una opción: ');

        switch (opcion) {
            case '1':
                await anadirProducto();
                break;
            case '2':
                await consultarProductos();
                break;
            case '3':
                await actualizarProducto();
                break;
            case '4':
                await eliminarProducto();
                break;
            case '5':
                await calcularVentaTotal();
                break;
            case '6':
                await calcularVentaPorProducto();
                break;
            case '7':
                salir = true;
                await borrarArchivoVentas();
                rl.close();
                break;
            default:
                console.log('Opción no válida.');
        }
    }
}

// Función para añadir un producto
async function anadirProducto() {
    const nombre = await pregunta('Nombre del producto: ');
    const cantidad = await pregunta('Cantidad vendida: ');
    const precio = await pregunta('Precio: ');

    const linea = `${nombre}, ${cantidad}, ${precio}\n`;
    await fs.appendFile(SALES_FILENAME, linea);
    console.log('Producto añadido con éxito.');
}

// Función para consultar productos
async function consultarProductos() {
    try {
        const contenido = await fs.readFile(SALES_FILENAME, 'utf8');
        console.log('\nProductos:');
        console.log(contenido);
    } catch (error) {
        if (error.code === 'ENOENT') {
            console.log('No hay productos registrados.');
        } else {
            console.error('Error al consultar productos:', error.message);
        }
    }
}

// Función para actualizar un producto
async function actualizarProducto() {
    const nombreActualizar = await pregunta('Nombre del producto a actualizar: ');
    const nuevaCantidad = await pregunta('Nueva cantidad vendida: ');
    const nuevoPrecio = await pregunta('Nuevo precio: ');

    try {
        let contenido = await fs.readFile(SALES_FILENAME, 'utf8');
        let lineas = contenido.split('\n');
        let encontrado = false;

        lineas = lineas.map(linea => {
            const [nombre, ...resto] = linea.split(', ');
            if (nombre === nombreActualizar) {
                encontrado = true;
                return `${nombre}, ${nuevaCantidad}, ${nuevoPrecio}`;
            }
            return linea;
        });

        if (encontrado) {
            await fs.writeFile(SALES_FILENAME, lineas.join('\n'));
            console.log('Producto actualizado con éxito.');
        } else {
            console.log('Producto no encontrado.');
        }
    } catch (error) {
        console.error('Error al actualizar producto:', error.message);
    }
}

// Función para eliminar un producto
async function eliminarProducto() {
    const nombreEliminar = await pregunta('Nombre del producto a eliminar: ');

    try {
        let contenido = await fs.readFile(SALES_FILENAME, 'utf8');
        let lineas = contenido.split('\n');
        let encontrado = false;

        lineas = lineas.filter(linea => {
            const [nombre] = linea.split(', ');
            if (nombre === nombreEliminar) {
                encontrado = true;
                return false;
            }
            return true;
        });

        if (encontrado) {
            await fs.writeFile(SALES_FILENAME, lineas.join('\n'));
            console.log('Producto eliminado con éxito.');
        } else {
            console.log('Producto no encontrado.');
        }
    } catch (error) {
        console.error('Error al eliminar producto:', error.message);
    }
}

// Función para calcular la venta total
async function calcularVentaTotal() {
    try {
        const contenido = await fs.readFile(SALES_FILENAME, 'utf8');
        const lineas = contenido.split('\n');
        let ventaTotal = 0;

        lineas.forEach(linea => {
            if (linea.trim() !== '') {
                const [, cantidad, precio] = linea.split(', ');
                ventaTotal += parseFloat(cantidad) * parseFloat(precio);
            }
        });

        console.log(`Venta total: ${ventaTotal.toFixed(2)}`);
    } catch (error) {
        console.error('Error al calcular venta total:', error.message);
    }
}

// Función para calcular la venta por producto
async function calcularVentaPorProducto() {
    const nombreProducto = await pregunta('Nombre del producto: ');

    try {
        const contenido = await fs.readFile(SALES_FILENAME, 'utf8');
        const lineas = contenido.split('\n');
        let encontrado = false;

        lineas.forEach(linea => {
            if (linea.trim() !== '') {
                const [nombre, cantidad, precio] = linea.split(', ');
                if (nombre === nombreProducto) {
                    const ventaProducto = parseFloat(cantidad) * parseFloat(precio);
                    console.log(`Venta de ${nombreProducto}: ${ventaProducto.toFixed(2)}`);
                    encontrado = true;
                }
            }
        });

        if (!encontrado) {
            console.log('Producto no encontrado.');
        }
    } catch (error) {
        console.error('Error al calcular venta por producto:', error.message);
    }
}

// Función para borrar el archivo de ventas
async function borrarArchivoVentas() {
    try {
        await fs.unlink(SALES_FILENAME);
        console.log('Archivo de ventas borrado con éxito.');
    } catch (error) {
        if (error.code === 'ENOENT') {
            console.log('El archivo de ventas no existe.');
        } else {
            console.error('Error al borrar el archivo de ventas:', error.message);
        }
    }
}

// Ejecutar el programa principal
main().catch(console.error);