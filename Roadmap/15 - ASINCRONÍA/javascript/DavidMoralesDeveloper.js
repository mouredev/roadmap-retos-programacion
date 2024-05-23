// * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
//  * asíncrona una función que tardará en finalizar un número concreto de
//  * segundos parametrizables. También debes poder asignarle un nombre.
//  * La función imprime su nombre, cuándo empieza, el tiempo que durará
//  * su ejecución y cuando finaliza.

function temporizador (tiempo){
    function saludar(){
        console.log('hola buenas tardes')
    }

    setTimeout(() => {
    saludar()
    }, tiempo);
}

temporizador(3000)


//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Utilizando el concepto de asincronía y la función anterior, crea
//  * el siguiente programa que ejecuta en este orden:
//  * - Una función C que dura 3 segundos.
//  * - Una función B que dura 2 segundos.
//  * - Una función A que dura 1 segundo.
//  * - Una función D que dura 1 segundo.
//  * - Las funciones C, B y A se ejecutan en paralelo.
//  * - La función D comienza su ejecución cuando las 3 anteriores han
//  *   finalizado.
//  */