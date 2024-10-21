/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

const miStr = 'Loki es mi mi perro ';
console.log(miStr.replace('mi', 'nuestro'));
console.log(miStr.replaceAll('mi', 'nuestro'));

console.log(miStr.split(' '));

const trimmed = miStr.trim().length;

console.log(`trimmed tiene length ${trimmed}, sin trimmed ${miStr.length}`);

console.log(miStr.includes('Loki'));

console.log(miStr.concat('inteligente'));

console.log(miStr.toUpperCase());

console.log(miStr.toLocaleLowerCase());

console.log(miStr.startsWith('oki', 1));

console.log(miStr.slice(1, 3));

console.log(miStr.search('/d'));

console.log(miStr.repeat(2));

console.log(miStr.padStart(30, 'relleno'));

const isPalindroma = (word) => {

    const wordArr = word.split('');
    const wordArrReverse = word.split('').reverse();

    for (let i = 0; i < wordArr.length; i++) {
        if (wordArr[i] !== wordArrReverse[i]) {
            console.log('no es palindroma');
            return;
        }
    }
    console.log('es palindroma');
}

isPalindroma('oso')

const isAnagrama = (word1, word2) => {

    const word1Arr = word1.split('').sort();
    const word2Arr = word2.split('').sort();

    for (let i = 0; i < word1Arr.length; i++) {
        if (word1Arr[i] !== word2Arr[i]) {
            console.log('no es un anagrama');
            return;
        }
    }

    console.log('es un anagrama');
}


isAnagrama('roma', 'amor');

const isIsograma = (word) => {

    const set = new Set();

    for (letter in word) {
        if (set.has(letter)) {
            console.log('no es un isograma');
            return;
        } else {
            set.add(letter);
        }
    }

    console.log('es un isograma');
}

isIsograma('murcielago');

