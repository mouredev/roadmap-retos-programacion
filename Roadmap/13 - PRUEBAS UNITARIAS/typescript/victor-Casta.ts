const assert = require('assert')
/*
  * EJERCICIO:
  * Crea una función que se encargue de sumar dos números y retornar
  * su resultado.
  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
  * capaz de determinar si esa función se ejecuta correctamente.
*/

function addition(a: number, b: number): number {
  return a + b
}

try {
  assert.equal(addition(1, 2), 3)
  console.log(`Test 1: pasó. Resultado de la suma: ${addition(1, 2)}`)
} catch (error) {
  console.error(`Test 1: falló. Error: ${error.message}`)
}

/*
  * Crea un diccionario con las siguientes claves y valores:
  * "name": "Tu nombre"
  * "age": "Tu edad"
  * "birth_date": "Tu fecha de nacimiento"
  * "programming_languages": ["Listado de lenguajes de programación"]
  * Crea dos test:
  * - Un primero que determine que existen todos los campos.
  * - Un segundo que determine que los datos introducidos son correctos.
*/

interface Person {
  name: string;
  age: number;
  birthDate: Date;
  programmingLanguages: string[];
}

const person: Person = {
  name: 'Victor',
  age: 21,
  birthDate: new Date(2002, 11, 17),
  programmingLanguages: ['TypeScript', 'JavaScript', 'Python']
};

function validateStructure(expected: Person, actual: Person): void {
  const expectedKeys = Object.keys(expected);
  const actualKeys = Object.keys(actual);
  assert.strictEqual(expectedKeys.length, actualKeys.length, 'Las estructuras no tienen el mismo número de claves.');
  expectedKeys.forEach(key => {
    assert.ok(actual.hasOwnProperty(key), `La propiedad "${key}" falta en el objeto real.`);
  });
}

function validateValues(expected: Person, actual: Person): void {
  const expectedKeys = Object.keys(expected);
  expectedKeys.forEach(key => {
    assert.strictEqual(typeof actual[key], typeof expected[key], `El tipo de la propiedad "${key}" no coincide.`);
  });
}

try {
  validateStructure({
    name: '',
    age: 0,
    birthDate: new Date(2002, 11, 17),
    programmingLanguages: ['']
  }, person);
  console.log('Test 1: pasó. La estructura es correcta.');
} catch (error) {
  console.error('Test 1: falló. Error: ', error.message);
}

try {
  validateValues({
    name: '',
    age: 0,
    birthDate: new Date(2002, 11, 17),
    programmingLanguages: ['']
  }, person);
  console.log('Test 2: pasó. Los tipos son correctos.');
} catch (error) {
  console.error('Test 2: falló. Error: ', error.message);
}