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

// EJERCICIO:
const date = new Date();
const options = {
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
};

// Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
const fechaActual = date.toLocaleString("es-AR", options);
console.log(fechaActual);

// Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
const fechaNacimiento = new Date(2000, 7, 3, 7, 30, 10);
console.log(fechaNacimiento);

// Calcula cuántos años han transcurrido entre ambas fechas.
function aniosTranscurridos(fechaNac) {
  const hoy = new Date();
  const nacimiento = new Date(fechaNac);

  let edad = hoy.getFullYear() - nacimiento.getFullYear();
  let mes = hoy.getMonth() - nacimiento.getMonth();
  if (mes < 0 || (mes === 0 && hoy.getDate() < nacimiento.getDate())) {
    edad--;
  }
  return edad;
}

const fechaNac = "2000-08-03";
console.log(`Años transcurridos: ${aniosTranscurridos(fechaNac)}`);

// DIFICULTAD EXTRA:
// 1
console.log(fechaNacimiento.toLocaleString("es-AR"));
// 2
console.log(fechaNacimiento.toLocaleDateString("es-AR"));
// 3
console.log(fechaNacimiento.toLocaleTimeString("es-AR"));
// 4
console.log(fechaNacimiento.toISOString());
// 5
console.log(fechaNacimiento.toUTCString());
// 6
const optionsMonthYear = { year: "numeric", month: "long" };
console.log(fechaNacimiento.toLocaleString("es-AR", optionsMonthYear));
// 7
const option = {
  year: "numeric",
  month: "long",
  day: "numeric",
  weekday: "long",
  hour: "numeric",
  minute: "numeric",
  second: "numeric",
};
console.log(fechaNacimiento.toLocaleString("es-AR", option));
// 8
const optionsDayMonth = { day: "numeric", month: "long" };
console.log(fechaNacimiento.toLocaleString("es-AR", optionsDayMonth));
// 9
const year = fechaNacimiento.getFullYear();
const month = String(fechaNacimiento.getMonth() + 1).padStart(2, "0");
const day = String(fechaNacimiento.getDate()).padStart(2, "0");
console.log(`${year}-${month}-${day}`);
// 10
const hours = String(fechaNacimiento.getHours()).padStart(2, "0");
const minutes = String(fechaNacimiento.getMinutes()).padStart(2, "0");
const seconds = String(fechaNacimiento.getSeconds()).padStart(2, "0");
console.log(`${hours}:${minutes}:${seconds}`);
