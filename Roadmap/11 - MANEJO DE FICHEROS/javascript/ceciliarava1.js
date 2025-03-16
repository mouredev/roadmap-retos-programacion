import fs from 'fs';
const writeStream = fs.createWriteStream('ceciliarava1.txt', { flags: 'a' }) // a - Appending data

const lines = ["Name: Cecilia Rava", "Age: 22 Years old", "Favorite programming language: Javascript"]
lines.forEach(line => {
    writeStream.write(line + '\n')
})
writeStream.end();


fs.readFile("ceciliarava1.txt", (err, data) => {
    if (err) throw err
    console.log(data.toString())

    fs.unlink("ceciliarava1.txt", (err) => {
        if (err) throw err
        console.log("File deleted!")
    })
})




/* Desarrolla un programa de gestión de ventas que almacena sus datos en un
* archivo .txt.
* - Cada producto se guarda en una línea del archivo de la siguiente manera:
*   [nombre_producto], [cantidad_vendida], [precio].
* - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
*   actualizar, eliminar productos y salir.
* - También debe poseer opciones para calcular la venta total y por producto.
* - La opción salir borra el .txt.
*/