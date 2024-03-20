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
 * - Palíndromos: un palíndromo se lee igual de izquierda a derecha
 * - Anagramas: dos palabras son anagramas si tienen las mismas letras 
 * - Isogramas: palabra en la que no hay letras repetidas
 */

// check Palindromo
console.log('------------------------------------- PALINDROMO -----------------------------------------');
const checkPalindromo = (palabra1, palabra2) => {
    const palabraInvertida = palabra1.split('').reverse().join('');
    return console.log((palabra2 === palabraInvertida) ? 
        `${palabra1} y ${palabra2} son palíndromos.` : `${palabra1} y ${palabra2} no son palíndromos.`);
}

checkPalindromo("amor", "roma");
checkPalindromo('Ana', 'Ana');
checkPalindromo('cama', 'ssdad');
checkPalindromo('rapar', 'romparaa');

console.log('------------------------------------- ANAGRAMA -----------------------------------------');
// check Anagram
const checkAnagrama = (palabra1, palabra2) => {
    let isAnagrama = false;
    for (let i = 0; i < palabra1.length ; i++) {
        for (let j = 0; j < palabra2.length; j++) {
            const checkIso = (palabra1, palabra2) => {
                (palabra1[i] === palabra2[j]) ? isAnagrama = true : isAnagrama = false;
            }
            checkIso(palabra1, palabra2);
        }
    }
    return console.log((isAnagrama === true) ? `${palabra1} y ${palabra2} son anagramas` : 'No son anagramas');
}

checkAnagrama('llenaba', 'ballena');
checkAnagrama('salame', 'melase');

console.log('--------------------------------------- ISOGRAMAS --------------------------------------------');
// check Isogramas
const checkIsograma = (palabra1, palabra2) => {
    const checkLetters = (palabra) => {
        let letrasVistas = {};
        for (let i = 0; i < palabra.length; i++) {
            const letra = palabra[i];
            if (letrasVistas[letra]) {
                return false;
            }
            letrasVistas[letra] = true;
        }
        return true; 
    };

    console.log(checkLetters(palabra1) ? `${palabra1} es un isograma` : `${palabra1} no es un isograma`);
    console.log(checkLetters(palabra2) ? `${palabra2} es un isograma` : `${palabra2} no es un isograma`);
};

checkIsograma('Nicolas', 'Nicole');
checkIsograma('Andres', 'Caca');
