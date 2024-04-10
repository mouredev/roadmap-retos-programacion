"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require('fs');
var readlineSync = require('readline-sync');
//writeFile permite escribir en un fichero, y tambien lo crea si este aun no existe
fs.writeFile('achapeton.txt', "\n    - Nombre: Andres Chapeton\n    - Edad: 26\n    - Lenguaje favorito: TypeScript\n  ", function (error) {
    if (error)
        throw error;
    console.log('File created');
});
//Leer contenido del fichero
fs.readFile('achapeton.txt', function (error, data) {
    if (error)
        throw error;
    console.log(data.toString());
});
//Eliminar un fichero
fs.unlink('achapeton.txt', function (error) {
    if (error)
        throw error;
    console.log('File deleted');
});
// DIFICULTAD EXTRA
var guardarVenta = function () {
    var nombreProducto = readlineSync.question('Nombre del producto ');
    var cantidadVendida = readlineSync.question('Cantidad vendida: ');
    var precioTotal = readlineSync.question('Precio: ');
    fs.appendFile('ventas.txt', "".concat(nombreProducto, ", ").concat(cantidadVendida, ", $").concat(precioTotal, "]"), function (error) {
        if (error)
            throw error;
    });
};
var listarVentas = function () {
    fs.readFile('ventas.txt', function (error, data) {
        if (error)
            throw error;
        console.log(data.toString());
    });
};
var gestionarVentas = function () {
    var option = '';
    var menu = 'MENU: \n 1. Agregar nueva venta \n 2. Listar ventas \n 3. Salir \n Escoger una opcion: ';
    while (option !== '3') {
        option = readlineSync.question(menu);
        switch (option) {
            case '1':
                guardarVenta();
                break;
            case '2':
                listarVentas();
                break;
            case '3':
                fs.unlink('ventas.txt', function (error) {
                    if (error)
                        throw error;
                    console.log('Fichero eliminado');
                });
                break;
            default:
                console.log('Opcion no valida. Intentar de nuevo.');
                break;
        }
    }
};
gestionarVentas();
