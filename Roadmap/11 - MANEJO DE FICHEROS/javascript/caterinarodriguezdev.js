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

const fs = require('fs');

const crearArchivoTexto = (nombre, edad, lenguaje) => {
    const contenido = `Mi nombre es ${nombre}, tengo ${edad} años y mi lenguaje de programación favorito es ${lenguaje}`;
    fs.writeFile(nombre + '.txt', contenido, (error) => {
        if (error) {
            console.error('Error al crear el archivo:', error);
        }
    });
}

const readline = require('readline');
const rl = readline.createInterface(process.stdin, process.stdout   );

let productos = [];

const gestionDeVentas = () => {

    console.log(`
        
        ----------------------------------------------
        BIENVENIDO AL PROGRAMA DE GESTIÓN DE VENTAS:
        1. Añadir producto
        2. Eliminar producto
        3. Ver productos
        4. Actualizar producto`);

    rl.question('Elija una opción -> ', (term) => {
        switch(term) {
            case '1': 
                addProduct();
                break;
            case '2': 
                deleteProduct();
                break;
            case '3':
                listProducts();
                break;
            case '4': 
                updateProduct();
                break;
            default:
                gestionDeVentas();
                break;
        }
    })
}

const addProduct = () => {
    rl.question('Nombre del producto -> ', (term) => {
        const nombre = term;

        rl.question('Cantidad vendida -> ', (term) => {
            const cantidadVendida = term;

            rl.question('Precio -> ', (term) => {
                const precio = term;

                const producto = {
                    nombre,
                    cantidadVendida,
                    precio
                }

                productos.push(producto);

                updateFromProductos();

                console.log('Producto añadido!');

                gestionDeVentas();
            })
        })
    })
}

const deleteProduct = () => {
    rl.question('Nombre del producto que quiere eliminar -> ', (term) => {
        productos = productos.filter(prod => prod.nombre !== term);

        updateFromProductos();
        
        console.log('Producto eliminado!');

        gestionDeVentas();
    })
}

const listProducts = () => {
    productos.forEach(prod => 
        console.log(`Nombre: ${prod.nombre}, Cantidad Vendida: ${prod.cantidadVendida}, Precio: ${prod.precio}`)
    );
    rl.question('Seguir? -> ', (term) => {
        if (term === 'Si') {
            gestionDeVentas();
        } else {
            rl.close();
        }
    })
}

const updateProduct = () => {
    rl.question('¿Qué producto desea actualizar? -> ', (term) => {
        let prodToUpdate = productos.find(prod => prod.nombre === term);
        
        if (!prodToUpdate) {
            console.log('Producto no encontrado.');
            return gestionDeVentas();
        }

        let prodIndex = productos.indexOf(prodToUpdate);

        rl.question('¿Qué desea actualizar? -> ', (term) => {

            switch(term) {
                case 'nombre': 
                    rl.question('¿Qué nombre desea ponerle? -> ', (term) => {
                        prodToUpdate.nombre = term;
                        productos[prodIndex] = prodToUpdate;

                        updateFromProductos();
                        console.log('Producto actualizado!');
                        gestionDeVentas();
                    });
                    break;
                case 'cantidad vendida':
                    rl.question('¿Qué cantidad se ha vendido? -> ', (term) => {
                        prodToUpdate.cantidadVendida = term;
                        productos[prodIndex] = prodToUpdate;

                        updateFromProductos();
                        console.log('Producto actualizado!');
                        gestionDeVentas();
                    });
                    break;
                case 'precio':
                    rl.question('¿Qué precio tiene? -> ', (term) => {
                        prodToUpdate.cantidadVendida = term;
                        productos[prodIndex] = prodToUpdate;

                        updateFromProductos();
                        console.log('Producto actualizado!');
                        gestionDeVentas();
                    });
                    break;
            }
        })
    })
}

const updateFromProductos = () => {
    let content = '';
    productos.forEach(prod => content += `\n${prod.nombre}, ${prod.cantidadVendida}, ${prod.precio}`);
    fs.writeFile('gestionProductos.txt', content, (error) => {
        if (error) {
            console.error('Error al crear el archivo:', error);
        }
});
}

const crearArchivoTextoWithReadline = () => {
    rl.question('Nombre -> ', (term) => {
        const nombre  = term;

        rl.question('Edad -> ', (term) => {
            const edad = term;

            rl.question('Lenguaje de programación favorito -> ', (term) => {
                const lenguaje = term;

                crearArchivoTexto(nombre, edad, lenguaje);

                console.log('Archivo Creado :)');

                entryPoint();
            })
        })
    })
}

const entryPoint = () => {

    console.log(` PROGRAMAS 
        1. Crea un archivo de texto
        2. Controla tus ventas`);

    rl.question('¿Qué programa quiere iniciar? -> ', (term) => {
        switch(term) {
            case '1':    
                crearArchivoTextoWithReadline();
                break;
            case '2':
                gestionDeVentas();
                break;
            default:
                'Por favor, elije un programa existente :,('
        }
    })
}

entryPoint();