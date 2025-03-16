/* 🔥🔥 EJERCICIO: =======================================================
Crea una función que se encargue de sumar dos números y retornar
su resultado.
*/

// Instalar `npm install --save-dev jest`

// * file as 'sumar.js' ------------------------------------------------------
function sumar(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('Deben ser números.');
    }
    return a + b;
}
module.exports = sumar;
/*
Dictionary📗 = {
    typeof : "¿Qué tipo eres?"
    throw : "¡Alto! Aquí hay un problema"
    new Error("...") : "Quiero un nuevo objeto de tipo Error con este mensaje"
}
*/

// * file as 'sumar.test.js' ------------------------------------------------------
/* 🔥🔥
Crea un test, utilizando las herramientas de tu lenguaje, que sea
capaz de determinar si esa función se ejecuta correctamente.
*/
const sumar = require('./sumar');

test('suma de dos números', () => {
    expect(sumar(2, 3)).toBe(5);
});
test('lanza error si los parámetros no son números', () => {
    expect(() => sumar("2", 3)).toThrow('Deben ser números.');
});
/*
Dictionary📗 = {
    expect : "Verifica que algo sea correcto",
    .toBe : "Espera que el resultado sea exactamente esto"
    .toThrow : "Espera que se lance un error con este mensaje"
}
*/

/* 🔥🔥🔥 DIFICULTAD EXTRA (opcional): =======================================================
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre"
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de programación"]
*/
// * file as 'datos.js' ------------------------------------------------------
const datos = {
    name: "Anderson",
    age: 20,
    birth_date: "01/01/2005",
    programming_languages: ["JavaScript", "Python", "Java"]
};
module.exports = datos;

// * file as 'datos.test.js' ------------------------------------------------------
/* 🔥🔥🔥 Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducidos son correctos.
*/
const datos = require('./datos');

// Test 1: Verificar que existen todos los campos
test('todos los campos existen', () => {
    const clavesEsperadas = ['name', 'age', 'birth_date', 'programming_languages'];
    const clavesActuales = Object.keys(datos)
    expect(clavesActuales.sort()).toEqual(clavesEsperadas.sort())
});

// Test 2: Verificar que los datos introducidos son correctos
test('los datos introducidos son correctos', () => {
    expect(typeof datos.name).toBe('string')
    expect(typeof datos.age).toBe('number')
    expect(typeof datos.birth_date).toBe('string')
    expect(Array.isArray(datos.programming_languages)).toBe(true)
    expect(datos.programming_languages.every(lang => typeof lang === 'string')).toBe(true)
});


// ! Al ejecutar `npm test`

/*
npm test

> test
> jest

 PASS  js/sumar.test.js
 PASS  js/datos.test.js

Test Suites: 2 passed, 2 total
Tests:       4 passed, 4 total
Snapshots:   0 total
Time:        2.064 s
Ran all test suites.
*/