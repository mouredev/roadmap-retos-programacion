const birthDate = new Date(1979, 8, 16, 7, 30, 15);
const currentDate = new Date();

//Retorna edad
const añosTranscurridos = currentDate.getFullYear() - birthDate.getFullYear();

//Retorna fecha de nacimiento
const diaMesAñoNacimiento = birthDate.toLocaleDateString('es-es', {day: 'numeric', month: 'numeric', year: 'numeric'});

//Retorna hora del nacimiento
const horaMinutoSegundoNacimiento = birthDate.toLocaleTimeString('es-es', {hour: 'numeric', minute: 'numeric', second: 'numeric'});

//Retorna año de nacimiento
const añoNacimiento = birthDate.getFullYear();

//Retorna día de la semana del nacimiento
const diaNacimiento = birthDate.toLocaleDateString('es-es', {weekday: 'long'});

//Retorna mes del año del nacimiento
const mesNacimiento = birthDate.toLocaleDateString('es-es', {month: 'long'});

//Retorna fecha y hora
const horaLocal = birthDate.toLocaleString();

//Día del año
const inicioAño = new Date(birthDate.getFullYear(), 0, 0);
const diferencia = birthDate - inicioAño;
const dia = 86400000;
const diaAño = Math.floor(diferencia / dia);


console.log(añosTranscurridos);
console.log(diaMesAñoNacimiento);
console.log(horaMinutoSegundoNacimiento);
console.log(añoNacimiento);
console.log(diaNacimiento);
console.log(birthDate.getDate());
console.log(mesNacimiento);
console.log(horaLocal);
console.log(diaAño);
console.log(birthDate.toISOString());
console.log(birthDate.toUTCString());