// * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
//  * asíncrona una función que tardará en finalizar un número concreto de
//  * segundos parametrizables. También debes poder asignarle un nombre.
//  * La función imprime su nombre, cuándo empieza, el tiempo que durará
//  * su ejecución y cuando finaliza.

// ------------------------------No es asincrona
// function temporizador (tiempo){
//     function saludar( nombre ){
//         console.log('hola buenas tardes ' + nombre)
//     }
//     console.log('aqui comienza settimeout')
//     setTimeout(() => {
//     saludar('David')
//     console.log('finaliza settimeout')
//     }, tiempo);
// }

// temporizador(3000)

//async , await --------------------------------------------------------------


  function promiseFunction( tarea, tiempo){
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('la funcion ' + tarea + ' que dura ' + tiempo/1000 + 'segundos')
        }, tiempo);
    })
  }

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

  async function CallAsync () {
    console.log('llamando a mis tareas')
    const llamadoa = await promiseFunction('A', 1000)
    const llamadob = await promiseFunction('B', 2000)
    const llamadoc = await promiseFunction('C', 3000)
    const llamadod = await promiseFunction('D', 1000)
    console.log( await Promise.all([llamadoc, llamadob, llamadoa]))
    console.log(llamadod)
  }

  CallAsync()


