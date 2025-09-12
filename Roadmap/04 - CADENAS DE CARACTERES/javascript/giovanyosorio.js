/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

//Operaciones Cadenas



// charAt()
// devuelve en un nuevo String el carácter UTF-16 de una cadena.
var cualquierCadena = "Brave new world";

console.log(
  "El carácter en el índice 0 es '" + cualquierCadena.charAt(0) + "'",
);
//El carácter en el índice 0 es 'B'


//concat()
// combina dos o más cadenas de texto y devuelve una cadena de texto nueva.
const str1 = 'Hello';
const str2 = 'World';

console.log(str1.concat(' ', str2));
// Expected output: "Hello World"


//indexOf()
// devuelve el índice, dentro del objeto String que realiza la llamada
"Blue Whale".indexOf("Blue"); // returns 0
"Blue Whale".indexOf("Blute"); // returns -1


//match()
//devuelve todas las ocurrencias de una expresión regular dentro de una cadena.
const paragraph = 'The quick brown fox jumps over the lazy dog. It barked.';
const regex = /[A-Z]/g;
const found = paragraph.match(regex);

console.log(found);
// Expected output: Array ["T", "I"]

//padStart()
//rellena la cadena actual con una cadena dada (repetida eventualmente) de modo que la cadena resultante alcance una longitud dada.
"abc".padStart(10); // "       abc"
"abc".padStart(10, "foo"); // "foofoofabc"
"abc".padStart(6, "123465"); // "123abc"


//repeat()
//construye y devuelve una nueva cadena que contiene el número especificado de copias de la cadena en la cual fue llamada, concatenados.
"abc".repeat(1); // 'abc'
"abc".repeat(2); // 'abcabc'
"abc".repeat(3.5); // 'abcabcabc' (count will be converted to integer)
"abc".repeat(1 / 0); // RangeError


//replace()
//devuelve una nueva cadena con una, algunas, o todas las coincidencias de un patrón
const paragraph2 = "I think Ruth's dog is cuter than your dog!";

console.log(paragraph2.replace("Ruth's", 'my'));
// Expected output: "I think my dog is cuter than your dog!"

//search()
// ejecuta una búsqueda que encaje entre una expresión regular y el objeto String desde el que se llama.
function testinput(re, str) {
    var midstring;
    if (str.search(re) != -1) {
      midstring = " contains ";
    } else {
      midstring = " does not contain ";
    }
    console.log(str + midstring + re);
  }
  

//slice()
//El método slice() extrae una sección de una cadena y devuelve una cadena nueva.
var cadena1 = "La mañana se nos echa encima.";
var cadena2 = cadena1.slice(3, -2);
console.log(cadena2);
// mañana se nos echa encim

//split()
//divide un objeto de tipo String en un array (vector) de cadenas mediante la separación de la cadena en subcadenas.
var miCadena = "Hola Mundo. Cómo estás hoy?";
var divisiones=miCadena.split(" ")
console.log(divisiones)
//[ 'Hola', 'Mundo.', 'Cómo', 'estás', 'hoy?' ]

// to string()
// El toString() método devuelve una cadena que representa al objeto especificado.
cadena = new String("Hello world");
alert(cadena.toString()); // Displays "Hello world"


//toLowerCase()
//devuelve el valor en minúsculas de la cadena que realiza la llamada.
var textoMayusculas = "ALFABETO";
document.write(textoMayusculas.toLowerCase());

//toUpperCase()
//método devuelve el valor convertido en mayúsculas de la cadena que realiza la llamada.
console.log("alphabet".toUpperCase()); // "ALPHABET"

// valueOf()
//The valueOf() método devuelve el valor primitivo de un objeto String.
cadena = new String("Hello world");
alert(cadena.valueOf()); // Displays "Hello world"

//trim()
//El método trim( ) elimina los espacios en blanco en ambos extremos del string

var orig = "   foo  ";
console.log(orig.trim()); // 'foo'


// palindromos

function isPalindrome(texto){
    return texto== texto.split('').reverse().join('')
  }
  isPalindrome("reconocer")

  //Anagramas
  function isAnagrama(palabra, posibleAnagrama){
    return palabra.toLowerCase().split("").sort().join("") === posibleAnagrama.toLowerCase().split("").sort().join("");
  }
  isAnagrama("roma","amor")

  //Isogramas
  function isIsograma(palabra){
    palabra = palabra.toLowerCase().replace(/A-Z/gi);
      const letras = new Set(palabra);
    return letras.size === palabra.length;


}
isIsograma("murcielago")