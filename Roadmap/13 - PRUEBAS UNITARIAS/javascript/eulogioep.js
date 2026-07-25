// Importamos la biblioteca de pruebas Jest
const assert = require('assert');

/**
 * Función que suma dos números y retorna el resultado.
 * @param {number} a Primer número a sumar.
 * @param {number} b Segundo número a sumar.
 * @return {number} La suma de a y b.
 */
function suma(a, b) {
    return a + b;
}

/**
 * Crea y retorna un objeto con datos personales.
 * @return {Object} Objeto con datos personales.
 */
function crearObjeto() {
    return {
        name: "Tu nombre",
        age: 30,
        birth_date: "1993-01-01",
        programming_languages: ["JavaScript", "Python", "Java"]
    };
}

// Pruebas unitarias
describe('Pruebas de la función suma', () => {
    test('Suma de 2 y 3 debería ser 5', () => {
        assert.strictEqual(suma(2, 3), 5);
    });

    test('Suma de -1 y 1 debería ser 0', () => {
        assert.strictEqual(suma(-1, 1), 0);
    });

    test('Suma de -2 y -3 debería ser -5', () => {
        assert.strictEqual(suma(-2, -3), -5);
    });
});

describe('Pruebas del objeto de datos personales', () => {
    const objeto = crearObjeto();

    test('El objeto debe contener todas las claves requeridas', () => {
        assert(objeto.hasOwnProperty('name'), "El objeto debe contener la clave 'name'");
        assert(objeto.hasOwnProperty('age'), "El objeto debe contener la clave 'age'");
        assert(objeto.hasOwnProperty('birth_date'), "El objeto debe contener la clave 'birth_date'");
        assert(objeto.hasOwnProperty('programming_languages'), "El objeto debe contener la clave 'programming_languages'");
    });

    test('Los datos en el objeto deben ser correctos', () => {
        assert.strictEqual(objeto.name, "Tu nombre", "El nombre debe ser 'Tu nombre'");
        assert(typeof objeto.age === 'number', "La edad debe ser un número");
        assert(/^\d{4}-\d{2}-\d{2}$/.test(objeto.birth_date), "La fecha de nacimiento debe tener el formato YYYY-MM-DD");
        assert(Array.isArray(objeto.programming_languages), "Los lenguajes de programación deben ser un array");
        assert(objeto.programming_languages.length > 0, "La lista de lenguajes de programación no debe estar vacía");
    });
});