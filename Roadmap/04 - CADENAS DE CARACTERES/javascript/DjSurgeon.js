/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

// Operaciones con cadenas
let string = "Hola mundo!";

// Encontrar la longitud de una cadena *.length

console.log(string.length); // Devuelve 11 incluye espacios y simbolos.

// Extraer un caracter de la cadena. Para ello utilizaremos la notación del punto *.[n]

console.log(string[0]); // Devuelve "H"
console.log(string[string.length - 1]); // Devuelve "!"

// Encontrar una subcadena dentro de una cadena y extraerla *.indexOf()
// Como parametro utilizaremos la cadena a buscar y el resultado sera -1 si no se encuentra la cadena, y si se encuentra el numero n a partir de donde empieza la cadena.

console.log(string.indexOf("mundo")); // Devuelve 5
console.log(string[5]); // Devuelve "m"
console.log(string.indexOf("world")); // Devuelve -1

// Si sabes donde comienza una subcadena dentro de una cadena y sabes hasta cuál caracter deseas que termina puede usarse *.slice().
// Recibe dos parametrosel primero es la posicion en la que comienza a extraer el caracter y el segundo la posicion del caracter posterior al ultimo a ser extraido.

console.log(string.slice(5, 10)); // Devuelve "mundo"
console.log(string.slice(8, string.length)); // Devuelve "do!"
// El segundo parametro es opcional, si no se añade el corte termina al final de la cadena original
console.log(string.slice(5)); // Devuelve "mundo!"
console.log(string.slice(2)); // Devuelve "la mundo!"

// Cambiar todo a mayuscula o todo a minuscula *.toLowerCase() y *.toUpperCase()

console.log(string.toLowerCase()); // Devuelve "hola mundo!"
console.log(string.toUpperCase()); // Devuelve "HOLA MUNDO!"

// Actualizar partes de una cadena *.replace()

console.log(string.replace("Hola", "Hello")); // Devuelve "Hello mundo!"

// Combinar cadenas *.concat()

console.log(string.concat(", ", "Hello")); // Devuelve "Hola mundo!, Hello"

// Dividir cadenas *.split()
// El paremetro es el elemento separador de la cadena

console.log(string.split(" ")); // Devuelve [ 'Hola', 'mundo!' ]
console.log(string.split("")); // Devuelve [  'H', 'o', 'l', 'a',' ', 'm', 'u', 'n','d', 'o', '!']
console.log(string.split("-")); // Devuelve [ 'Hola mundo!' ]

//Buscar un valor dentro de la cadena *.includes()

console.log(string.includes("mundo")); // Devuelve true
console.log(string.includes("world")); // Devuelve false

// Eliminar los espacios en blanco al principio y final de una cadena

let string2 = "        Hello  World!    ";
console.log(string2.trim()); // Devuelve "Hello  World!"

// Extra =======
/* Un palíndromo es un término o una expresión que puede leerse tanto de izquierda a derecha como de derecha a izquierda (es decir, expresa lo mismo al ser leído de manera tradicional o al revés).
 */

const isPalindromo = (string) => {
  let element1 = string.toLowerCase().trim().split(" ").join(""); // almacenamos en la variable la cadena en minuscula y sin huecos a los lados y eliminamos los huecos entremedia y lo volvemos a juntar
  let element2 = element1.split("").slice().reverse().join(""); // Hacemos una copia de la string y le damos la vuelta

  if (element1 === element2) {
    console.log(`${string} es palindromo.`);
  } else {
    console.log(`${string} no es palindromo.`);
  }
};

isPalindromo("as$sa");
isPalindromo("12jeja85");

/* 
Un anagrama es una palabra que resulta de la transposición de todas las letras de otra palabra. Dicho de otra forma, una palabra es anagrama de otra si las dos tienen las mismas letras, con el mismo número de apariciones, pero en un orden diferente. Esto se aplica también a grupos de palabras o frases.
*/

const isAnagrama = (string1, string2) => {
  let element1 = string1.toLowerCase().trim();
  let element2 = string2.toLowerCase().trim();
  if (element1.length === element2.length) {
    element3 = element1.split("").sort().join("");
    element4 = element2.split("").sort().join("");
    if (element3 === element4) {
      console.log(`${element1} y ${element2} son anagramas.`);
    } else {
      console.log(`${element1} y ${element2} no son anagramas.`);
    }
  } else {
    console.log(`${element1} y ${element2} no son anagramas.`);
  }
};

isAnagrama("Nacionalista", "Altisonancia");
isAnagrama("Seudo", "Sesudo");

/* 
En morfología y juego verbal , un isograma es una palabra sin letras repetidas (como ambidestro ) o, más ampliamente, una palabra en la que las letras aparecen el mismo número de veces.
*/

const isIsograma = (string) => {

  let element1 = string.toLowerCase().trim();
  let set1 = new Set()

  for(let letra of element1) {
    if(set1.has(letra)) {
      return console.log(`${string}, no es un isograma.`)
    }
    else {
      set1.add(letra);
    }
  }
return console.log(`${string} es un isograma.`)

}

isIsograma("bilabial");
isIsograma("ambidestro");
