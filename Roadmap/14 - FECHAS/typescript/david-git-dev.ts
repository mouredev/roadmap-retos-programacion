const now = new Date(Date.now()).getFullYear();
const birthDate = new Date("1999-06-13").getFullYear();
let age = now - birthDate;
console.log("han pasado->", age, "años");
//dificultad extra
const birthDateX = new Date("1999-06-13");
const fechas = {
  formato1: `${birthDateX.getDate()}-${birthDateX.getDay()}-${birthDateX.getFullYear()}`,
  formato2: `${birthDateX.getTime()}->milisegundos han pasado desde tu nacimiento`,
  formato3: `${birthDateX.getUTCFullYear()}-> welcome to earth boy!!`,
  formato4: `${birthDateX.toISOString()}->tu fecha en formato iso`,
  formato5: birthDateX.toLocaleString(),
  formato6: birthDateX.toLocaleTimeString(),
  formato7: birthDateX.toString(),
  formato8: birthDateX.toTimeString(),
  formato9: birthDateX.toUTCString(),
  formato10: `${birthDateX.getDay()}/${birthDateX.getMonth()}/${birthDateX.getFullYear()}`
};
console.log(fechas);
