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


// EJERCICIO

const { error } = require('console')
const fs = require('fs')

const fileName = "airesEsteban.txt"

function crearArchivo(){
const contenido =`Nombre: Esteban \nEdad: 20\nLenguaje favorito: Javascript`
    fs.writeFile(fileName, contenido, (e) => {
        if (e) {
            console.error("Error al crear archivo", e)
            return
        }
        console.log(`Archivo ${fileName} creado con éxito`)
        leerArchivo()
    })
}

function leerArchivo(){
    fs.readFile(fileName, "utf-8", (e,data)=> {
        if (e) {
            console.error("Error al leer el archivo", e)
            return
        }
        console.log(`Contenido del archivo: ${data}`)
        eliminarArchivo()
    })
}

function eliminarArchivo(){
    fs.unlink(fileName, (e) => {
        if (e){
            console.error("Error al borrar el archivo", e)
            return
        }
        console.log(`Archivo ${fileName} borrado con exito`)
    })
}

crearArchivo()

// EXTRA
const readline = require('readline')

const fileName1 = "ventas.txt"

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function preguntar(pregunta) {
    return new Promise((resolve) => {
        rl.question(pregunta, (respuesta) => resolve(respuesta))
    })
}

async function menu(){
    while(true){
        console.log("- MENÚ DE GESTIÓN DE VENTAS -")
        console.log("1. Añadir producto")
        console.log("2. Consultar producto")
        console.log("3. Actualizar producto")
        console.log("4. Eliminar producto")
        console.log("5. Calcular venta total")
        console.log("6. Calcular venta por producto")
        console.log("7. Salir")

        const opcion = await preguntar ("Seleccione una opción")

        switch(opcion){
            case "1":
                await añadirProducto()
                break
            case "2":
                await consultarProducto()
                break
            case "3":
                await actualizarProducto()
                break
            case "4":
                await eliminarProducto()
                break
            case "5":
                await ventaTotal()
                break
            case "6":
                await ventasPorProducto()
                break
            case "7":
                await salir()
                return
            default:
                console.log("Opción no válida, intente de nuevo")    
        }
    }
}

async function añadirProducto() {
    const nombre = await preguntar("Nombre del producto: ")
    const cantidad = await preguntar("Cantidad de unidades vendidas: ")
    const precio = await preguntar("Precio unitario: ")
    const linea = `${nombre}, ${cantidad}, ${precio}\n`

    fs.appendFile(fileName1, linea, (error) => {
        if (error) {
            console.error("Error al añadir producto", error)
        } else {
            console.log("Producto añadido con éxito")
        }
    })
}

async function actualizarProducto() {
    const nombre = await preguntar("Nombre del producto: ")
    const cantidad = await preguntar("Cantidad de unidades vendidas: ")
    const precio = await preguntar("Precio unitario: ")

    fs.readFile(fileName1, "utf8", (error, data) =>{
        if (error){
            console.error("Error al leer los productos", error)
            return
        }
        const lineas = data.split("\n").filter(linea => linea.trim())
        let encontrado = false
        for(let i = 0; i < lineas.length; i++){
            const [producto] = lineas[i].split(",")
            if (producto.trim() === nombre.trim()){
                lineas[i] = `${nombre}, ${cantidad}, ${precio}`
                encontrado = true
                break
            }
        }
        if(!encontrado){
            console.log("El producto no fue encontrado")
            return
        }

        fs.writeFile(fileName1, lineas.join("\n"), (error)=> {
            if(error){
                console.error("Error al actualizar el producto:", error)
            } else{
                console.log("Producto actualizado con éxito.")
            }
        })
    }
    )
}

async function consultarProducto() {
    fs.readFile(fileName1, 'utf8', (error, data) => {
        if (error) {
            console.error("Error al leer los productos:", error);
            return;
        }
        if (!data.trim()) {
            console.log("No hay productos registrados.")
            return;
        }
        console.log("Productos registrados:")
        console.log(data)
    });
}


async function eliminarProducto() {
    const nombre = await preguntar("Nombre del producto a eliminar")

    fs.readFile(fileName1, 'utf8', (error, data) => {
        if(error){
            console.error("Error al leer los productos:", error)
            return
        }

        const lineas = data.split("\n").filter(linea => linea.trim())
        const nuevasLineas = lineas.filter(linea => {
            const [producto] = linea.split(",")
            return producto && producto.trim().toLowerCase() !== nombre.trim().toLowerCase()
        })

        if(lineas.length === nuevasLineas.length){
            console.log("Producto no encontrado")
            return
        }
        const contenidoFinal = nuevasLineas.join("\n") + (nuevasLineas.length ? "\n" : "")

        fs.writeFile(fileName1, contenidoFinal, (error) => {
            if (error) {
                console.error("Error al eliminar el producto:", error);
            } else {
                console.log("Producto eliminado con éxito.");
            }
        })
    })
}

async function ventaTotal() {
    fs.readFile(fileName1, "utf8", (error ,data)=> {
        if(error){
            console.error("Error al leer los productos",error)
            return
        }

        const lineas = data.split('\n').filter(linea => linea.trim())
        let total = 0

        for(const linea of lineas){
            const [, cantidad,precio] = linea.split(',').map(valor => parseFloat(valor.trim()))
            total += cantidad * precio
        }
        console.log(`Venta total: ${total.toFixed(2)}`)
    })
}

async function ventasPorProducto() {
    const nombre = await preguntar("Nombre del producto:")

    fs.readFile(fileName1, "utf8", (error ,data)=> {
        if(error){
            console.error("Error al leer los productos",error)
            return
        }

        const lineas = data.split('\n').filter(linea => linea.trim())
        let encontrado = false

        for(const linea of lineas){
            const [producto, cantidad,precio] = linea.split(',').map(valor => (valor.trim()))
            if(producto === nombre){
                const venta = parseFloat(cantidad) * parseFloat(precio)
                console.log(`Venta del producto: ${nombre}: $${venta.toFixed(2)}`)
                encontrado = true
                break
            }
        }
        if(!encontrado){
            console.log("Producto no encontrado.")
        }
    })

}

async function salir() {
    fs.unlink(fileName1, (error)=> {
        if (error && error.code !== "ENOENT"){
            console.error("Error al borrarl el archivo",  error)
        }else {
            console.log("Archivo borrado")
        }
        rl.close()
    })
}

menu()