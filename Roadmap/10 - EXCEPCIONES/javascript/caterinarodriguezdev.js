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


try {
    const result = 10/0; // En Javascript no tira un error sino que resulta en Infinity
    console.log(result);

    const arr = [10, 20, 30];
    console.log(arr[100]); // En Javascript no tira un error sino que resulta en undefined

    console.log(patata);
} catch (error) {
    console.error('ha habio un error', error);
}


console.log('----------------------DIFICULTAD EXTRA-----------------------------');



const tirarErrores = (funcion, exponencial, equipo) => {

    funcion();

    let num = 2;
    console.log('num exponencial', num.toExponential(exponencial));

    if (equipo === 'Barça') {
        console.log('Barça');
    } else {
        throw new Error('Equipo incorrecto!')
    }
}

const cate = () => {}

try {
    tirarErrores(funcionIntexistente, -2, 'madrid')
} catch(error) {
    console.error(error);
    console.log('---------------------------------------------------');
}

try {
    tirarErrores(cate, -2, 'madrid')
} catch(error) {
    console.error(error);
    console.log('---------------------------------------------------');
}

try {
    tirarErrores(cate, 2, 'madrid')
} catch(error) {
    console.error(error);
}