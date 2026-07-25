// En package.json se debe agregar "type": "module" para usar archivo .js

import { open, unlink, access, constants } from 'node:fs/promises';
import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

async function manageFile() {
    try {
        console.log('Creando archivo de texto edalmava.txt...');
        const filehandle = await open('edalmava.txt', 'a');        
        await filehandle.appendFile("Edalmava\n");
        await filehandle.appendFile("30\n");
        await filehandle.appendFile("JavaScript\n");
        await filehandle.close();

        console.log('\nImprimiendo el contenido del archivo edalmava.txt:');
        const file = await open('edalmava.txt');
        for await (const line of file.readLines()) {
            console.log(line);
        }
        await file.close();

        console.log('\nBorrando archivo de texto edalmava.txt...')
        await unlink('edalmava.txt');
        console.log('Borrado exitoso del archivo edalmava.txt');

        await retoExtra();
    } catch (error) {
        console.error('Ha ocurrido un error:', error.message);
    }
}

async function guardarVenta(rl2) {    
    try {
        console.log('Añadir Venta');        

        const nombreProducto = await rl2.question('Nombre Producto: ');
        const cantidadVendida = await rl2.question('Cantidad Vendida: ');
        const precio = await rl2.question('Precio Producto: ');

        const producto = [nombreProducto, cantidadVendida, precio, precio * cantidadVendida].join(',')

        const filehandle = await open('ventas.txt', 'a');        
        await filehandle.appendFile(`${producto}\n`);
        await filehandle.close();        
    } catch(error) {
        console.error('Ha ocurrido un error:', error.message);
    }
}

async function mostrarProductos() {
    try {
        await access('ventas.txt', constants.F_OK);
        console.log('\nVentas:\n');
        const file = await open('ventas.txt');
        for await (const line of file.readLines()) {
            console.log(line);
        }
        await file.close();
    } catch(error) {
        if (error.code === 'ENOENT') {
            console.error('Todavía no se han añadido productos al archivo de ventas');
        } else {
            console.error('Ha ocurrido un error:', error.message);
        }        
    }
}

async function retoExtra() {
    const rl = readline.createInterface({ input, output, terminal: false });
    try {
        
        let opcion = '';

        while (opcion !== '3') {
            console.log('\nMenú Principal\n');
            opcion = await rl.question('1. Añadir venta\n2. Consultar Ventas\n3. Salir\n\nEscoja su opción: ');
            switch (opcion) {
                case '1':
                    await guardarVenta(rl);
                    break;
                case '2':
                    await mostrarProductos();
                    break;
                case '3':
                    console.log('Saliendo...')
                    try {
                        await access('ventas.txt', constants.F_OK);
                        await unlink('ventas.txt');
                        console.log('Archivo de ventas borrado');
                    } catch(error) {
                        if (error.code !== 'ENOENT') {
                            console.error('Error al verificar o borrar el archivo de ventas:', error.message);
                        }
                    }
                    
                    break;
                default:
                    console.log('Opción no válida\n')
            }
        }

        rl.close();
    } catch (error) {
        console.error('Ha ocurrido un error:', error.message);
        rl.close();
    }
}

manageFile();
