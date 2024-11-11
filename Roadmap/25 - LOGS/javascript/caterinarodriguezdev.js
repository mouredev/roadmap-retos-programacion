/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 */

console.log('Mensaje general 💚');
console.error('Mensaje de error 🔴');
console.warn('Mensaje de alerta 🚩');
console.info('Mensaje informativo ℹ️');
console.debug('Mensaje de depuración')
console.trace('Mensaje detallado sobre la ejecución del programa 🔢');

console.group('Lista de mensajes');
console.log('M1');
console.log('M2');
console.log('M3');
console.groupEnd();

console.time('tiempoEjecucion');
console.timeEnd('tiempoEjecucion');