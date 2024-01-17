//Funciones declarativas

/*Sin Argumentos ni Retorno*/
function saludo() {
  console.log("Hola");
}

/*Con Argumentos*/
function saludoExtendido(nombre) {
  console.log("Hola" + " " + nombre);
}

/*Con Retorno*/
function suma(a, b) {
  return a + b;
}

console.log(suma(4, 6));

//Funciones expresivas

let diHola = function () {
  console.log("Hola");
}

//Funciones arrow

let resta = (a, b) => a - b;

console.log(resta(5, 2));

//Funciones dentro de funciones

function solicitudDeNombre() {
  let nombre = prompt("Dinos tu nombre", "Luis");
  return nombre;
}

function saludo() {
  console.log("Hola" + " " + solicitudDeNombre());
}

//Función creada en el lenguaje

/*prompt() es una función propia de javascript al igual que console.log(), etc..*/
let nombre = prompt("Dinos tu nombre", "Luis");

//Ámbito de variables

/*Variable global edad está disponible de ser usada en otro lugar del código
actual*/
let edad = prompt("Ingresa tu edad", "30");

/*Variable local edad solo está disponible dentro de una función */
function edadUsuario() {
  let edad = prompt("Ingresa tu edad", "30");
  console.log("La edad ingresada es: " + edad + "años.");
}

//Dificultad extra

function stringsAndNumbers(txt1, txt2) {
  let count = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(txt1 + " " + txt2);
    } else if (i % 5 === 0) {
      console.log(txt2);
    } else if (i % 3 === 0) {
      console.log(txt1);
    } else {
      console.log(i);
      count++;
    };
  }
  return count;
}