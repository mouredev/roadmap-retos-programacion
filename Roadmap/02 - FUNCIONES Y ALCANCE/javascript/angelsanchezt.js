/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/*
Funciones definidas por el usuario
*/

// Simple
function greet() {
    console.log("Hola, JavaScript!");
}

greet();

// Con retorno
function returnGreet() {
    return "Hola, JavaScript!";
}

console.log(returnGreet());

// Con un argumento
function argGreet(name) {
    console.log(`Hola, ${name}!`);
}

argGreet("Angel");

// Con argumentos
function argsGreet(saludo, nombre) {
    console.log(`${saludo}, ${nombre}! `);
}

argsGreet("Hi", "Angel");


// Con un argumento predeterminado
function defaultArgGreet(name = "JavaScript") {
    console.log(`Hola, ${name}!`);
}

defaultArgGreet("Angel");
defaultArgGreet();

// Con argumentos y return
function returnArgsGreet(greet, name) {
    return `${greet}, ${name}!`;
}

console.log(returnArgsGreet("Hi", "Angel"));

// Con retorno de varios valores
function multipleReturnGreet() {
    return ["Hola", "JavaScript"];
}

let [greetWord, language] = multipleReturnGreet();
console.log(greetWord);
console.log(language);

// Con un número variable de argumentos
function variableArgGreet(...names) {
    for (let name of names) {
        console.log(`Hola, ${name}!`);
    }
}

variableArgGreet("JavaScript", "Angel", "Sanchez", "comunidad");

// Con un número variable de argumentos con palabra clave
function variableKeyArgGreet(names) {
    for (let [key, value] of Object.entries(names)) {
        console.log(`${value} (${key})!`);
    }
}

variableKeyArgGreet({
    language: "JavaScript",
    name: "Angel",
    alias: "angelsanchezt",
    age: 36
});

/*
Funciones dentro de funciones
*/

function outerFunction() {
    function innerFunction() {
        console.log("Función interna: Hola, JavaScript !");
    }
    innerFunction();
}

outerFunction();

/*
Funciones del lenguaje (built-in)
*/

console.log("Angel".length);
console.log(typeof 36);
console.log("Angel".toUpperCase());

/*
Variables locales y globales
*/

let globalVar = "JavaScript";

function helloJavaScript() {
    let localVar = "Hola";
    console.log(`${localVar}, ${globalVar}!`);
}

console.log(globalVar);
// console.log(localVar); // No se puede acceder desde fuera de la función

helloJavaScript();

/*
Extra
*/

function printNumbers(text1, text2) {
    let count = 0;
    for (let number = 1; number <= 100; number++) {
        if (number % 3 === 0 && number % 5 === 0) {
            console.log(text1 + text2);
        } else if (number % 3 === 0) {
            console.log(text1);
        } else if (number % 5 === 0) {
            console.log(text2);
        } else {
            console.log(number);
            count++;
        }
    }
    return count;
}

console.log(printNumbers("Fizz", "Buzz"));
