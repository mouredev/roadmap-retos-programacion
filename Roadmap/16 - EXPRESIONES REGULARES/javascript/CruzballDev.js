/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
*/

const texto = "La fecha de hoy es: 3/08/2026 y me he comprado 2 hamburguesas y 1 cocacola."

const numeros = texto.match(/\d+/g).map(Number)
console.log(numeros)

/*
* DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
*/

// Email
const regeEmail = /^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$/

// Numero de teléfono
const regeTelefono = /^\d{2,}\+\d{9,}$/ //En España el prefijo es +34

// URL (http o https)
const regeUrl = /^https?:\/\/[\w.-]+\.[a-zA-Z]{2,}$/

const email = "cruzballDev@developer.dev"
const telefono = "34+654987456"
const url = "https://mouredev.dev"

console.log(regeEmail.test(email))
console.log(regeTelefono.test(telefono))
console.log(regeUrl.test(url))