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


