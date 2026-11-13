/* 
#04 Cadenas de caracteres
*/

let string1 = "Jose" //Declaracion
let phrase = "como estas " + string1 + "!" //Concatenacion
string1 = 'Ernesto'  //Declaracion con comillas simples
let phrase2 = `No te vayas ${string1}!` //interpolacion de strings con comilla  
console.log(phrase)
console.log(phrase2)
const string2 = new String('Otra declaracion de strings')
console.log(string2)

console.log(`Longitud del string: ${phrase2.length}`) //longitud o tamaño de un string
console.log('Caracter de la posicion 5 del string: ' + string2[5]) //obtener el valor individual en una posicion de un string
console.log('Caracter de la posicion 18 del string: ' + string2[18])
 
console.log("Conversion a mayusculas del string: " + string2.toUpperCase())
console.log("Conversion a minusculas del string: " + string2.toLowerCase())

console.log(`Indice de la palabra 'vayas': ${phrase2.indexOf('vayas')}`) //obtencion del indice de la palabra que se busque
console.log(`Indice de la letra 't': ${phrase2.indexOf('t')}`) // sirve para letras sueltas tambien
console.log(`Indice de la letra 'gol': ${phrase2.indexOf('gol')}`) // devuelve -1 si no encuentra nada

console.log('Includes para palabras' + phrase.includes('Jose')) //Para verificar que una palabra si existe en el string
console.log('Includes para letras ' + phrase.includes('m')) //Tambien sirve solo para letra suelta
console.log(phrase.includes('Bien')) //Devuelve false si no existe

console.log(phrase2.slice(0, 12)) // Seccionar, agarra una porcion del string basado en los indices que se pasan como argumentos, el inicio y el final
console.log(phrase2.replace('vayas', 'golpees')) //reemplazar el primer argumento que se le pasa por el segundo en caso que exista

console.log(phrase2.split('')) //Una especie de separador que devuelve un array de los valores separados basados en el criterio del argumento que se pase
console.log(phrase2.split(' ')) 
console.log(phrase2.split(',')) // al no haber comas en el texto no lo separa por ese criterio y es uno solo

console.log(phrase.repeat(3)) // con este metodo se repite el string las veces que especifiques en el argumento

//Recorrido
for(let i = 0; i<phrase.length; i++){
    console.log(phrase[i])
}

/*
Extra
DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
*/

let wordsArray = ['Reconocer', 'Roma']

function isPalindromo(word){
    let sanitizeWord = word.toLowerCase()
    let result;
    let lengthWord = word.length - 1
    let cont = 0
    for(let i=0; i<=lengthWord; i++){
        if (sanitizeWord[i] !== sanitizeWord[lengthWord-i]){
            result = `Esta palabra ${word} no es un palindromo` 
            return result
        }
        cont++
        break
    }
    return result = `${word}: Es Palindromo`
}

function areAnagramas(word1, word2){
    if (word1.length !== word2.length){
        return 'Estas palabras no son anagramas por que no miden lo mismo'
    }
    let word1Sanitize = word1.toLowerCase()
    let word2Sanitize = word2.toLowerCase()
    let letterFrecuencyWord1 = new Map()
    let letterFrecuencyWord2 = new Map()
    for(let i = 0; i<=word1Sanitize.length - 1; i++){
        letterFrecuencyWord1.has(word1Sanitize[i]) ? letterFrecuencyWord1.set(`${word1Sanitize[i]}`, letterFrecuencyWord1.get(word1Sanitize[i]) + 1) : letterFrecuencyWord1.set(`${word1Sanitize[i]}`, 1)
    }
    for(let i = 0; i<=word2Sanitize.length - 1; i++){
        letterFrecuencyWord2.has(word2Sanitize[i]) ? letterFrecuencyWord2.set(`${word2Sanitize[i]}`, letterFrecuencyWord2.get(word2Sanitize[i]) + 1) : letterFrecuencyWord2.set(`${word2Sanitize[i]}`, 1)
    }
    for (let clave of letterFrecuencyWord1.keys()){
        if (!(letterFrecuencyWord2.has(clave)) || !(letterFrecuencyWord1.get(clave) == letterFrecuencyWord2.get(clave))){
            return `Estas palabras: ${word1} y ${word2} no son anagramas`
        }
    }
    return `Estas palabras ${word1} y ${word2} si son anagramas`
}

function isIsograma(word) {
    let lettersArray = word.split('');
    let wordSet = new Set(lettersArray);
    let isogramaResult
    if (lettersArray.length !== wordSet.size){
        return isogramaResult = `${word} Esto no es un isograma`
    }
    return isogramaResult = `${word} Esto es un isograma`
}

function analyzeWord(words) {
    for (let i = 0; i<=words.length-1; i++){
        let esPalindromo = isPalindromo(words[i]);
        console.log(esPalindromo)
        if (words[i + 1] == undefined){
            console.log(`Recorrido ${i}, No hay otra palabra mas para analizar la actual y ver si son anagramas`)
        } else {
            let sonAnagramas = areAnagramas(words[i], words[i+1])
            console.log(sonAnagramas)
        }
        let esIsograma = isIsograma(words[i])
        console.log(esIsograma)
    }
}

analyzeWord(wordsArray)
