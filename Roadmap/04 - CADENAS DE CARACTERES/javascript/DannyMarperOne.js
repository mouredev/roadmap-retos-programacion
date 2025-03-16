//#04 CADENAS DE CARACTERES

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

//CONSTRUCTOR

// ************** string() y new String() *******************

//String() convierte un valor a cadena de texto y lo retorna como un valor primitivo.
let numbers = 1234;
let cadenaString = String(numbers); // "1234"
console.log(typeof cadenaString); //string

//new String() crea un objeto de tipo string, se utiliza como contructor, y devulve un objeto string
let numb = 9874;
let stringObj = new String(numb); //[String: '9874']
console.log(typeof stringObj); // object





// MÉTODOS ESTATICOS

// ******************** String.raw **************************

//Devuleve cadenas en crudo, sin procesar

let name1 = "Daniel";
let full = String.raw`Hola\n${name1}\\ como estás \"`;
/* No procesa secuencias de escape (barras invertidas), no da saltos de linea, 
ni agrega comillas, todo lo pasa literal. */
console.log(full); //Salida: Hola\nDaniel\\ como estás \"





//PROPIEDADES

//*************  Longitud = Length  *****************

//Devuelve la longitud de una cadena

let player = "Cristiano Ronaldo"
let cr7 = player.length;

console.log(cr7) //Salida: 17
console.log('The name ' + player + ' has ' + player.length + ' characters'); //Salida: The name Cristiano Ronaldo has 17 characters





//MÉTODOS

//**************  charAt = Acceder a un solo caracter  ****************

//Devuelve el valor de index al que se desea acceder

let escuderia = "Ferrari";
//Acceder a la posición del caracter
console.log(escuderia.charAt(3)); //Salida: r
//Acceder al último caracter del string
console.log(escuderia.charAt(escuderia.length - 1)); //Salida: i
//Si se busca una posición que supere el tamaño del string, devulve cadena vacia.



//************** concat() ****************

//Ayuda a concatenar o unir variables, cadenas, etc.

let hello = "Hello, ";
console.log(hello.concat("Kevin", ". Have a nice day.")); //Salida: Hello, Kevin. Have a nice day.

let greetList = ["Hello", " ", "Venkat", "!"];
console.log("".concat(...greetList)); //Salida: "Hello Venkat!"

"".concat({}); // [object Object]
"".concat([]); // ""
"".concat(null); // "null"
"".concat(true); // "true"
"".concat(4, 5); // "45"



//************** includes() *************

//Determina si una cadena de texto se encuentra dentro de otra cadena de texto, devolviendo true o false

let frase = "El campeon Max Verstappen vs el 7 veces campeon Lewis Hamilton"
let piloto = "Max";

console.log(`La palabra ${piloto} ${frase.includes(piloto) ? 'si' : 'no'} está dentro de la frase principal!`); //Devuelve si o no
console.log(`La palabra ${piloto} ${frase.includes(piloto)} está dentro de la frase principal!`); //Devulve true o false
console.log(`La palabra ${piloto} ${frase.includes(piloto, 12)} está dentro de la frase principal!`); //Busca apartir de la posición 12 de la cadena (False)



//*************** startsWith() ************* */

//Determina si una cadena de texto inicia con los caracteres de una cadena indicada, devolviendo true o false

let fraseFour = "Arriba el futbol de Monterrey"
console.log(`La primera palabra de la frase es Monterrey? ${fraseFour.startsWith('Arriba') ? 'SI' : 'NO'}`);
console.log(`La última palabra de la frase es Monterrey? ${fraseFour.startsWith('Arriba', 3) ? 'SI' : 'NO'}`);

//Ejemplo
let palabraStarsWith = "Tengo frio ahorita mismo. Mañana no creo.";
let iniciaCon = palabraStarsWith.startsWith("Ten");
let inciciaCon2 = palabraStarsWith.startsWith("Ten", 1);
console.log(iniciaCon);
console.log(inciciaCon2);
//Toma en cuenta los puntos finales
let puntoFinal = palabraStarsWith.startsWith("Ma", 26);
console.log(puntoFinal);



//*************** endsWhith() ************* */

//Determina si una cadena de texto termina con los caracteres de una cadena indicada, devolviendo true o false

let fraseTwo = "Arriba el futbol de Monterrey"
console.log(`La última palabra de la frase es Monterrey? ${fraseTwo.endsWith('Monterrey') ? 'SI' : 'NO'}`); //Determina la última palabra del string
console.log(`La última palabra de la frase es Monterrey? ${fraseTwo.endsWith('Monterrey', 3) ? 'SI' : 'NO'}`); //La posición de busqueda va de cualquier posición hacia atras



//*************** indexOf() y lastIndexOf() ************* */

//indexOf() Encuentra la primera ocurrencia de una subcadena (o carácter) dentro de una cadena. Va de izquierda a derecha.

//lastIndexOf() Encuentra la última ocurrencia de una subcadena (o carácter) dentro de una cadena o la primera ocurrencia llendo de derecha a izquierda.

let cadena = "MasterClassEnds";

console.log(cadena.indexOf("m")); //Salida: -1 (no encontrará la posición de 'm' porque indexOf es sencible a Mayusculas)
console.log(cadena.indexOf("M")); //Salida: 0
console.log(cadena.indexOf("r")); //Salida: 5 (indexOf busca el primer caracter de izquierda a derecha)
console.log(cadena.lastIndexOf("a")); //Salida: 8 (lasIndexOf busca el primer caracter pero de derecha a izquierda)

//Ejemplo
let cuenta = 0;
let posicion = cadena.indexOf("s"); //2
while (posicion != -1) {
    cuenta++;//1,2,3,4
    posicion = cadena.indexOf("s", posicion + 1); // 9(3), 10(10), 14(11) -1(15)
}
console.log(cuenta); //Salida: 4 (En si porque solo existen 4 's' dentro del string entonces la iteración fue de 4)
console.log(posicion); //Salida: -1 (Cuando ya no encontra más posiciones en el string retorna -1)



// ********************* localeCompare() *******************

//Sirve para hacer comparaciones entre cadenas de texto dependiento el alfabeto

let palabra1 = "manzana";
let palabra2 = "banana";

let resultado = palabra2.localeCompare(palabra1);
console.log(resultado); //Salida: -1
let resultado2 = palabra1.localeCompare(palabra2);
console.log(resultado2); //Salida: 1
/* Nota: entiendo que la cadena que está antes del localCompare es el dato a comparar, 
y este manda si el resultado es -1,1 o 0 (Si va antes de lo que está entre parentesis o después) */

//Ejemplo
let nombres = ["Pedro", "Ana", "Juan"];
nombres.sort((a, b) => a.localeCompare(b)); //Ocupamos sort para ordenar un arreglo y con localCompare le decimos que lo ordene alfabeticamente.
console.log(nombres);

//Se puede especificar el idioma en el que se requiere hacer la comparación
console.log("ä".localeCompare("z", "de")); // un valor negativo: en alemán, ä se ordena antes que z
console.log("ä".localeCompare("z", "sv")); // un valor positivo: en sueco, ä se ordena después que z



// ************************ Secuencias de escape o Notación de escape ****************************

/*
Estas notaciones permiten incluir caracteres que de otro modo serían difíciles de escribir o 
que podrían causar problemas en la interpretación del código. 
Las notaciones de escape comienzan con una barra invertida (\), seguida de un carácter que indica el tipo de escape. 
 */

let saludar = "Hola \n Daniel como estás \'Amigo\' \nMi nombre es \\ Gloria \\ \"Cabeza de Bolo\" Jejejej \r y tu? \v tabulacion vertical \t jejjeej \f ijijjiji \ud83d";
console.log(saludar);

// Cadenas literales largas
let adios = "Adios amigo \
me tengo que ir \
mañana debo de trabajar"; //Adios amigo me tengo que ir mañana debo de trabajar

let bye = "Adios amigo" +
    "me tengo que ir" +
    "mañana debo de trabajar"; //Adios amigo me tengo que ir mañana debo de trabajar



// ******************** String.fromCharCode() ********************************

// Devuelve una cadena creada de valores Unicode.

console.log(String.fromCharCode(65, 69, 67)); //Salida: AEC



// **************** .match() ***************

//Devuelve un array que contiene todas las coincidencias encontradas dentro de un string apartir de una Expresion Regula

let fraseThree = "Hola mi nombre es Optimus Prime, comandante de los 'Autobots'"
const expresionReg = /[A-Z]/g;
let resultMatch = fraseThree.match(expresionReg); //devuelve todas (/g) las mayusculas de la A-Z 
console.log(resultMatch);

const expresionReg2 = /[A-Z]/;
let resultMatch2 = fraseThree.match(expresionReg2); //devuelve la primer mayuscula entre la A-Z, su index, el input y el grupo
console.log(resultMatch2)



// ***************** padEnd() ****************

//Este metodo rellena un string con el string que nosotros proporciones colocando el index en el maxlenght que deseemos

let phraseEnd = "Esta frase termina con * apartir de aqui ";
let padExample = phraseEnd.padEnd(55, "*");
console.log(padExample);
//Si el maxLength es menor o igual al string, devolverá el string tal cual fue declarado.
console.log(phraseEnd.padEnd(10, "Repeat"));
// Si solo se coloca el maxLength sin el fillString como resultado por defecto es rellenar las posiciones con " ".
console.log(phraseEnd.padEnd(60));
console.log(phraseEnd.padEnd(60, "Repeat"));



// ***************** padStart() ****************

//Este metodo rellena un string con el string que nosotros proporciones colocando el index en el maxlenght que deseemos
//pero rellenará desde el principio del string original

//las condiciones de uso son las mismas que las de padEnd()
let phraseStart = "Esta frase empieza con *.";
console.log(phraseStart.padStart(40, "*"));



// ***************** repeat() ****************

//Repite un string la cantidad de veces necesarias (Solo numeros enteros)

console.log("hola".repeat(10)); //holaholaholaholaholaholaholaholaholahola
console.log("hola".repeat(10)); // RangeError
console.log("abc".repeat(0)); // ''



// ***************** replace() ****************

//Cualquier cosa que no sea un texto o un regex, este lo convierte en string

// Reemplaza un string completo, buscando una coincidencia y cambiandola por otro string
console.log("viva mexico cabrones".replace("cabrones", "******"));
//Se pueden utilizar expresiones regulares
let expRegReplace = /comer/i;
console.log("Es hora de ir a comer".replace(expRegReplace, "Dormir"));

// Ejemplo
const re = /apples/gi;
const str = "Apples are round, and apples are juicy.";
const newstr = str.replace(re, "oranges");
console.log(newstr); // orange are round, and oranges are juicy.

// Ejemplo
const ree = /(\w+)\s(\w+)/;
const stre = "Maria Cruz";
const newstre = stre.replace(ree, "$2, $1");
console.log(newstre); // Cruz, Maria

//Ejemplo: Uso de parametros match, p1, offset, string
function replacer(match, p1, offset, string) {
    console.log(`match: ${match}`); // La coincidencia completa
    console.log(`p1: ${p1}`); // El primer grupo de captura
    console.log(`offset: ${offset}`); // La posición en la cadena donde se encuentra la coincidencia
    console.log(`string: ${string}`); // La cadena original completa
    return p1.toUpperCase(); // Ejemplo de transformación
}
const regex = /(\w+)\s/;
const strr = "Hello world!";
const newStr = strr.replace(regex, replacer);
console.log(newStr);

//Ejemplo: Remplace con RegEx
function f2c(x) {
    function convert(str, p1, offset, s) {
        return `${((p1 - 32) * 5) / 9}C`;
    }
    const s = String(x);
    const test = /(-?\d+(?:\.\d*)?)F\b/ig;
    return s.replace(test, convert);
}
console.log(f2c("En mexico estamos a 100F y en alaska estan a -3f"));

//Ejemplo
console.log("bc abcd abcssssss sas".replace(/(bc)/, (match, p1, offset) => `${match} (${offset}) -`));

//Ejemplo Dificil
function addOffset(match, ...args) {
    const hasNamedGroups = typeof args.at(-1) === "object";
    const offset = hasNamedGroups ? args.at(-3) : args.at(-2);
    return `${match} (${offset}) `;
}
console.log("abcd".replace(/(bc)/, addOffset)); // "abc (1) d"



// ***************** replaceAll() ****************

//Basicamente hace lo mismo que remplace() pero en lugar de remplazar un solo valor, este remplaza todas las ocurrencias.
//Cuando se utliza con RegEx es necesario que este último lleve el valor global (g) ya que de lo contrario marcará error.



// ***************** search() ****************

//Busca una ocurrencia respecto a una expresión regular. (Solo funciona con expreciones regulares)

function testinput(re, str) {
    var midstring;
    if (str.search(re) != -1) {
        midstring = " contains ";
    } else {
        midstring = " does not contain ";
    }
    console.log(str + midstring + re);
}
/* let exp = /\hola/g;
let text = "hola a todos, hola.";
testinput(exp, text); */

testinput(/\hola/g, "hola a todos, hola.");



// ***************** slice() ****************

//Extrae un trozo de una cadena, eligiendo desde que indice de inicio hasta el indice final, y crea una nueva cadena.
//desde el inicio se cuenta desde el indice 0 y el final desde el indice -1

var cadena1 = "La mañana se nos echa encima.";
var cadena2 = cadena1.slice(3, -4);
console.log(cadena2); // retorna 'mañana se nos echa enc'

var cad = "La mañana se nos echa encima.";
cad.slice(-3); // retorna 'ma.'
cad.slice(-3, -1); // retorna 'ma'
cad.slice(0, -1); // retorna 'La mañana se nos echa encima'

/* 
slice(startIndex, endIndex): Extrae desde startIndex hasta endIndex, pero sin incluir endIndex.
slice(startIndex): Extrae desde startIndex hasta el final de la cadena.
Índices negativos: Los índices negativos cuentan desde el final de la cadena hacia atrás. 
*/



// ***************** split() ****************

//Delvuelve un arreglo apartir de una cadena. Donde encuentre el separador, ahí delimita un elemento del arreglo.

//Ejemplo
function dividirCadena(cadenaADividir, separador) {
    var arrayDeCadenas = cadenaADividir.split(separador);
    console.log('<p>La cadena original es: "' + cadenaADividir + '"');
    console.log('<br>El separador es: "' + separador + '"');
    console.log("<br>El array tiene " + arrayDeCadenas.length + " elementos: ",);

    for (var i = 0; i < arrayDeCadenas.length; i++) {
        console.log(arrayDeCadenas[i] + " / ");
    }
}

var cadenaVerso = "Oh brave new world that has such people in it.";
var cadenaMeses = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec";

var espacio = " "; //donde encuentre espacio separa
var coma = ","; //donde encuentre una coma separa

dividirCadena(cadenaVerso, espacio);
dividirCadena(cadenaVerso);
dividirCadena(cadenaMeses, coma);

/*
La cadena original es: "Oh brave new world that has such people in it."
El separador es: " "
El array tiene 10 elementos: Oh / brave / new / world / that / has / such / people / in / it. /

La cadena original es: "Oh brave new world that has such people in it."
El separador es: "undefined"
El array tiene 1 elementos: Oh brave new world that has such people in it. /

La cadena original es: "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec"
El separador es: ","
El array tiene 12 elementos: Jan / Feb / Mar / Apr / May / Jun / Jul / Aug / Sep / Oct / Nov / Dec /
*/

//Ejemplo
function slplitCadena(cadenita, separadores) {
    let pruebaSplit = cadenita.split(separadores);
    console.log(pruebaSplit);
    console.log(pruebaSplit.length);
}

let cadenaSp = "Hola, muchas gracias, por estar aqui, bye."
let sepa = ",";

slplitCadena(cadenaSp, sepa);

//Ejemplo
var strt = "asdfghjkl"; // Original string
var strReverse = strt.split("") // Step 1: Split into characters
    .reverse() // Step 2: Reverse the array
    .join(""); // Step 3: Join the characters into a string

console.log(strReverse); // Output: "lkjhgfdsa"



// ***************** substring() ****************

//Devuleve un subconjunto de cadena apartir de el indice de inicio e indice fin.
//Si el indice final es mayor al indice inicial, substring lo invierte (el indice menor siempre lo toma como indice a)

var cualquierCadena = "Mozilla";

// Muestra "Moz"
console.log(cualquierCadena.substring(0, 3));
console.log(cualquierCadena.substring(3, 0));
// Muestra "lla"
console.log(cualquierCadena.substring(4, 7));
console.log(cualquierCadena.substring(7, 4));
// Muestra "Mozill"
console.log(cualquierCadena.substring(0, 6));
console.log(cualquierCadena.substring(6, 0));
//Devuelve cadena vacia porque el indiceA es igual al indiceB
console.log(cualquierCadena.substring(1, 1));
//Devuelve desde el indiceA hasta el length de la cadena. Ya queno se asigna indiceB
console.log(cualquierCadena.substring(1));

//Ejemplo
function reemplazarCadena(cadenaVieja, cadenaNueva, cadenaCompleta) {
    // Reemplaza cadenaVieja por cadenaNueva en cadenaCompleta

    for (var i = 0; i < cadenaCompleta.length; i++) {
        if (cadenaCompleta.substring(i, i + cadenaVieja.length) == cadenaVieja) {
            cadenaCompleta =
                cadenaCompleta.substring(0, i) +
                cadenaNueva +
                cadenaCompleta.substring(i + cadenaVieja.length, cadenaCompleta.length); //retorna cadena vacia
        }
    }
    console.log(cadenaCompleta)
    return cadenaCompleta;
}
reemplazarCadena("Mundo", "Web", "Bravo Nuevo Mundo");



// ***************** toLowerCase() ****************

//Si una cadena contiene caracteres en mayusculas, este método lo devulve en minusculas

let ejemploLowerUpperCase = "HOLA A TODOS mi nombre es Daniel";
console.log(ejemploLowerUpperCase.toLowerCase()); //hola a todos mi nombre es daniel



// ***************** toUpperCase() ****************

//Si una cadena contiene caracteres en minusculas, este método lo devulve en mayusculas

console.log(ejemploLowerUpperCase.toUpperCase());



// ***************** toString() ****************

// Es utilizado para convertir un objeto a su representación en forma de cadena de texto.

let tex = "Hola"
console.log(tex.toString); //"Hola"
let num = 123;
console.log(num.toString); //"123"
let arr = [1, 2, 3, 4, 5];
console.log(arr.toString()); // "1,2,3,4,5"
let obj = { a: 1, b: 2 };
console.log(obj.toString()); // "[object Object]"

//Ejemplo
function Perro(nombre, criadero, color, sexo) {
    this.nombre = nombre;
    this.criadero = criadero;
    this.color = color;
    this.sexo = sexo;
}

let elPerro = new Perro("Gabby", "Laboratorio", "chocolate", "femenino");
Perro.prototype.toString = function perroToString() {
    var retorno = `El perro ${this.nombre} es del sexo ${this.sexo}, tiene un color ${this.color} y fue criado en un ${this.criadero}`;
    return console.log(retorno);
};

console.log(elPerro.toString());
// El perro Gabby es del sexo femenino, tiene un color chocolate y fue criado en un Laboratorio          undefined



// ***************** trim() ****************

//Elimina los espacios de ambos extremos de una cadena
let ejemploTrim = "       Cadena de ejemplo con trim       "
console.log(ejemploTrim.trim());

//Ejemplo
let jaja = `Elimina los espacios de ejemlo trim, ${ejemploTrim.trim()}, al final tambien lo elimina.`;
console.log(jaja);



// ***************** trimStart() ****************

//Elimina los espacios que estén solo al inicio de una cadena
console.log(ejemploTrim.trimStart());



// ***************** trimEnd() ****************

//Elimina los espacios que estén solo al final de una cadena
console.log(ejemploTrim.trimEnd());



// ***************** valueOf() ****************

//Delvuelve el valor primitivo de un objeto string

cadena = new String("Hello world");
console.log(cadena.valueOf()); // Displays "Hello world"

//Practicamente con las cadenas de texto es lo mismo que colocar
console.log(cadena.toString());



// ******************* [Symbol.iterator](); *******************

/* 
La propiedad [Symbol.iterator] permite definir el comportamiento de iteración de un objeto. 
Cuando un objeto tiene una propiedad [Symbol.iterator], puede ser utilizado en contextos que esperan un iterable, 
como en los bucles for...of, el operador de propagación (...), y métodos como Array.from.
*/

const strg = "The quick red fox jumped over the lazy dog's back.";

const iterator = strg[Symbol.iterator]();
let theChar = iterator.next();

while (!theChar.done && theChar.value !== '') {
    console.log(theChar.value);
    theChar = iterator.next();
    // Expected output: "T"
    //                  "h"
    //                  "e"
}

//Ejemplo Manual
const strig = "Daniel Martinez";
const strIter = strig[Symbol.iterator]();

console.log(strIter.next().value); // "D"
console.log(strIter.next().value); // "a"
console.log(strIter.next().value); // "n"


/* 
DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas 
 * */

// Palindromos
function palindromo(firstWord) {
    let deleteSpace = firstWord.toLowerCase().split(' ').join('');
    let arrayWord = Array.from(deleteSpace).toReversed().join('');
    let result = arrayWord === deleteSpace ? `${firstWord} es un palindromo` : `${firstWord} no es un palindromo`;
    console.log(result);
}
palindromo("ANITA LAVA LA TINA");

// Anagramas
function anagrama(secondWord, thirdWord) {
    let arraySecondWord = secondWord.split('').sort((a, b) => a.localeCompare(b));
    arraySecondWord = arraySecondWord.join('').toLowerCase();
    let arrayThirWord = thirdWord.split('').sort((a, b) => a.localeCompare(b));
    arrayThirWord = arrayThirWord.join('').toLowerCase();
    let result = arraySecondWord === arrayThirWord
        ? `La palabras ${secondWord} y ${thirdWord}, son anagramas`
        : `La palabras ${secondWord} y ${thirdWord}, no son anagramas`;
    console.log(result);
}
anagrama("Daniel", "DANIEL");

// Isogramas
function isograma(fourthWord) {
    let arrayIsograma = fourthWord.toLowerCase().split('').join('');
    let textSet = new Set(arrayIsograma);

    const array = [];
    textSet.forEach(v => array.push(v));
    let emptyArray = array.join('');
    if (arrayIsograma === emptyArray) {
        console.log(`${fourthWord} es un Isograma`);
    } else {
        console.log(`${fourthWord} no es un Isograma`);
    }
}
isograma("Murcielago");
