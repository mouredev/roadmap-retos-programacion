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

let text: string = "hola";
let text2: string = "mundo";
let text3: string = "Java,Typescript,Python,Javascript,C";
let text4: string = "    Hola    ";
let text5: string = "Jesus|25|Peter|36|James|85";
const numberRegexp = /^[A-Z a-zs]+$/;

//--- Acceso especifico a un caracter de una cadena
console.log(text[0]);
console.log(text2[1]);

//--- Concatenando 2 cadenas de texto (concat)
console.log(text.concat(" ").concat(text2));

//--- Tomando 2 caracteres de una cadena de texto (substring o slice)
console.log(text.substring(2, 4));
console.log(text2.slice(3,6));

//--- Dividiendo un cadena de texto (split), esto retorna un array de cadenas
console.log(text3.split(","));

//--- Numero de caracteres que contiene un cadena (length)
console.log(text.length);

//--- Remplazando caracteres por otros en una cadena (replace)
console.log(text3.replace(",", "|"));

//--- Repitiendo la misma cadena (repeat)
console.log(text.repeat(3));

//--- Cadena en mayusculas (toUpperCase)
console.log(text.toUpperCase());

//--- Cadena en minusculas (toLowerCase)
console.log(text.toLowerCase());

//--- Buscar un caracter dentro de una cadena (search)
console.log(text3.search("P"));

//--- Buscar una cadena dentro de una cadena de texto (includes)
console.log(text3.includes("Python"));

//--- Quitar espacios en una cadena de texto (trim)
console.log(text4.trim());

//--- Quitar el primer espacio en blanco de una cadena (trimStart)
console.log(text4.trimStart());

//--- Quitar el ultimo espacio en blanco de una cadena (trimEnd)
console.log(text4.trimEnd());

//--- Crear un array mediante la coincidencia de una expresion regular dentro de una cadena de texto (match)
console.log(text5.match(numberRegexp));

//--- Ejercicio Extra
function analizedString(text1: string, text2: string): void{
    //--- Palindromos
    let text1Reverse: string = text1.split("").reverse().join("").toLowerCase();
    let text2Reverse: string = text2.split("").reverse().join("").toLowerCase();
    let result: string = "";

    result = text1 == text1Reverse
        ? `La palabra ${text1} es Palindroma`
        : `La palabra ${text1} NO es Palindroma`;
    console.log(result);

    result = text2 == text2Reverse
        ? `La palabra ${text2} es Palindroma`
        : `La palabra ${text2} NO es Palindroma`;
    console.log(result);

    //--- Anagramas
    let text1Sorted = text1.split("").sort((a, b) => a.localeCompare(b)).join("");
    let text2Sorted = text2.split("").sort((a, b) => a.localeCompare(b)).join("");

    result = text1Sorted == text2Sorted
        ? `Las palabras ${text1} y ${text2} son Anagramas`
        : `Las palabras ${text1} y ${text2} NO son Anagramas`

    //--- Isogramas
    let textSet1: Set<string> = new Set<string>(text1);
    let textSet2: Set<string> = new Set<string>(text2);
    result = text1.length == textSet1.size
        ? `La palabra ${text1} es Isograma`
        : `La palabra ${text1} NO es Isograma`;
    console.log(result);

    result = text2.length == textSet2.size
        ? `La palabra ${text2} es Isograma`
        : `La palabra ${text2} NO es Isograma`;
    console.log(result);
}

analizedString("roma", "amor");
