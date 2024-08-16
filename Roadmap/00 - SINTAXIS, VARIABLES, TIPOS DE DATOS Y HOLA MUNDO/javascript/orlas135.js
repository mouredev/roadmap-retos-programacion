/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */


//Comentario de una sola línea en JavaScript

/*
  Comentarios de
  varias líneas
  en JavaScript
*/


// Sitios WEB y documentación de Javascript de interés: 

/* 
  https://developer.mozilla.org/es/docs/Web/JavaScript
  https://jonmircha.com/javascript
  https://lenguajejs.com/javascript/
*/



/*Definiendo variables*/
//Para definir una variable se hace uso de la palabra reservada let.
//Para definir una constante se hace uso de la palabra reservada const

/* 
TIPOS DE DATOS EN JS:
Primitivos: Se accede directamente al valor.

string
number
boolean
null
undefined
NaN

Compuestos: Se accede a la referencia del valor.

object = {}
array = []
function () { }
Class {}
*/


/*Definiendo el nombre de una variable*/
let nombre;

/*Inicializando el valor de una variable*/
nombre = 'Alexander';

//Definiendo e inicializando una variable es una misma línea de código:
let apellido = 'Martínez'

/*Number*/
let edad = 28;


/*Boolean*/
let es_menor = false;

/*Creando un objeto en JS*/
let persona = {
  nombre: nombre,
  apellido: apellido,
  edad: edad,
  saludo : () => {
    console.log(`Mi nombre es: ${nombre + " " + apellido}. Tengo ${edad} años`)
  }
}

/*Haciendo uso de los demás tipos primitivos en JS*/
let variable_nula = null;
let no_es_numero = NaN;
let indefinido;

/*Utilizando la función saludo del objeto persona*/
persona.saludo();

/*Imprimiendo el valor de los demás tipos primitivos de JS*/
console.log(indefinido);
console.log(variable_nula)
console.log(no_es_numero)

/*Consultado el tipo de dato de algunas variables y del objeto*/
console.log(typeof(nombre))
console.log(typeof(es_menor))
console.log(typeof(persona))