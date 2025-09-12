import * as fs from 'fs/promises';
import * as readline from 'readline';

// Constantes para los nombres de archivo
const FILENAME: string = 'info_personal.txt';
const SALES_FILENAME: string = 'ventas.txt';

// Interfaz para la estructura de un producto
interface Producto {
    nombre: string;
    cantidad: number;
    precio: number;
}

// Configuración de la interfaz de lectura
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para preguntar al usuario
function pregunta(pregunta: string): Promise<string> {
    return new Promise((resolve) => {
        rl.question(pregunta, resolve);
    });
}

// Función principal
async function main(): Promise<void> {
    await crearArchivoPersonal();
    await gestionVentas();
}

// Función para crear y manipular el archivo personal
async function crearArchivoPersonal(): Promise<void> {
    try {
        // Crear y escribir en el archivo
        await fs.writeFile(FILENAME, 'Nombre: Juan\nEdad: 30\nLenguaje de programación favorito: TypeScript');
        console.log('Archivo creado y escrito con éxito.');

        // Leer y mostrar el contenido
        const contenido = await fs.readFile(FILENAME, 'utf8');
        console.log('Contenido del archivo:');
        console.log(contenido);

        // Borrar el archivo
        await fs.unlink(FILENAME);
        console.log('Archivo borrado con éxito.');
    } catch (error) {
        console.error('Error:', (error as Error).message);
    }
}

// Función para la gestión de ventas
async function gestionVentas(): Promise<void> {
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
async function anadirProducto(): Promise<void> {
    const nombre = await pregunta('Nombre del producto: ');
    const cantidad = parseInt(await pregunta('Cantidad vendida: '));
    const precio = parseFloat(await pregunta('Precio: '));

    const producto: Producto = { nombre, cantidad, precio };
    const linea = `${producto.nombre}, ${producto.cantidad}, ${producto.precio}\n`;
    await fs.appendFile(SALES_FILENAME, linea);
    console.log('Producto añadido con éxito.');
}

// Función para consultar productos
async function consultarProductos(): Promise<void> {
    try {
        const contenido = await fs.readFile(SALES_FILENAME, 'utf8');
        console.log('\nProductos:');
        console.log(contenido);
    } catch (error) {
        if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
            console.log('No hay productos registrados.');
        } else {
            console.error('Error al consultar productos:', (error as Error).message);
        }
    }
}

// Función para actualizar un producto
async function actualizarProducto(): Promise<void> {
    const nombreActualizar = await pregunta('Nombre del producto a actualizar: ');
    const nuevaCantidad = parseInt(await pregunta('Nueva cantidad vendida: '));
    const nuevoPrecio = parseFloat(await pregunta('Nuevo precio: '));

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
        console.error('Error al actualizar producto:', (error as Error).message);
    }
}

// Función para eliminar un producto
async function eliminarProducto(): Promise<void> {
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
        console.error('Error al eliminar producto:', (error as Error).message);
    }
}

// Función para calcular la venta total
async function calcularVentaTotal(): Promise<void> {
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
        console.error('Error al calcular venta total:', (error as Error).message);
    }
}

// Función para calcular la venta por producto
async function calcularVentaPorProducto(): Promise<void> {
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
        console.error('Error al calcular venta por producto:', (error as Error).message);
    }
}

// Función para borrar el archivo de ventas
async function borrarArchivoVentas(): Promise<void> {
    try {
        await fs.unlink(SALES_FILENAME);
        console.log('Archivo de ventas borrado con éxito.');
    } catch (error) {
        if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
            console.log('El archivo de ventas no existe.');
        } else {
            console.error('Error al borrar el archivo de ventas:', (error as Error).message);
        }
    }
}

// Ejecutar el programa principal
main().catch(console.error);