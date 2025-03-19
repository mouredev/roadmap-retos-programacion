/* 
EJERCICIO 2
- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
    Sin parametros ni retorno, con uno o varios parámetros, con retorno..
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA:
- Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

*/

const myName = "Ozkar";
const age = 25;

// funcion sin parámetros
function helloWorld() {
    console.log("Hola Mundo");
}

helloWorld();

// funcion con un parámetro
function showName(name) {
    console.log("Hola " + name);
}

showName(myName);

// funcion con varios parámetros
function showNameAndAge(name, age) {
    console.log("Hola " + name + " Tu edad es: " + age);
}

showNameAndAge(myName, age);

// funcion con retorno
function withReturn(name) {
    return `Hola ${name}`;
}

withReturn();

// funcion dentro de otra función
function externalFunction() {
    console.log("Esta es la función externa");

    function innerFunction() {
        console.log("Esta es la función interna");
    }
}

externalFunction();

// Ejemplo de función ya creada en el lenguaje: Math.round()
function redondear(numero) {
    return Math.round(numero);
}

console.log("Funcion redondear:", redondear(3.14159)); // Funcion redondear: 3

const msg = "Hola Mundo";
const msg2 = "Mi nombre es Ozkar";

// funcion ya creada en el lenguaje
function showMessage(msg, msg2) {
    console.log(msg.toUpperCase() + " " + msg2.toUpperCase()); // Utiliza una función de JavaScript para convertir el texto a mayúsculas
}

showMessage(msg, msg2);

// Funciones anónimas o lambdas (funciones sin nombre)
const funcionAnonima = function(a, b) {
    console.log(`Soy una función anónima con parámetros ${a} y ${b}`);
}

console.log(funcionAnonima); // Se obtiene la función anónima
funcionAnonima(1, 2); // Se ejecuta la función anónima

// Es posible establecer valores por defecto para los argumentos:
function funcionValorPorDefecto(a, b = 'valor por defecto') {
    console.log(`Me llamo ${a} y mi valor es: ${b}`);
}
funcionValorPorDefecto('Miguel');

// funcion flecha (arrow function)
var arrowFunction = () => {
    console.log('Soy una función flecha');
}

// Variable global
const globalVariable = "Soy una variable global";

function funcExternal() {
  // Variable local
  const localVariable = "Soy una variable local";
  console.log("Desde la función externa:", globalVariable); // Acceso a la variable global
  console.log("Desde la función externa:", localVariable); // Acceso a la variable local
}

// Intentamos acceder a las variables fuera de su alcance
console.log("Fuera de la función:", globalVariable); // Acceso a la variable global
//console.log("Fuera de la función:", localVariable); // Esto producirá un error, ya que localVariable está definida solo dentro de la función

// Llamamos a la función
funcExternal();

// EJERCICIO EXTRA

const cadena1 = "Multiplo de 3";
const cadena2 = "Multiplo de 5";
let countNumbers = 0;

function calculateMultiples(cadena1, cadena2) {
    for (var i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(cadena1 + " y " + cadena2);
        }
        else if (i % 3 === 0) {
            console.log(cadena1);
        }
        else if (i % 5 === 0) {
            console.log(cadena2);
        }
        else {
            console.log(i);
            countNumbers += 1;
        }
    }
}

calculateMultiples(cadena1, cadena2);
console.log("Número de veces que se imprimio un numero: ", countNumbers);