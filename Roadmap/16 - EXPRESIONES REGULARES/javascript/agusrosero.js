/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 */
const text = "H0L4 QU3 T4L";
const myRe = /\d+/g;
console.log(text.match(myRe));

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

// Validar un email.
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const email = "test@email.com";
console.log(emailRegex.test(email));

// Validar un número de teléfono.
const phoneRegex =
  /^\+?(\d{1,3})?[-.\s]?(\(?\d{3}\)?)?[-.\s]?\d{3}[-.\s]?\d{4}$/;
const phone = "+54 341 3777777";
console.log(phoneRegex.test(phone));

// Validar una url.
const urlRegex = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$/;
const url = "https://www.google.com";
console.log(urlRegex.test(url));
