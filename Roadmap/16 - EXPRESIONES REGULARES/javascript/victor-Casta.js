/*
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
*/

const getNumbersRegex = /\d/g;
console.log("JavaScript1995".match(getNumbersRegex).join(""))

/*
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
*/

// Email Regex
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
const phoneRegex= /^\+?[1-9]\d{1,14}$/
const urlRegex = /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/