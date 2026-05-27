// EJERCICIO:
//  * - Crea ejemplos de funciones básicas que representen las diferentes
//  *   posibilidades del lenguaje:
//  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
//  * - Comprueba si puedes crear funciones dentro de funciones.
//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
//  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
//  * - Debes hacer print por consola del resultado de todos los ejemplos.
//  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

// Declaracion de funciones tradicional

function sayHi(nombre) {
    return `Hola, ${nombre}!`;
}
console.log(sayHi("Juank"));

function temon(musica)  {
    return `Este es un temota: ${musica}`;
}
console.log(temon("Runner"))

//Expresion de Funcion anonima

const sumar = function(a, b) {
    return a + b;
}
console.log(sumar(12, 8));

const restar = function(z, c) {
    return z - c;
}
console.log(restar(12, 8))

//Arrow Function(Funciones Flecha)

const multiplicar = (a, b) => a * b;
console.log(multiplicar(12, 8));

const dividir = (c, d) => c / d;
console.log(dividir(12, 8)); 

//Funcion con Parametros Predeterminados

function configurarUsuario (usuario = "Invitado") {
    return `Bienvenido, ${usuario}!`;
}
console.log(configurarUsuario());

function esMusico (user = "Musico") {
    return `Hola, resulta que eres ${user}, eso es verdad?`;
}
console.log(esMusico());

//Funcion de orden superior(CallBack)

function procesarOperacion(a, b, operacion) {
    return operacion(a, b);
}
const resultado = procesarOperacion(10, 5, (x, y) => x - y);
console.log(resultado)


function operacionDefinida(c, d, definida) {
    return definida(c, d);
}

const residuo = operacionDefinida(100, 150, (c, d) => c * d);
console.log(residuo)


//IIFE (Immediately Invoked Function Expression)
console.log(typeof console.log);

(function() {
  console.log("Esta función se ejecuta sola");
})();
