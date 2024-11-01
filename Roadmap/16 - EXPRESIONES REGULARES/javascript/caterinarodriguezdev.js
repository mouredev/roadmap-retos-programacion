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

const textoConNumeros = "El universo es un vasto y enigmático lugar que se estima tiene alrededor de 13.800 millones de años de antigüedad. Contiene más de 2 billones de galaxias, cada una con miles de millones de estrellas; por ejemplo, nuestra propia galaxia, la Vía Láctea, alberga aproximadamente 100.000 millones de estrellas.";

const todosLosDigitos = /\d/g;
const digitos = textoConNumeros.match(todosLosDigitos);
console.log(digitos);

const email = "a@a.com";
const regexEmail = /^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$/;
console.log(regexEmail.test(email) ? 'email válido' : 'email no válido');

const url = "https://google.com";
const regexUrl = /^(https?:\/\/)[a-z]+\.[a-z]{2,}$/;
console.log(regexUrl.test(url) ? 'URL válida' : 'URL no válida');
