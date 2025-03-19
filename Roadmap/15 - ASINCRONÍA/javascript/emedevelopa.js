/* EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.*/

function asincrona (nombre, segundos) {
    console.log(`${nombre} comienza.`);
    console.log(`${nombre} empezó a las ${new Date().toLocaleTimeString()}.`);
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`${nombre} ha finalizado después de ${segundos} segundos.`);
            console.log(`${nombre} terminó a las ${new Date().toLocaleTimeString()}.`);
            resolve();
        }, segundos * 1000);
    });
}
asincrona("El programa",13);

//EXTRA
/*Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
* - Una función C que dura 3 segundos.
* - Una función B que dura 2 segundos.
* - Una función A que dura 1 segundo.
* - Una función D que dura 1 segundo.
* - Las funciones C, B y A se ejecutan en paralelo.
* - La función D comienza su ejecución cuando las 3 anteriores han finalizado.*/

async function programa() {
    try {
        await Promise.all([
            asincrona("Función C", 3),
            asincrona("Función B", 2),
            asincrona("Función A", 1)
        ]);
        await asincrona("Función D", 1);
    } catch (error) {
        console.log("Se produjo un error:", error);
    }
}

programa();