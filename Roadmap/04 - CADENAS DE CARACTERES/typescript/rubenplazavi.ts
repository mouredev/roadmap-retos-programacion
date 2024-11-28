
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

/*

Los palíndromos son palabras o frases que al leerse de izquierda a derecha y viceversa dicen lo mismo

Un anagrama es una palabra que resulta de la transposición de todas las letras de otra palabra12. Puede aplicarse también a grupos de palabras o frases1. Existen dos tipos de anagramas:

Isogramas
*/

const cadenaAmigo: string = "amigo"; 
const cadenaUn = "Un";
const cadenaEres = "eres";

//! concatenar strings
const cadenaConcatenadaConSeparador: string = cadenaEres.concat("-",cadenaUn,"-").concat(cadenaAmigo);
console.log(cadenaConcatenadaConSeparador);

//Otra forma
const cadenaConcatenada2: string = `${cadenaEres}${cadenaUn}${cadenaAmigo}`;
console.log(cadenaConcatenada2);

// otra forma
const cadenaConcatenada3: string = cadenaEres + cadenaUn + cadenaAmigo;
console.log(cadenaConcatenada3);

//! Cortar Strings - //!división
//slice
const cadenaCortada: string = cadenaAmigo.slice(0, 4);
console.log(cadenaCortada);

//split
const cadenaSplit: string[] = cadenaAmigo.split("");
console.log("split(''): ", cadenaSplit);

const cadenaSplit2: string[] = cadenaConcatenadaConSeparador.split("-");
console.log(cadenaSplit2);

//! recoger length of a string
const lengthCadenaAmigo: number = cadenaAmigo.length;
console.log("longitud cadenaAmigo: ",lengthCadenaAmigo);

//! recoger caracter de un string
const caracterPosicion4: string = cadenaAmigo.charAt(3);
console.log(caracterPosicion4);

//! Pillar una subcadena de carácteres dentro de la cadena
const subcadena: string = cadenaConcatenada2.substring(4,2);
console.log("subcadena un: ",subcadena);

//! Comparar cadenas
const cadenaIgualValorQueAmigo: string = "amigo";

console.log(`comparacion: ${cadenaIgualValorQueAmigo} === ${cadenaAmigo}`);
cadenaIgualValorQueAmigo.match(cadenaAmigo) 
    ? console.log("son iguales") 
    : console.log("no son iguales");

console.log(`comparacion: ${cadenaIgualValorQueAmigo} === ${cadenaConcatenadaConSeparador}`);
cadenaIgualValorQueAmigo === cadenaConcatenadaConSeparador
    ? console.log("son iguales")
    : console.log("no son iguales");

//! comparar si existe una subcadena dentro de un string
const substringExists: boolean = cadenaConcatenadaConSeparador.search(cadenaAmigo) !== -1;

//! Recorrer cadenas
const CadenaMayusculas: string = cadenaAmigo.toLocaleLowerCase()
console.log("cadenaAmigo en minusculas: ",CadenaMayusculas);
cadenaAmigo.toLocaleUpperCase()
console.log("cadenaAmigo en minusculas: ",cadenaAmigo.toUpperCase());

//! Repetir string
console.log(cadenaAmigo.repeat(5)); //cadenaAmigo.repeat(5);ç

const monjaRepetida = "monja".repeat(5);
console.log(monjaRepetida);

//!reemplazo
const cadenaRemplazada: string = cadenaConcatenadaConSeparador.replace("-",'.');
console.log(`cadena antes: ${cadenaConcatenadaConSeparador}, cadenaRemplazada: ${cadenaRemplazada}`);


const palabraDividida: string = cadenaConcatenadaConSeparador.slice(0,4);
console.log("Palabra dividida", palabraDividida);

//! interpolación
const nombre: string = "Carlos";
const apellido: string = "Augusto";   
const edad: number = 30;

const mensaje: string = `Mi nombre es ${nombre}, mi apellido es ${apellido} y tengo ${edad} años.`;
console.log(mensaje);

//! verificación
console.log("cadenaAmigo.startsWith('am') --> ",cadenaAmigo.startsWith("am"));
console.log("cadenaAmigo.endsWith('rot') --> ",cadenaAmigo.endsWith("rot"));

//! Comprobar si pasa un regex
console.log("cadenaAmigo.match(/amig/) --> ",cadenaAmigo.match(/amig/)!=null);
//! Comprobar si pasa un regex
console.log("cadenaAmigo.match(/amig/) Respuesta real --> ",cadenaAmigo.match(/amig/));
//! comprobar si contiene un substring
console.log("cadenaAmigo.includes('amig') --> ",cadenaAmigo.includes("amig"));

//! recorrido
for(let i=0; i<cadenaAmigo.length; i++){
    console.log(`posicion: ${i+1} - caracter: ${cadenaAmigo[i]}`); // cadenaAmigo.charAt(i) 
}


/**
 * ------------------ Reto Extra ------------------
 * Palindromos
 * Anagramas
 * Isogramas
 */

//! Palindromos

const palindromo: string = "anilina";
const noPalindromo: string = "amigo";

// Una forma de hacerlo

let palindromoInvertido: string = "";
const ultimoIndex: number = palindromo.length -1;

for (let i = 0; i < palindromo.length; i++) {
    palindromoInvertido += palindromo[ultimoIndex - i];
}
console.log("palindromoInvertido", palindromoInvertido);
palindromoInvertido == palindromo
    ? console.log(`${palindromo} es una palabra palíndroma`)
    : console.log(`${palindromo} no es una palabra palíndroma`);


// Otra forma más directa

    palindromo.toLowerCase() === palindromo.toLowerCase().split("").reverse().join("")
    ? console.log(`${palindromo} es una palabra palíndroma`)
    : console.log(`${palindromo} no es una palabra palíndroma`);


//! Anagramas

const inglaterra: string = "inglaterra";
const integrarla: string = "integrarla";
let dobleIntegrarla = integrarla;

const inglaterraArray: Array<string> = inglaterra.split(""); //convierte el string en un array
let contador: number = 0;
if(inglaterra.length === integrarla.length){
    const length: number = inglaterraArray.length;
    for (let i = 0; i < length; i++) {
        const caracterAComparar = inglaterraArray[i];
        if(dobleIntegrarla.includes(caracterAComparar)){
            contador++;
            const index = dobleIntegrarla.indexOf(caracterAComparar);
            if(index !== -1){
                dobleIntegrarla = integrarla.slice(0, index) + integrarla.slice(index + 1);
            }
        }
    }
}
if(contador === inglaterra.length){   
    console.log(`${integrarla} es un anagrama de ${inglaterra}`);
}else{
    console.log(`${integrarla} no es un anagrama de ${inglaterra}`);
}


// Ejemplo refactorizado y optimizado:
function areAnagrams(word1: string, word2: string): boolean {
    if (word1.length !== word2.length) return false;
    const sortedWord1 = word1.toLowerCase().split("").sort().join("");
    const sortedWord2 = word2.toLowerCase().split("").sort().join("");
    return sortedWord1 === sortedWord2;
}

if (areAnagrams(inglaterra, integrarla)) {
    console.log(`${integrarla} es un anagrama de ${inglaterra}`);
} else {
    console.log(`${integrarla} no es un anagrama de ${inglaterra}`);
}


//! Isogramas