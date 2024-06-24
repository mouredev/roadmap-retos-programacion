/** #25 - JavaScript ->Jesus Antonio Escamilla */

/**
 * El concepto de "logging" en JavaScript se refiere al proceso de registrar información
 * sobre la ejecución de un programa. Esto es crucial para el desarrollo y mantenimiento
 * de software, ya que ayuda a los desarrolladores a entender lo que está sucediendo en
 * su código en tiempo real, diagnosticar errores y mejorar el rendimiento.
 */

//---EJERCIÓ---
// Registra un mensaje informativo en la consola
console.log('Esto es un mensaje informativo');

// Es un mensaje error en consola
console.error('Error en la linea xx, corregirla');

// Advertencia del código en la consola
console.warn('Alto aun no has declaro la variable');

// Un mensaje informativo en la consola (similar al `console.log`)
console.info('Te informo que esta quedando super');

// Mensaje depuración en la consola (no siempre esta disponible en todos los navegadores)
console.debug('Mensaje Depurador en tu Proyecto');

// Muestra datos tabulares como tabla en la consola
const usuario = [
    { nombre: 'Jesus', edad: 24},
    { nombre: 'Fatima', edad: 20}
];
console.table(usuario);

// Agrupa los mensajes en la consola
console.group('Detalles del Usuario');
console.log('Nombre: Antonio');
console.log('Edad: 24');
console.groupEnd();



/**-----DIFICULTAD EXTRA-----*/

// Pendiente

/**-----DIFICULTAD EXTRA-----*/