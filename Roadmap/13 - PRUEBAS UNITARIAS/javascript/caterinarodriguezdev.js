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

const sum = (num1, num2) => {
    return num1 + num2;
}

const testSum = () => {

    const result1 = sum(1, 4);
    const expected1 = 5;

    const result2 = sum(-3, 4);
    const expected2 = 1;

    if (result1 !== expected1) {
        console.log('Test fallado');
        return;
    } else {
        console.log('✅ Test 1 pasado');
    }

    if (result2 !== expected2) {
        console.log('Test fallado');
    } else {
        console.log('✅ Test 2 pasado');
    }
}

testSum();

const persona = {
    name: 'Ada Lovelace',
    age: 208,
    birth_date: '10/12/1815',
    programming_languages: ['Ada']
}

const existenTodosLosCamposTest = () => {

    const campos = ['name', 'age', 'birth_date', 'programming_languages'];

    campos.every(campo => campo in persona) ? console.log('✅ Test existenTodosLosCamposTest pasado') : console.log('Test existenTodosLosCamposTest fallado');
}

const checkCamposSonCorrectosTest = () => {

    if (typeof persona.name !== 'string') {
        console.log('Test checkCamposSonCorrectosTest fallado: el campo name debe ser una string');
        return;
    }

    if (persona.age < 0) {
        console.log('Test checkCamposSonCorrectosTest fallado: el campo age no puede ser negativo');
        return;
    }

    const formatoFecha = /^\d{2}\/\d{2}\/\d{4}$/;
    if (!formatoFecha.test(persona.birth_date)) {
        console.log('Test checkCamposSonCorrectosTest fallado: el campo birth_date tiene un formato incorrecto');
        return;
    }

    const lenguajesDeProgramacionAceptados = ['Javascript', 'Ada', 'Python', 'Java'];

    if (persona.programming_languages.some(lenguaje => !lenguajesDeProgramacionAceptados.includes(lenguaje))) {
        console.log('Test checkCamposSonCorrectosTest fallado: el lenguaje de programación no es aceptado');
        return;
    }

    console.log('✅ Test checkCamposSonCorrectosTest pasado');
}

existenTodosLosCamposTest();
checkCamposSonCorrectosTest();