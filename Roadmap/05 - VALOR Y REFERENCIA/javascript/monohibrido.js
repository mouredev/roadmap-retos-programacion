/* VALOR Y REFERENCIA */
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*/

/*
- Cómo se almacenan las variables en la memoria de la computadora.
- Qué pasa cuando asignamos una variable.
- Qué pasa cuando pasamos una variable como parámetro en una función

*/

/*
DATOS QUE SON PASADOS POR VALOR: Boolean, Null, Undefined, String, Number (valores primitivos del lenguaje)
- Cambiar una no cambia la otra porque las variables no tienen ninguna relación entre sí.
*/
console.log("====VALOR====")
let valor1 = 15;
let valor2 = valor1;
valor2 = 99;
console.log(`El valor1 es: ${valor1}`);
console.log(`El valor2 es: ${valor2}`);

/* FUNCTIONS */
let miArray = [1, 2, 3];

function modificarRef(arr) {
    arr.push(999);
    console.log("Dentro de la función: ", arr);
}

modificarRef(miArray);
console.log("Función externa: ", miArray);



/*
DATOS QUE SON PASADOS POR REFERENCIA: Object, arrays, functions
💡Las variables a las que se les asigna un valor no primitivo reciben una referencia a ese valor. 
Esa referencia apunta a la ubicación del objeto en la memoria. Las variables no contienen realmente el valor💡
*/
console.log("====REFERENCIA====")
/* ARRAYS */
let arrayNumeros = [1, 1, 2, 3];
let arrayNumeros2 = arrayNumeros;
arrayNumeros2.push(5);
console.log(`array números: ${arrayNumeros}`);
console.log(`array números 2: ${arrayNumeros2}`);


/* OBJECTS */
let objeto1 = {
    ciudad: "Santiago",
    pais: "Chile"
};

let objecto2 = objeto1;

objecto2.pais = "España";

console.log(objeto1);
console.log(objecto2);


/*EXCEPCIÓN   - CLONACIÓN PARA EVITAR PROBLMAS DE REFERENCIA, PARA EVITAR MODIFICAR EL OBJETO ORIGINAL,
CREE UNA COPIA SUPERFICIAL*/
let original = { nombre: "Cristian " };
let copia = { ...original };
copia.nombre = "Rodrigo";
console.log(`original: ${original.nombre}`);
console.log(`copia: ${copia.nombre}`)




/*
 * DIFICULTAD EXTRA (opcional):
 *   Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 *   Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.

*/


//PROGRAMA 1
function intercambiaPorValor(a, b) {
    let primerValor = a;
    a = b;
    b = primerValor;
    return [a, b];
}
let x = 10;
let y = 20;

let nuevoXeY = intercambiaPorValor(x, y);
console.log(`valor original de X e Y: ${x} , ${y}`);
console.log(`valor de nuevoX y nuevoY: ${nuevoXeY}`);

//==================================================================

//PROGRAMA 2

function intercambioPorReferencia(obj) {

    let temp = obj.a;
    obj.a = obj.b;
    obj.b = temp;
    return obj;
}

let miObjetivillo = { a: 10, b: 20 };

let nuevoObjetivillo = intercambioPorReferencia(miObjetivillo);

console.log(`Objetivillo originalillo: a=${miObjetivillo.a}, b=${miObjetivillo.b}`);
console.log(`Objetivillo nuevillo: a=${nuevoObjetivillo.a}, b=${nuevoObjetivillo.b}`);