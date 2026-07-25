/**
 * Operaciones con cadenas de caracteres
 */

const string1 = '   JavaScript';
const string2 = 'Programming   ';

// Concatenación
let newString = string1.concat(' ', string2);   // '   JavaScript Programming   '
console.log(newString);

// Longitud
newString.length();   // 28

// Acceso a un caracter especifico
newString[0];   // ''
newString[14];   // 'P'
newString[28];   // 'undefined -> El índice no existe

// .charAt() = Permite comprobar el índice de un cracter
newString.charAt();   // '' -> Si el argumento del paréntesis esta vacío devuleve el índice 0
newString.charAt(7);   // 'S'
newString.charAt(30);   // '' -> Devuelve un string vacio cuando el índice no exíste

// .indexOf() = Devuelve el índice del caracter indicado
newString.indexOf();   // -1 -> Devuelve -1 en caso de no indicar el caracter al método o cuando no encuentra el caracter en el string
newString.indexOf('a');   // 4
newString.indexOf('a', 10); // 19 -> El segundo argumento indica el índice desde donde debe empezar a buscar el valor indicado

// .lastIndexOf() = Realiza la busqueda de un caracter desde el final del string
newString.lastIndexOf('r'); // 18
newString.lastIndexOf('r', 12); // 9

// .repeat()
string1.repeat(3);   // '   JavaScript   JavaScript   JavaScript'
string2.repeat();   // '' -> Devuleve un string vacio si no se indican las repeteciones

// .slice() = Extrae una sección del string indicada sin incluir el índice del segundo argumento
newString.slice(3, 13);   // 'JavaScript'
newString.slice(14);   // 'Programming   '
newString.slice(-11)   // 'gramming   '

// .substring()
newString.substring(3, 7);   // 'Java'
newString.substring(13, 7);   // 'Script' -> Cuando argStart > argEnd, JS invierte los argumentos
newString.substring(-15);   // '   JavaScript Programming   ' -> Este método no acepta índices snegativos

// .split() = Divide un strung en un Array de substrings a partir de separadores indicados: puntos, comas, espacios, etc
newString.split(' ');   // ['', '', '', 'JavaScript', 'Programming', '', '', '']

// .startsWith() = Comprueba si el string comienza por el argumento indicado
newString.startsWith('');   // true
newString.startsWith('S');   // false
newString.startsWith('Java', 3)   // true

// .endsWith() = Comprueba si el string termina por el argumento indicado
newString.endsWith('');   // true
newString.endsWith('P');   // false
newString.endsWith('ing', 25);  // true

// .includes() = Comprueba si el string contiene el argumento indicado
newString.includes('Pro');   // true
newString.includes('gamming');   // false
newString.includes('Java', 5);   // false

// .search() = Este método realiza una busqueda en el string unicamente cuando el argumento es una Expresión Regular (RegExp)
newString.search(/c/g);   // 8
newString.search(/ram/g);   // 18
newString.search(/Python/g);   // -1

// .match() = Busca coincidencias y devuleve un Array; su comportamiento cambia al utilizar el flag -g-
newString.match(/a+/);   // ['a', index: 4, input: '   JavaScript Programming   ', groups: undefined]
newString.match(/a+/g);   // ['a', 'a', 'a']
newString.match(/e+/g);   // null

// .matchAll() = Busca todas las coincidencias y devuelve un iterador con sus detalles. Es obligatorio el uso de -g-
for(const match of newString.matchAll(/v/g)){
    console.log(`Letra '${match[0]}', en índice ${match.index}`)   // Letra 'v', en índice 5
}

// .replace() = Permite reemplazar la primiera coincidencia en un string
newString.replace('JavaScript', 'Python');   // '   Python Programming   '
newString.replace('JavaScript', 'Python').replace('Programming', 'Language');   // '   Python Language   '

// .replaceAll() = Permite reemplazar todas las coincidencias en un string
newString.replaceAll('a', 'e');   // '   JeveScript Progremming   '

// .replace(RegExp)
newString.replace(/[aio]/g, 'u');   // '   JuvuScrupt Prugrummung   '

// Convertir en Mayúsculas y Minúsculas
newString.toLowerCase();   // '   javascript programming   '
newString.toUpperCase();   // '   JAVASCRIPT PROGRAMMING   '

// .trim() = Elimina los espacios sobrantes que no esten entre palabras de un string
newString.trim();   // 'JavaScript Programming'
newString.trimStart();   // 'JavaScript Programming   '
newString.trimEnd();   // '   JavaScript Programming'

// .padStart() y .padEnd() = Rellena un string al pricipio o al final indicando el argumento ysu longitud
const stringNumber = '5';
stringNumber.padStart(3, '0');   // '005'
stringNumber.padEnd(3, '0');   // '500'

/**
 * Dificultad Extra:
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
 *  - Palíndromos
 *  - Anagramas
 *  - Isogramas
 */


// const comprobarPalindroma = () => {
//     let word = prompt("Escribe una frase o palabra: ");

//     const validarPalabra = word.toLocaleLowerCase().split("").reverse().join("");

//     if(validarPalabra === word.toLocaleLowerCase()){
//         console.log(`${word} es una Palabra Pálindroma`);
//         return;
//     } else{
//         console.log(`${word} no es una Palabra Pálindroma`);
//         return;
//     };
// }

// comprobarPalindroma();

// const comprobarAnagrama = () => {
//     let word1 = prompt("Escribe la primera palabra: ");
//     let word2 = prompt("Escribe la segunda palabra: ");

//     if(word1.length !== word2.length){
//         console.log(`${word1} y ${word2} no son Palabras Anagramas`);
//         return;
//     }

//     const validarPalabra1 = word1.toLocaleLowerCase().split("").sort().join("");
//     const validarPalabra2 = word2.toLocaleLowerCase().split("").sort().join("");

//     if(validarPalabra1 === validarPalabra2){
//         console.log(`${word1} y ${word2} son Palabras Anagramas`);
//     } else{
//         console.log(`${word1} y ${word2} no son Palabras Anagramas`);
//     };
// }

// comprobarAnagrama();

// const comprobarIsograma = () => {
//     let word = prompt("Escribe una palabra: ");

//     const validarPalabra = new Set(word.toLocaleLowerCase());

//     if(validarPalabra.size === word.length){
//         console.log(`${word} es una Palabra Isograma`);
//     } else{
//         console.log(`${word} no es una Palabra Isograma`);
//     }
// }

// comprobarIsograma();

const comprobarPalabra = () => {
    let word1 = prompt("Escribe la primera palabra: ");
    let word2 = prompt("Escribe la segunda palabra: ");

    const comprobarPalindroma = (word) => {
        const validarPalabra = word.toLocaleLowerCase().split("").reverse().join("");

        if(validarPalabra === word.toLocaleLowerCase()){
            console.log(`${word} es una Palabra Pálindroma`);
        } else{
            console.log(`${word} no es una Palabra Pálindroma`);
        };
    }

    comprobarPalindroma(word1);
    comprobarPalindroma(word2);

    const comprobarAnagrama = (word1, word2) => {
        if(word1.length !== word2.length){
            console.log(`${word1} y ${word2} no son Palabras Anagramas`);
            return;
        }

        const validarPalabra1 = word1.toLocaleLowerCase().split("").sort().join("");
        const validarPalabra2 = word2.toLocaleLowerCase().split("").sort().join("");

        if(validarPalabra1 === validarPalabra2){
            console.log(`${word1} y ${word2} son Palabras Anagramas`);
        } else{
            console.log(`${word1} y ${word2} no son Palabras Anagramas`);
        };
    }

    comprobarAnagrama(word1, word2);

    const comprobarIsograma = (word) => {
        const validarPalabra = new Set(word.toLocaleLowerCase());

        if(validarPalabra.size === word.length){
            console.log(`${word} es una Palabra Isograma`);
        } else{
            console.log(`${word} no es una Palabra Isograma`);
        }
    }

    comprobarIsograma(word1);
    comprobarIsograma(word2);
}

comprobarPalabra();