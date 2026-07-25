// Fechas 

const fechaFormat = (fecha) => {

    format = fecha.toLocaleString()
    return format

}

// Fecha Actual 

const fechaActual = new Date()
console.log(fechaActual)

const fechaActualFormat = fechaFormat(fechaActual)
console.log(fechaActualFormat)


const year = fechaActual.getFullYear();
const month = String(fechaActual.getMonth() + 1).padStart(2, '0');
const day = String(fechaActual.getDate()).padStart(2, '0');
const hour = String(fechaActual.getHours()).padStart(2, '0');
const minute = String(fechaActual.getMinutes()).padStart(2, '0');
const second = String(fechaActual.getSeconds()).padStart(2, '0');

console.log(`${day}-${month}-${year}  ${hour}:${minute}:${second}`)


// Fecha Nacimiento

const fechaNacimiento = new Date(2004, 10, 10, 15, 20)

const fechaNacimientoFormat = fechaFormat(fechaNacimiento)

console.log(fechaNacimientoFormat)


// Diferencia entre fechas

const diferencia = fechaActual - fechaNacimiento;
const diferenciaDias = Math.round(diferencia / (3.154e+10))

console.log(diferenciaDias)
