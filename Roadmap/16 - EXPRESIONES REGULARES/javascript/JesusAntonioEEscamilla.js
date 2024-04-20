/**
 * Las expresiones regulares son patrones que se utilizan para hacer coincidir combinaciones de caracteres en cadenas.
 * En JavaScript, las expresiones regulares también son objetos.
 * Una expresión regular es una secuencia de caracteres que forma una buscar patrón.
*/

//---EJERCIÓ---

// Expresión con Función Objeto
let re = new RegExp("Jesus Antonio");

// Expresión Literal
let regex = /\d/;

// El textos en particulares.
const texto1 = "Yo nací en 1999 y tengo 24 años de edad.";
const yo = "Jesus Antonio Escamilla - de la tierra 616, del universo 999"

// Se llama en consola y se usa uno de los métodos de excreciones regulares el text(string).
console.log(`El texto, "${texto1}" contiene números:`, regex.test(texto1));


//---Alguno Método de Expresiones Regulares---
// exec(string)
let exec = re.exec(yo);
console.log(`Si se encontró`,exec);

//---Otr ejemplos de expresiones regulares---
// Uso de caracteres especiales
let reg = /e/g;
// Pero existen mas como: /CHAR+/ (Mas a en el texto), /\d+/ (Mas dígitos), /\w+/ (Mas letras), /\s+/ (Mas espacios)
const abecedario = ['a', 'b', 'c', 'd', 'e', 'f'];
console.log('Si se encontró las letras:', reg.exec(abecedario));

// Búsqueda de caracteres específicos
let reg_especifico = /[abc]/;
console.log('Se lo logro encontrar abc:', reg_especifico.test(abecedario));




/**-----DIFICULTAD EXTRA-----*/
//Pendientes
/**-----DIFICULTAD EXTRA-----*/