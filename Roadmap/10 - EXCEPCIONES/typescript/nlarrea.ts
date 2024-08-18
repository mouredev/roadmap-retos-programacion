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


const months: string[] = [
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
]


try {
    const wrongResult: number = 10 / 0
    if (wrongResult === Infinity) {
        throw new Error('You can\'t divide by zero!')
    }

    const myMonth: string = months[12]
    if (myMonth === undefined) {
        throw new Error('You tried to access an item out of index.')
    }
} catch (error) {
    console.error(error)
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
    constructor(message: string) {
        super(message)
        this.name = 'UnknownTypeError'
    }
}


function processParams(...params: any) {
    const knownTypes: string[] = [
        'number',
        'string',
        'array'
    ]

    for (const param of params) {
        if (!knownTypes.includes(typeof param)) {
            throw new UnknownTypeError(
                'I don\'t know about this type of data.'
            )
        }

        if (typeof param === 'string' && param.length < 10) {
            throw new SyntaxError('The length of the string is too short.')
        }

        if (typeof param === 'number' && param < 5) {
            throw new RangeError('The number must be positive and greater than 5.')
        }
    }
}


try {
    processParams(
        3.14,
        true,
        'short',
        [1, 2, 3]
    )
} catch (error) {
    console.error(error)
}