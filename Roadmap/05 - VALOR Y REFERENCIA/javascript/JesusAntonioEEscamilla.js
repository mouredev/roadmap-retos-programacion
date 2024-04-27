/** #05 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Los tipos de datos primitivos en JavaScript,
    como números, cadenas, booleanos, null y undefined, se manejan por valor.
 * Cuando asignas un valor a una variable, se copia directamente ese valor en la variable. 
 * Modificar la variable no afecta a la variable original.
 * Excepto los valores nulls o undefined esos siempre serán vacíos.
 */

//-----NÚMEROS-----
var num1 = 10;
var num2 = num1;
num2 = 20;

console.log(num1); // Se imprime 10 ya que no se a modificado
console.log(num2); // Se imprime 20 aquí si se cambio el valor que se asigno inicialmente


//-----CADENAS DE TEXTO-----
var str1 = "Hola";
var str2 = str1;
str2 = "Hola Mundo";

console.log(str1); // Se imprime "Hola" ya que no se a modificado
console.log(str2); // Se imprime "Hola Mundo" aquí si se cambio el valor que se asigno inicialmente


//-----BOOLEANOS-----
var bool1 = true;
var bool2 = bool1;
bool2 = false;

console.log(bool1); // Se imprime TRUE ya que no se a modificado
console.log(bool2); // Se imprime FALSE aquí si se cambio el valor que se asigno inicialmente



/**
 * Los objetos y arreglos en JavaScript se manejan por referencia.
 * Cuando asignas un objeto o un arreglo a una variable, en realidad
    estás asignando una referencia a la ubicación en memoria donde se almacena ese objeto o arreglo.
 * Modificar el objeto o arreglo a través de una variable
    también afectará a otras variables que hagan referencia al mismo objeto o arreglo.
 */

//-----OBJETOS-----
var obj1 = {
    nombre: "Jesus Antonio",
    edad: 25
};
var obj2 = obj1;
obj2.edad = 30;

console.log(obj1.edad); // Se imprime 30 ya que el objeto esta ocupando la misma memoria de objeto


//-----ARREGLOS-----
var arr1 = [1, 2, 3];
var arr2 = arr1;
arr2.push(4);

console.log(arr1); // Se imprime [1, 2, 3, 4] ya se ocupan el misma memoria los arreglos



/**
 * Ahora lo haremos con funciones de valor y referencia.
 */

//-----POR VALOR-----

function duplicarNumero(numero) {
    numero = numero * 2;
    return numero;
}

var miNumero = 5;
var resultado = duplicarNumero(miNumero);

console.log(miNumero); // Imprime 5 por que es el valor original
console.log(resultado); // Imprime el valor 10 ya que es el valor duplicado



function agregarPrefijo(texto) {
    texto = "Prefijo " + texto;
    return texto;
}

var miTexto = "Palabra";
var nuevoTexto = agregarPrefijo(miTexto);

console.log(miTexto); // Imprime 'Palabra' por que es el valor original
console.log(nuevoTexto); // Imprime el valor 'Prefijo Palabra' ya que es el valor modificado


//-----POR REFERENCIA-----

function modificarObjeto(obj) {
    obj.propiedad = "Nueva propiedad";
}

var miObjeto = {propiedad: "Valor original"};
modificarObjeto(miObjeto);

console.log(miObjeto.propiedad); // Imprime 'Nueva propiedad' y es el valor nuevo ya que es por referencia



function modificarArreglo(arr) {
    arr.push(5);
}

var miArreglo = [1, 2, 3, 4];
modificarArreglo(miArreglo);

console.log(miArreglo); // Imprime todos los valores incluyendo el 5 ya que el es por referencia


/**-----DIFICULTAD EXTRA-----*/

/**-----DIFICULTAD EXTRA-----*/