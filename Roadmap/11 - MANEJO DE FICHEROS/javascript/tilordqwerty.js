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

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require('fs')
var readlineSync = require('readline-sync');

fs.writeFile('tilordqwerty.txt', '-Nombre: Gabriel\n-Edad: 18\nLenguaje favorito: JavaScript', function(err){
    if (err){
        return console.log(err)
    }
    console.log('El archivo fue creado correctamente');
});

fs.readFile('tilordqwerty.txt', 'utf8', function(err, data){
    if (err){
        return console.log(err)
    }
    console.log(data);
});

fs.unlink('tilordqwerty.txt', function(err){
    if(err){
        return console.log(err)
    }
    console.log('El archivo fue borrado')
})

// Extra

const READLINE = require('readline');

function agregarProducto() {
    let nombreProducto = readlineSync.question('Nombre: ')
    let cantidadVendida = readlineSync.question('Cantidad: ')
    let precioTotal = readlineSync.question('Precio: ')  
    fs.appendFile('ventas.txt',  `-${nombreProducto}\n -${cantidadVendida}\n -${precioTotal}`, function(err){
if (err){
    return console.log(err);}
});
}

function listarProductosVentas(){
    fs.readFile('ventas.txt', 'utf8', function(err, data){
      if (err){
        return console.log(err);
    }
          console.log(data.toString());
       });       
    }

function gestionarVentas(){
    let selectOptions = '';
    let opciones = "--- BIENVENIDO --- \n 1. Agregar producto\n 2. Mostrar productos\n 3. Borrar producto\n 4. Salir\n Escoge una opcion: "
    while(selectOptions !== '3'){
        selectOptions = readlineSync.question(opciones);
        switch(selectOptions){
            case '1':
                agregarProducto();
                break;
            case '2':
                listarProductosVentas();
                break;
            case '3':
                fs.unlink('ventas.txt', function(err){
                    if(err){
                        return console.log(err);
                    }
                    console.log('El archivo fue borrado')
                });
                break;
            case '4':
                console.log('Adios')
                break;
            default:
                console.log('Opcion no valida. Intentar de nuevo.');
                return;
        }
    }
};
gestionarVentas();
