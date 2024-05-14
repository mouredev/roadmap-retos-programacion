const string = 'ferrocarril';
const regex = /roca/;
const resultado = regex.test(string);
const ocurrencia = string.match(regex)
const someText = 'El siguiente número primo es el 11, por lo que tachamos todos los múltiplos de 11, que son el 22, 33, 44, 55, 66, 77, 88, y el 99.';
const matchNum = /\d{2,}/g;

/* console.log(resultado);
console.log(ocurrencia[0]);
console.log(someText.match(matchNum));
 */
//Extra

const mail = 'angelenarvaezm@gmail.com';
const regexMail = /\w+([.][\w]+)*@\w+([.][\w]+)*\.[a-zA-Z]{2,5}/;
console.log(regexMail.test(mail));
/* Debo buscar prohibir espacios \s */

/* Validaciín url */
const regexUrl = /^w{3}\.[a-zA-Z_.]{1,14}\.(com|org)$/;