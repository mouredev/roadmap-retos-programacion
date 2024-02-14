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

// Acceso a caracteres específicos
let string = 'Oleojake dev';
console.log(string[6]); // k

// Subcadenas
console.log(string.substring(0, 8)); // Oleojake

// Longitud
console.log(string.length); // 12

// Concatenación
let concatenated = string + ' 1993'; 
console.log(concatenated); // Oleojake dev 1993

// Repetición
let repeated = string.repeat(2);
console.log(repeated); // Oleojake devOleojake dev

// Recorrido
for (let i = 0; i < string.length; i++) {
    console.log(string[i]);
}

// Conversión a mayúsculas
console.log(string.toUpperCase()); // OLEOJAKE DEV

// Conversión a minúsculas
console.log(string.toLowerCase()); // oleojake dev

// Reemplazo
let replaced = string.replace('dev', 'DEVELOPER');
console.log(replaced); // Oleojake DEVELOPER

// División
let split = string.split(' ');
console.log(split);

// Unión
let joined = split.join(', ');
console.log(joined);

// Interpolación
let name = 'Oleojake';
let interpolated = `Hola, ${name}`;
console.log(interpolated);

// Verificación (includes)
console.log(string.includes('dev')); // true

// Reverse
console.log(string.toLowerCase().split('').reverse().join(''));


// EJERCICIO EXTRA

function checkPalindromo (word){
    
    return word.toLowerCase() === word.toLowerCase().split('').reverse().join('');

    /* RESOLUCIÓN CON RECORRIDO
    let len = Math.floor(word.length / 2);
    for(let i=0;i<len;i++){
        if(word[i] != word[word.length-i-1]){
            return false;
        }
    }
    return true;
    */

}

function checkAnagrama (word1, word2){
    
    return word1.toLowerCase().split('').sort().join('') === word2.toLowerCase().split('').sort().join('')

}

function checkIsograma (word){
    
    let myMap = new Map;

    for(let i = 0; i < word.length; i++){
        if(myMap.has(word[i])){
            myMap.set(word[i], myMap.get(word[i]) + 1);
        }
        else{
            myMap.set(word[i], 1); 
        }
    }

    let compare = myMap.get(word[0]);
    for (let amount of myMap.values()) {
        if(compare != amount){
            return false;
        }
    }

    return true;

}

function check (word1,word2){

    // Palíndromo
    console.log("¿La palabra " + word1 + " es palíndromo?: " + checkPalindromo(word1));
    console.log("¿La palabra " + word2 + " es palíndromo?: " + checkPalindromo(word2));

    // Anagramas
    console.log("Las palabras " + word1 + " y " + word2 + " son Anagramas?: " + checkAnagrama(word1,word2));

    // Isograma
    console.log("¿La palabra " + word1 + " es un Isograma?: " + checkIsograma(word1));
    console.log("¿La palabra " + word2 + " es un Isograma?: " + checkIsograma(word2));

}

check("radrad", "radar")