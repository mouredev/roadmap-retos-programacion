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

async function demorarAPedido(demora, nombre) {
  return new Promise((resolve, reject) => {
    let inicio = Date.now()
    if (demora < 0) {
      reject('El valor para demora debe ser mayor que cero');
    } else {
      setTimeout(() => { 
        let ahora = Date.now();
        let message = `Inicio: ${inicio} /Demora en milis:${ahora - inicio}/ ${Date.now()}: Finalizado ${nombre} (${demora})`;
        resolve(message); 
        console.log(message);
      }, demora)
    }
  })
  
}


async function main() {
  await Promise.all([demorarAPedido (3000, 'C'), demorarAPedido (2000, 'B'), demorarAPedido (1000, 'A')])
  .then((data) => { })  
  .catch((err) => {
    console.log(err);
 })
 console.log('por ejecutar D')
 let D = await demorarAPedido (1000, 'D');
}
    
main()
.catch(error => console.error('Error: ', error));






