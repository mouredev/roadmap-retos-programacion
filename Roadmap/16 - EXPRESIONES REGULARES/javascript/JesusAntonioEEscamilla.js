/** #16 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Las expresiones regulares son patrones que se utilizan para hacer coincidir combinaciones de caracteres en cadenas.
 * En JavaScript, las expresiones regulares también son objetos.
 * Una expresión regular es una secuencia de caracteres que forma una buscar patrón.
*/

//---EJERCIÓ---

// Expresión con Función Objeto
let re = new RegExp("Jesus Antonio");

// Expresión Literal
let regex = /\d+/g;

// El textos en particulares.
const texto1 = "Yo nací en 1999 y tengo 24 años de edad.";
const yo = "Jesus Antonio Escamilla - de la tierra 616, del universo 999"

// Se llama la función y se usa uno de los métodos de excreciones regulares que muestre los números.
function texto_Num(texto) {
    const númerosEncontrados = texto.match(regex);
    return númerosEncontrados.map(num => parseInt(num));
}
console.log(`El texto, "${texto1}" contiene los siguientes números:`,texto_Num(texto1));

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

//  Excreción para Email
const regex_Email = /^[\w.%+-]+@[\w.-]+\.[a-zA-Z]+$/;   //Aquí es la expresión regular propia
// Los ejemplos de correos electrónicos
const emailJesus = 'JesusA@outlook.com';
const emailEmpresa = '@trnetwork.com.mx'
//  Imprimiendo en la consola
console.log(`Es valido el correo "${emailJesus}":`, regex_Email.test(emailJesus));
console.log(`Es valido el correo "${emailEmpresa}"`, regex_Email.test(emailEmpresa));


//  Expresión para Teléfono
const regex_Teléfono = /^\+([\d]{2})-([\d]{3})-([\d]{3})-([\d]{4})/;    //Aquí es la expresión regular propia
// Los ejemplos de los teléfonos
const teléfonoA = '+52-953-123-4567';
const teléfonoB = '+1 123 456 7890';
//  Imprimiendo en la consola
console.log(`Es valido el teléfono "${teléfonoA}":`, regex_Teléfono.test(teléfonoA));
console.log(`Es valido el teléfono "${teléfonoB}"`, regex_Teléfono.test(teléfonoB));


//  Expresión para URL
const regex_URL = /^(http[s]?:\/\/)?([\d\w]*\.)?[\w]*\.([\w]{3})(\.[\w]{2,3})?\/?$/;  //Aquí es la expresión regular propia
// Los ejemplos de URL
const google_Url = 'www.google.com';
const moure_Url = 'https://www.moure.dev';
const aventure_Url = 'jajatoonstime.blogspot'
//  Impresiones en la consola
console.log(`Es valido la URL "${google_Url}":`, regex_URL.test(google_Url));
console.log(`Es valido la URL "${moure_Url}":`, regex_URL.test(moure_Url));
console.log(`Es valido la URL "${aventure_Url}":`, regex_URL.test(aventure_Url));


/**-----DIFICULTAD EXTRA-----*/