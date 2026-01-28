//http://ecmascript.org/.


/* Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...) */

// Comentario en 1 linea 

/* Comentario 
para bloques 
más extensos */

// Crea una variable (y una constante si el lenguaje lo soporta).

var variable = "alcance global si esta afuera de una funcion";

let variable = "tiene alcance de bloque ({})";

const constante = 'su valor no puede ser reasignado después de la inicialización';


/*Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...)*/

let string = "Cadena de texto";

let number = 2305;

let undefined = "Valor de una variable que ha sido declarada pero no se le ha asignado un valor";

let symbol = "Un identificador único e inmutable, útil para claves de objetos";

let null = "Representa la ausencia intencional de un valor, aunque su tipo en typeof es 'object' debido a un error histórico";

let boolean = "Representa valores lógicos: true o false";

let BigInt = "Para números enteros que superan el límite seguro del tipo Number, se añade una n al final, como 9007199254740991n"


// Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

console.log("¡Hola, JavaScript");