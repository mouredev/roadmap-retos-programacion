// FUNCIONES Y ALCANCE
() => {}; // Función anónima
(a, b) => {}; // Función anónima con parámetros
(a, b) => {
  return a + b;
}; // Función anónima con parámetros y retorno

var num1 = 10;
var num2 = 6;

function suma() {
  return num1 + num2;
} // Función que suma dos números
console.log(suma());

function ejemplo() {
  return suma();
} // Función que llama a la función suma
console.log(ejemplo());

function usuario(nombre, apellido) {
  return nombre + " " + apellido;
} // Función que concatena dos strings
console.log(usuario("Jose", "Farias"));

var num7 = 10;
var num8 = 5;

function multiplicacion() {
  return num7 * num8;
} // Función que multiplica dos números y utiliza variables globales
console.log(multiplicacion());

function variable_saludar() {
  function saludar() {
    console.log("Hola, como estas?");
  }
  return saludar();
}
variable_saludar(); // Función que llama a otra función

function multiplicar() {
  var numero4 = 4;
  var numero5 = 5;
  return numero4 * numero5;
} // Función que multiplica dos números y declara dos variables locales

console.log(multiplicar());

console.log(typeof 2);

// Ejercicio
function ejercicio(num1, num2) {
  count = 0;

  for (var i = 0; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(num1 + num2);
    } else if (i % 3 === 0) {
      console.log(num1);
    } else if (i % 5 === 0) {
      console.log(num2);
    } else {
      console.log(i);
      count++;
    }
  }
  return count;
}

console.log(ejercicio("num1", "num2"));
