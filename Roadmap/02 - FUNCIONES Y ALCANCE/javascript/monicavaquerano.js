// 02 FUNCIONES Y ALCANCE
// Monica Vaquerano
//  https://monicavaquerano.dev

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

//  * - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:

// Funciones Autoinvocadas (Immediately Invoked Function Expressions - IIFE):
/* Son funciones que se ejecutan inmediatamente después de ser definidas.
* Son útiles para encapsular el código y evitar la contaminación del ámbito global.
*/

(function () {
    console.log('Esta función se ejecuta inmediatamente.');
})();

// Funciones Declarativas (Declarative Functions):
/* Estas son las funciones más comunes y tradicionales en JavaScript, donde defines una función utilizando la palabra clave function. 
 * Puedes declararlas en cualquier lugar en el código, y JavaScript las "eleva" al inicio del contexto de ejecución, 
 * por lo que puedes llamar a la función antes de que aparezca en el código. 
 */

function square(number) {
    return number * number;
}
console.log(square(3))

// Expresiones de Funciones (Function Expressions):
/* Estas son funciones que se asignan a variables como valores. Puedes definir funciones en línea y asignarlas a variables. 
 * Son útiles cuando necesitas funciones como argumentos para otras funciones o cuando deseas encapsular una función dentro de un contexto. 
 */

const multiply = function (a, b) {
    return a * b;
};

console.log(multiply(2, 2))

// Funciones Flecha (Arrow Functions):
/* Las funciones flecha son una forma más concisa de escribir funciones en JavaScript.
 * Tienen una sintaxis más corta y no cambian el contexto de this dentro de la función.
 * Son útiles para funciones simples y en contextos donde necesitas preservar el valor de this.
 */

const greet = (name) => {
    return `Hello, ${name}!`;
};

console.log(greet("Monica"))

// Métodos de Objeto (Object Methods):
/* Son funciones que se definen como propiedades de un objeto.
 * Estos métodos son funciones que se pueden invocar en el contexto de ese objeto utilizando la notación de punto.
 */
const user = {
    name: 'John',
    greet: function () {
        return `Hello, ${this.name}!`;
    }
};

console.log(user.greet())

// Funciones Constructoras (Constructor Functions):
/* Estas son funciones que se utilizan para crear nuevos objetos mediante el uso del operador new.
 * Son útiles cuando necesitas crear múltiples instancias de un tipo de objeto.
 */
function Person(name, age) {
    this.name = name;
    this.age = age;
}

const person1 = new Person('Alice', 30);
const person2 = new Person('Bob', 25);

console.log(person1, person2)

// Callback:
/* A callback is a function passed as an argument to another function. 
 * This technique allows a function to call another function.
 * A callback function can run after another function has finished
 */
var funcionB = () => {
    return console.log('Funcion B ejecutada');
};
var funcionA = (a, b, callback) => {
    console.log("Funcion A:", a + b)
    callback();
};

funcionA(1, 2, funcionB);


// # Sin parámetros ni retorno
function cuentaRegresiva() {
    for (let i = 10; i >= 0; i--) {
        if (i == 0) { console.log("BOOM!"); }
        else { console.log(i); }
    }
}

cuentaRegresiva();

// # Con parámetro, no retorno
var greeting = (name) => {
    console.log("Hello, " + name + "!");
}

greeting("Charlie");

// # Con uno o más parámetros y con retorno
var suma = (a, b) => {
    return a + b;
}

console.log(suma(5, 6));


// # Una lista como argumento
function sortList(arr, reverse = false) {
    arr.sort();
    if (reverse) { arr.reverse(); }
    return arr;
}

console.log(sortList([3, 0, 1, 2]));
console.log(sortList([3, 0, 1, 2], true));


// Function Rest Parameter
// The rest parameter (...) allows a function to treat an indefinite number of arguments as an array:
function sum(...args) {
    let sum = 0;
    for (let arg of args) sum += arg;
    return sum;
}

let x = sum(4, 9, 16, 25, 29, 100, 66, 77);
console.log(x);


// # Parámetros con keywords
function vocales(vocal1, vocal2, vocal3, vocal4, vocal5) {
    console.log(`Las vocales cerradas son ${vocal4} y ${vocal5}, las abiertas son ${vocal3}, ${vocal2} & ${vocal1}.`)
}

vocales(vocal2 = "e", vocal1 = "a", vocal3 = "i", vocal5 = "u", vocal4 = "o");

// # Recursion
function recurrente(num) {
    let result;
    if (num > 0) {
        result = num + recurrente(num - 1);
        console.log(result);
    } else {
        result = 0;
    }
    return result;
}

recurrente(3);


// """
// * - Comprueba si puedes crear funciones dentro de funciones.
// """

function funcionPrincipal(string) {
    function funcionSecundaria(string) {
        let newStr = "";
        for (let i = 0; i < string.length; i++) {
            if (i % 2 == 0) {
                newStr += string[i];
            } else {
                newStr += string[i].toUpperCase();
            }
        }
        return newStr;
    }
    return funcionSecundaria(string);
}
console.log(funcionPrincipal("hola"));


// """
//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
// """

console.log("\nAlgunas funciones ya creadas en JavaScript (Built-in Functions):");

var lista = [5, 7, 4, 6, 1];

// Len
console.log(`len(): la longitud de {lista} es de: ${lista.length}`);
// concat
var alpha = ["a", "b", "c"];
var numeric = [1, 2, 3];
var alphaNumeric = alpha.concat(numeric);
console.log("concat(): ", alphaNumeric);

// # Abs
console.log(`Math.abs(x): el absoluto de - 20 es: ${Math.abs(-20)}`);
// # Max
console.log(`Math.max(x): el máximo en {...lista} es: ${Math.max(...lista)}`);
// # Min
console.log(`Math.min(x): el mínimo en {...lista} es: ${Math.min(...lista)}`);
// # Pow
console.log(`Math.pow(x, y): 7 elevado al cuadrado {Math.pow(7, 2)} es: ${Math.pow(7, 2)}`);
// # Print
console.log(`console.log(x): imprime los resultados en la consola. {True}, {None}, {lista}, etc.`);
// # Sorted
console.log(`sort(): lista.sort(): ${lista.sort()}`);
// # Reversed
console.log(`reverse(): lista.reverse(): ${lista.reverse()}`);
// # toString
console.log(`toString(): lista.toString(): ${lista.toString()}`);

// """
// * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
// """

console.log("\nVariable local y global:");

// Variable Global
let nombre = "Juan";

function devolverNombre() {
    // Variable Local
    let nombre = "Carlos"
    return nombre;

}
console.log(`Yo regreso la variable global (nombre = ${nombre})\nYo regreso la variable local dentro de la funcion (nombre = ${devolverNombre()}).`);


// """
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
//  *
//  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
//  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
// """

function miFuncion(str1, str2) {
    let counter = 0;
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(str1 + " " + str2);
        } else if (i % 5 == 0) {
            console.log(str2);
        } else if (i % 3 == 0) {
            console.log(str1);
        } else {
            console.log(i);
            counter++;
        }
    }
    return counter;
}

console.log("\nDIFICULTAD EXTRA (opcional):")
x = miFuncion("hakuna", "matata")
console.log(`\nNúmero de veces que se ha impreso el número en lugar de los textos:\n> ${x}`)
