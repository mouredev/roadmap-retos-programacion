/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
*/

// +++++++++ EJERCICIO +++++++++
// UTILIZANDO JEST, PRIMERO SE CREA EL ARCHIVO PARA EL EJEMPLO:
function addition(a, b) {
  return a + b;
}

module.exports = addition;
// EJEMPLO USANDO JEST

// SE CREA EL ARCHIVO DE PRUEBA:
test('Description', () => {
  expect(functionName(args)).toBe(result);
});

// SE PONE A PRUEBA EL EJEMPLO EN UNA FUNCIÓN DE PRUEBA:
const addition = require('../src/addition');

test('testing simple additions', () => {
  expect(doSomeMath(1, 1)).toBe(2);
  expect(doSomeMath(2, 2)).toBe(4);
});

