// EJERCICIO:
// Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
// asíncrona una función que tardará en finalizar un número concreto de
// segundos parametrizables. También debes poder asignarle un nombre.
// La función imprime su nombre, cuándo empieza, el tiempo que durará
// su ejecución y cuando finaliza.

async function myAsyncFunction(name: string, seconds: number): Promise<void> {
    return new Promise<void>((resolve, reject) => {
        if (seconds < 0) {
            console.error("Seconds must be a positive number.");
            return;
        }
        console.log(`${name} started at ${new Date().toLocaleTimeString()}, duration: ${seconds} seconds.`);
        setTimeout(() => {
            console.log(`${name} finished at ${new Date().toLocaleTimeString()}`);
            resolve();
        }, seconds * 1000);
    });
}

myAsyncFunction("Task 1", 5);

// DIFICULTAD EXTRA (opcional):
// Utilizando el concepto de asincronía y la función anterior, crea
// el siguiente programa que ejecuta en este orden:
// - Una función C que dura 3 segundos.
// - Una función B que dura 2 segundos.
// - Una función A que dura 1 segundo.
// - Una función D que dura 1 segundo.
// - Las funciones C, B y A se ejecutan en paralelo.
// - La función D comienza su ejecución cuando las 3 anteriores han
//   finalizado.

async function myAsyncMultipleFunctions(): Promise<void> {
    await Promise.all([
        myAsyncFunction("C", 3),
        myAsyncFunction("B", 2),
        myAsyncFunction("A", 1)
    ]).then(() => myAsyncFunction("D", 1));
}

myAsyncMultipleFunctions();


