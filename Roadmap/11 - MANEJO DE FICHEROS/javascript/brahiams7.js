// * EJERCICIO:
//  * Desarrolla un programa capaz de crear un archivo que se llame como
//  * tu usuario de GitHub y tenga la extensión .txt.
//  * Añade varias líneas en ese fichero:
//  * - Tu nombre.
//  * - Edad.
//  * - Lenguaje de programación favorito.
//  * Imprime el contenido.
//  * Borra el fichero.

const fs = require('fs');
const carpeta="BrahiamS7.txt"
const contenido="Brahiam, 19, Node"
const contenido2=`\n Barco, 19, Python`

fs.writeFileSync(carpeta,contenido)
fs.appendFile(carpeta,contenido2,function (err){
    if (err) throw err;
})

fs.readFile(carpeta,'utf8',(err,data)=>{
    if(err){
        console.log(err);
    } else {
        console.log(`El contenido de el archivo es ${data}`);
        
    }
}) 



fs.unlink(carpeta,function (err){
    if (err) throw err;
})

// * DIFICULTAD EXTRA (opcional):
//  * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
//  * archivo .txt.
//  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
//  *   [nombre_producto], [cantidad_vendida], [precio].
//  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
//  *   actualizar, eliminar productos y salir.
//  * - También debe poseer opciones para calcular la venta total y por producto.
//  * - La opción salir borra el .txt.
//  *
let readline = require('readline')
let rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let carpetaV="ventas.txt"


function sellings(){
    if(!fs.existsSync(carpeta)){
        fs.writeFile(carpeta,`Nuevo sistema de ventas \n`,(err)=>{
            if (err) {
                console.log(err)
            };
        })
    }
    
    rl.question(`Ingrese un producto, elige si deseas consultar, actualizar, eliminar o escribe (salir) para salir del programa: \n`,(answer)=>{
        let ans=answer.trim().toLowerCase()

        switch (ans) {
            case 'consultar':
                fs.readFile(carpetaV,'utf8',(err,data)=>{
                    if(err){
                        console.log(err);
                    } else {
                        console.log(`Las ventas registradas son: ${data}`);
                    }
                })
                sellings()
                break;
            case 'salir':
                fs.unlink(carpetaV,(err)=>{
                    if (err) console.log(err);
                })
                rl.close()
                break;
            default:
                fs.appendFile('ventas.txt',ans,(err)=>{
                    if (err) console.log(err);
                    
                })
                sellings()
                break;
        }

    })

}
sellings()