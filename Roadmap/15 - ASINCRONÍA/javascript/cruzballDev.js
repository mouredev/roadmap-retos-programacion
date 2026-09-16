/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 */


// Función que espera un número de segundos
function delay(segundos) {
    return new Promise(resolve => {
        setTimeout(resolve, segundos * 1000)
    })
}

// Función asíncrona

async function comienzoFinSegundos(nombre, segundos) {
    console.log(`${nombre}`)
    console.log(`Comienzo: ${new Date().toLocaleTimeString("es-ES")} `)
    console.log(`Duración ${segundos} segundos.`)

    await delay(segundos)

    console.log(`${nombre} Finaliza: ${new Date().toLocaleTimeString("es-ES")}`)
}

//comienzoFinSegundos("Descarga de documento", 5)


/*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
*/

async function variosCasos() {
    
    await Promise.all([
        comienzoFinSegundos("C", 3),
        comienzoFinSegundos("B", 2),
        comienzoFinSegundos("A", 1)
    ])
    await comienzoFinSegundos("D", 1)
}

variosCasos()
