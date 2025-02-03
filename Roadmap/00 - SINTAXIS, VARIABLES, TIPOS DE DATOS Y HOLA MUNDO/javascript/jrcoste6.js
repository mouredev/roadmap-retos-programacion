//Ejercicio #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO;

//Sitio Web Oficial de JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript;

//Formas de crear comentarios en JavaScript;

    //#1 Usando el caracter "Slash" de forma duplicada y seguida al inicio de la línea de código, solamente para una efectuar una línea de comentario.

    /*#2 Usando el caracter "Slash" y "Asterisk" lo cual permite plasmar el comentario en forma de varias
    *lineas como está viendose en este ejemplo*/;

    /*#3 Bonus: Según la documentación oficial de JavaScript, hay una tercera forma de declarar un 
    *comentario, el cual es el comentario Hashbang, y se usa para especificar la ruta de un motor de
    *JavaScript en particular.*/;

/* VARIABLES Y FORMAS DE DECLARARLAS EN JAVASCRIPT

    Con la palabra reservada VAR
    Con la palabra reservada LET
    Con la palabra reservada CONST
*/

var letras = "ABC";
let numeros = "1,2,3";
const PI = 3.14;

/* TIPOS DE DATOS

    1- Booleano. true y false.
    2- null. Una palabra clave especial que denota un valor nulo. (Dado que JavaScript distingue entre mayúsculas y minúsculas, null no es lo mismo que Null, NULL o cualquier otra variante).
    3- undefined. Una propiedad de alto nivel cuyo valor no está definido.
    4- Number. Un número entero o un número con coma flotante. Por ejemplo: 42 o 3.14159.
    5- BigInt. Un número entero con precisión arbitraria. Por ejemplo: 9007199254740992n.
    6- String. Una secuencia de caracteres que representan un valor de texto. Por ejemplo: "Hola"
    7- Symbol (nuevo en ECMAScript 2015). Un tipo de dato cuyas instancias son únicas e inmutables
    8- Object.*/

let myboolean = true;
let mynull = null;
let myUndefined = undefined;
let myNumber = 1234;
let myBigInt = 3835853489573827548873461733924n;
let myString = "Hola";
let mySymbol =  Symbol();
let myObject = {
    name: "Junior",
    edad: 36,
    sexo: "Masculino"

}

console.log("¡Hola, JavaScript!");