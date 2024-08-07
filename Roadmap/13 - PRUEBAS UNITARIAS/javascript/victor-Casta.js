/*
  * Crea una función que se encargue de sumar dos números y retornar
  * su resultado.
  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
  * capaz de determinar si esa función se ejecuta correctamente.
*/
const assert = require('assert')

function additionNumbers(a, b) {
  return a + b
}

function runTests() {
  try {
    assert.equal(additionNumbers(5, 5), 10)
    console.log('Test passed: additionNumbers(5, 5) === 10')
  } catch (error) {
    console.error('Test failed: additionNumbers(5, 5) !== 10')
    console.error(error)
  }

  try {
    assert.equal(additionNumbers(1, 9), 10)
    console.log('Test passed: additionNumbers(1, 9) === 10')
  } catch (error) {
    console.error('Test failed: additionNumbers(1, 9) !== 10')
    console.error(error)
  }

  try {
    assert.equal(additionNumbers(0, 0), 0)
    console.log('Test passed: additionNumbers(0, 0) === 0')
  } catch (error) {
    console.error('Test failed: additionNumbers(0, 0) !== 0')
    console.error(error)
  }

  try {
    assert.equal(additionNumbers(-1, -1), -2)
    console.log('Test passed: additionNumbers(-1, -1) === -2')
  } catch (error) {
    console.error('Test failed: additionNumbers(-1, -1) !== -2')
    console.error(error)
  }

  try {
    assert.equal(additionNumbers(1, 2), 1)
  } catch (error) {
    console.error('Test failed: additionNumbers(1, 2) !== 1')
    console.error(error)
  }
}

// runTests()

/*
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

let dictionary = {
  name: 'Victor',
  age : 21,
  birth_date: '17-12-2002',
  programming_languages: ['JavaScript', 'TypeScript', 'Python']
}

function hasAllFields(obj, fields) {
  for (const field of fields) {
    if (!obj.hasOwnProperty(field)) {
      return false;
    }
  }
  return true;
}


const requireItems = ['name', 'age', 'birth_date', 'programming_languages']

function dictionaryTest() {
  try {
    assert.strictEqual(hasAllFields(dictionary, requireItems), true)
    console.log('test passed: complete dictionary')
  }catch (err) {
    console.error('test failed: incomplete dictionary')
    console.error(err)
  }

  try {
    assert.strictEqual(typeof dictionary.name, 'string', 'el nombre debe ser un string')
    assert.strictEqual(typeof dictionary.age, 'number', 'La edad debe ser un number')
    assert.strictEqual(typeof dictionary.birth_date, 'string', 'La fecha debe ser tipo string')
    assert.strictEqual(typeof dictionary.programming_languages, 'object', 'Debe ser una lista de lenguajes')
  } catch (error) {
    console.error(error)
  }

}

dictionaryTest()