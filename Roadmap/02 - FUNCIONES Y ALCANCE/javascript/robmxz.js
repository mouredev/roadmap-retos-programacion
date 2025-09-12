/*#02 FUNCIONES Y ALCANCE*/

// Funciones sin argumentos
function noArgs() {
  console.log("Hola Mundo");
}
noArgs();
console.log("-".repeat(30));

// Funciones con un argumento
function oneArg(arg) {
  console.log(`Hola ${arg}`);
}
oneArg("RobMxz");
console.log("-".repeat(30));

// Funciones con varios argumentos
function variosArgs(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
}
variosArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
console.log("-".repeat(30));

// Funciones anidadas
function Anidada(arg1) {
  return function Anidada2(arg2) {
    return arg1 + arg2;
  };
}
console.log(Anidada(2)(3));
console.log("-".repeat(30));

// Variables globales y locales
var a = 10;

function global() {
  console.log(a);
}
global();
console.log("-".repeat(30));

function local() {
  var a = 20;
  console.log(a);
}
local();
console.log("-".repeat(30));

// Funciones flecha

// Funciones flecha sin argumentos
const noArgs2 = () => console.log("Hola Mundo");
noArgs();
console.log("-".repeat(30));

// Funciones flecha con un argumento
const oneArg2 = (arg) => console.log(`Hola ${arg}`);
oneArg("Comunidad");
console.log("-".repeat(30));

// Funciones flecha con varios argumentos
const variosArgs2 = (...args) => {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
};
variosArgs("Hola", "Mundo", "¿", "Como", "Estan", "?");
console.log("-".repeat(30));

// Funciones flecha anidadas
const Anidada2 = (arg1) => (arg2) => arg1 + arg2;
console.log(Anidada2(2)(3));
console.log("-".repeat(30));

// Variables globales y locales en funciones flecha
const global2 = () => console.log(a);
global2();
console.log("-".repeat(30));

const local2 = () => {
  var a = 20;
  console.log(a);
};

// Dificultad extra :)

/*
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    -La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    -Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    -Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    -Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    -La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function extra(arg1, arg2) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    console.log(i);
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(arg1, arg2);
      continue;
    }
    if (i % 3 == 0) {
      console.log(arg1);
      continue;
    }
    if (i % 5 == 0) {
      console.log(arg2);
      continue;
    }
    contador++;
  }
  return contador;
}
console.log(
  "Número de veces que se ha impreso el número:",
  extra("Retos de Programación", "JavaScript")
);
