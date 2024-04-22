// EJERCICIO

const regexHasNumbers = /[0-9]/;

const text1 = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas desde el año 1500';
const text2 = 'Solo letras, sin nada de numeros';
const text3 = '1234567890-abc';

console.log("El texto \"".concat(text1, "\" tiene numeros?: "), regexHasNumbers.test(text1));
console.log("El texto \"".concat(text2, "\" tiene numeros?: "), regexHasNumbers.test(text2));
console.log("El texto \"".concat(text3, "\" tiene numeros?: "), regexHasNumbers.test(text3));


// DESAFIO EXTRA

//Regex para correos
const regexEmail = /^[\w\-\.]+@([\w]+\.)+[\w]{2,4}$/;

const email1 = 'andres.chapeton0206@gmail.com';
const email2 = 'andres@gmail';

console.log("El correo \"".concat(email1, "\" es valido?: "), regexEmail.test(email1));
console.log("El correo \"".concat(email2, "\" es valido?: "), regexEmail.test(email2));

// Regex para telefonos (Con formato 0000-0000)

const regexPhone = /([0-9]{4})-([0-9]{4})/;

const phone1 = '7777-9999';
const phone2 = '77-5555';

console.log("El telefono \"".concat(phone1, "\" es valido?: "), regexPhone.test(phone1));
console.log("El telefono \"".concat(phone2, "\" es valido?: "), regexPhone.test(phone2));

// Regex para URL (Con formato https o http)

const regexURL = /^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?$/;

const url1 = 'https://www.moure.dev';
const url2 = 'http://www.holamundo.dev';
const url3 = 'www.google.com';
const url4 = 'https://www.google';
const url5 = 'w.google';

console.log("La URL \"".concat(url1, "\" es valida?: "), regexURL.test(url1));
console.log("La URL \"".concat(url2, "\" es valida?: "), regexURL.test(url2));
console.log("La URL \"".concat(url3, "\" es valida?: "), regexURL.test(url3));
console.log("La URL \"".concat(url4, "\" es valida?: "), regexURL.test(url4));
console.log("La URL \"".concat(url5, "\" es valida?: "), regexURL.test(url5));
