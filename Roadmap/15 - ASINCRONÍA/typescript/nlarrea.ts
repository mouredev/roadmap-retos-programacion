/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
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


function printParameters(seconds: number, name: string): Promise<void> {
    console.log(
        `Task: ${name}\nTime: ${seconds}\nStart: ${new Date().toLocaleTimeString()}\n`
    )

    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`Task: ${name}\nEnd: ${new Date().toLocaleTimeString()}\n`)
            resolve()
        }, seconds * 1000)
    })
}


async function mainFunction() {
    await Promise.all([
        printParameters(5, 'task 1'),
        printParameters(8, 'task 2'),
        printParameters(1, 'task 3'),
        printParameters(15, 'task 4')
    ])
}


mainFunction()


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


async function asyncRun() {
    const tasks: Promise<void>[] = [
        printParameters(3, 'C'),
        printParameters(2, 'B'),
        printParameters(1, 'A')
    ]
    await Promise.all(tasks)

    await printParameters(1, 'D')
}


asyncRun()