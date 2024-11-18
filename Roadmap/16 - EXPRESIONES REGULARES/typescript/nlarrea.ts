/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */


const getNumbersFromText = (text: string): string[] | null => {
    const regExp = /\d{1,}/g
    return text.match(regExp)
}


const longText = `
Lorem ipsum dolor1 sit amet, consectetur adipiscing elit. Nullam ac mi in
ipsum ultricies 2 varius. Nullam euismod, justo nec fermentum ultricies, nunc
nisl tempus purus, 3 sed dictum 563 nulla odio nec purus. Nullam nec purus
consectetur, consectetur justo. 10 Nullam nec purus consectetur, consectetur.
`
getNumbersFromText(longText)  // ['1', '2', '3', '563', '10']


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */


function printTests(pattern: RegExp, text: string): void {
    const result: RegExpMatchArray | null = text.match(pattern)

    console.log(`${text}: ${(result?.length ?? 0) > 0}`)
}


// Validar un email

const checkEmailPattern: RegExp = /^[\w]{1,}[\w\d\._]{4,}\@[\w]{2,}\.[\w]{2,3}$/g
console.log('\nTesting emails:')
printTests(checkEmailPattern, 'an_email@gmail.com')  // true
printTests(checkEmailPattern, '1234@email.com')  // false
printTests(checkEmailPattern, 'an_email1234')  // false
printTests(checkEmailPattern, 'an2_email4@gmail.com')  // true
printTests(checkEmailPattern, 'another.2024@gmail')  // false
printTests(checkEmailPattern, 'another.2024@gmail.')  // false
printTests(checkEmailPattern, 'another.2024@gmail.com')  // true

// Validar un número de teléfono

const checkPhonePattern: RegExp = /^\+?\d{3,}$/g
console.log('\nTesting phone numbers:')
printTests(checkPhonePattern, '123456789')  // true
printTests(checkPhonePattern, '+34123456789')  // true
printTests(checkPhonePattern, 'abcdefghi')  // false

// Validar una url

const checkUrlPattern: RegExp = /^https?:\/\/(w{3}\.)?[\w\d\.\-\?]+\.[\w]{2,}\/?$/g
console.log('\nTesting URLs:')
printTests(checkUrlPattern, 'https://github.com/')  // true
printTests(checkUrlPattern, 'https://www.twitch.tv')  // true