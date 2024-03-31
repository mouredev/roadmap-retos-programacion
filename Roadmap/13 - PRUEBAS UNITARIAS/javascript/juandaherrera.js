/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 */

function customSum(num1, num2) {
    return num1 + num2;
}

const { describe, it, expect } = require("@jest/globals");

describe("customSum", () => {
    it("should sum two positive numbers correctly", () => {
        expect(customSum(5, 6)).toBe(11);
    });

    it("should sum two negative numbers correctly", () => {
        expect(customSum(-5, -6)).toBe(-11);
    });

    it("should sum a positive and a negative number correctly", () => {
        expect(customSum(-5, 6)).toBe(1);
    });
});

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

const myDict = {
    name: "Juan David Herrera",
    age: "24",
    birthDate: "1999-12-05",
    programmingLanguages: ["Python", "Javascript", "VBA", "Bash"],
};

describe("myDict", () => {
    it("should have all required fields", () => {
        const requiredFields = [
            "name",
            "age",
            "birthDate",
            "programmingLanguages",
        ];
        requiredFields.forEach((field) => {
            expect(myDict).toHaveProperty(field);
        });
    });

    it("should contain the correct data", () => {
        const correctData = {
            name: "Juan David Herrera",
            age: "24",
            birthDate: "1999-12-05",
            programmingLanguages: ["Python", "Javascript", "VBA", "Bash"],
        };
        expect(myDict).toEqual(correctData);
    });
});
