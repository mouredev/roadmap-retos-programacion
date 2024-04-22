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


const months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
];


try {
    const myResult = 10 / 0;
    if (myResult === Infinity) {
        throw new Error('You can\'t divide by zero!');
    }

    const myItem = months[12];
    if (myItem === undefined) {
        throw new Error('You tried to access an item out of index.')
    }
} catch (error) {
    console.error(error);
}


/*
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


class UnknownTypeError extends Error {
    constructor(message) {
        super(message);
        this.name = "UnknownTypeError";
    }
}


function processParams(...params) {
    for (let param of params) {
        if (
            typeof param !== 'number' &&
            typeof param !== 'string' &&
            typeof param !== 'array'
        ) {
            throw new UnknownTypeError(
                'I don\'t know about this type of data.'
            );
        }

        if (typeof param === 'string' && param.length < 10) {
            throw new SyntaxError('The length of the string is too short.');
        }

        if (typeof param === 'number' && param > 0 && param < 5) {
            throw new RangeError('The number must be positive and greater than 5.');
        }
    }
}

processParams(3.14, true, 'short', [1, 2, 3]);