/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
*/

// Concatenation
// Used + or concat()
let string = 'Hello,';
let string2 = ' world!';
console.log(string + string2); // Hello, world!
console.log(string.concat(string2)); // Hello, world!

// String length
let stringLength = 'Good Morning!';
console.log(stringLength.length); // 13

// Slice String
// slice assign number for start 0 (include) and number for the finish (exclude)
let sliceExample = 'Do you go to the park?'
console.log(sliceExample.slice(0, 7)); // Do you

// Index Of
// Index of give you index where start the word.
let indexOfExample = 'My mom went shopping at Wallmart';
console.log(indexOfExample.indexOf('went')); // 7

// Split
// Split process the string and return a array with de words separated for an any character that you choose.
let splitExample = 'Hi,how,are,you';
console.log(splitExample.split(',')); // [ 'Hi', 'how', 'are', 'you' ]

// Replace
// Replace, search in the string the word that you give and replace for another one you give.
let replaceExample = 'on my way';
console.log(replaceExample.replace('way', 'table')); // on my table

// toUpperCase() / toLowerCase()
let exampleUpperLowerCase = 'She is a big woman.'
console.log(exampleUpperLowerCase.toLowerCase()); // she is a big woman.
console.log(exampleUpperLowerCase.toUpperCase()); // SHE IS A BIG WOMAN.

// charAt: Return index from a string
// this method init on 0
let exampleCharAt = 'Hello';
console.log(exampleCharAt.charAt(0)); // H

// Trim
// This method erase blanks on the start and finish from a string.
let exampleTrim = '     Hellow     ';
console.log(exampleTrim.trim()); // 'Hellow'

// Repeat
// This method repeats the text on a string any many times as you indicate.
console.log(exampleCharAt.repeat(5)); // HelloHelloHelloHelloHello


// endsWith/ startsWith
console.log(exampleCharAt.startsWith('H')); // True
console.log(exampleCharAt.endsWith('a')); // False

// includes
// This method verify if the string contain the word thar you indicate.
// is case sensitive
console.log(exampleCharAt.includes('Hello')); // True

/*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
*/

// Importamos elmódulo 'readline' de Node.js para poder recuperar los datos de terminal
const readline = require('readline');

// Interfaz de lectura
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

function readTerminal(){
    rl.question('Elije la opción deseada:\n1: Verificar si es palindromo\n2: Verificar si es un anagrama\n3: Verificar si es un isograma\n0: Salir\n ', (opcion) => {
        if(opcion === '0'){
            console.log('Se ha terminado la ejecución!')
            rl.close();
            process.exit(0);
        } else if(opcion > 0 && opcion < 4){
            opciones(opcion);
        } else {

        }
    })
}

// Options
function opciones(option){
        switch (option) {
        case '1':
            console.log('opcion 1!!!!');
            palindromo();
            break;
        case '2':
            anagrama();
            break;
        case '3':
            isograma();
            break;
    }
}


// Funcion Palíndromo
function palindromo(){
    rl.question('Ingrese la palabra a evaluar: ', palabra => {
        let reverseWord = [];
        let palabraArray = palabra.split('')
        for(let i = 0; i < palabraArray.length; i++){
            reverseWord.unshift(palabraArray[i]);

        }
        let str = reverseWord.join('');
        (str === palabra) ? console.log('- - - - - - - - - - -\nEs palindromo!\n- - - - - - - - - -') : console.log('- - - - - - - - - - -\nNo es palindromo!\n- - - - - - - - - -');
        readTerminal();
    })
}

function anagrama(){
    rl.question('Ingrese la primera palabra a comparar: ', palabra1 => {
        rl.question('Ingrese la segunda palabra a comparar: ', palabra2 => {
            let str = palabra1.split('').sort().join();
            let str2 = palabra2.split('').sort().join();
                if(str === str2){
                    console.log('- - - - - - - - \n Es un anagrama!\n- - - - - - -'); 
                } else {
                    console.log('- - - - - - - - \n No es anagrama!\n- - - - - - -');
                    readTerminal();
                }
            readTerminal();         
        })
})};

function isograma(){
    let isIso = true;
    rl.question('Ingrese la palabra para verificar si es un isograma: ', palabra => {
        let str = palabra.split('').sort();
        for(let i = 1; i <= str.length; i++){
            if(str[i-1] === str[i]){
                console.log('- - - - - - - - - - -\nNo es un isograma!\n- - - - - - - - - - -')
                isIso = false;
                break;
            }
        }
        if(isIso){
        console.log('- - - - - - - - - - -\nEs un isograma :D!\n- - - - - - - - - - -');
        }
        readTerminal();
    })
}

readTerminal();