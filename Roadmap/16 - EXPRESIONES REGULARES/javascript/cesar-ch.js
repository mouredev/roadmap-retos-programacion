/*
 * #16 EXPRESIONES REGULARES
*/

const texto = "Es texto contiene 5 numeros del 1 al 5: 1,2,3,4,5"
const regexNumeros = /\d+/g
console.log("Numeros encontrados: " + texto.match(regexNumeros))


/*
 * DIFICULTAD EXTRA 
*/

const emailCorrecto = "abc@mail.com"
const emailIncorrecto = "abcmail.com"
const regexEmail = /^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/

console.log(`${emailCorrecto} es un email valido? ` + regexEmail.test(emailCorrecto))
console.log(`${emailIncorrecto} es un email valido? ` + regexEmail.test(emailIncorrecto))

const numeroCorrecto = "+51 987654321"
const numeroIncorrecto = "987654321"
const regexNumero = /^\+[0-9]{2}\s[0-9]{9}$/

console.log(`${numeroCorrecto} es un numero valido? ` + regexNumero.test(numeroCorrecto))
console.log(`${numeroIncorrecto} es un numero valido? ` + regexNumero.test(numeroIncorrecto))


const urlCorrecta = "https://retosdeprogramacion.com"
const urlIncorrecta = "retosdeprogramacion.com/"
const regexUrl = /^https?:\/\/(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$/

console.log(`${urlCorrecta} es una url valida? ` + regexUrl.test(urlCorrecta))
console.log(`${urlIncorrecta} es una url valida? ` + regexUrl.test(urlIncorrecta))