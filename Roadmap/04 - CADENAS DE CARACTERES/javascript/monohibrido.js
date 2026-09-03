//====================CADENA DE CARACTERES====================
/*
- Variable que posee información de texto
- tipo de dato STRING
*/

//===Notación mediante objeto y comillas dobles===
let texto = new String("Hola chicas/os");
console.log(texto); //[String: 'Hola chicas/os']

//===Notación literal (preferida) y comillas simples===
let texto2 = 'Hola hola a todas/os';
console.log(texto2);//Hola hola a todas/os

/*
Propiedades (variables) y métodos (funciones) de un string
*/

//===Devolver el número de caracteres totales del texto===
text = "Cantidad de caracteres"
console.log(text.length); //22

//===Acceso a un caracter indicando la posición===
console.log(text[5]); //"d"

//Intentando acceder a una posición que no existe
console.log(text[40]); //undefined

//===Interpolación de variables===
let ciudad = "Santiago";
let pais = "Chile";

console.log("Concatenar texto: " + ciudad + "de" + pais) //SantiagodeChile
console.log(`La mejor forma: ${ciudad} de ${pais}`); //La mejor forma: Santiago de Chile


//===Métodos: Posición e Índice===

//Busca el caracter por medio del índice.
console.log(ciudad.charAt(3)); // "t"
console.log(ciudad.charAt(10)); // "" string vacío, por eso es mejor []
console.log(ciudad[10]); // undefined

//Busca un caracter en nuestro string y nos devuelve el índice de la primera aparición de dicho caracter
console.log(ciudad.indexOf("i")); //4

//buscar un caracter con un parámetro from, es la posición en la que empieza a buscar.
let word = "Consola"
console.log(word.indexOf("o", 3)); //4
console.log(word.indexOf("o", 14)); // -1 ->  Si no lo encuentra devolverá -1

//Creación de substring

//Devuelve el string repetido NUM veces
console.log(word.repeat(3)); //ConsolaConsolaConsola

//Devuelve el substring desde la posición START hasta END
//si se omite el parámetro END, abarcará hasta el final.
console.log(word.substring(2, 6)); // nsol
console.log(word.substring(3)); //sola

//Devuelve el substring desde la posición START hasta START+SIZE
//si se omite el parámetro SIZE, abarcará hasta el final
console.log(word.substr(2, 5)); // nsola
console.log(word.substr(1)); // onsola
console.log(word.substr(-3)); // ola -> desde la posición -3 en adelante
console.log(word.substr(-3, 2)); //ol -> desde la posición -3 y la cantidad de caracteres.

//concat() concatenar el texto de dos cadenas y devuelve una nuvea cadena

let str1 = "Hello";
let str2 = "World";

console.log(str1.concat(" ", str2)); // Hello world

//includes() determina si una cadena de texto puede ser encontrada dentro de otra cadena de texto
//devuelve true o false según corresponda. 

let sentence = "The quick brown fox jumps over the lazy dog.";
word = "fox";

console.log(
    `The word "${word}" ${sentence.includes(word) ? "is" : "is not"
    } in the sentence`
);

console.log(sentence.includes("quicke")); // return false


//toUpperCase() cambian todas las letras a mayúsculas
console.log(sentence.toUpperCase());

//toLowerCase() cambian todas las letras a minúsculas
let fraseEnMayuscula = "TODO EN MAYÚSCULA QUE PASARÁ A MINÚSCULA"
console.log(fraseEnMayuscula.toLowerCase());

//trim() Quita los espacios vacíos que están al inicio y al final del texto
let fraseConEspacios = "  esta frase tiene espacios al inicio y al final    ";
console.log(`Con espacios:    [${fraseConEspacios}]`);
console.log(`Sin espacios:    [${fraseConEspacios.trim()}]`);

//split("") / (",") Dividir texto en partes eligiendo el caracter donde lo separa, no con qué lo separa
console.log("Hola, cristian, como, estás,".split(",")); // ["Hola", "cristian", "como", "estás"]
console.log("Hola".split("")) // corta cada caracter -> ["H", "o", "l", "a"];


//replace() reemplazo de una palabra
let fraseReplace = "El perro come, el perro duerme";
console.log(fraseReplace.replace("perro", "canguro")); //reemplaza solo la primera palabra

//replaceAll() reemplazo de todas las palabras
console.log(fraseReplace.replaceAll("perro", "gato"));//reemplaza todas

//startsWith() / endsWith()  -> verificación de caracteres
let saludo = "Hola mundillo";
console.log(saludo.startsWith("Hola")); //true
console.log(saludo.endsWith("mundillo")); //true
console.log(saludo.startsWith("mundillo")); //false
console.log(saludo.endsWith("llo"));  //true

//slice() subcadena como substring pero con negativos.

let texto3 = "Javascript";
console.log(texto3.slice(0, 4)); //Java
console.log(texto3.slice(-6)) //script

//recorrido con for...of
for (let caracter of "hola") {
    console.log(caracter);
}

// ================================================= DIFICULTAD EXTRA ==============================================0

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
*/

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


rl.question("Ingresa la primera palabra: ", (p1) => {
    rl.question("Ingresa la segunda palabra: ", (p2) => {

        const palabra1 = p1.trim().toLocaleLowerCase();
        const palabra2 = p2.trim().toLocaleLowerCase();

        console.log("PALÍNDROMOS");
        console.log(`La palabra 1: ${palabra1.split("").reverse().join("") === palabra1 ? "Es un palíndromo" : "No es un palíndromo"}`);
        console.log(`La palabra 2: ${palabra2.split("").reverse().join("") === palabra2 ? "Es un palíndromo" : "No es un palíndromo"}`);

        console.log("ANAGRAMA");
        const p1Ordenada = palabra1.split("").sort().join("");
        const p2Ordenada = palabra2.split("").sort().join("");
        console.log(`¿Son anagramas?: ${p1Ordenada === p2Ordenada ? "Son un anagrama" : "No son un anagrama"}`);

        console.log("ISOGRAMAS");
        console.log(`La palabra 1: ${new Set(palabra1.split("")).size === palabra1.length ? "Es un isograma" : "No es un isograma"}`);
        console.log(`La palabra 2: ${new Set(palabra2.split("")).size === palabra2.length ? "Es un isograma" : "No es un isograma"}`);

        rl.close();
    })
})


