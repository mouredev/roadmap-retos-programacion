// Función sin parámetros ni retorno
function saludar() {
  console.log("¡Hola, mundo!");
}

saludar();

// Función con un parámetro y retorno
function cuadrado(numero) {
  return numero ** 2;
}

let resultadoCuadrado = cuadrado(5);
console.log("El cuadrado de 5 es:", resultadoCuadrado);

// Función con varios parámetros y retorno
function suma(a, b) {
  return a + b;
}

let resultadoSuma = suma(3, 7);
console.log("La suma de 3 y 7 es:", resultadoSuma);

// Función dentro de otra función
function operacionCompleja(x, y) {
  function multiplicar(a, b) {
    return a * b;
  }

  let resultadoMultiplicacion = multiplicar(x, y);
  return resultadoMultiplicacion + 10;
}

let resultadoOperacion = operacionCompleja(2, 3);
console.log("El resultado de la operación compleja es:", resultadoOperacion);

// Variable local y global
let variableGlobal = 10;

function funcionConVariables() {
  let variableLocal = 5;
  console.log("Variable local dentro de la función:", variableLocal);
  console.log("Variable global dentro de la función:", variableGlobal);
}

funcionConVariables();

// Intentar acceder a variableLocal aquí daría un error, ya que es local a la función.
// console.log("Intento de acceder a variableLocal fuera de la función:", variableLocal);
console.log("Variable global fuera de la función:", variableGlobal);

// Ejercicio extra
function imprimirNumerosYContarTextos(texto1, texto2) {
  let contadorTextos = 0;

  for (let numero = 1; numero <= 100; numero++) {
    if (numero % 3 === 0 && numero % 5 === 0) {
      console.log(texto1 + texto2);
      contadorTextos++;
    } else if (numero % 3 === 0) {
      console.log(texto1);
      contadorTextos++;
    } else if (numero % 5 === 0) {
      console.log(texto2);
      contadorTextos++;
    } else {
      console.log(numero);
    }
  }

  return contadorTextos;
}

let resultado = imprimirNumerosYContarTextos("Fizz", "Buzz");
console.log(`Se imprimieron ${resultado} textos en total.`);
