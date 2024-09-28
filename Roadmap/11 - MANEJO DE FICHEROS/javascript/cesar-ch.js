/*
    * #11 MANEJO DE FICHEROS
*/
const fs = require('fs');
const readline = require('readline');

const nombre = 'cesar-ch'
const edad = 4
const lenguajeFavorito = 'JavaScript'
const contenido = `Nombre: ${nombre}\nEdad: ${edad}\nLenguaje de programación favorito: ${lenguajeFavorito}`

fs.writeFile(`${nombre}.txt`, contenido, (err) => {
    if (err) throw err
    console.log(`1. Archivo ${nombre}.txt creado exitosamente`)
    console.log('2. Contenido añadido al archivo')
    leerArchivo(nombre)
})

function leerArchivo(nombre) {
    fs.readFile(`${nombre}.txt`, 'utf-8', (err, data) => {
        if (err) throw err
        console.log('3. Contenido leído del archivo')
        console.log(data)
        borrarArchivo(nombre)
    })
}

function borrarArchivo(nombre) {
    fs.unlink(`${nombre}.txt`, (err) => {
        if (err) throw err
        console.log('4. Archivo eliminado exitosamente')
        menu()
    })
}

/*
    * DIFICULTAD EXTRA
*/

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const menu = () => {
    console.log("\n=== Gestión de Ventas ===");
    console.log("1. Añadir producto");
    console.log("2. Consultar producto");
    console.log("3. Actualizar producto");
    console.log("4. Eliminar producto");
    console.log("5. Calcular venta total");
    console.log("6. Calcular venta por producto");
    console.log("7. Salir");
    console.log("===========================");

    seleccionarOpcion();
}

const seleccionarOpcion = () => {
    rl.question('Seleccione una opción: ', (opcion) => {
        if (opcion === '1') {
            añadirProducto();
        } else if (opcion === '2') {
            consultarProducto();
        } else if (opcion === '3') {
            actualizarProducto();
        } else if (opcion === '4') {
            eliminarProducto();
        } else if (opcion === '5') {
            calcularVentaTotal();
        } else if (opcion === '6') {
            calcularVentaPorProducto();
        } else if (opcion === '7') {
            eliminarArchivo()
            rl.close();
        } else {
            seleccionarOpcion();
        }
    });
}

const añadirProducto = () => {
    rl.question('Introduce el nombre del producto: ', (nombre) => {
        rl.question('Introduce la cantidad del producto: ', (cantidad) => {
            rl.question('Introduce el precio del producto: ', (precio) => {
                const producto = `${nombre},${cantidad},${precio}\n`;
                fs.appendFile('productos.txt', producto, (err) => {
                    if (err) throw err;
                    console.log('Producto añadido correctamente');
                    menu()
                    seleccionarOpcion()
                });
            });
        });
    });
}

const consultarProducto = () => {
    rl.question('Introduce el nombre del producto a consultar: ', (nombre) => {
        fs.readFile('productos.txt', 'utf-8', (err, data) => {
            if (err) throw err;
            const productos = data.split('\n');
            const productoEncontrado = productos.find((producto) => producto.split(',')[0] === nombre);
            if (productoEncontrado) {
                console.log(`Producto encontrado: ${productoEncontrado}`);
            } else {
                console.log('Producto no encontrado');
            }
            menu()
            seleccionarOpcion()
        });
    });
}

const actualizarProducto = () => {
    rl.question('Introduce el nombre del producto a actualizar: ', (nombre) => {
        rl.question('Introduce la nueva cantidad del producto: ', (cantidad) => {
            rl.question('Introduce el nuevo precio del producto: ', (precio) => {
                const producto = `${nombre},${cantidad},${precio}\n`;
                fs.readFile('productos.txt', 'utf-8', (err, data) => {
                    if (err) throw err;
                    const productos = data.split('\n');
                    const productoEncontrado = productos.find((producto) => producto.split(',')[0] === nombre);
                    if (productoEncontrado) {
                        const productosFiltrados = productos.filter((producto) => producto.split(',')[0] !== nombre);
                        const productosString = productosFiltrados.join('\n');
                        fs.writeFile('productos.txt', productosString + producto, (err) => {
                            if (err) throw err;
                            console.log('Producto actualizado correctamente');
                        });
                    } else {
                        console.log('Producto no encontrado');
                    }
                    menu()
                    seleccionarOpcion()
                });
            });
        });
    })
}

const eliminarProducto = () => {
    rl.question('Introduce el nombre del producto a eliminar: ', (nombre) => {
        fs.readFile('productos.txt', 'utf-8', (err, data) => {
            if (err) throw err;
            const productos = data.split('\n');
            const productoEncontrado = productos.find((producto) => producto.split(',')[0] === nombre);
            if (productoEncontrado) {
                const productosFiltrados = productos.filter((producto) => producto.split(',')[0] !== nombre);
                const productosString = productosFiltrados.join('\n');
                fs.writeFile('productos.txt', productosString, (err) => {
                    if (err) throw err;
                    console.log('Producto eliminado correctamente');

                });
            } else {
                console.log('Producto no encontrado');
            }
            menu()
            seleccionarOpcion()
        })
    });
}

const calcularVentaTotal = () => {
    fs.readFile('productos.txt', 'utf-8', (err, data) => {
        if (err) throw err;
        const productos = data.split('\n');
        let total = 0;
        productos.slice(0, productos.length - 1).forEach((producto) => {
            const [nombre, cantidad, precio] = producto.split(',');
            total += parseInt(cantidad) * parseInt(precio);
        });
        console.log(`Venta total: ${total}`);
        menu()
        seleccionarOpcion()
    })
}

const calcularVentaPorProducto = () => {
    rl.question('Introduce el nombre del producto a consultar: ', (nombre) => {
        fs.readFile('productos.txt', 'utf-8', (err, data) => {
            const productos = data.split('\n');
            const productoEncontrado = productos.find((producto) => producto.split(',')[0] === nombre);
            if (productoEncontrado) {
                const [nombre, cantidad, precio] = productoEncontrado.split(',');
                const total = parseInt(cantidad) * parseFloat(precio);
                console.log(`Venta total: ${total}`);
            } else {
                console.log('Producto no encontrado');
            }
            menu()
            seleccionarOpcion()
        })
    })
}

const eliminarArchivo = () => {
    fs.unlink('productos.txt', (err) => {
        if (err) throw err;
        console.log('Archivo eliminado correctamente');
    });
    rl.close()
}