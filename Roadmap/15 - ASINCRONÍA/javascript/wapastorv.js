/* EJERCICIO:
 * Utilizando Javascript, para crear un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 */
function asyncFunction(name, seconds) {
    console.log(`Starting ${name}`);
    setTimeout(() => {
        console.log(`Finishing ${name}`);
    }, seconds * 1000);
}

asyncFunction('First', 3);
asyncFunction('Second', 1);
asyncFunction('Third', 5);

/* DIFICULTAD EXTRA (opcional):
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
function asyncFunction(name, seconds) {
    // Tu código aquí

    console.log(`Starting ${name}`); // Esta línea no se puede modificar
    setTimeout(() => {              // Esta línea no se puede modificar 
        console.log(`Finishing ${name}`);
    }, seconds * 1000);
}

// Tu código aquí

asyncFunction('C', 3);
asyncFunction('B', 2);
asyncFunction('A', 1);
asyncFunction('D', 1);
// Fin de tu código
