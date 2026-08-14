/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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

/* const fs = require("fs")

const fileName = "cruzballDev.txt"

// Crear el archivo líneas y escribir varias líneas.
fs.writeFileSync(
    fileName,
    "Nombre: Antonio\nEdad: 38\nLenguaje favorito: JavaScript"
)

// Leer e imprimir el contenido del archivo.
const contenido = fs.readFileSync(fileName, "utf8")
console.log(contenido)

// Borrar el archivo
fs.unlinkSync(fileName) */

/*
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

const readline = require("node:readline/promises");
const { stdin, stdout } = require("node:process");

const rl = readline.createInterface({
    input: stdin,
    output: stdout
});

const fs = require("fs")

const fileName = "archivo.txt"

async function main() {
    let activo = true

    while(activo) {

        const opcion = await rl.question(`
        Elige una de las siguientes opciones:

        1. Añadir producto
        2. Consultar producto
        3. Actualizar producto
        4. Eliminar producto
        5  Mostrar producto
        6 Venta por producto
        7 Venta total
        8 Salir

        Opción elegida: `)

        switch(opcion) {
            case "1": //Añadir producto
                {
                    const añadirNombre = await rl.question(`Nombre: \n`)
                    const añadirCantidad = await rl.question(`Cantidad: \n`)
                    const añadirPrecio = await rl.question(`Precio: \n`)
                    fs.appendFileSync(
                        fileName,
                        `${añadirNombre}, ${añadirCantidad}, ${añadirPrecio}\n`
                    )
                }
                break;
            case "2": // Consultar producto
                {
                    const consulta = await rl.question("Nombre del producto: ")

                    const datos = fs.readFileSync(fileName, "utf-8")
                    const productos = datos
                        .split("\n")
                        .filter(producto => producto !== "")

                    let encontrado = false

                    for(const producto of productos) {
                        const partes = producto.split(", ")
                        if(partes[0] === consulta) {
                            console.log(`Nombre: ${partes[0]}`)
                            console.log(`Cantidad: ${partes[1]}`)
                            console.log(`Precio: ${partes[2]}`)
                            encontrado = true
                            break;
                        }
                    }
                    if(!encontrado) {
                        console.log("¡El producto no existe!")
                    }
                }
                break;
            case "3": // Actualizar producto
                {
                    const datos = fs.readFileSync(fileName, "utf-8")
                    const productos = datos
                        .split("\n")
                        .filter(producto => producto !== "")

                    const actualizarNombre = await rl.question(`Nombre: \n`)
                    const actualizarCantidad = await rl.question(`Cantidad: \n`)
                    const actualizarPrecio = await rl.question(`Precio: \n`)

                    let encontrado = false

                    for(let i = 0; i < productos.length; i ++) {
                        const producto = productos[i].split(", ")

                        if(producto[0] === actualizarNombre) {
                            productos[i] = `${actualizarNombre}, ${actualizarCantidad}, ${actualizarPrecio}`
                            encontrado = true
                            break;
                        }
                    }
                    if(!encontrado) {
                        console.log("¡Producto no encontrado!")
                    }
                    fs.writeFileSync(fileName, productos.join("\n"))
                }
                break;
            case "4": // Eliminar producto
                    {
                        const eliminarProducto = await rl.question("Nombre del producto: ")
                        const datos = fs.readFileSync(fileName, "utf-8")
                        const productos = datos
                            .split("\n")
                            .filter(producto => producto !== "")

                        let encontrado = false

                        const productoEliminado = productos.filter(producto => {
                            const partes = producto.split(", ")

                            if(partes[0] === eliminarProducto) {
                                encontrado = true
                            }

                            return partes[0] !== eliminarProducto
                        })
                        if(!encontrado) {
                            console.log("¡Producto no encontrado!")
                        }
                        fs.writeFileSync(fileName, productoEliminado.join("\n"))
                    }
                break;
            case "5": // Mostrar producto
                    {
                        const datos = fs.readFileSync(fileName, "utf-8")
                        console.log(datos)
                    }
                break;
            case "6": //venta por producto
                    {
                        const datos = fs.readFileSync(fileName, "utf-8")
                        const productos = datos
                            .split("\n")
                            .filter(producto => producto !== "")

                        const consulta = await rl.question("Introduce el nombre del producto: ")

                        let encontrado = false

                        for(const producto of productos) {
                            const partes = producto.split(", ")

                            if(consulta === partes[0]) {
                                const cantidad = Number(partes[1])
                                const precio = Number(partes[2])

                                const total = cantidad * precio
                                encontrado = true
                                console.log(`El dinero que genera este producto es: ${total}€`)
                                break;
                            }
                        }
                        if(!encontrado) {
                            console.log("¡Producto no encontrado!")
                        }
                    }
                break;
            case "7": //venta total
                {
                    const datos = fs.readFileSync(fileName, "utf-8")
                    const productos = datos
                        .split("\n")
                        .filter(producto => producto !== "")

                    let ventaTotal = 0

                    for (const producto of productos) {
                        const partes = producto.split(", ")

                        const cantidad = Number(partes[1])
                        const precio = Number(partes[2])
                        ventaTotal += cantidad * precio;
                    }
                    console.log(`La venta total ha sido de: ${ventaTotal}€`)
                }
                break;
            case "8": // Salir
                if (fs.existsSync(fileName)) { // Borramos el archivo al salir con: fs.existsSync(fileName) → Comprueba si el archivo 
                                               // existe y con fs.unlinkSync(fileName) → Elimina el archivo del sistema de archivos.
                    fs.unlinkSync(fileName);
                }

                activo = false;
                console.log("El programa ha finalizado.");
                break;
            default:
                console.log("¡Introduce datos validos!")
                break;
        }
    }
    rl.close()
}
main()