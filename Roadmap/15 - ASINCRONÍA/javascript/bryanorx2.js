/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 */

function asyncFunction (name, time){
    const timeStart = Date.now()
    const currentday = new Date(timeStart)
    console.log(`${name} inicia a ${currentday.toString()} - durará ${time} segundos`)
    return new Promise((resolve) => {
        setTimeout(() => {
            const timeEnd = Date.now()
            const finalday = new Date(timeEnd)
            console.log(`${name} termina a ${finalday.toString()}`)
            resolve()
        }, time * 1000);
    })
}

asyncFunction("Bryan",2)

/* DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */

Promise.all([asyncFunction("C", 3), asyncFunction("B", 2), asyncFunction("A", 1)])
    .then(() => asyncFunction("D", 1))