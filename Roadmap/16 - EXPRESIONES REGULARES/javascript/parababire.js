const string = 'ferrocarril';
const regex = /roca/;
const resultado = regex.test(string);
const ocurrencia = string.match(regex)
const someText = 'El siguiente número primo es el 11, por lo que tachamos todos los múltiplos de 11, que son el 22, 33, 44, 55, 66, 77, 88, y el 99.';
const matchNum = /\d{2,}/g;

console.log(resultado);
console.log(ocurrencia[0]);
console.log(someText.match(matchNum));

//Extra

const mail = 'angelenarvaezm@gmail.com';
const phoneNum = '02812769886';
const url = 'www.frecodecamp.com'

/* Validación de email */
const regexMail = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/;
console.log(regexMail.test(mail));

/* Validación número de teléfono */
const regexPhone = /^0\d{10}$/;
console.log(regexPhone.test(phoneNum));

/* Validación url */
const regexUrl = /^w{3}\.[a-z_\.?]+\.(com|org)$/;
console.log(regexUrl.test(url));