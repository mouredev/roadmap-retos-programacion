/*
🔥 EJERCICIO:
Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
asíncrona una función que tardará en finalizar un número concreto de
segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará
su ejecución y cuando finaliza.
*/
// Función asíncrona parametrizable
function ejecutarTarea(nombre, duracion) {
  console.log(`${nombre} empieza. Durará ${duracion} segundos.`);
  return new Promise((resolve) => {
      setTimeout(() => {
          console.log(`${nombre} ha finalizado.`);
          resolve();
      }, duracion * 1000); // Seg a Miliseg
  });
}

ejecutarTarea("Tarea de ejemplo", 5);
// Tarea de ejemplo empieza. Durará 5 segundos.
// Tarea de ejemplo ha finalizado.

/* --------------------------------------------------------------------------------------
🔥 DIFICULTAD EXTRA (opcional):
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundo.
- Una función D que dura 1 segundo.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han
finalizado.
*/

// Reutilizamos : ejecutarTarea()
async function programaPrincipal() {
  console.log("Iniciando programa...");

  // Ejecutar en paralelo
  const tareaC = ejecutarTarea("Función C", 3);
  const tareaB = ejecutarTarea("Función B", 2);
  const tareaA = ejecutarTarea("Función A", 1);

  // Esperar a que C, B y A terminen
  await Promise.all([tareaC, tareaB, tareaA]);

  // Ejecutar D después de que C, B y A hayan terminado
  await ejecutarTarea("Función D", 1);

  console.log("Programa finalizado.");
}

programaPrincipal();

// S A L I D A

// Iniciando programa...
// Función C empieza. Durará 3 segundos.
// Función B empieza. Durará 2 segundos.
// Función A empieza. Durará 1 segundos.
// Función A ha finalizado.
// Función B ha finalizado.
// Función C ha finalizado.
// Función D empieza. Durará 1 segundos.
// Función D ha finalizado.
// Programa finalizado.
// Tarea de ejemplo ha finalizado.