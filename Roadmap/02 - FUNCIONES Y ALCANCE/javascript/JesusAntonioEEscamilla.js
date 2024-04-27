/** #02 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Dentro de las Funciones Básicas de JavaScript se utilizan:
 * Declarativas
 * Expresión
 * Función Flecha
 * Auto-ejecutable
 * Constructiva
 */

//-----DECLARATIVAS-----
//  Aquí se declara la función y después se llama para poder usarla.
function saludar(nombre) {
    console.log(`Hola , ${nombre}!!!!`);
}
saludar("Jesus Antonio"); //La función funciona cuando se le envía un nombre y lo imprime


//-----EXPRESIÓN-----
//  Estas funciones no llevan nombre ya que va declara de una variable o buen de un objeto
//  también se llama función anónima y de igual forma puede llevar nombre la función para
//  hacerse referencia asi misma pero son casos especiales
var sumar = function(a, b) {
    return a + b;
}
var resultado = sumar(5, 10);
console.log(resultado); //La función arroga la respuesta.  15


//-----FUNCIÓN FLECHA-----
// Esta función funciona cuando un variable se declara con la función que va a
// realizar y después de puede llamar para poder utilizarla y hacer cualquier ejecución
var a = ["Hidrógeno", "Helio", "Litio", "Berilio"];

var a2 = a.map((s) => s.length);

console.log(a2); // logs [9, 5, 5, 7]



/**
 * Se puede realizar funciones dentro de funciones 
 * siempre y cuando se cumpla si paramentos o bien se cumplan las acciones
 */
//  Vemos que la función tiene que hacer una resta,
//  pero dentro la función tiene realizar un incremento 
//  de las variables y después puede realizar la resta
function resta(a, b) {
    function incrementar(x) {
        return x + 1;
    }
    // Llamada a la función interna
    return incrementar(a) - incrementar(b);
}  
console.log(resta(17, 6)); // Devuelve 11



/**
 * FILTER()
 * Un método de arrays para javascript en la cual hacer filtrado del mismo objeto
 */
const numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Filtrar los números pares
const numeroPares = numero.filter(function(numero) {
    return numero % 2 === 0;
});

console.log(numeroPares); // Imprime [2, 4, 6, 8, 10]



/**
 * VARIABLE GLOBAL Y VARIABLE LOCAL
 * Existen los grandes variables la global y variable la local
 */


//-----VARIABLE GLOBAL-----
var contador = 2; // Variable global
function incrementarContador() {
    contador++;
}
console.log(contador); // Imprime 2


//-----VARIABLE LOCAL-----
function saludar() {
    var mensaje = "Hola, mundo!"; // Variable local
    console.log(mensaje);
}
saludar(); // Imprime "Hola, mundo!"
console.log(mensaje); // Error: mensaje is not defined



/**-----DIFICULTAD EXTRA-----*/
function extra(param1 , param2) {
    let cont = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0) {
            console.log(param1);
        }else if(i % 5 == 0) {
            console.log(param2);
        }else if(i % 3 == 0 && i % 5 == 0){
            console.log(param1 + param2);
        } else{
            cont ++;
            console.log(i);
        }
    }
    return cont
}
console.log(extra("FIZZ","BUZZ"));
/**-----DIFICULTAD EXTRA-----*/
