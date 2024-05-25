let re = /ab+c/;
let re1 = new RegExp("ab+c");

const paragraph = 'The quick brown fox jumps over the lazy dog. It barked. abc';
const mayus = /[A-Z]/g;
const minus = /[a-z]/g;
const found = paragraph.match(mayus);
// const found1 = paragraph.match(minus);
const found2 = paragraph.match(re1);
console.log(found)
console.log(found2)
// ejemplos

// * EJERCICIO:
// * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
// * creando una que sea capaz de encontrar y extraer todos los números
// * de un texto.
// Crea una exprecion regular
const regexnum = /[0-9]/g
function extraerNum (frase) {
    const numeros = frase.match(regexnum)
return console.log(numeros)
}

extraerNum('Este es el ejercicio 16 publicado 15/04/2024.')

// *
// * DIFICULTAD EXTRA (opcional):
// * Crea 3 expresiones regulares (a tu criterio) capaces de:
// * - Validar un email.
// * - Validar un número de teléfono.
// * - Validar una url.

const email1 = 'ejemplo@gmail.com'
const email2 = 'ejemplo@gmail.'

function ecmailCheck(email){
    const mailRegex =(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,3}$/)
    if(mailRegex.test(email))  {
        console.log('email aprobo el test')
    }else{
        console.log('email no aprobo el test')
    }
}
ecmailCheck(email1)
ecmailCheck(email2)
// ------------------------------------------------------------
const phone = '3490-8904'
const phone1 = '4141-515'

function phoneCheck( phone ){
    const phoneRegex = /([0-9]{4})-([0-9]{4})/
    if(phoneRegex.test(phone)){
       console.log( 'phone telefono valido')
    }else{
        console.log('phone no valido')
    }
}

phoneCheck(phone)

// -----------------------------------------------------------
const web = "http://www.moure.dev"
const web1 = "http://www.mouredev"

function webCheck(web){

    const webRegex = /^http\[s\]?:\/\/(www.)?[\w]+\.\[a-zA-Z\]{2,}$/;
    if(webRegex.test(web)){
        console.log('web aprobada')
    }else{
        console.log('web no aceptable' )
    }
}

webCheck(web)
webCheck(web1)