"use strict";

const fs = require('fs');
const readline = require('readline');

// Definición de las funciones principales del programa
const ventas = {
    archivo: 'ventas.txt',

    async agregarProducto(producto) {
        await appendToFile(this.archivo, `${producto.nombre}, ${producto.cantidad}, ${producto.precio}\n`);
    },

    async consultarProductos() {
        const data = await readFile(this.archivo);
        console.log(data);
    },

    async actualizarProducto(nombre, cantidad, precio) {
        const tempFile = 'temporal.txt';
        const readStream = fs.createReadStream(this.archivo);
        const writeStream = fs.createWriteStream(tempFile);
        const rl = readline.createInterface({
            input: readStream,
            output: writeStream
        });

        for await (const line of rl) {
            const [nombreProducto, cantidadStr, precioStr] = line.split(',');
            if (nombreProducto.trim() === nombre) {
                writeStream.write(`${nombre}, ${cantidad}, ${precio}\n`);
            } else {
                writeStream.write(`${line}\n`);
            }
        }

        await new Promise(resolve => {
            readStream.close();
            writeStream.close();
            fs.unlink(this.archivo, () => {
                fs.rename(tempFile, this.archivo, resolve);
            });
        });
    },

    async eliminarProducto(nombre) {
        const tempFile = 'temporal.txt';
        const readStream = fs.createReadStream(this.archivo);
        const writeStream = fs.createWriteStream(tempFile);
        const rl = readline.createInterface({
            input: readStream,
            output: writeStream
        });

        for await (const line of rl) {
            const [nombreProducto, , ] = line.split(',');
            if (nombreProducto.trim() !== nombre) {
                writeStream.write(`${line}\n`);
            }
        }

        await new Promise(resolve => {
            readStream.close();
            writeStream.close();
            fs.unlink(this.archivo, () => {
                fs.rename(tempFile, this.archivo, resolve);
            });
        });
    },

    async calcularVentaTotal() {
        const data = await readFile(this.archivo);
        const lines = data.split('\n');
        let total = 0;
        for (const line of lines) {
            const [cantidadStr, precioStr] = line.split(',');
            const cantidad = parseInt(cantidadStr.trim());
            const precio = parseFloat(precioStr.trim());
            total += cantidad * precio;
        }
        return total;
    },

    async calcularVentaPorProducto(nombre) {
        const data = await readFile(this.archivo);
        const lines = data.split('\n');
        for (const line of lines) {
            const [nombreProducto, cantidadStr, precioStr] = line.split(',');
            if (nombreProducto.trim() === nombre) {
                const cantidad = parseInt(cantidadStr.trim());
                const precio = parseFloat(precioStr.trim());
                return cantidad * precio;
            }
        }
        return 0;
    },

    async salir() {
        await fs.promises.unlink(this.archivo);
        console.log("Archivo borrado. Saliendo del programa...");
        process.exit(0);
    }
};

// Funciones de utilidad
async function appendToFile(filename, data) {
    await fs.promises.appendFile(filename, data);
}

async function readFile(filename) {
    return await fs.promises.readFile(filename, 'utf8');
}

// Lógica principal del programa
async function main() {
    console.log("===== Gestión de Ventas =====");
    console.log("1. Añadir producto");
    console.log("2. Consultar productos");
    console.log("3. Actualizar producto");
    console.log("4. Eliminar producto");
    console.log("5. Calcular venta total");
    console.log("6. Calcular venta por producto");
    console.log("7. Salir");

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Seleccione una opción: ", async (opcion) => {
        switch (opcion) {
            case '1':
                const producto = await obtenerDatosProducto();
                await ventas.agregarProducto(producto);
                break;
            case '2':
                await ventas.consultarProductos();
                break;
            case '3':
                const { nombre, cantidad, precio } = await obtenerDatosProducto();
                await ventas.actualizarProducto(nombre, cantidad, precio);
                break;
            case '4':
                const nombreProductoEliminar = await obtenerNombreProducto();
                await ventas.eliminarProducto(nombreProductoEliminar);
                break;
            case '5':
                console.log("Venta total: $" + await ventas.calcularVentaTotal());
                break;
            case '6':
                const nombreProductoVenta = await obtenerNombreProducto();
                console.log("Venta de " + nombreProductoVenta + ": $" + await ventas.calcularVentaPorProducto(nombreProductoVenta));
                break;
            case '7':
                await ventas.salir();
                break;
            default:
                console.log("Opción no válida");
                break;
        }
        rl.close();
    });
}

async function obtenerDatosProducto() {
    return new Promise(resolve => {
        const producto = {};
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question("Nombre del producto: ", (nombre) => {
            rl.question("Cantidad vendida: ", (cantidad) => {
                rl.question("Precio: ", (precio) => {
                    rl.close();
                    resolve({ nombre, cantidad: parseInt(cantidad), precio: parseFloat(precio) });
                });
            });
        });
    });
}

async function obtenerNombreProducto() {
    return new Promise(resolve => {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question("Nombre del producto: ", (nombre) => {
            rl.close();
            resolve(nombre);
        });
    });
}

// Ejecución del programa
main().catch(error => console.error(error));

