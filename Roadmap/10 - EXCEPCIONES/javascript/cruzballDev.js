/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */

class ConversionNumeroError extends Error {
    constructor(message) {
        super(message);
        this.name = "ConversionNumeroError"
    }
}

let x = "23"
/* console.log(typeof(x)) */

function aString(valor) {
    if( valor === null) {
        throw new TypeError("¡No se puede convertir a String un valor de tipo null. !")
    }
    if (typeof valor !== "number") {
       throw new ConversionNumeroError ("¡Tienes que introducir un número!")
    }
    return valor.toString()
}
/* console.log(typeof(aString(x)))
let texto = aString(x) // Guardamos el resultado para poder reutilizar el String devuelto.
console.log(typeof(texto)) */

/*
 *DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */



try {
    console.log(aString(x)) // Excepción personalizada.
}catch(error) {
    if(error instanceof ConversionNumeroError) {
        console.log("¡Error personlizado!", error.message )
    }
}

try {
    console.log(x.toString())  // Excepción del sistema //Poniendolo aquí también podemos controlar las excepciones del sistema.
}catch(error) {
    if(error instanceof TypeError) {
        console.log("Error al llamar a toString():", error.message)
    }else {
        console.log("Cualquier otro error: ", error.message)
    }
}
finally { // finally simpre se ejecute halla errores o no los halla.
        console.log("El programa con o sin errores, pero finalizó sin tener que interrumpirse.")
}
console.log("¡El programa ha finalizado!")
