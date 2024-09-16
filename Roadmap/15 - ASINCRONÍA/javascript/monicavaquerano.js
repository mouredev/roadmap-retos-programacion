// 15 ASINCRONÍA
// Monica Vaquerano
//  https://monicavaquerano.dev

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

async function asincrona() {
    let inicio = new Date();
    console.log(`starts at ${inicio.toString()}`)

    console.log("Soy una ...\n")

    await new Promise((resolve) => {
        setTimeout(resolve, 5000);
    });

    console.log("\n... función asíncrona!")

    let final = new Date();
    let seconds = (final.getTime() - inicio.getTime()) / 1000

    console.log(`ends at ${final.toString()}`)
    console.log(`\nLa función se demoró ${seconds.toFixed(2)} segundos.\n`)

}

asincrona();

async function tarea(nombre = "default", segundos = 1) {
    let inicio = new Date();

    console.log(`\tNombre: ${nombre} Comienzo: ${inicio.toString()} Duración: ${segundos} segundo(s).`)

    await new Promise((resolve) => {
        setTimeout(resolve, segundos * 1000);
    });

    let final = new Date();
    console.log(`\t... Nombre: ${nombre} Final: ${final.toString()}.`)


    let seconds = (final.getTime() - inicio.getTime()) / 1000

    console.log(`\t\tLa función se demoró ${seconds.toFixed(2)} segundos.\n`)

}

tarea("Prueba", 1);


// #  * DIFICULTAD EXTRA (opcional):
// #  * Utilizando el concepto de asincronía y la función anterior, crea
// #  * el siguiente programa que ejecuta en este orden:
// #  * - Una función C que dura 3 segundos.
// #  * - Una función B que dura 2 segundos.
// #  * - Una función A que dura 1 segundo.
// #  * - Una función D que dura 1 segundo.
// #  * - Las funciones C, B y A se ejecutan en paralelo.
// #  * - La función D comienza su ejecución cuando las 3 anteriores han
// #  *   finalizado.

async function tareas() {
    await Promise.all([tarea("A", 1), tarea("B", 2), tarea("C", 3)])
    await tarea("D", 1);
}

tareas();
