/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#15 ASINCRONÍA
---------------------------------------
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
 *   finalizado.
*/
// ________________________________________________________

async function process(name, time) {
    console.log(`- Iniciar función: ${name} -> Duración: ${time}s`);
    await new Promise(resolve => setTimeout(resolve, time * 1000));
    console.log(`* Función ${name} finaliza.`);
}

async function test() {
    await Promise.all([
        process("Test 2", 4),
        process("Test 1", 2)
    ]);
}

// ________________________________________________________
// DIFICULTAD EXTRA

async function in_parallel() {
    await Promise.all([
        process("C", 3),
        process("B", 2),
        process("A", 1)
    ]);
}

async function main() {
    await test();
    await in_parallel();
    await process("D", 1); 
}

main();
