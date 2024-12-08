/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */

const dateNow = new Date();
console.log("Fecha Actual: ",dateNow);

const dateOfBirth = new Date(1993, 6, 21, 10, 30, 0, 0);
console.log("Fecha de Nacimiento: ",dateOfBirth)


const añosTranscurridos = dateNow.getFullYear() - dateOfBirth.getFullYear();
/*const mesesTranscurridos = dateNow.getMonth() - dateOfBrith.getMonth();
const diasTranscurridos = dateNow.getDate() - dateOfBrith.getDate();
const horasTranscurridas = dateNow.getHours() - dateOfBrith.getHours();
const minutosTranscurridos = dateNow.getMinutes() - dateOfBrith.getMinutes();
const segundosTranscurridos = dateNow.getSeconds() - dateOfBrith.getSeconds();*/

console.log("Años Transcurridos: ",añosTranscurridos);
/*console.log("Meses Transcurridos: ",mesesTranscurridos);
console.log("Días Transcurridos: ",diasTranscurridos);
console.log("Horas Transcurridas: ",horasTranscurridas);
console.log("Minutos Transcurridos: ",minutosTranscurridos);
console.log("Segundos Transcurridos: ",segundosTranscurridos);*/



/*console.log("Datos de la fecha actual:")
console.log("Año:", dateNow.getFullYear());      // Año actual
console.log("Mes:", dateNow.getMonth());         // Mes (0 a 11)
console.log("Día:", dateNow.getDate());          // Día del mes
console.log("Día de la semana:", dateNow.getDay());  // Día de la semana (0 a 6)
console.log("Hora:", dateNow.getHours());        // Hora
console.log("Minutos:", dateNow.getMinutes());   // Minutos
console.log("Segundos:", dateNow.getSeconds());  // Segundos
console.log("Milisegundos:", dateNow.getMilliseconds());  // Milisegundos
console.log("Timestamp:", dateNow.getTime());    // Milisegundos desde 1970

console.log("Datos de la fecha de nacimiento:")
console.log("Año:", dateOfBrith.getFullYear());      // Año actual
console.log("Mes:", dateOfBrith.getMonth());         // Mes (0 a 11)
console.log("Día:", dateOfBrith.getDate());          // Día del mes
console.log("Día de la semana:", dateOfBrith.getDay());  // Día de la semana (0 a 6)
console.log("Hora:", dateOfBrith.getHours());        // Hora
console.log("Minutos:", dateOfBrith.getMinutes());   // Minutos
console.log("Segundos:", dateOfBrith.getSeconds());  // Segundos
console.log("Milisegundos:", dateOfBrith.getMilliseconds());  // Milisegundos
console.log("Timestamp:", dateOfBrith.getTime());    // Milisegundos desde 1970


const fechaModificable = new Date();

fechaModificable.setFullYear(2025);       // Cambiar el año
fechaModificable.setMonth(5);             // Cambiar el mes (junio)
fechaModificable.setDate(15);             // Cambiar el día
fechaModificable.setHours(12);            // Cambiar la hora
fechaModificable.setMinutes(45);          // Cambiar los minutos
fechaModificable.setSeconds(30);          // Cambiar los segundos

console.log("Fecha Modificada:", fechaModificable);


const fechaFormateada = new Date();

console.log("ISO:", fechaFormateada.toISOString());  // Formato ISO
console.log("Fecha Local:", fechaFormateada.toLocaleDateString());  // Fecha local
console.log("Hora Local:", fechaFormateada.toLocaleTimeString());  // Hora local
console.log("Fecha y Hora Local:", fechaFormateada.toLocaleString());  // Todo en uno*/


//Formato ISO (Internacional)
console.log("ISO:", dateOfBirth.toISOString()); 
// Resultado: 1993-07-21T10:30:00.000Z

//Fecha Local (Idioma del Sistema)
console.log("Fecha Local:", dateOfBirth.toLocaleDateString()); 

//Hora Local
console.log("Hora Local:", dateOfBirth.toLocaleTimeString()); 

//Fecha y Hora Local
console.log("Fecha y Hora Local:", dateOfBirth.toLocaleString());

//Fecha en Formato Personalizado (Manual)
const dia = dateOfBirth.getDate();
const mes = dateOfBirth.getMonth() + 1; 
const anio = dateOfBirth.getFullYear();
console.log(`Fecha Personalizada: ${dia}-${mes}-${anio}`); 

//Día de la Semana y Fecha Completa (en Inglés)
const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
console.log("Día y Fecha Completa:", dateOfBirth.toLocaleDateString('en-US', opciones));

//Solo el Mes y el Año
console.log("Mes y Año:", `${dateOfBirth.getMonth() + 1}/${dateOfBirth.getFullYear()}`); 

//Formato UTC
console.log("UTC:", dateOfBirth.toUTCString()); 

//Timestamp (Milisegundos desde 1970)
console.log("Timestamp:", dateOfBirth.getTime()); 

//Día, Mes y Año en Cadena de Texto
const nombresMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
console.log(`Día, Mes y Año en Texto: ${dia} de ${nombresMeses[mes - 1]} de ${anio}`); 
