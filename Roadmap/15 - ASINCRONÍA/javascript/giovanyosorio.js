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

function resolve(name,time) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve('resolved');
      }, time);
    });
  }
  
  async function asyncCall(name,time) {
    console.log(`calling my first function ${name} in ${time/1000} segundos`);
    const result = await resolve(name,time);
    console.log(result);
    // Expected output: "resolved"
  }
  
  asyncCall("myfunction",4000);
  

  function sleep(duration) {
    return new Promise(resolve => setTimeout(resolve, duration));
  }  
  async function A(){
    await sleep(1000)
    console.log('Función A completada (1 segundo)');
  }

  async function B(){
    await sleep(2000)
    console.log('Función B completada (2 segundo)');
  }
  async function C(){
    await sleep(3000)
    console.log('Función C completada (3 segundo)');
  }
  async function D(){
    await sleep(1000)
    console.log('Función D completada (1 segundo)');
  }

  async function execute(){
    console.log('Iniciando funciones A, B y C en paralelo');
    await Promise.all([A(),B(),C()])
    console.log("han finalizado las tres funciones en paralelo")
    await D()

    console.log('Función D ha finalizado');

  }

  execute();