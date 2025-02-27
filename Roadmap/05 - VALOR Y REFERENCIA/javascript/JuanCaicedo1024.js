/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */



//Por valor 
let string = "Hola "
let Number = 12345
let boolean = true
let Noexite = null


// Asignación "Por Referencia"
let obj1 = { nombre: "Juan" };
let obj2 = obj1; // Se copia la referencia en memoria

obj2.nombre = "Pedro"; // Modificamos obj2, pero también cambia obj1

console.log(obj1.nombre); // "Pedro"
console.log(obj2.nombre); // "Pedro"


// funciones por valor 

function Iva (precio) {
    precioIva = precio * 0.25
    final = precioIva + precio
    console.log (`este es el precio original ${precio}`);
    console.log (`este es el precio con Iva ${final}`);
}

//funcion por referencia 

let stock = [
    {nombre: "cafe", precio: 1000, stock: 5},
    {nombre: "agua", precio: 1800, stock: 7},
    {nombre: "Bombilla", precio: 80, stock: 2}
]

function actualizaStock(producto,cantidad) {
    stockProductos[producto].stock=cantidad;
    console.log(`El nuevo stock de ${stockProductos[producto].nombre} es: ${cantidad}`);
}

actualizaStock(1,9);


/* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


let A = 1024
let B = 1001


function InversosPorValor (A , B) {
    let Aguardado = A
    A = B
    B = Aguardado

    return (
        console.log(`Los valores invertidos de A = ${A} y los valores inciales de B = ${B}`)
    )
}
console.log(`Los valores inciales de A = ${A} y los valores inciales de B = ${B}`)
InversosPorValor(A,B)

let arrayUno = [
    1,2,3,4
    ]
    let arrayDos = [
        0,1,1,1,1
    ]
    function InversosPorReferencia (arrayUno, arrayDos){
        let ArryaUnoGuardada = arrayUno
        arrayUno = [...arrayDos]
        arrayDos = [...ArryaUnoGuardada]
        
        return (console.log(`array uno es = ${arrayUno} y arrayDos es = ${arrayDos}`))
    
    }
    InversosPorReferencia(arrayUno, arrayDos)

