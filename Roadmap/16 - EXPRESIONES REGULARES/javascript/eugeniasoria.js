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

function extraerNumerosDeTexto(texto) {
  let result = '';
  result = texto.match(/\d/g);
  return result;
}

let miTexto = 'Este texto 1 puede tener algu3nos numeros 0 en el medio99';
console.log(miTexto);
let numeros = extraerNumerosDeTexto(miTexto);
console.log("Numeros encontrados:", numeros.join(', '));


function emailEsValido(email) {
   const expRegEmail = new RegExp(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/);
  let evaluado = expRegEmail.exec(email);  
  return evaluado === null ? false : true;  
}

let email ='miemail123%valido@gmail.com';
let emailNoValido = 'culTTmail@@quenoPuedeser.com.com@'

console.log(`El email ${email} es válido? : ${emailEsValido(email)}`);
console.log(`El email ${emailNoValido} es válido? : ${emailEsValido(emailNoValido)}`);


function telefonoEsValido(numeroTelefono) {
  const expRegEmail = new RegExp(/^\+[0-9]+[\s0-9]*$/);
  let evaluado = expRegEmail.exec(numeroTelefono);  
  return evaluado === null ? false : true;  
}

let telefono ='+598 85 69856325';
let telefonoNoValido = '- 852 A45892'

console.log(`El telefono ${telefono} es válido? : ${telefonoEsValido(telefono)}`);
console.log(`El telefono ${telefonoNoValido} es válido? : ${telefonoEsValido(telefonoNoValido)}`);



function urlEsValida(url) {
  const expRegEmail = new RegExp(/^[a-zA-Z0-9-_.~:\/]*$/);
  let evaluado = expRegEmail.exec(url);  
  return evaluado === null ? false : true;  
}

let url ='https://miviejayquerida.url.com/subcarpeta/contenido.com.uy';
let urlNoValida = 'xyh((((65555%%%%%'

console.log(`La url ${url} es válida? : ${urlEsValida(url)}`);
console.log(`La url ${urlNoValida} es válida? : ${urlEsValida(urlNoValida)}`);