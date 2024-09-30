// Parte 1: Manejo básico de excepciones

// Ejemplo 1: División por cero
try {
    // Intentamos dividir por cero para forzar una excepción
    let resultado = 10 / 0;
    console.log(resultado); // En JavaScript, esto no lanza una excepción, imprime Infinity
} catch (error) {
    console.log("Error aritmético:", error.message);
}

// Ejemplo 2: Acceso a índice no existente
try {
    // Intentamos acceder a un índice no existente de un array
    let array = ["Elemento"];
    let elemento = array[5]; // Esto no lanza una excepción en JavaScript, devuelve undefined
    console.log(elemento);
    // Para forzar un error, podemos intentar acceder a una propiedad de undefined
    console.log(elemento.length);
} catch (error) {
    console.log("Error de acceso:", error.message);
}

// Parte 2: Función con múltiples excepciones (DIFICULTAD EXTRA)

// Definimos nuestra excepción personalizada
class MiExcepcionPersonalizada extends Error {
    constructor(mensaje) {
        super(mensaje);
        this.name = "MiExcepcionPersonalizada";
    }
}

// Función que puede lanzar 3 tipos diferentes de excepciones
function procesarParametro(parametro) {
    if (typeof parametro !== 'number') {
        throw new TypeError("El parámetro debe ser un número");
    }
    if (parametro < 0) {
        throw new RangeError("El parámetro no puede ser negativo");
    }
    if (parametro === 0) {
        throw new Error("No se puede dividir por cero");
    }
    if (parametro > 10) {
        throw new MiExcepcionPersonalizada("El parámetro es demasiado grande");
    }

    // Si no hay errores, realizamos alguna operación
    let resultado = 100 / parametro;
    console.log("Resultado:", resultado);
}

// Probamos la función con diferentes valores
function probarProcesarParametro(valor) {
    try {
        procesarParametro(valor);
        console.log("No se ha producido ningún error.");
    } catch (error) {
        console.log("Tipo de error:", error.constructor.name);
        console.log("Mensaje:", error.message);
    } finally {
        console.log("La ejecución ha finalizado.");
    }
    console.log("---");
}

// Probamos con diferentes valores
probarProcesarParametro("no es un número");
probarProcesarParametro(-1);
probarProcesarParametro(0);
probarProcesarParametro(5);
probarProcesarParametro(15);