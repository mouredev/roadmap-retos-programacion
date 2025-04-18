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

//
// STRINGS
//

// Declaracion

let myStr = "Soy un strig con comillas dobles"
let myStrr = 'Soy un string con comillas simple'
let myStrrr = `Soy un string con backsticks`

console.log(myStr)
console.log(myStrr)
console.log(myStrrr)

//
// METODOS 
//

// charAt()
const ejemploCharAt = "Hola mundo"; // Devuelve el caracter en la posicion indicada
console.log('Caracter buscado mediante la posicion: ',ejemploCharAt.charAt(2)); 
console.log('Caracter buscado mediante la posicion: ',ejemploCharAt.charAt(7)); 

//charCodeAt()
const ejemploCharCodeAt = "Hola"; // Devuelve el valor UTF-16 del carácter en la posición indicada.
console.log(ejemploCharCodeAt.charCodeAt(0)); 

// codePointAt()
const ejemploCodePointAt = "A"; // Devuelve el valor Unicode del punto de código en la posición dada.
console.log(ejemploCodePointAt.codePointAt(0)); 

// concat()
const ejemploConcat = "Hola, ".concat("Gianfranco", "!"); // Concatena (une) una o más cadenas.
console.log(ejemploConcat); 

// includes()
const ejemploIncludes = "JavaScript es genial"; // Verifica si la cadena contiene la subcadena especificada.
console.log(ejemploIncludes.includes("genial")); 

// endsWith()
const ejemploEndsWith = "Hola mundo"; // Verifica si la cadena termina con la subcadena especificada.
console.log(ejemploEndsWith.endsWith("mundo")); 

// indexOf()
const ejemploIndexOf = "banana"; // Devuelve la posición de la primera ocurrencia del valor indicado.
console.log(ejemploIndexOf.indexOf("a")); 

// lastIndexOf()
const ejemploLastIndexOf = "banana"; // Devuelve la posición de la última ocurrencia del valor indicado.
console.log(ejemploLastIndexOf.lastIndexOf("a")); 

// localCompare()
const ejemploLocaleCompare = "café"; // Compara dos cadenas según la configuración regional.
console.log(ejemploLocaleCompare.localeCompare("cafe")); 

// match()
const ejemploMatch = "Hoy es 17 de abril"; // Devuelve las coincidencias de una expresión regular.
console.log(ejemploMatch.match(/\d+/)); 

// matchAll()
const ejemploMatchAll = "uno, dos, tres"; // Devuelve un iterador con todas las coincidencias de una expresión regular.
const matches = [...ejemploMatchAll.matchAll(/\w+/g)]; 
console.log(matches.map(m => m[0])); 

// normalize()
const ejemploNormalize = "\u004e\u006f\u0072\u006d\u0061\u006c\u0065"; // Normaliza una cadena en su forma Unicode.
console.log(ejemploNormalize.normalize()); 

// padEnd()
const ejemploPadEnd = "123"; // Agrega caracteres al final de la cadena hasta llegar a la longitud deseada.
console.log(ejemploPadEnd.padEnd(6, "0")); 

// padStart()
const ejemploPadStart = "45"; // Agrega caracteres al inicio de la cadena hasta llegar a la longitud deseada.
console.log(ejemploPadStart.padStart(5, "0")); 

// repeat()
const ejemploRepeat = "ha"; // Repite la cadena la cantidad de veces indicada.
console.log(ejemploRepeat.repeat(3)); 

// replace()
const ejemploReplace = "Me gusta el pan"; // Reemplaza la primera aparición de una subcadena.
console.log(ejemploReplace.replace("pan", "queso")); 

// replaceAll()
const ejemploReplaceAll = "Hola mundo mundo mundo"; // Reemplaza todas las apariciones de una subcadena.
console.log(ejemploReplaceAll.replaceAll("mundo", "universo")); 

// search()
const ejemploSearch = "El número 42 es especial"; // Devuelve el índice de la primera coincidencia con una expresión regular.
console.log(ejemploSearch.search(/\d+/)); 

// slice()
const ejemploSlice = "JavaScript"; // Devuelve una porción de la cadena desde beginIndex hasta endIndex (sin incluirlo).
console.log(ejemploSlice.slice(4, 10)); 

// split()
const ejemploSplit = "manzana,banana,pera"; // Divide la cadena en un array usando un separador.
console.log(ejemploSplit.split(","));

// startsWith()
const ejemploStartsWith = "Buenos días"; // Verifica si la cadena comienza con la subcadena indicada.
console.log(ejemploStartsWith.startsWith("Buenos")); 

// substring()
const ejemploSubstring = "JavaScript"; // Devuelve los caracteres entre dos índices (sin incluir indexEnd).
console.log(ejemploSubstring.substring(4, 10)); 

// toLowerCase()
const ejemploToLowerCase = "HOLA MUNDO"; // Convierte toda la cadena a minúsculas.
console.log(ejemploToLowerCase.toLowerCase()); 

// toString()
const ejemploToString = 12345; // Devuelve una representación en forma de cadena del objeto.
console.log(ejemploToString.toString()); 

// toUpperCase()
const ejemploToUpperCase = "hola mundo"; // Convierte toda la cadena a mayúsculas.
console.log(ejemploToUpperCase.toUpperCase()); 

// trim()
const ejemploTrim = "   espacio   "; // Elimina espacios en blanco al inicio y al final de la cadena.
console.log(ejemploTrim.trim()); 

// trimStart()
const ejemploTrimStart = "   inicio"; // Elimina espacios al comienzo de la cadena.
console.log(ejemploTrimStart.trimStart()); 

// trimEnd()
const ejemploTrimEnd = "fin   "; // Elimina los espacios en blanco al final de la cadena.
console.log(ejemploTrimEnd.trimEnd()); 

// valueOf()
const ejemploValueOf = new String("valor primitivo"); // Devuelve el valor primitivo de un objeto String.
console.log(ejemploValueOf.valueOf()); 

// @@iterador()
const ejemploIterator = "hola"; // Permite recorrer los caracteres de una cadena con un iterador.
for (const letra of ejemploIterator[Symbol.iterator]()) {
    console.log(letra);
}

// 
// Metodos que funcionan como propiedades internas o funciones
//

// Acceder al carácter con notación de corchete (similar a charAt)
const ejemploBracket = "cadena";
console.log(ejemploBracket[2]); 

// Comparación de cadenas con ===
const str1 = "abc";
const str2 = "abc";
console.log(str1 === str2); 

// .length
const ejemploLength = "longitud"; // Longitud de una cadena.
console.log(ejemploLength.length);  

//
// EXTRA
//

function compareString(str1, str2) {
    const a = str1.toLowerCase();
    const b = str2.toLowerCase();

    console.log('🔄 Palabras comparadas:', a, '-', b);

    console.log('* ¿Es Palíndroma? *');
    if (isPalindromo(a)) {
        console.log(`✅ La palabra "${a}" es palíndroma.`);
    } else {
        console.log(`❌ La palabra "${a}" no es palíndroma.`);
    }
    if (isPalindromo(b)) {
        console.log(`✅ La palabra "${b}" es palíndroma.`);
    } else {
        console.log(`❌ La palabra "${b}" no es palíndroma.`);
    }

    console.log('* ¿Son Anagramas entre sí? *');
    if (isAnagrama(a, b)) {
        console.log(`✅ Las palabras "${a}" y "${b}" son anagramas entre sí.`);
    } else {
        console.log(`❌ Las palabras "${a}" y "${b}" no son anagramas entre sí.`);
    }

    console.log('* ¿Es Isograma? *');
    if (isIsograma(a)) {
        console.log(`✅ La palabra "${a}" es un isograma.`);
    } else {
        console.log(`❌ La palabra "${a}" no es un isograma.`);
    }
    if (isIsograma(b)) {
        console.log(`✅ La palabra "${b}" es un isograma.`);
    } else {
        console.log(`❌ La palabra "${b}" no es un isograma.`);
    }

    console.log('------------------------------');
}

function isPalindromo(str) {
    return str === str.split("").reverse().join("")
}
function isAnagrama(str1,str2){
    return str1.split('').sort().join('') === str2.split('').sort().join('');
}
function isIsograma(str){
    for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j < str.length; j++) {
        if (str[i] === str[j]) {
        return false;
        }}}
    return true;
}

// 🧪 Casos de prueba
compareString("reconocer", "reconocer"); 
compareString("anita", "atina");         
compareString("murcielago", "pantheon"); 
compareString("abc", "cab");             
compareString("banana", "perro");       
compareString("radar", "luz");           
compareString("gato", "gaga");           
compareString("amor", "roma");           
