/*const fs = require("fs"); //Importa el módulo que permite interactuar con el sistema de archivos

const nombreUsuario = "emedevelopa";
const contenido = [
    "Nombre: María Campos",
    "Edad: 33",
    "Lenguaje de programación: JavaScript"
].join("\n") //lo transforma a string y hace salto de linea.

const nombreArchivo = `${nombreUsuario}.txt`;

//Escribir contenido en el archivo
fs.writeFile(nombreArchivo, contenido, (err) => {
    if (err) {
        console.error("Error al crear el archivo:", err);
    } else {
        console.log(`Archivo '${nombreArchivo}' creado con éxito`);

        //Leer contenido del archivo
        fs.readFile(nombreArchivo, "utf8", (err, data) => {
            if (err) {
                console.error("Error al leer el archivo:", err);
            } else {
                console.log(`Contenido del archivo '${nombreArchivo}':\n`, data);

                //Borrar archivo
                fs.unlink(nombreArchivo, (err) => {
                    if(err) {
                        console.error("Error al borrar el archivo:", err);
                    } else {
                        console.log(`Archivo '${nombreArchivo}' borrado con éxito`);
                    }
                });
            }
        });
    }
}); */

//EXTRA
const fs = require("fs");
const { arch } = require("os");
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const archivoVentas = "ventas.txt";

function añadirProductos() {
        rl.question("Nombre del producto: ", (nombre) => {
            rl.question("Cantidad vendida: ", (cantidad) => {
                rl.question("Precio: ", (precio) => {
                    const linea = `${nombre}, ${cantidad}, ${precio}\n`;
                    fs.appendFile(archivoVentas, linea, (err) => {
                        if(err) {
                            console.error("Ha ocurrido un error", err);
                        } else {
                            console.log("Producto añadido con éxito");
                        }
                        mostrarMenu();
                    });
                });
            });
        });
    
}

function consultaVentas() {
    fs.readFile(archivoVentas, "utf8", (err,data) => {
        if (err) {
            console.error("Error al leer el archivo", err);
        } else {
            console.log("Ventas:\n", data);
        }
        mostrarMenu();
    });
}

function actualizarProductos () {
    rl.question("Añade el nombre del producto que deseas actualizar: ", (nombre) => {
        fs.readFile(archivoVentas, "utf8", (err, data) => {
            if (err) {
                console.error("Error al leer el archivo:", err);
                mostrarMenu();
                return;
            }
            const lineas = data.split("\n");
            let productoEncontrado = false;
            const nuevoContenido = [];

            for (const linea of lineas) {
                const[nombreProducto, cantidadVendida, precio] = linea.split(', ');
                if (nombreProducto === nombre) {
                    rl.question ("Añade la nueva cantidad vendida: ", (nuevaCantidad) => {
                        rl.question("Añade el nuevo precio: ", (nuevoPrecio) => {
                            const nuevaLinea = `${nombre}, ${nuevaCantidad}, ${nuevoPrecio}`;
                            nuevoContenido.push(nuevaLinea);
                            productoEncontrado = true;
                            console.log("Producto actualizado con éxito.");
                            rl.close();
                        });
                    });
                } else {
                    nuevoContenido.push(linea);
                }
            } if (!productoEncontrado) {
                console.log("No se encontró el producto.");
                mostrarMenu();
            } else {
                fs.writeFile(archivoVentas, nuevoContenido.join('\n'), (err) => {
                    if (err) {
                        console.error("Error al escribir el archivo.", err);
                    }
                    mostrarMenu();
                });
            }
        });
    });
}

function eliminarProducto () {
    rl.question("Añade el nombre del producto que deseas eliminar: ", (nombre) => {
        fs.readFile(archivoVentas, "utf8", (err, data) => {
            if (err) {
                console.log("Error al leer el archivo.", err);
                mostrarMenu();
                return;
            }
            const lineas = data.split('\n');
            let productoEncontrado = false;
            const nuevoContenido = [];

            for (const linea of lineas) {
                const [nombreProducto] = linea.split(', ');
                if (nombreProducto === nombre) {
                    productoEncontrado = true;
                    console.log("Producto eliminado con éxito.");
                } else {
                    nuevoContenido.push(linea);
                }
            }
            if (!productoEncontrado) {
                console.log("No se encontró el producto.");
            }
            fs.writeFile(archivoVentas, nuevoContenido.join('\n'), (err) => {
                if (err) {
                    console.error("Error al escribir en el archivo.", err);
                }
                mostrarMenu();
            });
        });
    });
}

function salir () {
    fs.unlink (archivoVentas, (err) => {
        if (err) {
            console.error("Error al borrar el archivo:", err);
        } else {
            console.log("Archivo borrado con éxito. Saliendo...");
        }
        rl.close();
    });
}

function mostrarMenu() {
    console.log('\n-- MENÚ --');
    console.log('1. Añadir producto');
    console.log('2. Actualizar producto');
    console.log('3. Consultar ventas');
    console.log('4. Eliminar producto');
    console.log('5. Salir');
    rl.question('6. Selecciona una opción: ', (opcion) => {
        switch (opcion) {
            case '1':
                añadirProductos();
                break;
            case '2':
                actualizarProductos();
                break;
            case '3':
                consultaVentas();
                break;
            case '4':
                eliminarProducto();
                break;
            case '5':
                salir();
                break;
            default:
                console.log("Opción no válida. Intentalo de nuevo.");
                mostrarMenu();
        }
    });
}
mostrarMenu();