// Obteniendo la fecha actual
var fechaActual = new Date();

// Especificando la fecha de nacimiento
var fechaNacimiento = new Date("1994-09-11T13:40:03");

// Calculando la diferencia de tiempo en milisegundos
var diferenciaTiempo = fechaActual - fechaNacimiento;

// Convirtiendo la diferencia de tiempo en años
var añosTranscurridos = Math.floor(
  diferenciaTiempo / (1000 * 60 * 60 * 24 * 365)
);

// Imprimiendo el resultado
console.log(
  "Han transcurrido " +
    añosTranscurridos +
    " años desde mi fecha de nacimiento."
);

// Ejercicio extra

console.log(
  "1. Día, mes y año:",
  fechaNacimiento.getDate(),
  fechaNacimiento.getMonth() + 1,
  fechaNacimiento.getFullYear()
);
console.log(
  "2. Hora, minuto y segundo:",
  fechaNacimiento.getHours(),
  fechaNacimiento.getMinutes(),
  fechaNacimiento.getSeconds()
);
console.log(
  "3. Día de año:",
  Math.ceil(
    (fechaNacimiento - new Date(fechaNacimiento.getFullYear(), 0, 0)) / 86400000
  )
);
console.log("4. Día de la semana:", fechaNacimiento.getDay());
console.log("5. Nombre del mes:", obtenerNombreMes(fechaNacimiento.getMonth()));

// Función para obtener el nombre del mes
function obtenerNombreMes(numeroMes) {
  var meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
  ];
  return meses[numeroMes];
}

// Formatos adicionales
console.log("6. Día del mes:", fechaNacimiento.getDate());
console.log("7. Año:", fechaNacimiento.getFullYear());
console.log("8. Hora:", fechaNacimiento.getHours());
console.log("9. Minuto:", fechaNacimiento.getMinutes());
console.log("10. Segundo:", fechaNacimiento.getSeconds());
