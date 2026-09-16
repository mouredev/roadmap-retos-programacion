/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
*/

const assert = require("assert")

function suma (a, b) {
    return a + b
}

/* if(suma(2, 3) !== 7) {
    throw new Error( "Error personalizado: \n") // Esta comentado porque si salta el throw, termina el programa y no se ejecuta lo que está justo después.
} */
console.assert(suma(2, 3) === 5, "¡El test ha fallado!") 


assert.strictEqual(
    suma(2, 3),
    5,
    "La suma no funciona correctamente"
)
console.log("Test terminado")

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

const persona = {
    name: "Antonio",
    age: 47,
    birth_date: "1978-11-02",
    programming_languages: ["JavaScript", "Java", "Python", "C#"]
}

// Test 1: comprobar que existen todas las propiedades.

// De forma manual
function test_propiedadesExistenManual(persona) {
    if(!("name" in persona ) ){
    throw new Error("¡Falta la propiedad name!")
    }
    if(!("age" in persona ) ){
        throw new Error("¡Falta la propiedad age!")
    }
    if(!("birth_date" in persona ) ){
        throw new Error("¡Falta la propiedad birth_date!")
    }
    if(!("programming_languages" in persona ) ){
        throw new Error("¡Falta la propiedad programming_languages!")
    }
    console.log("¡Test superado!")
    console.log("Las propiedades existen comprobado de manera manual:" )
    console.log("name" in persona)
}

test_propiedadesExistenManual(persona)

// De forma automática

function test_propiedadesExistenAutomatico(persona) {
    assert.ok("name" in persona) // Con assert.ok() es lo mismo que preguntar: existe esta propiedad en el objeto persona?.
    assert.ok("age" in persona)
    assert.ok("birth_date" in persona) // Con birth_date lo hacemos igual porque lo tenemos como un string no como un dato de tipo date.
    assert.ok("programming_languages" in persona)
}
console.log("Las propiedades existen comprobado de manera automática:" )
test_propiedadesExistenAutomatico(persona)

// Test 2: comprobar que los datos introducidos son correctos.

// De manera manual
function test_datosCorrectosManual(persona) {

    console.log("Comprobar los datos de manera manual: ")

    if(persona.name !== "Antonio") {
        throw new Error("El nombre es incorrecto")
    }
    if(persona.age !== 47){
    throw new Error("Los años son incorrectos")
    }
    if(persona.birth_date !== "1978-11-02"){
        throw new Error("La fecha de nacimiento es incorrecta")
    }
    if(persona.programming_languages[0] !== "JavaScript"){
        throw new Error("El primer lenguaje debería ser JavaScript#")
    }
    if(persona.programming_languages[1] !== "Java") {
        throw new Error("El segundo lenguaje debería ser Java#")
    }
    if(persona.programming_languages[2] !== "Python") {
        throw new Error("El tercero lenguaje debería ser Python#")
    }
    if(persona.programming_languages[3] !== "C#") {
        throw new Error("El cuarto lenguaje debería ser C#")
    }
    console.log("¡Datos correctos!")
}

test_datosCorrectosManual(persona)

// Mismo ejercicio pero de forma automática usando assert.

function test_datosCorrectosAutomatico(persona) {
    assert.strictEqual(persona.name, "Antonio") // comprobación para datos primitivos con strictEqual.
    assert.strictEqual(persona.age, 47)
    assert.strictEqual(persona.birth_date, "1978-11-02")
    assert.deepStrictEqual(
        persona.programming_languages,
        ["JavaScript", "Java", "Python", "C#"] // comprobación profunda para objetos como el array con deepStrictEqual.
    )
    console.log("¡Datos correctos de manera automática!")
}
test_datosCorrectosAutomatico(persona)
