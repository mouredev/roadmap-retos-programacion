/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */

try {
    const myVar = 10 / 0;
    console.log(myVar);
} catch (e) {
    console.log(e.toString());
}

try {
    const myVar = [1, 2, 3];
    console.log(myVar[10]);
} catch (e) {
    console.log(e.toString());
    console.log(`Tipo de excepción: ${e.name}`);
}

console.log("-".repeat(35));

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

class MyException extends Error {
    constructor(message) {
        super(message);
        this.name = "MyException";
    }
}

function myFunction(param1, param2, param3) {
    if (
        typeof param1 !== "number" ||
        typeof param2 !== "number" ||
        typeof param3 !== "string"
    ) {
        throw new TypeError(
            "Los parámetros deben ser del tipo específico: number, number, string"
        );
    }
    if (param1 > 1000) {
        throw new MyException('El valor de "param1" no puede ser mayor a 1000');
    }
    if ((param3.match(/ /g) || []).length > 1) {
        throw new SyntaxError(
            'El valor del "param3" no puede tener más de un espacio en blanco'
        );
    }
    console.log((param3.match(/ /g) || []).length);
    return [param1, param2, param3];
}

try {
    const testVar1 = myFunction(2500, 10.5, "avg");
    console.log(testVar1);
} catch (e) {
    console.log(`${e.name}: ${e.message}`);
}

try {
    const testVar2 = myFunction(1, 10.5, "avg   ");
    console.log(testVar2);
} catch (e) {
    console.log(`${e.name}: ${e.message}`);
}

try {
    const testVar3 = myFunction(1, 10.5, "avg");
    console.log(testVar3);
} catch (e) {
    console.log(`${e.name}: ${e.message}`);
} finally {
    console.log("Ejecución finalizada");
}
