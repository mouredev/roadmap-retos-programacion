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

//Calcular años desde el nacimiento
function calculateYearsSinceBirthday(birthDay) {
  console.log("EJERCICIO");
  let currentDate = new Date();
  let resultado = "";
  //La fecha de nacimiento no puede ser mayor que la fecha actual
  if (birthDay > currentDate) {
    console.log(
      "La fecha de nacimiento no puede ser mayor que la fecha actual"
    );
    return;
  }

  //Comparar la fecha dia/mes para saber si ya pasó o no en este año
  let fecha = new Date(currentDate.getFullYear(), birthDay.getMonth(), birthDay.getDate(), birthDay.getHours())

if (fecha <= currentDate)
  resultado = currentDate.getFullYear() - birthDay.getFullYear();
else
  resultado = currentDate.getFullYear() - birthDay.getFullYear() - 1; 
  console.log(`Han transcurrido ${resultado} años desde tu nacimiento`);
}

//Mostrar la fecha de nacimiento en 10 formatos diferentes
function showDateInDifferentFormats(yourDate) {
  console.log("\n10 Formas de ver la fecha de nacimiento");
  console.log("1", yourDate);
  console.log("2", yourDate.toDateString());
  console.log("3", yourDate.toISOString());
  console.log("4", yourDate.toUTCString());
  console.log("5", yourDate.toLocaleDateString());
  console.log("6", yourDate.toLocaleString());
  console.log("7", yourDate.getDay());
  console.log("8", yourDate.getHours());
  console.log("9", yourDate.toTimeString());
  console.log(
    "10",
    `Año: ${yourDate.getFullYear()}, Mes: ${
      yourDate.getMonth() + 1
    }, Dia: ${yourDate.getDate()}`
  );
}

//Ejecucion
let birthDay = new Date(1980, 5, 13, 6); //13  de Junio de 1980 a las 6am
calculateYearsSinceBirthday(birthDay);
showDateInDifferentFormats(birthDay);
