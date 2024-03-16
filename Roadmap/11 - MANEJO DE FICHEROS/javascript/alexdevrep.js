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
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */

const fs = require('fs')
const nombreArchivo = "alexdevrep.txt"
const contenido = ["Alejandro", "24", "JavaScript"]
const contenidoFinal= contenido.join('\n')

/*
    Creamos las funciones callback que son requeridas como parámetro obligatorio 
    en las funciones asíncronas writeFile y unlink (para crear y borrar
    el fichero respectivamente)
*/
function errorCrear(err){
    if(err){
        console.log("Error al crear el archivo", err)
    }
    else{
        console.log("Archivo creado exitosamente")
    }
}

function errorBorrar(err){
    if(err){
        console.log("Error al borrar el fichero",err)
    }
    else{
        console.log("Archivo borrado exitosamente")
    }
}

//Creamos un fichero
fs.writeFile(nombreArchivo, contenidoFinal, errorCrear)

//Imprimimos el fichero
const datos=fs.readFileSync('alexdevrep.txt','utf-8')
console.log(datos)

//Borramos el fichero
fs.unlink(nombreArchivo,errorBorrar)

//Dificultad EXTRA

//Añadimos la función para enviar datos el programa
const prompt = require('prompt-sync')()
const nombreDocumento= "gestion_de_ventas.txt"

//Creamos la función principal del programa
const lista= [] 

function errorCrear(err){
    if(err){
        console.log("Error al crear el archivo", err)
    }
    else{
        console.log("Archivo creado exitosamente")
    }
}
function erroreliminar(err){
    if(err){
        console.log("No ha sido posible eliminar el fichero",err)

    }
    else{
        console.log("Fichero borrado con éxito")
    }

}

function gestion(accion){
    
    switch(accion){
        case 'añadir':
            console.log("Añada el producto a la lista")
            let nombre_producto = prompt("Por favor indique el nombre del producto: ")
            let cantidad_vendida = prompt("Porfavor indique las unidades vendidas: ")
            let precio = prompt("Por favor indique el precio unitario: ")
            let producto={
                "Nombre del producto": nombre_producto,
                "Cantidad_vendida": cantidad_vendida,
                "Precio unitario":precio
            }
            lista.push(producto)
            break
        
        case 'consultar':
            if (lista.length > 0) {
                console.log(lista);
            } else {
                console.log("No hay productos que mostrar en la lista")
            }
            break;
            
        case 'actualizar':
            let actualizar=prompt("Ingrese la clave del producto a actualizar: ")
            let nuevoProducto= lista.findIndex(producto => producto["Nombre del producto"]===actualizar)
            if (nuevoProducto !==-1){
                let nombre_producto = prompt("Por favor indique el nombre del producto: ")
                let cantidad_vendida = prompt("Porfavor indique las unidades vendidas: ")
                let precio = prompt("Por favor indique el precio unitario: ")
                let productoNuevo={
                    "Nombre del producto": nombre_producto,
                    "Cantidad_vendida": cantidad_vendida,
                    "Precio unitario":precio
                }
                
                lista.splice(nuevoProducto,1,productoNuevo)
            }
            else{
                console.log("No se encuentra el producto")
            }
            break
        case 'eliminar':
            let eliminar = prompt("Ingrese la clave del producto a eliminar: ")
            let indice=lista.findIndex(producto => producto["Nombre del producto"]=== eliminar)
            if (indice !== -1){
                lista.splice(indice,1)
                console.log("Producto eliminado exitosamente")
            }
            else{
                console.log("No se encuentra el producto")
            }
            break
        
            case 'ventaTotal':
                let ventaTotal = 0
                for (let i=0; i<lista.length;i++){
                    let producto = lista[i]
                    let cantidadVendida= parseFloat(producto["Cantidad_vendida"])
                    let precioUnitario= parseFloat(producto["Precio unitario"])
                    if (!isNaN(cantidadVendida) && !isNaN(precioUnitario)) {
                        ventaTotal += cantidadVendida * precioUnitario;
                    } else {
                        console.log(`Advertencia: El producto ${producto["Nombre del producto"]} tiene datos de cantidad o precio no válidos.`)
                    }
                }
                console.log("La venta total de todos los productos es: " ,ventaTotal,"euros")
                break
            case 'ventaProducto':
                let ventaProducto =0
                let venta = prompt("Ingrese el producto de que desea sacar la venta unitaria: ")
                for(let i=0;i<lista.length;i++){
                    let producto =lista[i]
                    if(producto["Nombre del producto"]===venta){
                        let cantidad = parseFloat(producto["Cantidad_vendida"])
                        let precio = parseFloat(producto["Precio unitario"])
                        if(!isNaN(cantidad)&& !isNaN(precio)){
                            ventaProducto = cantidad * precio
                            console.log("La venta unitaria es de ", ventaProducto, "euros")
                        }
                        else{
                            console.log(`Advertencia: El producto ${producto["Nombre del producto"]} tiene datos de cantidad o precio no válidos.`)
                        }
                    }
                    
                    
                    break
                }
        case 'guardar':
            let contenidoLista = JSON.stringify(lista, null, 2);  // Convierte la lista a una cadena JSON con formato
            try {
                fs.writeFileSync(nombreDocumento, contenidoLista)
                console.log("Datos guardados")
            } catch (err) {
            console.error("Error al escribir en el archivo", err)
            }
            break
        
        case 'salir':
            fs.unlink("gestion_de_ventas.txt",erroreliminar)
            break
                

        default:
            console.log("Opción no válida")
            break

    }
}
while (true){
    
    console.log("Archivo de la gestión de ventas")
    console.log("Funciones disponibles: añadir , consultar, actualizar, eliminar, salir, ventaTotal, ventaProducto, guardar, salir")
    let accion = prompt("Escriba una de las opciones disponibles: ")
    gestion(accion)
    

    if (accion == "salir"){
        
        break
    }
}



