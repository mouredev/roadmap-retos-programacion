// JavaScript
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Grammar_and_types

// El comentario en una única línea 

/*Este es un 
bloque de comentario, 
donde podemos escribir
varias líneas de estos
 */

//La documentación destaca el hecho de que los comentarios no pueden anidarse

/*Los comentarios funcionan de tal forma que son "ignorados" cuando se ejecuta 
el código, estan destinados sólo a ser interpretados por humanos y no formar 
parte del programa de manera funcional (solo aclarativa) */

// VARIABLES Y CONSTANTES

//var - declara una variable global, y se le puede asignar su valor también de inmediato
var egVar = 9;
//let - Declara una variable local con ámbito de bloque ({ ... }), se le epuede asignar un valor también de inmediato
let egLet = "Soy una variable let";
// const - Declara un nombre de constante de solo lectura (inmutable) y ámbito de bloque.
const egConst = 3.14159;

console.log(`Soy una variable var de valor ${egVar}, yo soy una variable let que dice '${egLet}', y yo una constante bien conocida, ${egConst}. `);

//Tipos de datos
//JS sigue el estándar de ECMAScript, que define 8 tipos de datos, 7 primitivos y un objeto

//1) Boolean 
var boolTrue = true;
var boolFalse = false;

console.log(`verdadero = ${boolTrue} y falso = ${boolFalse}`);

//2) Null 
var amNull = null;
console.log(`soy una variable null, de valor ${amNull}`);

//3) Undefined
var amUndef = undefined;
console.log(`soy una variable indefinida, de valor ${amUndef}`);

//4) Number, considera flotantes (decimales) y enteros
var num1 = 0.45;
var num2 = 24;

console.log(`Las variables num1 y num2, son números de valor ${num1} y ${num2} respectivamente`);

// 5) BigInt, que son  números gigantes para cálculos precisos (trunca decimales), debe tener la letra n al final
var bigNum1 = 9007199254740993n;
var bigNum2 = (3n / 10n);

/*nota
    las comparaciones de number con bigInt tienen diferencias
    Por ejemplo, si comparamos el valor de 2 y 2n (2 == 2n), se obtiene true por que se compara el valor y no el tipo 
    En cambio si comparamos de forma estricta (2 === 2n), es false, puesto que los tipos son diferentes (number y bigInt)
    De lo anterior se desprende que tampoco es posible realizar operaciones entre ambos (2 + 5n) puesto que son tipos diferentes
*/

console.log(`Las variables bigNum1 y bigNum2, son números de valor ${bigNum1} y ${bigNum2} respectivamente`);

//6) string
var string = "Soy una cadena de texto";
console.log(`La variable string dice ${string}`);

//7) symbol es tipo de dato único e inmutable 
const idSymbol = Symbol("id");

const persona = {
    nombre: "Juan",
    [idSymbol]: 12345 // definmos el symbol como su clave única, también notar que al invocarla en la cadena de texto, debemos hacerlo con notación [] y no con notación de punto
};

console.log(`Una variable symbol es una variable que debe ser única e inmutable, por ejemplo una Id como ${persona[idSymbol]}`);

//8) Object, es un tipo que contiene una estructura de datos, generalmente arreglados en formato de "clave-valor"
var amAnObject = {
    nombre: "Perro",
    raza: "Impostor Alemán",
    eadd: 2
}
console.log(`Este es un objeto que representa un animal. Es un ${amAnObject.nombre}, de raza ${amAnObject.raza}, de ${amAnObject.eadd} años`);


//Salida por consola del lenguaje seleccionado
const selectedLang = "JavaScript";
console.log(`¡¡¡Hola, ${selectedLang}!!!`); 



