// Excepciones 


function division(num, den){

    let result = num / den

    if (typeof num != 'number' || typeof den != 'number'){
        throw new Error("Las variables deben ser de tipo numerico");
    }

    else if(!(isFinite(result))){
        throw new Error("Error al dividir");
    }

    else {
        console.log(result)
    }

}

try {
    division(10, 5)
} catch (error) {
    console.log(error.message)
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

// Excepción personalizada
class MiExcepcionPersonalizada extends Error {
    constructor(mensaje) {
        super(mensaje);
        this.name = "MiExcepcionPersonalizada";
    }
}

// Función que procesa parámetros y puede lanzar excepciones
function procesarParametros(parametro) {
    if (typeof parametro !== "number") {
        throw new TypeError("El parámetro debe ser un número");
    }

    if (parametro < 0) {
        throw new RangeError("El parámetro no puede ser negativo");
    }

    if (parametro === 42) {
        throw new MiExcepcionPersonalizada("El parámetro no puede ser 42");
    }

    // Si no hay errores, procesar el parámetro
    console.log(`Parámetro procesado correctamente: ${parametro}`);
}

// Captura de excepciones
try {
    procesarParametros(42); // Cambia este valor para probar diferentes casos
} catch (error) {
    console.log(`Se ha producido un error: ${error.name}`);
    console.log(`Mensaje de error: ${error.message}`);
} finally {
    console.log("La ejecución ha finalizado.");
}
