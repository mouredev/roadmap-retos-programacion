// Pruebas Unitarias 

// Una funcion Sumar en un archivo math.js

function sumar(a, b) {
    return a + b;
  }
  
module.exports = sumar;


// La prueba unitaria de dicha funcion se hara en un archivo separado llamado math.test.js

const sumar = require('./math');

test('sumar 1 + 2 debe ser igual a 3', () => {
  expect(sumar(1, 2)).toBe(3);
});

test('sumar -1 + 1 debe ser igual a 0', () => {
  expect(sumar(-1, 1)).toBe(0);
});

// Para ejecutar la prueba en Jest se utiliza el comando  npx jest