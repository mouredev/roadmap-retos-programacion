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
const fecha_Nacimiento = new Date(1999, 12, 22, 22, 30, 1, 2); // Aquí se pone la fecha de nacimiento
const diferenciaFechas = Date.now() - fecha_Nacimiento.getTime();
const añosTranscurridos = Math.floor(diferenciaFechas/ (1000 * 60 * 60 * 24 * 365.5));
console.log(añosTranscurridos);



/**-----DIFICULTAD EXTRA-----*/
//Pendientes
/**-----DIFICULTAD EXTRA-----*/