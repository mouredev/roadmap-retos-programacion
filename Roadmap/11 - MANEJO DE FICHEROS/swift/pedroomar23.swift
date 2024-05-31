import Foundation

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

let file = "pedroomar23.text"
let fileUrl = FileManager.default.urls(from: .documentDirectory, in: .userDomainMask).appendingPathComponent(file)
let fileContent = """
    nombre: Pedro Omar 
    edad: 25
    lenguaje favorito: Swift 
"""

do {
    try fileContent.write(to: fileUrl, atomically: true, encoding: .utf8)
    let content = String(contentsOf: fileUrl, encoding: .utf8)
    print(content)

    try FileManager.default.removeItem(at: fileUrl)
} catch {
    print("Se encontraron varios errores \(error.localizedDescription)")
}

