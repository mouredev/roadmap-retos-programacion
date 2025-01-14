//1- Crea un comentario en el código y coloca la URL del sitio web oficial dellenguaje de programación que has seleccionado:
//URL de la web oficial de java script: https://developer.mozilla.org/es/docs/Web/JavaScript


//2- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...): 
//En una linea = //
/*
Esta es la forma de escribir
en varias lineas.
*/


//3- Crea una variable (y una constante si el lenguaje lo soporta):
var nombre1 = 'Luiggi';
let apellido = 'Reyes';
const pais = 'Republica Dominicana';


//4- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...):

/*String (Cadena de textos): se refiere a una cadena de texto, es decir, una secuencia de caracteres que puede estar encerrada 
entre comillas simples ('), dobles (") o backticks (`).*/
let nombre  = 'Luiggi';
let lenguaje = 'javascript';
let saludo = 'hola';

/*Number (Numero): los números son de tipo number y pueden ser enteros o decimales.*/
let edad = '21';
let precio = '99.99';

/*Boolean (booleano): es un valor que puede ser true (verdadero) o false (falso), estos no se ponen en comillas.*/
let estaAprendiendoAPrograma = true;
let MiEdadEs21 = false;

/*Null: es un valor intencionalmente vacio o desconocido.*/
let moto = null;

/*Undefined: indica que una variable ha sido delcarada pero no tiene un valor asiganado.*/
let valorIndefinido;

/*Symbol: es un valor unico e inmutable que sirve como identificador.*/
let id = Symbol();
//Tambien a este tipo de dato se le puede asignar una descripcion como referencia para depuracion:
let idDescrpcion = symbol('este id es unico');

/*BigInt: se utiliza para representar numeros enteros grandes, que no pueden ser representados con el
tipo Number.*/
let numeroGrande = BigInt(97374320283746383627);


//5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/
console.log('¡Hola, [JavaScript]!');