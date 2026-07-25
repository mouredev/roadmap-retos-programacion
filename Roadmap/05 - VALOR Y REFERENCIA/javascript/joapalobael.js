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
    stockProductos[producto].stock=cantidad;
    console.log(`El nuevo stock de ${stockProductos[producto].nombre} es: ${cantidad}`);
}

actualizaStock(1,9);

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//Programa 1
let a =  "Abierto"
let b = "Cerrado"

function intercambiaPorValor(a,b) {
    let guardaA = a; //Guardas el primer valor
    a = b; // le asignas al primer valor, el segundo
    b = guardaA; //Le asignas al segundo valor, el primero
    return[a,b]
}
let resultado = intercambiaPorValor(a, b);
// Muestra los valores intercambiados
console.log(`Los valores intercambiados son: ${resultado}`); 
//comprobar valores originales
console.log(`Los valores originales son: ${a}, ${b}`); 

// Programa2
let programa2 = [
    {nombre: "Gary" , tipo: "Caracol"},
    {nombre: "Bob", tipo: "Esponja"},
    {nombre: "Patricio", tipo: "Estrella"},

]

function intercambiaPorReferencia (objeto,index1, index2){
    let guardaA = objeto[index1]; //Guardas el primer valor
    objeto[index1] = objeto[index2]; //Asignas el primer valor, al segundo
    objeto[index2] = guardaA; //Asignas al segundo valor, el primero que guardaste

    console.log(programa2);
}

intercambiaPorReferencia(programa2,0,2);


