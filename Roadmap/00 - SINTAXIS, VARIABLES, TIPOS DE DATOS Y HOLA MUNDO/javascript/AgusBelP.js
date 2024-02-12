// -------------------------- ENUNCIADO

/*
 ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 - Recuerda que todas las instrucciones de participación están en el repositorio de GitHub.
 
 Lo primero... ¿Ya has elegido un lenguaje?
 - No todos son iguales, pero sus fundamentos suelen ser comunes.
 - Este primer reto te servirá para familiarizarte con la forma de participar enviando tus propias soluciones.
 
 EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 
 ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y debemos comenzar por el principio.
 */

// -------------------------- RESOLUCIÓN
// Mi lenguaje de programación es Javascript

/* No existe una página oficvial, lo más cercano es https://developer.mozilla.org/es/docs/Web/JavaScript  */

// Es posible hacer comentarios en una sola línea utilizando dos barras

/* Los comentarios multilinea se generan con la ayuda de una barra y un asterisco */

// ---------- Creación de variables

var variable = 'Backend'; // Las variables declaradas con var son procesadas antes de la ejecución del código.El scope de una variable declarada con var, es su contexto de ejecución.

const variable2 = 'Frontend'; // Const es un tipo de variable a la cual no es posible re asignar su valor una vez declarada

// ---------- Tipos de datos
//En Javascript existen 7 tipos de datos. En los siguientes ejemplos el nombre de la variable es el nombre del tipo de dato

let undefined_example = undefined; // representa una variable que no ha sido declarada o a la cual no se le ha asignado un valor.

let boolean = true; //representa un valor lógico y puede tener dos valores, ya sean true o false.

let number = 1; //permite representar y manipular valores numéricos

let string = 'Soy una cadena de texto'; // representa cadenas de caracteres

let bigInt = 1234567890123456789012345678901234567890n; //representa valores numéricos que son demasiado grandes para ser representados por el tipo de dato number.

let symbol = Symbol(); //El tipo symbol (símbolo) se utiliza para crear identificadores únicos para los objetos.

let variable_null = null; //representa la ausencia intencional de cualquier valor, un valor nulo o «vacío»

// ---------- Impresión por consola
console.log('Hola Javascript!!!');
