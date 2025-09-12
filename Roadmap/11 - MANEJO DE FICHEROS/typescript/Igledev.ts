//  1º Ejercicio
    import * as fs from 'fs/promises';
    import { writeFile, readFile, unlink } from 'fs/promises'; //Utilizamos esto para poder manejar ficheros.

    let nickname : string = 'Igledev';  //Ponemos nuestro nombre de GitHub

    // Creamos el contenido de nuestro archivo
    let msg : string = `
        Nombre : Adrián
        Edad : 19
        Lenguaje de programación favorito : TypeScript
    `

    let nombre_archivo = `${nickname}.txt` //  Llamamos al archivo como nuestro nombre de Github

    writeFile(nombre_archivo, msg)
    .then(() => {
        // Leemos el contenido de nuestro archivo.
        return readFile(nombre_archivo, 'utf8');
    })
    .then(msg => {
        // Mostramos el archivo
        console.log(`Contenido del archivo ${msg}`)

        // Borramos el archivo
        return unlink(nombre_archivo);
    })
    .then(() => {
        console.log(`Archivo borrado ${nombre_archivo}`)
    })
    .catch((error) => {
        throw new Error(`Fallo en el archivo: ${error}`);
    });

// Ejercicio Extra
    let nombreArchivo = 'ventas.txt';

    // Función para mostrar el menú
    function mostrarMenu() {
        console.log('\n--- Menú ---');
        console.log('1. Añadir producto');
        console.log('2. Consultar producto');
        console.log('3. Actualizar producto');
        console.log('4. Eliminar producto');
        console.log('5. Calcular venta total');
        console.log('6. Calcular venta por producto');
        console.log('7. Salir');
    }

    // Función para añadir un producto
    async function agregarProducto() {
        let nombreProducto = await obtenerInput('Nombre del producto:');
        let cantidadVendida = parseFloat(await obtenerInput('Cantidad vendida:'));
        let precio = parseFloat(await obtenerInput('Precio:'));
        let linea = `${nombreProducto}, ${cantidadVendida}, ${precio}\n`;

        await fs.appendFile(nombreArchivo, linea);
        console.log('Producto agregado correctamente.');
    }

    // Función para consultar un producto
    async function consultarProducto() {
        let nombreProducto = await obtenerInput('Nombre del producto:');
        try {
            let contenido = await fs.readFile(nombreArchivo, 'utf-8');
            let lineas = contenido.split('\n');
            let producto = lineas.find(linea => linea.startsWith(nombreProducto));
            if (producto) {
                console.log('Datos del producto:', producto);
            } else {
                console.log('Producto no encontrado.');
            }
        } catch (error) {
            console.error('Error al leer el archivo:', error);
        }
    }

    // Función para actualizar un producto
    async function actualizarProducto() {
        let nombreProducto = await obtenerInput('Nombre del producto:');
        let nuevaCantidad = parseFloat(await obtenerInput('Nueva cantidad vendida:'));
        let nuevoPrecio = parseFloat(await obtenerInput('Nuevo precio:'));

        try {
            let contenido = await fs.readFile(nombreArchivo, 'utf-8');
            let lineas = contenido.split('\n');
            let indice = lineas.findIndex(linea => linea.startsWith(nombreProducto));
            if (indice !== -1) {
                lineas[indice] = `${nombreProducto}, ${nuevaCantidad}, ${nuevoPrecio}`;
                await fs.writeFile(nombreArchivo, lineas.join('\n'));
                console.log('Producto actualizado correctamente.');
            } else {
                console.log('Producto no encontrado.');
            }
        } catch (error) {
            console.error('Error al leer/escribir el archivo:', error);
        }
    }

    // Función para eliminar un producto
    async function eliminarProducto() {
        let nombreProducto = await obtenerInput('Nombre del producto a eliminar:');
        try {
            let contenido = await fs.readFile(nombreArchivo, 'utf-8');
            let lineas = contenido.split('\n');
            let filtradas = lineas.filter(linea => !linea.startsWith(nombreProducto));
            await fs.writeFile(nombreArchivo, filtradas.join('\n'));
            console.log('Producto eliminado correctamente.');
        } catch (error) {
            console.error('Error al leer/escribir el archivo:', error);
        }
    }

    // Función para calcular la venta total
    async function calcularVentaTotal() {
        try {
            let contenido = await fs.readFile(nombreArchivo, 'utf-8');
            let lineas = contenido.split('\n');
            let ventaTotal = 0;
            for (let linea of lineas) {
                let [, cantidadVendida, precio] = linea.split(',').map(parseFloat);
                ventaTotal += cantidadVendida * precio;
            }
            console.log('Venta total:', ventaTotal.toFixed(2));
        } catch (error) {
            console.error('Error al leer el archivo:', error);
        }
    }

    // Función para calcular la venta por producto
    async function calcularVentaPorProducto() {
        let nombreProducto = await obtenerInput('Nombre del producto:');
        try {
            let contenido = await fs.readFile(nombreArchivo, 'utf-8');
            let lineas = contenido.split('\n');
            let producto = lineas.find(linea => linea.startsWith(nombreProducto));
            if (producto) {
                let [, cantidadVendida, precio] = producto.split(',').map(parseFloat);
                console.log('Venta por producto:', (cantidadVendida * precio).toFixed(2));
            } else {
                console.log('Producto no encontrado.');
            }
        } catch (error) {
            console.error('Error al leer el archivo:', error);
        }
    }

    // Función para obtener input del usuario
    async function obtenerInput(mensaje: string): Promise<string> {
        process.stdout.write(`${mensaje} `);
        return new Promise(resolve => {
            process.stdin.once('data', data => {
                resolve(data.toString().trim());
            });
        });
    }

    // Función para salir y borrar el archivo
    async function salir() {
        try {
            await fs.unlink(nombreArchivo);
            console.log('Archivo borrado. Saliendo del programa.');
            process.exit();
        } catch (error) {
            console.error('Error al borrar el archivo:', error);
        }
    }

    // Función principal
    async function main() {
        try {
            // Mostrar el menú
            mostrarMenu();

            // Esperar la selección del usuario
            let opcion = parseInt(await obtenerInput('Selecciona una opción:'));

            // Realizar la operación correspondiente
            switch (opcion) {
                case 1:
                    await agregarProducto();
                    break;
                case 2:
                    await consultarProducto();
                    break;
                case 3:
                    await actualizarProducto();
                    break;
                case 4:
                    await eliminarProducto();
                    break;
                case 5:
                    await calcularVentaTotal();
                    break;
                case 6:
                    await calcularVentaPorProducto();
                    break;
                case 7:
                    await salir();
                    break;
                default:
                    console.log('Opción inválida.');
            }

            // Volver a mostrar el menú
            main();
        } catch (error) {
            console.error('Error en el programa:', error);
        }
    }

    // Iniciar el programa
    main();