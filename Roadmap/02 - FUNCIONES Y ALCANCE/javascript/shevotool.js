// Funciones básicas
function caminar() {
  console.log("Hola");
}
caminar();

function ejercitarse(caminarP, correrP) {
  return { trotar: caminarP, correr: correrP };
}
const { trotar, correr } = ejercitarse("hiking", "pista");
console.log(trotar);
console.log(correr);

function entrenar() {
  caminar();
  return "Entrenamiento completado";
}
console.log(entrenar());

function tareas() {
  function lavar() {
    console.log("Lavar la ropa");
  }
  lavar();
}
tareas();

//Funciones ya creadas en el lenguaje

// Function declarations
function sumar(a, b) {
  return a + b;
}
console.log(sumar(3, 4));

// Function expresion
const restar = function (a, b) {
  return a - b;
};
console.log(restar(10, 5));

// Arrow function
const multiplicar = (a, b) => a * b;
console.log(multiplicar(3, 4));

// Callback
function hacerEjercicio(callback) {
  console.log("Empezando ejercicio");
  callback();
}
hacerEjercicio(caminar);

// Variable LOCAL y GLOBAL
let apodo = "Ramone"; // variable global

function saludar(persona) {
  let saludo = "Hola"; // variable local
  return `Hola ${persona} ${apodo}`;
}
console.log(saludar("Jonny"));

// DIFICULTAD EXTRA

function textoANumero(parametro1, parametro2) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(parametro1 + parametro2);
    } else if (i % 3 === 0) {
      console.log(parametro1);
    } else if (i % 5 === 0) {
      console.log(parametro2);
    } else {
      contador++;
    }
  }
  return contador;
}
console.log(textoANumero("Fizz", "Buzz"));
