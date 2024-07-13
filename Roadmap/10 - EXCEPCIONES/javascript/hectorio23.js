// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";


/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
*/


// Función para dividir dos números e intentar forzar un error
function dividir() {
    try {
        let divisor = 0;
        if (divisor === 0) {
            throw new Error("División por cero");
        }
        let resultado = 10 / divisor; // Intento de dividir por cero
        console.log(`El resultado de la división es: ${resultado}`);
    } catch (error) {
        console.error(`Se produjo un error: ${error.message}`);
    }
}

// Función que puede lanzar excepciones personalizadas
function procesarParametro(parametro) {
    try {
        if (parametro === 0) {
            throw new Error("El parámetro no puede ser cero");
        } else if (parametro < 0) {
            throw new Error("El parámetro no puede ser negativo");
        } else {
            console.log("Procesamiento exitoso");
        }
    } catch (error) {
        console.error(`Se produjo un error: ${error.message}`);
    } finally {
        console.log("La ejecución ha finalizado.");
    }
}

// Función principal
(function main() {
    // Forzar un error al dividir por cero
    console.log("Intentando dividir por cero:");
    dividir();

    console.log("\n---------------------------------------\n");

    // Intento de procesar un parámetro
    console.log("Intentando procesar parámetro:");
    procesarParametro(-3);
})();
