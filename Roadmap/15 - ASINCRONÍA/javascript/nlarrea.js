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


function print_parameters(seconds, name) {
    console.log(
        `Task: ${name}\nTime: ${seconds}\nStart: ${new Date().toLocaleTimeString()}\n`
    );
    
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`Task: ${name}\nEnd: ${new Date().toLocaleTimeString()}\n`);
            resolve();
        }, seconds * 1000);
    });
}


async function main() {
    await Promise.all([
        print_parameters(5, "task 1"),
        print_parameters(8, "task 2"),
        print_parameters(1, "task 3"),
        print_parameters(15, "task 4"),
    ])
}


main();


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


async function run() {
    const tasks = [
        print_parameters(3, "C"),
        print_parameters(2, "B"),
        print_parameters(1, "A"),
    ];
    await Promise.all(tasks);

    await print_parameters(1, "D");
}

run()