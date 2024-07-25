// https://regexone.com/
// https://www.freecodecamp.org/espanol/news/expresiones-regulares-regex-en-javascript-manual-para-principiantes/

/*
  EJERCICIO:
  Utilizando tu lenguaje, explora el concepto de expresiones regulares,
  creando una que sea capaz de encontrar y extraer todos los números
  de un texto.
*/

const text = "Gundam RX-78-2";
const modifiedText = text.replace(/\d+/g, '');

console.log(`Texto inicial: ${text}`);
console.log(`Texto sin números: ${modifiedText}`);

/*
  DIFICULTAD EXTRA (opcional):
  Crea 3 expresiones regulares (a tu criterio) capaces de:
  - Validar un email.
  - Validar un número de teléfono.
  - Validar una url.
*/

const email = "raul@mail.com";
const validateEmail = /[^\s@](\.[a-z]{2,63})/

const phone = "5555089590";
const valiodatePhone = /\d{10}/;

const url = "https://raul.com.mx";
const validateURL = /(https?:\/\/)?(\.[a-z]{2,63})/;

console.log(`¿El email es válido? ${validateEmail.test(email)}`);
console.log(`¿El teléfono es válido? ${valiodatePhone.test(phone)}`);
console.log(`¿La URL es válida? ${validateURL.test(url)}`);
