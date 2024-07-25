let fecha = new Date();
console.log(fecha);

let miFecha = new Date(1990, 11, 8, 4, 11, 11);
console.log(miFecha);


function años (fecha, miFecha) {
    let tiempoEnMs = fecha - miFecha;
    let tiempoPasado = tiempoEnMs / (1000 * 60 * 60 * 24 * 365);
    tiempoPasado = Math.floor(tiempoPasado);
    return tiempoPasado;
}

console.log(años(fecha, miFecha));

//EXTRA
console.log("Día, mes y año:", miFecha.getDate(), "/" + (miFecha.getMonth() + 1), "/" + miFecha.getFullYear());
console.log("Hora, minutos y segundos:", miFecha.getHours() + ":" + miFecha.getMinutes() + ":" + miFecha.getSeconds());
console.log("Día de año:", Math.floor((miFecha - new Date(miFecha.getFullYear(), 0, 0)) / (1000 * 60 * 60 * 24)));
let diaSemana = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado"]
console.log("Día de la semana:", diaSemana[miFecha.getDay()]);
let nombreMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
console.log("Mes de año:" , nombreMes[miFecha.getMonth()])
