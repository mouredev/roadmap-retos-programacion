/** #14 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Los objetos Date representan en JavaScript un momento fijo en el tiempo en un formato independiente.
*/

//---EJERCIÓ---

// Asi se representa las fechas en JavaScript
// Variable de la fecha actual (Hora Central)
const fecha = new Date();
console.log(fecha);

// Fecha en Mexico
console.log(fecha.toLocaleString());


// Variable de fecha de nacimiento
// Aquí se pone la fecha de nacimiento
const fecha_Nacimiento = new Date(1999, 11, 22, 20, 20, 0); // Le quito 1 dígito al mes para que este correctamente la fecha de nacimiento.
const diferenciaFechas = Date.now() - fecha_Nacimiento.getTime();
const añosTranscurridos = Math.floor(diferenciaFechas/ (365.25 * 24 * 60 * 60 * 1000));
console.log(añosTranscurridos);



/**-----DIFICULTAD EXTRA-----*/

//  Las variables de escritura
const days = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];


//  10 maneras diferentes de mostrar la fecha de nacimiento

console.log('1-. Dia, Mes, y Año de nacimiento', fecha_Nacimiento.toLocaleDateString());
console.log('2-. Dia de año', fecha_Nacimiento.getDate());
console.log('3-. Hora, Minutos y Segundos', fecha_Nacimiento.toLocaleTimeString());
console.log('4-. Mes de año', fecha_Nacimiento.getMonth() + 1); // Aquí le agrego 1 mas para que me el mes correcto.
console.log('5-. Dia de la semana' , (fecha_Nacimiento.getDay() > 7 
                ? days[fecha_Nacimiento.getDay() - 7 ] 
                : days[fecha_Nacimiento.getDay()]));
console.log('6-. Año de nacimiento', fecha_Nacimiento.getFullYear());
console.log('7-. Nombre del Mes de año', months[fecha_Nacimiento.getMonth()]);
console.log('8-. Fecha en Ingles', fecha_Nacimiento.toDateString());
console.log('9-. Tiempo en 24 horas', fecha_Nacimiento.toLocaleTimeString());
console.log('10-. Fecha Completa', fecha_Nacimiento.getDate(), 'de', months[fecha_Nacimiento.getMonth()], 'de', fecha_Nacimiento.getFullYear());

/**-----DIFICULTAD EXTRA-----*/