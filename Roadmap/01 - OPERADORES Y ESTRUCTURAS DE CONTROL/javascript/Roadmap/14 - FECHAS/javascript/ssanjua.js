
const fechaActual = new Date();
const fechaNacimiento = new Date("1991-04-15T16:30:00"); 

const diferenciaEnMilisegundos = fechaActual - fechaNacimiento;
const diferenciaEnAños = diferenciaEnMilisegundos / (1000 * 60 * 60 * 24 * 365.25); 

// Día, mes y año
console.log(`mi nacimiento fue: ${fechaNacimiento.getDate()}/${fechaNacimiento.getMonth() + 1}/${fechaNacimiento.getFullYear()}`);

// Hora, minuto y segundo
console.log(`la hora de mi nacimiento fue: ${fechaNacimiento.getHours()}:${fechaNacimiento.getMinutes()}:${fechaNacimiento.getSeconds()}`);

// Día del año
const inicioAño = new Date(fechaNacimiento.getFullYear(), 0, 0);
const diferencia = fechaNacimiento - inicioAño;
const unDia = 1000 * 60 * 60 * 24;
const diaDelAño = Math.floor(diferencia / unDia);
console.log(`pasaron ${diaDelAño} del año 1991 y nací`);

// Día de la semana
const diasDeLaSemana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
console.log(diasDeLaSemana[fechaNacimiento.getDay()]);

// Nombre del mes
const mesesDelAño = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
console.log(`nací un ${diasDeLaSemana[fechaNacimiento.getDay()]}.`);

// - Año en formato de dos dígitos
console.log(`soy modelo ${fechaNacimiento.getFullYear().toString().slice(-2)}`);

// - Fecha en formato ISO
console.log(`formato ISO: ${fechaNacimiento.toISOString()}`);

// - Fecha larga
console.log(fechaNacimiento.toLocaleDateString("es-ES", {weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'}));

// - Hora en formato 12 horas
const horas = fechaNacimiento.getHours();
const minutos = fechaNacimiento.getMinutes();
console.log(`${horas % 12 || 12}:${minutos < 10 ? '0' + minutos : minutos} ${horas < 12 ? 'AM' : 'PM'}`);

// - Marca de tiempo UNIX
console.log(`desde el 1 de enero de 1970 pasaron ${Math.floor(fechaNacimiento.getTime() / 1000)} segundos`);