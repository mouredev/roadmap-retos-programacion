/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#10 EXCEPCIONES
---------------------------------------
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

// ________________________________________________________
// 1: Capturar excepción por división entre 0 (personalizada)
try {
    const a = 7;
    const b = 0;
    if (b === 0) {
        throw new Error("No se puede dividir entre cero.");
    }
    const r = a / b;
    console.log("Resultado: ", r);
} catch (error) {
    console.error("Error capturado: ", error.message);
}

// 2: Capturar errores de conversión o concatenación
try {
    // Genera un error al intentar sumar un número con una cadena
    const r = parseInt("uno") + 2; // Aquí "uno" no puede convertirse
    if (isNaN(r)) {
        throw new TypeError("Conversión fallida: el resultado no es un número.");
    }
} catch (error) {
    console.error("Error capturado: ", error.message);
}

// 3: Capturar múltiples tipos de excepciones
try {
    // Lanza manualmente un error de tipo o rango
    const value = -1;
    if (value < 0) {
        throw new RangeError("El valor no puede ser negativo.");
    }
} catch (error) {
    if (error instanceof RangeError) {
        console.error("Error de rango: ", error.message);
    } else if (error instanceof TypeError) {
        console.error("Error de tipos: ", error.message);
    } else {
        console.error("Error desconocido: ", error.message);
    }
}

//4: Capturar una excepción genérica
try {
    // Intentar acceder a un índice fuera de rango en un arreglo
    const myArray = [1, 2, 3];
    console.log(myArray[10]); // No genera error automáticamente
    throw new Error("Índice fuera de rango."); // Lanzamos un error manualmente
} catch (error) {
    console.error("Error capturado: ", error.message);
}

// 5: Capturar y mostrar el tipo de excepción
try {
    // Genera un error lanzando un número en lugar de un mensaje (caso extraño)
    throw 42;
} catch (error) {
    console.error("Tipo de error: ", typeof error, " | Valor: ", error);
}

// 6: Bloque finally (ejecutar siempre)
try {
    // Simula un error de división
    const a = 5;
    const b = 0;
    if (b === 0) {
        throw new Error("No se puede dividir entre cero.");
    }
} catch (error) {
    console.error("Error capturado: ", error.message);
} finally {
    console.log("Bloque finally ejecutado.");
}

// 7: Lanzar una excepción personalizada
class CustomException extends Error {
    constructor(message) {
        super(message);
        this.name = "CustomException";
    }
}

try {
    throw new CustomException("Este es un error personalizado.");
} catch (error) {
    if (error instanceof CustomException) {
        console.error("Error personalizado capturado: ", error.message);
    } else {
        console.error("Error desconocido: ", error.message);
    }
}

// 8: Pasar un objeto a la excepción
class DictionaryException extends Error {
    constructor(data) {
        super("Excepción con datos adicionales");
        this.data = data;
    }
}

try {
    throw new DictionaryException({ msg: "Mensaje", info: "Información adicional" });
} catch (error) {
    if (error instanceof DictionaryException) {
        console.error("Datos de la excepción: ", error.data);
    }
}


// ________________________________________________________
// DIFICULTAD EXTRA

class OddNumberError extends Error {
    constructor(msg = "No dividir entre impares") {
        super(msg);
        this.name = "OddNumberError";
    }
}

function division(a, b) {
    if (b % 2 !== 0) {
        throw new OddNumberError();
    }
    return a / b;
}

function operation(a, b) {
    try {
        console.log("Resultado: ", division(a, b));
    } catch (error) {
        console.error("Error: ", error.constructor.name, error.message);
    } finally {
        console.log("Operación terminada.");
    }
}

console.log("\n___________\nEjercicio:");
operation(10, "uno");
operation(10, 0);
operation(10, 5);
operation(10, 2);
