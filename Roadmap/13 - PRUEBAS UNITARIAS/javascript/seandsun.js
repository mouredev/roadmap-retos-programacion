/* <-------------- Pruebas unitarias con jest -------------->
1 - El archivo donde se escriben los test debe llevar la extensión .test.js así: pruebas.test.js
2 - Crear un package json: npm init --yes
3 - Instalar jest: npm i --save-dev jest o npm i jest -D
4 - En el package.json cambiar ésto: "scripts": { "test": "echo \"Error: no test specified\" && exit 1" }
    Por estó: "scripts": { "test": "jest" }
5 - Para ejecutar los test, ejecutar el comando: npm run test
*/

function suma(x,y) {
    return x + y
}

describe('Test de sumas', () => {
    // Pasa la prueba porque está bien escrito
    test('3 + 5', () => {
        const resultado = suma(3,5)

        expect(resultado).toBe(8)
    })
    
    // No pasa la prueba porque el resultado recibido es diferente al especificado
    test('2 + 4', () => {
        const resultado = suma(2,4)

        expect(resultado).toBe(7)
    })
})
