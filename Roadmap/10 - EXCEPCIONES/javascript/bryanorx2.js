/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */

let array = [1, 2]
try {
    let resultado = 10/0
    if (resultado === Infinity) {
        throw new Error("No se puede dividir entre 0")
    }
    if (array[2] === undefined){
        throw new Error("No se puede acceder a un índice no existente")
    }
} catch (error) {
    console.log("Se ha producido un error: ", error.message)
}


/* DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */

class MiErrorPersonalizado extends Error {
    constructor(message) {
        super(message)
        this.name = "MiErrorPersonalizado"
    }
}

function validarEdad(edad) {
    if (typeof edad !== "number") {
        throw new TypeError("La edad debe ser un número")
    }
    if (!Number.isInteger(edad)) {
        throw new RangeError("La edad no puede ser decimal")
    }
    if (edad < 0 || edad > 150){
        throw new MiErrorPersonalizado("Debe ingresar una edad válida")
    }
}

try {
    validarEdad(-18)
    console.log("Ejecución sin problemas")
} catch (error) {
    if (error instanceof TypeError){
        console.log("Se ha producido un error:", error.message, "el error es:",error.name)
    } else if (error instanceof MiErrorPersonalizado) {
        console.log("Se ha producido un error:", error.message, "el error es:",error.name)
    } else if (error instanceof RangeError) {
        console.log("Se ha producido un error: ", error.message, "el error es:",error.name)
    }
} finally {
    console.log("La ejecución a finalizado")
}