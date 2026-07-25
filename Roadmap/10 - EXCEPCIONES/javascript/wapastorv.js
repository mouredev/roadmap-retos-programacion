/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
*/
/*  Manejo de excepciones en JavaScript:
    JavaScript tiene un mecanismo de manejo de excepciones que permite
    capturar errores y manejarlos de forma controlada. Para ello, se
    utiliza la estructura try-catch-finally, que permite intentar
    ejecutar un bloque de código, capturar cualquier excepción que
    se produzca y ejecutar un bloque de código adicional. Por ejemplo:
*/
function dividir(a, b) {
    // Intentamos dividir a por b
    try {
        var resultado = a / b;
        console.log('Resultado:', resultado);
    }
    catch (error) {
        // Capturamos cualquier excepción que se produzca
        console.error('Error:', error);
    }
    finally {
        // Este bloque se ejecuta siempre, haya o no excepciones
        console.log('Fin de la función');
    }
}

// Probamos la función con distintos valores
dividir(10, 2); // Resultado: 5
dividir(10, 0); // Error: Infinity
dividir(10, 'a'); // Error: NaN
dividir(10); // Error: NaN
dividir(); // Error: NaN
dividir(10, 2, 3); // Error: NaN
// Ejmeplo sin el uso de excepciones
function dividirSinExcepciones(a, b) {
    if (b === 0) {
        console.error('Error: División por cero');
        return;
    }
    var resultado = a / b;
    console.log('Resultado:', resultado);
    console.log('Fin de la función');
}

// Probamos la función con distintos valores
dividirSinExcepciones(10, 2); // Resultado: 5
dividirSinExcepciones(10, 0); // Error: División por cero
dividirSinExcepciones(10, 'a'); // Resultado: NaN

/*  En este caso, al intentar dividir 10 por 0, se produce una excepción
    de tipo "Infinity". Esta excepción es capturada por el bloque catch,
    que imprime un mensaje de error. A continuación, se ejecuta el bloque
    finally, que imprime un mensaje de fin de programa. De esta forma,
    el programa no se detiene de forma inesperada y podemos controlar
    el flujo de ejecución. 
*/

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

function procesarParametros(param1, param2) {
    try {
        if (param1 === undefined || param2 === undefined) {
            throw new Error('Error: Parámetros indefinidos');
        }
        if (isNaN(param1) || isNaN(param2)) {
            throw new Error('Error: Parámetros no numéricos');
        }
        if (param1 === 0 || param2 === 0) {
            throw new Error('Error: División por cero');
        }
        var resultado = param1 / param2;
        console.log('Resultado:', resultado);
    }
    catch (error) {
        console.error('Error:', error.message);
    }
    finally {
        console.log('Fin de la función');
    }
}

// Probamos la función con distintos valores
procesarParametros(10, 2); // Resultado: 5
procesarParametros(10, 0); // Error: División por cero
procesarParametros(10, 'a'); // Error: Parámetros no numéricos
procesarParametros(10); // Error: Parámetros indefinidos
procesarParametros(); // Error: Parámetros indefinidos
procesarParametros(10, 2, 3); // Resultado: 5
