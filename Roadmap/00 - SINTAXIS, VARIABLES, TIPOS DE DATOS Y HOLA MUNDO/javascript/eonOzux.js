/* * EJERCICIO:
* 1 Crea un comentario en el código y coloca la URL del sitio web oficial del
*   lenguaje de programación que has seleccionado.
* 2 Representa las diferentes sintaxis que existen de crear comentarios
*   en el lenguaje (en una línea, varias...).
* 3 Crea una variable (y una constante si el lenguaje lo soporta).
* 4 Crea variables representando todos los tipos de datos primitivos
*   del lenguaje (cadenas de texto, enteros, booleanos...).
* 5 Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */

/* 1- Primer comentario en Javascrip en bloque 
URL de Javascript: https://www.javascript.com/ */

//2- Tipos de comentario de linea// 

/* Comentario 
de 
bloques */

/* 3- Variables y Constantes */
var primerVariable = "Javascript";
let segundaVariable = "";  
// Las variables son valores que pueden ser actualizados con nuevos valores en el codigo.

const primerContante = "";
 // Las Constantes son valores que a diferencia de las variables, 
//se les asignan valores pero estos son estaticos a lo largo del codigo si se invocan 
//no pueden almacenar nuevos valores. 

/* 4- Tipos de Datos */

/* 
1. String
2. Number
3. Bigint
4. Boolean
5. Undefined
6. Null
7. Symbol
8. Object 
*/

var datos_texto = "Mi nombre es Yohan Arce"; // Tipo String.

let dato_Num = 2024 // Tipo Number o Bigint.

let valor = true && false;  // Tipo Booleano.

const a = "";// El resultado de la constante "a" es Undefined la estamos definiendo pero no tiene ningun valor.

let b = null; // El valor de Nulo puede ser asignado a una variable. Se usa para comprobaciones

const sym1 = Symbol(); // Por medio del metodo Symbol se pueden crear o insertar algun simbolo
const sym2 = Symbol("foo"); 
const sym = new Symbol(); // Este codigo arroja el error -> TypeError

const person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}; // Creacion de objetos
// El objeto es una constante al que se le pueden asignar valores y atributos.

/* 5- Imprimir en la consola el lenguaje */
console.log("Hola soy" + primerVariable + datos_texto);