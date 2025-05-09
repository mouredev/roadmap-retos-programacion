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

//
// Exepciones (try and catch)
//

// Error al dividir por cero, genero el error  
try {
    const resultado = 10 / 0
    console.log("🔢 División por cero:", resultado)
} catch (error) {
    console.error("⚠️ Error al dividir:", error.message)
}
console.log("✅ El programa continúa tras dividir por cero")

// Error al acceder a un indice que no existe
try {
    const lista = [1, 2, 3]
    const valor = lista[10].toString() 
    console.log("📦 Valor accedido:", valor)
} catch (error) {
    console.error("🚨 Error al acceder a índice inexistente:", error.message)
}
console.log("✅ El programa continúa tras acceder a un índice no existente\n")

// Error en un listado
try {
    const texto = '{"nombre": "Gian", "edad": }' 
    const objeto = JSON.parse(texto)
} catch (error) {
    console.error("❌ Error al parsear JSON:", error.message)
}
console.log("✅ El programa continúa tras fallo en JSON\n")

// Error personalizado
function dividir(a, b) {
    if (b === 0) throw new Error("No se puede dividir por cero (personalizado)")
        return a / b
}

try {
    const resultado = dividir(10, 0)
    console.log("🧮 Resultado personalizado:", resultado)  
} catch (error) {
    console.error("🚫 Error personalizado:", error.message)
}
console.log("✅ El programa continúa tras lanzar un error personalizado")

//
// EXTRA
//

class MiErrorPersonalizado extends Error {
    constructor(mensaje) {
        super(mensaje)
        this.name = "MiErrorPersonalizado"
    }
}

function procesarValor(valor) {
    if (typeof valor !== "number") {
        throw new TypeError("El valor no es un número.")
    }

    if (valor < 0 || valor > 100) {
        throw new RangeError("El número debe estar entre 0 y 100.")
    }

    if (valor === 42) {
        throw new MiErrorPersonalizado("¡42 es un número prohibido!")
    }

    return `✅ Valor aceptado: ${valor}`
}


try {
    const resultado = procesarValor(42) 
    console.log(resultado)
    console.log("✅ No se produjo ningún error.")
} catch (error) {
    console.error(`❌ Se capturó un error de tipo: ${error.name}`)
    console.error("📣 Mensaje:", error.message)
} finally {
    console.log("🏁 La ejecución ha finalizado.")
}
