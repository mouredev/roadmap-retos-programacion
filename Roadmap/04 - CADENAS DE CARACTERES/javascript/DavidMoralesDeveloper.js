// 1 Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
//  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):

console.log("cadena basica");
//concatenaión
const string = "JavaScript";
const string2 = "ola k ace";
console.log(string + " espacio " + string2);
//interpolación
console.log(
  `ESC6 una manera moderna de concatenar ${string} junto a ${string2}`
);

// Propiedades de string pagina oficial: https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/replace

// Repetir
console.log(string.repeat(3));

// Indexación
console.log(string[1] + string2[0]);

//Longitud
console.log(string.length);

// Slice (porcion o rebanada)
const frase = "soy una frase muy corta";
console.log(frase.slice(3, 10));

//Busqueda
console.log(string2.includes("k"));
console.log(
  `el meme ola k ace incluye la palabra: ace =  ${
    string2.includes("ace") ? ", si lo inclue" : ", no lo incluye"
  } `
);
console.log(
  `el meme ola k ace incluye la palabra: hace = ${
    string2.includes("hace") ? ", si lo inclue" : ", no lo incluye"
  } `
);

// #remplazo
console.log(string2.replace("ace", "hace"));

// Division
let separadorArr = string.split("S");
console.log(separadorArr + " split JavaScript"); //[ 'Java', 'cript' ]

//Union

console.log(separadorArr.join("S") + " join propiedad"); //JavaScript join propiedad

//Mayusculas y minusculas
console.log(string.toLocaleLowerCase());
console.log(string.toLocaleUpperCase());
console.log(string.toLowerCase());
console.log(string.toUpperCase());
//Primera Mayus
console.log(string.charAt(0).toUpperCase() + string.slice(1));
console.log(string[0].toUpperCase() + string.slice(1));

//eliminación de espacios
console.log(string2.trim()); // no funciona pero que investigar
let unido = string2.split(" ");
console.log(unido);
console.log(unido.join("-"));

//Budqueda  al principio y final
// inicio
console.log(string.startsWith("Ja")); //true
console.log(string.startsWith("Scr")); //false
//final
console.log(string.endsWith("ipt")); //true
console.log(string.endsWith("Jav")); //false

//Busqueda de pisición
console.log(string2.search("ace")); //6

// de string a un array
let lista1 = string2.split("");
console.log(lista1); // ['o', 'l', 'a', ' ', 'k', ' ', 'a', 'c', 'e']
console.log(lista1.join("")); // ola k ace

//trasfomacion numerico

let numeros = "123456";
let numerosDecimal = "123.456";
console.log(typeof numeros); //string
console.log(typeof parseInt(numeros)); //number
console.log(parseFloat(numerosDecimal)); //numeros decimales
console.log(parseInt(numeros)); //numeros enteros

//Extra ------------------------------------------------

// Crea un programa que analice dos palabras diferentes y realice comprobaciones
//  * para descubrir si son:
//  * - Palíndromos
//  * - Anagramas
//  * - Isogramas

//funcion la cual analiza dos palabras

function analitic(word1, word2) {
  // el primer analicis seria si se lee al derecho y al reves y es estrictamente igual

  //   Palíndromos
  word1.split("").reverse().join("") === word1
    ? console.log(`${word1} :es un palindromo`)
    : console.log(`${word1} :no es un palindromo `);
  word2.split("").reverse().join("") === word2
    ? console.log(`${word2} :es un palindromo`)
    : console.log(`${word2} :no es un palindromo `);

  //   Anagrama
  word1.split("").sort().join() == word2.split("").sort().join()
    ? console.log(` ${word1} es anagrama de ${word2}  `)
    : console.log(` ${word1} no es anagrama de ${word2} `);

  //   Isograma
  //isograma de primer orden se repiten todas las palabras una sala vez

  //creo funcion de isograma
  function isograma (word){
    const wordArray = word.split("");
    const wordSet = new Set(wordArray);
    if (wordArray.length === wordSet.size) {
        // console.log(wordArray)
        // console.log(wordSet)
        // console.log(true)
       return true
    } else {
        // console.log(wordArray)
        // console.log(wordSet)
        // console.log(false)
       return false
    }
  }
 //EJECUTO FUNCION de isograma
  isograma(word1) ? console.log(` ${word1} es un isograma de primer orde`) : console.log(` ${word1} no es un isograma de primer orde`)
  isograma(word2) ? console.log(` ${word2} es un isograma de primer orde`) : console.log(` ${word2} no es un isograma de primer orde`)

//   isograma de multinivel queda pendiendiente , espero resolverlo pronto



} //final de funcion analitic

analitic("ana", "ala");
analitic("roma", "amor");
analitic('murcielago', 'ambiente')




