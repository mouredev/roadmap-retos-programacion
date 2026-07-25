// Ejercicio de manejo de fechas en JavaScript

// PARTE 1: Crear variables de fecha y calcular años transcurridos

// Creamos la fecha actual
const fechaActual = new Date();

// Creamos una fecha de nacimiento (ejemplo)
const fechaNacimiento = new Date(1990, 4, 15, 14, 30, 0); // Mes 4 es Mayo (0-11)

// Calculamos los años transcurridos
const añosTranscurridos = fechaActual.getFullYear() - fechaNacimiento.getFullYear();

// Ajustamos si aún no hemos llegado al mes y día de nacimiento este año
if (
    fechaActual.getMonth() < fechaNacimiento.getMonth() || 
    (fechaActual.getMonth() === fechaNacimiento.getMonth() && 
     fechaActual.getDate() < fechaNacimiento.getDate())
) {
    añosTranscurridos--;
}

console.log("Fecha actual:", fechaActual.toLocaleString());
console.log("Fecha de nacimiento:", fechaNacimiento.toLocaleString());
console.log("Años transcurridos:", añosTranscurridos);

// PARTE 2: DIFICULTAD EXTRA - Formatear la fecha de 10 maneras diferentes

console.log("\nDIFERENTES FORMATOS DE FECHA:");

// 1. Día, mes y año
console.log("1. Día, mes y año:", fechaNacimiento.toLocaleDateString());

// 2. Hora, minuto y segundo
console.log("2. Hora, minuto y segundo:", fechaNacimiento.toLocaleTimeString());

// 3. Día del año
const inicioDeLAño = new Date(fechaNacimiento.getFullYear(), 0, 0);
const diff = fechaNacimiento - inicioDeLAño;
const unDiaEnMs = 1000 * 60 * 60 * 24;
const diaDelAño = Math.floor(diff / unDiaEnMs);
console.log("3. Día del año:", diaDelAño);

// 4. Día de la semana
const diasSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
console.log("4. Día de la semana:", diasSemana[fechaNacimiento.getDay()]);

// 5. Nombre del mes
const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
console.log("5. Nombre del mes:", meses[fechaNacimiento.getMonth()]);

// 6. Formato largo personalizado
console.log("6. Formato largo:", `${diasSemana[fechaNacimiento.getDay()]}, ${fechaNacimiento.getDate()} de ${meses[fechaNacimiento.getMonth()]} de ${fechaNacimiento.getFullYear()}`);

// 7. Formato ISO
console.log("7. Formato ISO:", fechaNacimiento.toISOString());

// 8. Formato de 12 horas
console.log("8. Formato 12 horas:", fechaNacimiento.toLocaleTimeString('es-ES', { hour12: true }));

// 9. Timestamp Unix
console.log("9. Timestamp Unix:", Math.floor(fechaNacimiento.getTime() / 1000));

// 10. Trimestre del año
const trimestre = Math.floor(fechaNacimiento.getMonth() / 3) + 1;
console.log("10. Trimestre del año:", trimestre);

// Función auxiliar para formatear números con ceros iniciales
function padZero(num) {
    return num.toString().padStart(2, '0');
}