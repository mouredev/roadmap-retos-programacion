//Creacion de variables de tipo fecha
//fecha actual
const fechaActual = new Date();
//fecha nacimiento
const fechaNacimiento = new Date(2001,3,8,3,0,0);

// Cálculo de la diferencia en milisegundos
const diferenciaMilisegundos = fechaActual.getTime() - fechaNacimiento.getTime();

// Cálculo de la diferencia en años
const milisegundosEnUnAnio = 1000 * 60 * 60 * 24 * 365.25; // Incluye el ajuste de años bisiestos
const diferenciaAnios = diferenciaMilisegundos / milisegundosEnUnAnio;

// Imprimir resultados
console.log(`Fecha actual: ${fechaActual}`);
console.log(`Fecha de nacimiento: ${fechaNacimiento}`);
console.log(`Han transcurrido aproximadamente ${Math.floor(diferenciaAnios)} años entre ambas fechas.`);

//Otra opcion

// Fecha actual
const fechaActual2 = new Date();

// Fecha de nacimiento
const fechaNacimiento2 = new Date(2001, 3, 8, 3, 0, 0);

// Obtener los años de las fechas
const anioActual = fechaActual2.getFullYear();
const anioNacimiento = fechaNacimiento2.getFullYear();

// Calcular la diferencia en años
let diferenciaAnios2 = anioActual - anioNacimiento;

// Ajustar si el cumpleaños de este año aún no ha ocurrido
const mesActual = fechaActual2.getMonth();
const diaActual = fechaActual2.getDate();
const mesNacimiento = fechaNacimiento2.getMonth();
const diaNacimiento = fechaNacimiento2.getDate();

if (mesActual < mesNacimiento || (mesActual === mesNacimiento && diaActual < diaNacimiento)) {
    diferenciaAnios2--;
}

// Imprimir resultados
console.log(`Fecha actual: ${fechaActual2}`);
console.log(`Fecha de nacimiento: ${fechaNacimiento2}`);
console.log(`Han transcurrido aproximadamente ${diferenciaAnios2} años entre ambas fechas.`);


/****************************************/
//EXTRAAAA//
import { format } from 'date-fns';

// Fecha de nacimiento
const fechaNac = new Date(2001, 3, 8, 3, 0, 0); // 15 de mayo de 1999 a las 10:30:00

// 1. Día, mes y año
const formato1 = format(fechaNac, 'dd/MM/yyyy');
// 2. Hora, minuto y segundo
const formato2 = format(fechaNac, 'HH:mm:ss');
// 3. Día del año
const formato3 = format(fechaNac, 'DDD');
// 4. Día de la semana
const formato4 = format(fechaNac, 'EEEE');
// 5. Nombre del mes
const formato5 = format(fechaNac, 'MMMM');
// 6. Día del mes
const formato6 = format(fechaNac, 'do');
// 7. Año completo y corto
const formato7 = format(fechaNac, 'yyyy / yy');
// 8. Mes y año
const formato8 = format(fechaNac, 'MMMM yyyy');
// 9. Fecha y hora ISO 8601
const formato9 = fechaNac.toISOString();
// 10. Fecha y hora locales
const formato10 = fechaNac.toLocaleString();

console.log(`1. Día, mes y año: ${formato1}`);
console.log(`2. Hora, minuto y segundo: ${formato2}`);
console.log(`3. Día del año: ${formato3}`);
console.log(`4. Día de la semana: ${formato4}`);
console.log(`5. Nombre del mes: ${formato5}`);
console.log(`6. Día del mes: ${formato6}`);
console.log(`7. Año completo y corto: ${formato7}`);
console.log(`8. Mes y año: ${formato8}`);
console.log(`9. Fecha y hora ISO 8601: ${formato9}`);
console.log(`10. Fecha y hora locales: ${formato10}`);
