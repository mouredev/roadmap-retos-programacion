/* RETO #04 */
/*
var string = " Just a normal string ";

// string.at -> Retorna el caracter al cual le estas pasando el índice - Soporta índices negativos

console.log(`${string} el indice -5 retorna ${string.at(-5)}`); // r

// string.charAt -> Retorna el caracter al cual le estas pasando el índice - no soporta índices negativos

console.log(`${string} el indice 4 retorna ${string.at(4)}`); // t

// string.charCodeAt -> Retorna el valor unicode del caracter al cual le estas pasando el índice - no soporta índices negativos

console.log(`${string} el indice 4 retorna ${string.charCodeAt(4)}`); // 116

// string.concat -> Concatena dos o más strings

var string2 = "and another string";

console.log(string.concat(string2)); // Just a normal string and another string

// string.endsWith -> Retorna un valor booleano verificando si la cadena termina o no con el valor que le pasas

console.log(string.endsWith("string")); // false

// string.includes -> Retorna un valor booleano verificando si la cadena incluye o no el valor que le pasas

console.log(string.includes("string")); // true

// string.indexOf -> Retorna el índice de la primera ocurrencia del valor que le pasas

console.log(string.indexOf("string")); // 15

// string.lastIndexOf -> Retorna el índice de la última ocurrencia del valor que le pasas

console.log(string.lastIndexOf("t")); // 16

// string.length -> Retorna la longitud de la cadena

console.log(string.length); // 22

// string.match -> Busca una cadena por una expresión regular y retorna un array con los resultados

var regex = /[A-Z]/g;

console.log(string.match(regex)); // ['J']

// string.padEnd -> Completa la cadena con el valor que le pasas hasta la longitud que le indiques

console.log(string.padEnd(30, ".")); // Just a normal string ........

// string.padStart -> Completa la cadena con el valor que le pasas hasta la longitud que le indiques

console.log(string.padStart(30, "*")); // ******** Just a normal string

// string.repeat -> Repite la cadena el número de veces que le indiques

console.log("IDK ".repeat(5)); // IDK IDK IDK IDK IDK

// string.replace -> Reemplaza un valor por otro

var replaceable = "The day over the days";

console.log(replaceable.replace("day", "night")); // The night over the days

// string.replaceAll -> Reemplaza todas las ocurrencias de un valor por otro

console.log(replaceable.replaceAll("day", "night")); // The night over the nights

// string.slice -> Extrae una sección de la cadena y la retorna como una nueva cadena

console.log(replaceable.slice(4, 7)); // day

// string.split -> Divide la cadena en un array de subcadenas

console.log(string.split(" ")); // [ '', 'Just', 'a', 'normal', 'string', '' ]

// string.startsWith -> Verifica si la cadena comienza con el valor que le pasas

console.log(string.startsWith("Just")); // false

// string.substring -> Extrae los caracteres entre dos índices especificados

console.log(replaceable.substring(4, 7)); // day

// string.toLowerCase -> Convierte la cadena a minúsculas

console.log(string.toLowerCase()); // just a normal string

// string.toUpperCase -> Convierte la cadena a mayúsculas

console.log(string.toUpperCase()); // JUST A NORMAL STRING

// string.trim -> Elimina los espacios en blanco al inicio y al final de la cadena

console.log(string.trim()); // Just a normal string

// string.trimEnd -> Elimina los espacios en blanco al final de la cadena

console.log(string.trimEnd()); // Just a normal string

// string.trimStart -> Elimina los espacios en blanco al inicio de la cadena

console.log(string.trimStart()); // Just a normal string
*/
function identifier(str1, str2) {
  palindromo(str1);
  palindromo(str2);
  anagrama(str1, str2);
  isograma(str1);
  isograma(str2);
}

function palindromo(str) {
  var regex = /[a-z]/g;

  str = str.toLowerCase().match(regex).join("");

  return str === str.split("").reverse().join("")
    ? console.log(str, "es palindromo")
    : console.log(str, "no es palindromo");
}
//palindromo("A man, a plan, a canal, Panama");

function palindrome(str) {
  var regex = /[a-z]/g;

  str = str.toLowerCase().match(regex).join("");

  return str === str.split("").reverse().join("");
}

var anagramaTest1 = "Clint Eastwood";
var anamgramaTest2 = "Old West action";

function anagrama(str1, str2) {
  regex = /[a-z]/g;

  str1 = str1.toLowerCase().match(regex).join("");
  str2 = str2.toLowerCase().match(regex).join("");

  return str1.split("").sort().join("") === str2.split("").sort().join("")
    ? console.log(str1, "y", str2, "son anagramas")
    : console.log(str1, "y", str2, "no son anagramas");
}

//anagrama(anagramaTest1, anamgramaTest2);

function isograma(str) {
  var regex = /[a-z]/g;
  str = str.toLowerCase().match(regex);
  for (let i = 0; i < str.length; i++) {
    if (str.indexOf(str[i]) !== str.lastIndexOf(str[i])) {
      return console.log(str.join(""), "no es isograma");
    }
  }
  console.log(str.join(""), "es isograma");
}

//isograma("Hormiga");

identifier("Anita lava la tina", "Oso");
