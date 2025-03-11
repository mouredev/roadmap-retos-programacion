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

// Mejor eleccion cuando se utiliza el patrón constante
let re = /zcb/;

// Mejor cuando el patrón puede variar o proviene de una entrada dinámica
let red = new RegExp("vbn");

// Método Test para comprobar si hay coincidencias y arrojar un boolean
let test = /hola/.test("hola mundo"); // true

// Método exec() busca coincidencias y devuelve un array con los resultados o un null si no hay coincidencias
let result = /hola/.exec(
  "hola mundo"
) // Métodos del objeto "String"
`match()` // Busca coincidencias en una cadena y devuelve un array.
`replace()` // Reemplaza las coincidencias encontradas con otro texto.
`search()` // Busca una coincidencia y devuelve la posicion de la primera aparición.
`split()`; // Divide una cadena en un arreglo usando la expresión regular como delimitador.

// Ejercicio 1
let phoneNumber = "Hola, mi numero de telefono es +569 1234567";
let regex = /(\d+)/g;

let newNumber = phoneNumber.match(regex);

console.log(newNumber);

// Ejercicio 2

// Validar un email
function validarEmail(email) {
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return regex.test(email);
}

const emailPrueba = "ejemplo@dominio.com";
if (validarEmail(emailPrueba)) {
  console.log("El email es valido");
} else {
  console.log("El email es invalido");
}

// Validar un número telefónico
function validarTelefono(phone) {
  const regex = /\d/g;
  return regex.test(phone);
}

const telefono = "926333333";
if (validarTelefono(telefono)) {
  console.log("El telefono es valido");
} else {
  console.log("El numero telefonico es invalido");
}
// Validar una url
const isValidURL = (urlString) => {
  return patronURL.test(urlString);
};

console.log(isValidURL("https://www.ejemplo.com")); // true
console.log(isValidURL("ftp://www.ejemplo.com")); // false
