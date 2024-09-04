//Se instala Jest y las dependencias necesarias
//Se Configura Jest para TypeScript: Crea un archivo de configuración de Jest jest.config.js:
/*

module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',
};

*/

export function sum(a: number, b: number): number {
    return a + b;
}

//Crea el test para la función en un archivo llamado sum.test.ts:

/*
import { sum } from './sum';

test('sums two numbers correctly', () => {
    expect(sum(1, 2)).toBe(3);
    expect(sum(-1, 1)).toBe(0);
    expect(sum(0, 0)).toBe(0);
    expect(sum(2.5, 2.5)).toBe(5);
});

*/

//Ejecución de los Tests
//Para ejecutar los tests, añade un script en el archivo package.json:

/*
"scripts": {
    "test": "jest"
}

*/

