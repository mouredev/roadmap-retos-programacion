//1. función sin parámetros y sin return - Declaración de funciones
nombre = "Martín";

function saludar() {
  console.log(`!Hola ${nombre}`);
}

console.log(saludar());

//2. función con parámetros y return - Declaración de funciones
function suma(num1, num2) {
  return num1 + num2;
}

console.log(suma(43, 65));

//3. expresion function - función anonima
const square = function (number) {
  return number * number;
};

console.log(square(4));

//4. expresion function - función con nombre
const data = function dt(name, age, country) {
  return `Hola mi nombre es ${name}, tengo ${age} y soy de ${country}`;
};

console.log(data("Martín", 20, "Madrid"));

// 5. función flecha
const calcularArea = (ancho, alto) => {
  let area = ancho * alto;
  return area;
};

console.log(`El area es: ${calcularArea(23, 54)}`);

// 6. función flecha pero con 1 parámetro
const multiplicarNumero = (x) => x ** 3;

console.log(multiplicarNumero(10));

// 7. funcion como parámetro
const alerta = (fun, x) => {
  return alert(fun(x));
};

const saludaUsuario = (nombre = amigo) => {
  return `Hola ${nombre}`;
};

alerta(saludaUsuario, "Martín");

// DIFICULTAD EXTRA

const print_numbers = (text1, text2) => {
  let counter = 0;
  for (let i = 1; i < 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(text1 + text2);
    } else if (i % 3 == 0) {
      console.log(text1);
    } else if (i % 5 == 0) {
      console.log(text2);
    } else {
      console.log(i);
      counter++;
    }
  }
  console.log(
    `Las veces que se ha impreso el número en lugar de los textos: ${counter}`,
  );
};

console.log(print_numbers("texto1", "texto2"));
