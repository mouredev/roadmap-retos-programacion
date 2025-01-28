/*
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*/
const operationString = 'Hello world';
const supportString = 'Javascript!';

console.log('Original string: ' + operationString);
console.log('Access to second character: ' + operationString[1]);               // Accesing an specific character
console.log('Verifying the existence of a substring: ', operationString.includes('world'))  // Finding a substring
console.log('Getting the substring index: ', operationString.indexOf('world')); // Finding the index of a substring
console.log('Extracting a substring: ', operationString.slice(-5));             // Extracting a substring
console.log('String lenght is: ' + operationString.length);                     // Length of a string
console.log('Concatenated string: ' + `${operationString} - ${supportString}`); // Concatenating strings
console.log('Repeat a string: ', supportString.repeat(2));                      // Repeating a string
console.log('Convert to upper case: ', supportString.toUpperCase());            // Converting to upper cas
console.log('Convert to lower case: ', supportString.toLowerCase());            // Converting to lower case
console.log('Replacing a substring: ', operationString.replace('world', supportString));    // Replacing a substring with other substring
console.log('Spliting a string: ', operationString.split(' '));                 // Spliting a string
console.log(`Interpolating a string in ${supportString}`);                      // Interpolating a string
console.log('Using scape characters:\n', operationString);                      // Scape characters
// Iterating a string
for (i in supportString) {
    console.log(supportString[i]);
}

/*
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
*/

function preProcess(userText) {
    let lowerCaseString = userText.toLowerCase();
    let originalString = lowerCaseString.split(' ').join('');
    return originalString.split('');
}

function isPalindrome(userText) {
    let lowerCaseString = userText.toLowerCase();
    let originalString = lowerCaseString.split(' ').join('');
    let splitArray = originalString.split('');
    let reversedString = splitArray.reverse().join('');
    
    if (reversedString == originalString) {
        console.log(`The text "${userText}" is palindrome`);
        return true;
    }
    else {
        console.log(`The text "${userText}" is not a palindrome`);
        return false;
    }
}

function isAnagram(firstText, secondText) {
    let firstTextArray = preProcess(firstText);
    let secondTextArray = preProcess(secondText);

    if (firstTextArray.sort().join('') === secondTextArray.sort().join('')) {
        console.log(`The texts "${firstText}" and "${secondText}" are anagrams`);
        return true;
    }
    else {
        console.log(`The texts "${firstText}" and "${secondText}" are not anagrams`);
        return false;
    }

}

function isIsogram(userText) {
    let userTextArray = preProcess(userText);
    
    let evaluationSet = new Set();
    userTextArray.forEach(element => {
        evaluationSet.add(element);
    });
    evaluationArray = Array.from(evaluationSet);
    if (userTextArray.join('') === evaluationArray.join('')) {
        console.log(`The text "${userText}" is an isogram`);
        return true;
    }
    else {
        console.log(`The text "${userText}" is not an isogram`);
        return false;
    }

}

console.log('----- Palindrome -----')
isPalindrome('Hello Javascript');
isPalindrome('Nurses run');
console.log('----- Anagrams -----');
isAnagram('Javascript', 'Cinema');
isAnagram('iceman', 'Cinema');
console.log('----- Isogram -----');
isIsogram('Javascript');
isIsogram('Lumberjacks');
