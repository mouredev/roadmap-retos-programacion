
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

const cadenaBotarate = "botarate"; 
const cadenaUn = "Un";
const cadenaEres = "eres";

const cadenaIgualValorQueBotarate = "botarate";


//! concatenar strings
const cadenaConcatenada = cadenaEres.concat("-",cadenaUn,"-").concat(cadenaBotarate);
console.log(cadenaConcatenada);

//Otra forma
const cadenaConcatenada2 = `${cadenaEres}${cadenaUn}${cadenaBotarate}`;
console.log(cadenaConcatenada2);

// otra forma
const cadenaConcatenada3 = cadenaEres + cadenaUn + cadenaBotarate;
console.log(cadenaConcatenada3);

//! Cortar Strings
//slice
const cadenaCortada = cadenaBotarate.slice(0, 4);
console.log(cadenaCortada);

//split
const cadenaSplit = cadenaBotarate.split("");
console.log(cadenaSplit);
