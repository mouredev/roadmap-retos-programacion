/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#13 PRUEBAS UNITARIAS
---------------------------------------
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

________________________________________________________
// Instala Jest en tu proyecto
npm install --save-dev jest

// package.json
{
  "scripts": {
    "test": "jest"
  }
}

// Ejecuta las pruebas:
npm test
npm test -- --verbose
________________________________________________________
*/

// src/sum.js
function sum(a, b) {
    if (arguments.length < 2) {
        throw new TypeError("Se requieren dos argumentos");
    }

    if (typeof a === "number" && typeof b === "number") {
        return a + b;
    } else {
        return null;
    }
}

// module.exports = sum;

// _____________________________
// Pruebas unitarias
// tests/sum.test.js
// const sum = require("../src/sum");
describe("Test para función suma", () => {
    test("Debe devolver la suma correcta", () => {
        expect(sum(5, 2)).toBe(7);
        expect(sum(2.5, 1.25)).toBe(3.75);
        expect(sum(-2, 1)).toBe(-1);
        expect(sum(0, 0)).toBe(0);
    });

    test("Debería devolver nulo para entradas no válidas", () => {
        expect(sum(1, "2")).toBeNull();
        expect(sum("a", "b")).toBeNull();
    });

    test("No debería devolver sumas incorrectas", () => {
        expect(sum(1, 3)).not.toBe(5);
    });

    test("Debería lanzar TypeError si faltan argumentos", () => {
        expect(() => sum(10)).toThrow(TypeError);
    });
});

// ________________________________________________________
// DIFICULTAD EXTRA

// src/dictUser.js
const dictUser = {
    name: "Ken",
    age: 121,
    birth_date: "1903-03-19",
    prog_langs: ["cs", "py", "vb", "rs", "js"],
};

// module.exports = dictUser;

// _____________________________
// Pruebas unitarias
// tests/dictUser.test.js

// const dictUser = require("../src/dictUser");
describe("Pruebas para dictUser", () => {
    test("Verificar la existencia de las claves en dictUser", () => {
        expect(dictUser).toHaveProperty("name");
        expect(dictUser).toHaveProperty("age");
        expect(dictUser).toHaveProperty("birth_date");
        expect(dictUser).toHaveProperty("prog_langs");
    });

    test("Verificar los tipos de los valores en dictUser", () => {
        expect(typeof dictUser.name).toBe("string");
        expect(typeof dictUser.age).toBe("number");
        expect(typeof dictUser.birth_date).toBe("string");
        expect(Array.isArray(dictUser.prog_langs)).toBe(true);
    });

    test("Verificar el contenido de los valores en dictUser", () => {
        expect(dictUser.name).toBe("Ken");
        expect(dictUser.age).toBe(121);
        expect(dictUser.birth_date).toBe("1903-03-19");
        expect(dictUser.prog_langs).toEqual(["cs", "py", "vb", "rs", "js"]);
    });
});
