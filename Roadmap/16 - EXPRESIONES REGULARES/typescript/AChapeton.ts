// EJERCICIO

const regexHasNumbers: RegExp = /[0-9]/

const text1: string = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas desde el año 1500'
const text2: string = 'Solo letras, sin nada de numeros'

const text3: string = '1234567890-abc'

console.log(`El texto "${text1}" tiene numeros?: `, regexHasNumbers.test(text1))
console.log(`El texto "${text2}" tiene numeros?: `,regexHasNumbers.test(text2))
console.log(`El texto "${text3}" tiene numeros?: `,regexHasNumbers.test(text3))

// DESAFIO EXTRA

//Regex para correos
const regexEmail: RegExp = /^[\w\-\.]+@([\w]+\.)+[\w]{2,4}$/

const email1: string = 'andres.chapeton0206@gmail.com'
const email2: string = 'andres@gmail'

console.log(`El correo "${email1}" es valido?: `, regexEmail.test(email1))
console.log(`El correo "${email2}" es valido?: `, regexEmail.test(email2))


// Regex para telefonos (Con formato 0000-0000)

const regexPhone: RegExp = /([0-9]{4})-([0-9]{4})/

const phone1: string = '7777-9999'
const phone2: string = '77-5555'

console.log(`El telefono "${phone1}" es valido?: `, regexPhone.test(phone1))
console.log(`El telefono "${phone2}" es valido?: `, regexPhone.test(phone2))


// Regex para URL (Con formato https o http)

const regexURL: RegExp = /^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?$/

const url1: string = 'https://www.moure.dev'
const url2: string = 'http://www.holamundo.dev'
const url3: string = 'www.google.com'
const url4: string = 'https://www.google'
const url5: string = 'w.google'

console.log(`La URL "${url1}" es valida?: `, regexURL.test(url1))
console.log(`La URL "${url2}" es valida?: `, regexURL.test(url2))
console.log(`La URL "${url3}" es valida?: `, regexURL.test(url3))
console.log(`La URL "${url4}" es valida?: `, regexURL.test(url4))
console.log(`La URL "${url5}" es valida?: `, regexURL.test(url5))