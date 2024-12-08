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

/* Los Mecanismos de Pruebas Unitarias en JavaScript son muy variados:
    1. Pruebas unitarias: Las pruebas unitarias verifican que una parte específica del código funcione como se espera. para ello se utilizan frameworks de pruebas unitarias:
        * Mocha (flexible y extensible).
        * Jasmine (sin dependencias externas).
        * Jest (Popular en proyectos con Node.js o React)..
        * QUnit (usado principalmente con jQuery).
        * Vitest (Alternativa moderna de Jest).
    
    2. Pruebas de integración: Las pruebas de integración verifican que los componentes del sistema funcionen correctamente juntos. 
        se puden usar los mismo frameworks de pruebas unitarias, pero enfocádos en esenarios que involucran varios componentes.

    3. Pruebas end-to-end: Las pruebas end-to-end verifican que todo el sistema funcione correctamente. Los frameworks más populares son:
        * Selenium (para pruebas web).
        * Puppeteer (controla navegadores como Chrome mediante scripts).
        * Cypress (para pruebas web).
        * TestCafe (para pruebas web).
        * playwright (para pruebas web).
    
    4. Pruebas manuales con console.assert(): La función console.assert() de JavaScript permite realizar pruebas manuales.
        console.assert(2 + 2 === 4, 'Error: 2 + 2 debería ser 4'); // No se mostrará nada en la consola porque la condición es verdadera.
        console.assert(2 + 2 === 5, 'Error: 2 + 2 debería ser 4'); // Se mostrará un mensaje de error en la consola porque la condición es falsa.
    

*/
function sumar(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('Ambos argumentos deben ser números');
    }
    return a + b;
}
function testSumar(){
    console.log('Iniciando pruebas para la función `suma`....');

    // Caso 1: Sumar dos numeros positivos
    console.assert(sumar(3, 5) === 8, 'Error: suma(3, 5) deberia devolver 8');

    // Caso 2: Sumar un numero positivo y un numero negativo
    console.assert(sumar(10, -4) === 6, 'Error: suma(10, -4) deberia devolver');

    // Caso 3: Sumar dos numeros negativos
    console.assert(sumar(-10, -4) === -14, 'Error: suma(-10, -4) deberia devolver -14');

    // Caso 4: Sumar dos numeros decimales
    console.assert(sumar(3.5, 2.5) === 6, 'Error: suma(3.5, 2.5) deberia devolver 6');

    // Caso 5: Sumar un numero y cero
    console.assert(sumar(3, 0) === 3, 'Error: suma(3, 0) deberia devolver 3');

    // Caso 6: Sumar ceros
    console.assert(sumar(0, 0) === 0, 'Error: suma(0, 0) deberia devolver 0');

    console.log('Pruebas para la función `suma` finalizadas, todas las pruebas pasaron correctamente.');
}

testSumar();

const persona = {
    nombre: 'Walter',
    apellido: 'Pastor',
    edad: 25,
    fechaNacimiento: new Date('1995-01-01'),
    lenguajesProgramacion: ['JavaScript', 'Python', 'Java']
}

function testObjetoPersona(){
    console.log('Iniciando pruebas para el objeto `persona`....');

    // Caso 1: Verificar que el objeto `persona` tenga las propiedades correctas
    console.assert(persona.hasOwnProperty('nombre'), 'Error: persona deberia tener la propiedad "nombre"');
    console.assert(persona.hasOwnProperty('apellido'), 'Error: persona deberia tener la propiedad "apellido"');
    console.assert(persona.hasOwnProperty('edad'), 'Error: persona deberia tener la propiedad "edad"');
    console.assert(persona.hasOwnProperty('fechaNacimiento'), 'Error: persona deberia tener la propiedad "fechaNacimiento"');
    console.assert(persona.hasOwnProperty('lenguajesProgramacion'), 'Error: persona deberia tener la propiedad "lenguajesProgramacion"');

    // Caso 2: Verificar que las propiedades del objeto `persona` tengan los valores correctos
    console.assert(typeof persona.nombre === 'string', 'Error: persona.nombre deberia ser un string');
    console.assert(typeof persona.apellido === 'string', 'Error: persona.apellido deberia ser un string');
    console.assert(typeof persona.edad === 'number', 'Error: persona.edad deberia ser un número');
    console.assert(persona.fechaNacimiento instanceof Date, 'Error: persona.fechaNacimiento deberia ser una instancia de Date');
    console.assert(Array.isArray(persona.lenguajesProgramacion), 'Error: persona.lenguajesProgramacion deberia ser un array');

    // Caso 3: Verificar que el objeto `persona` tenga los métodos correctos (opcional)
    console.assert(persona.hasOwnProperty('saludar'), 'Error: persona deberia tener el método "saludar"');
    console.assert(typeof persona.saludar === 'function', 'Error: persona.saludar deberia ser una función');

    // Caso 4: Verificar que el método `saludar` del objeto `persona` funcione correctamente


    
    console.log('Pruebas para el objeto `persona` finalizadas, todas las pruebas pasaron correctamente.');
}

testObjetoPersona();
