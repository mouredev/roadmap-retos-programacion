/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
*/


// Función decoradora
function conLog(funcion) {
    return function(...args) {
        console.log(`Ejecutando ${funcion.name}...`)

        const resultado = funcion(...args)

        console.log(`Resultado: ${resultado}`)

        return resultado
    }

}

// Función original
function sumar(a, b) {
    return a + b
}

// Aplicamos el decorador
const sumarConLog = conLog(sumar)

// Usamos la función decorada
sumarConLog(5, 2)


/*
function (...args) { }  // REST → recoge argumentos

funcion(...args)         // SPREAD → expande argumentos

Esa diferencia entre rest y spread es fundamental en JavaScript, y en los decoradores aparece constantemente.
*/

// Ejemplo 2
function medirTiempo(funcion) { // Esta función solo recibe como referencia por parámetros la función original.
    return function(...args) { // Aquí la función recoge los argumentos que le pasamos al llamar a la función multiplicarMasTiempo(6, 2)
        const inicio = performance.now() // Aplicamos parte de la lógica que queremos añadirle a la función origial.
        
        const resultado = funcion(...args) // Ejecutamos la función desempaquetando todos sus argumentos y la guardamos en una constante para reutilizarla más adelante.

        const fin = performance.now() // Aplicamos otra parte de la lógica que queremos añadirle a la función origial.

        console.log(`Tiempo: ${(fin - inicio).toFixed(2)} ms`) // Mostramos por pantalla la lógica añadida a la función original.

        return resultado  // Retornamos la ejecución de la función original.
    }
}

// Función original
function multiplicar(a, b) {
    return a * b
}

const multiplicarMasTiempo = medirTiempo(multiplicar) // Aquí es el momento en el que aplicamos el decorador, con las funcionalidades añadidas a la función original.
console.log(multiplicarMasTiempo(6, 2))

/*
* DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
*/

// Función decoradora
function ContarLlamadas(funcion) {
    let contador = []

    return function(...args) {
        contador++      // Cuando contarLlamadas() termina, su ejecución ha terminado, pero el entorno donde vive contador se mantiene porque la función interna todavía tiene una referencia a él.

        const resultado = funcion(...args)

        console.log(`La función ${funcion} ha sido llamada ${contador} vez.`)
        return resultado
    }
}


// Función original
function resta(a, b) {
    return a - b
}

// Aplicamos el decorador

const restaContador = ContarLlamadas(resta)

console.log(restaContador(5, 2))
console.log(restaContador(5, 3))
console.log(restaContador(5, 3))