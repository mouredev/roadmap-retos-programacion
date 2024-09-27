/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

// Asignacion de variables por valor
let valor1 = 25;
console.log(`Asignación de variable por valor → valor1 = ${valor1}.`)

//Asignación de variables por referencia

let objeto1 = {nombre: "Johanna", edad: 30, signo: "Cancer"};
objetoReferencia = objeto1;
objetoReferencia.edad = 36;
console.log(`Asignación de variable por referencia → objetoReferencia = ${JSON.stringify(objeto1)}.`);

//Funciones con variables por valor
function descuento10(fullPrize) {
    fullPrize = fullPrize-fullPrize*0.10;
    console.log(`El precio del articulo con descuento es de ${fullPrize}`);
    return fullPrize;
}

let precioOriginal = 1480;
let precioConDescuento = descuento10(precioOriginal);

console.log(`El precio original fuera de la función sigue siendo: ${precioOriginal}`);
console.log(`El precio con descuento fuera de la función es: ${precioConDescuento}`);

// Funcion con variable por referencia

let stockProductos = [
    {nombre: "Mate", precio: 1000, stock: 5},
    {nombre: "Termo", precio: 1800, stock: 7},
    {nombre: "Bombilla", precio: 80, stock: 2}
]
function actualizaStock(producto,cantidad) {
    let nuevoStock = stockProductos;
    nuevoStock[producto].stock=cantidad;
    console.log(nuevoStock)
    return (nuevoStock);
}

actualizaStock(1,9);