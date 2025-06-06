/*
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.
*
DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado. 
*/

// 🔥 Forzar un error: Dividir entre cero
try {
    const resultado = 10 / 0
    console.log("Resultado:", resultado) // Resultado: Infinity
} catch (error) {
    console.error("Se produjo un error:", error.message)
} finally {
    console.log("La ejecución ha finalizado.")
}

// 🔥 Forzar otro error: Acceder a un índice no existente de un array
try {
    const lista = [1, 2, 3]
    console.log(lista[5])
} catch (error) {
    console.error("Se produjo un error:", error.message)
} finally {
    console.log("La ejecución ha finalizado.")
}

// 🔥 Extra
// Excepción personalizada
class MiErrorPersonalizado extends Error {
    constructor(message) {
        super(message);
        this.name = "MiErrorPersonalizado";
    }
}

// lanzar excepciones
function procesarParametros(parametro) {
    if (typeof parametro !== "number") {
        throw new TypeError("El parámetro debe ser un número.")
    }

    if (parametro < 0) {
        throw new RangeError("El parámetro no puede ser negativo.")
    }

    if (parametro === 42) {
        throw new MiErrorPersonalizado("El número 42 está prohibido.")
    }

    console.log("Procesamiento exitoso. Parámetro:", parametro)
}

// Casos específicos
function probarCaso(valor) {
    console.log(`\nProbando con el valor: ${valor}`)
    try {
        procesarParametros(valor)
        console.log("No se ha producido ningún error.")
    } catch (error) {
        console.error("Tipo de error:", error.name)
        console.error("Mensaje:", error.message)
    } finally {
        console.log("La ejecución ha finalizado.")
    }
}

probarCaso(10);       // Caso válido
probarCaso("texto");  // Caso inválido (no es un número)
probarCaso(-5);       // Caso inválido (número negativo)
probarCaso(42);       // Caso inválido (número prohibido)