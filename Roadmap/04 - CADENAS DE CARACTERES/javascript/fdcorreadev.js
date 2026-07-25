console.log("Cadena de caracteres")

console.log("-----------------------------------------------------------start--------------------------------------------------")
console.log("1. Formas de declara cadenas de caracteres")
const text1 = "Una cadena primitiva"
const text2 = 'Otra cadena primitiva'
const text3 = `Otra cadena primitiva`
const text4 = new String("Un bojeto String")


console.log("2. formas de obtener numeros caracteres")

console.log("cat".charAt(1))
console.log("cat"[1])
console.log("cat"[0])

console.log("3. manejo de string mayucula, minuscula")
console.log("hola".toUpperCase())
console.log("HOLA".toLowerCase())


console.log("4. concatenacion y separacion de caracteres")
const concat = 4
console.log(`con estas comillas podemos concatenar el valor ${concat}`)


const splitText = text1.split(' ')
console.log(splitText)
console.log(splitText[0] + " " + splitText[1] + " " + splitText[2])
console.log(splitText.join(" "))


console.log("5. verificacion de tipos para recorrerlos")
let s_prim = "foo";
let s_obj = new String(s_prim);

console.log(typeof s_prim); // Registra "string"
console.log(typeof s_obj); // Registra "object"

// tener cuidado con eval para operaciones

let s1 = "2 + 2"; // crea una string primitiva
let s2 = new String("2 + 2"); // crea un objeto String
console.log(eval(s1)); // devuelve el número 4
console.log(eval(s2)); // devuelve la cadena "2 + 2 es un Object se trata diferentre
// para que devuelva el mismo resultado debemos utilizar valueOF

console.log(eval(s2.valueOf()))

console.log("6. propiedade de las cadenas de caracteres")

console.log("hola".length)
console.log("Hola".replace("H", "h"))
console.log("hola".substring(1, 3))
console.log("hola".includes("o"))
//esta propiedad de indexOf si encuentra genera la posicion empezando del 0 pero si no encuentra lanza -1
console.log("hola".indexOf("f"))
console.log("hola".indexOf("l"))
console.log("hola".slice(1, 3))


console.log("-----------------------------------------------------------------------end-----------------------------------------------------------")

console.log("-----------------------------------------------------------------Dificultad extra------------------------------------------------------")

function verifyPalindromeWord(text){
    const textReverse = text.split('').reverse().join('')
    let isPalindrome = text === textReverse ? true : false
    let response
    
    if(isPalindrome){
        response = `La palabra ${text} es palindromo`
    } else {
        response = `La palabra ${text} no es palindromo`
    }

    return response
}

console.log("-------------------------------Palindromo--------------------------------------------------")
let word = "ana"
const res = verifyPalindromeWord(word)
console.log(res)


function verifyAnagramsWords(word, compareWord){
    const cleanWord = word.toLowerCase().replace(/[^a-z0-9]/g, '');
    const cleanCompareWord = compareWord.toLowerCase().replace(/[^a-z0-9]/g, '');
    let result

    if(cleanWord.length !== cleanCompareWord.length){
        result = 'No es Anagrama'
    }

    const ordenWord =  cleanWord.split('').sort().join('')
    const ordenCompareWord =  cleanCompareWord.split('').sort().join('')

    result = ordenWord === ordenCompareWord ? 'Es un Anagrama' : 'No es anagrame'

    return result
}

console.log("-------------------------------Anagramas--------------------------------------------------")
const resultAnagrams = verifyAnagramsWords("Debit card", "Bad credit")
console.log(resultAnagrams)

function verifyIsogramasWord(word){
    const splitWord = word.split('')
    const apariciones  = splitWord.filter(function (caracterActual,  indice, arreglo){
        const primerIndice = arreglo.indexOf(caracterActual)
        const esRepeticion = primerIndice !== indice
        return esRepeticion
    })
    let result
    if(!apariciones.length > 0){
        result = 'Es un isograma'
    } else {
        result = 'No es isograma'
    }
    
    return result
}
console.log("-------------------------------isograma--------------------------------------------------")
const resultIsogramas = verifyIsogramasWord('murcielago')
console.log(resultIsogramas)