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

/******************* PARTE 1 *******************/
const a = 10;

try{
    console.log(a/b);
} catch(error){
    console.log(error); //Se mostrará el error, debido a que la variable "b" no ha sido declarada
} finally{
    console.log("La ejecución ha finalizado");
}

console.log("El programa sigue con normalidad");

/******************* EXTRA *******************/

function processParams(param1, param2) {
    try {
        if (typeof param1 !== 'number' || typeof param2 !== 'number') {
            throw new TypeError('Los parámetros deben ser números');
        }

        if (param1 === 0 || param2 === 0) {
            throw new Error('Los parámetros no pueden ser cero');
        }

        if (param1 < 0 || param2 < 0) {
            throw new Error('Valores negativos no permitidos');
        }

        console.log('No se ha producido ningún error');
    } catch (error) {
        console.error('Tipo de error:', error instanceof Error ? error.name : 'Error personalizado');
        console.error('Mensaje de error:', error.message || error);
    }
}

processParams(10, 20); // No se produce ningún error
processParams(0, 30); // Lanza una excepción por división por cero
processParams(-5, 10); // Lanza una excepción personalizada por valores negativos
processParams('abc', 10); // Lanza una excepción por tipo de parámetro incorrecto

