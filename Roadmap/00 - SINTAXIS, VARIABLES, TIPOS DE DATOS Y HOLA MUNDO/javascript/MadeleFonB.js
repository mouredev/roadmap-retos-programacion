//https://www.javascript.com/

/*
Esto es un comentario de varias lineas
Esto es un comentario de varias lineas
Esto es un comentario de varias lineas
*/


//Variables y constante
var edad = 25;
const año = 2024;


//Datos primitivos
/*Number:El tipo de dato Number representa tanto números enteros como decimales
También puede representar números en notación científica, Infinity (infinito) y NaN (Not a Number).
*/
var edad = 16;
var peso = 60.3;
var infinito = Infinity
var NoEsNumero = NaN

/*
STRING: El tipo de dato String representa cadenas de texto, que pueden ser escritas utilizando comillas simples, dobles o acentos graves (backticks).
Los acentos graves permiten crear plantillas literales (template literals) que incluyen interpolación de variables y expresiones.
*/
var entero=0;
var comillasimple = 'Hola mundo';
var comillaDoble = "Hola mundo";
var plantillaLiteral = `Minumero favorito es ${entero}`;
var caracteresEscape = 'Texto con \"comillas\" y salto de linea  \n';

/*
BOOLEAN:El tipo de dato Boolean representa valores lógicos, que pueden ser verdadero (true) o falso (false). 
Estos valores son comúnmente utilizados en operaciones lógicas y de comparación.
*/

var falso = false;
var verdadero = true;
var mayorDeEdad = (5 >= 18)

/*
NULL:El tipo de dato Null representa un valor nulo o vacío. Se utiliza para indicar que una variable no tiene ningún valor asignado.
*/

var valorNulo = null;

/*
UNDEFINED:El tipo de dato Undefined indica que una variable no ha sido asignada a ningún valor. 
Este es el valor por defecto de las variables que no han sido inicializadas.
 */

var valorIndefinido;

/*
BIGINT:Es útil para representar números muy grandes que no caben en un tipo de dato “Number” y es compatible con la mayoría de las operaciones aritméticas básicas.
Sin embargo, aún no es compatible con algunas funciones como Math.floor o parseInt, por lo que es importante tener en cuenta sus limitaciones.
Se agregó en la versión ECMAScript 2020 y se puede crear añadiendo “n” al final de un número.
 */

var bigIntValue = 1234567891011n;

/*
SYMBOL:El tipo de dato Symbol representa valores únicos e inmutables que pueden ser utilizados como identificadores de propiedades en objetos.
Los símbolos se crean utilizando la función Symbol(), que opcionalmente puede recibir un argumento de tipo String para describir el símbolo.
 */

var simbolo1;
var simbolo2= Symbol('dos');
var simbolo3 = Symbol('tres')
//Imprimir por consola lenguaje seleccionado
console.log('¡Hola,[JavaScript]')
