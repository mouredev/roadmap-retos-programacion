// Función simple sin parametros ni retorno
function GetName() {
  console.log("Estoy obteniendo el nombre");
}
GetName();

// Función con un parametro y sin retorno
function GetMyName(name) {
  console.log(name);
}
GetMyName("Paloma");

// Función con dos parametros y con retorno
function GetMyFullName(name, lastName) {
  return `${name} ${lastName}`;
}
console.log(GetMyFullName("Paloma", "San Basilio"));

// Función tipo flecha
let getMyFullNameFlecha = (name, lastName) => `${name} ${lastName}`;
console.log(getMyFullNameFlecha("Paloma", "San Basilio"));

// Función dentro de otra función
function PaintMyColors() {
  function GetMyColors() {
    const color1 = "red";
    const color2 = "pink";
    return [color1, color2];
  }
  const myColors = GetMyColors();
  return myColors;
}
console.log(PaintMyColors());

// Función autoinvocada
(function () {
  function GetMyColors() {
    const color1 = "Light green";
    const color2 = "pink";
    return [color1, color2];
  }

  const myColors = GetMyColors();
  console.log(myColors);
})();

// Funciones de sistema

function miPuntuacion() {
  return Math.floor(7.89); // retorna el máximo entero menor o igual aun numerp
}
console.log(miPuntuacion());

function miNota() {
  return Math.round(7.89); // retorna el valor de un número redondeado al entero más cercano.
}
console.log(miNota());

// Variable global

let pacientes = [];
function agregarPaciente(nombre, edad, sexo) {
  pacientes.push({ nombre, edad, sexo });
}
agregarPaciente("Juan", 25, "Masculino");
console.log(pacientes);

// variable local
function MostrarPaciente(nombre, edad, sexo) {
  let fichaPaciente = `Nombre: ${nombre}, Edad: ${edad}, Sexo: ${sexo}`;
  console.log(fichaPaciente);
}
MostrarPaciente("Lady Gaga", 38, "femenino"); // imprime la ficha paciente

// reto extra
function misNumero(a, b) {
  a = " soy múltiplo de 3"; 
  b = " soy múltiplo de 5";
  
  let count = 0
  for (let i = 0; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(i + `${a} y${b}`);
      count++;
    } else if (i % 3 === 0) {
      console.log(i + a);
      count++;
    } else if (i % 5 === 0) {
      console.log(i + b);
      count++;
    }
  }
  console.log(`El número se ha impreso ${count} veces`);
  return count;
}
misNumero(0, 0);

