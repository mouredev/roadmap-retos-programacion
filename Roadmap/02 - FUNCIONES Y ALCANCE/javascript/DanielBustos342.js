//* Funcion declarada: se define utilizando la palabra clave `function` seguida del nombre de la funcion. Las funciones declaradas se pueden llamar antes de su definicion debido al "hoisting"

function sayHello() {
  console.log("Hello, world!");
}

// Llamando a la función
sayHello(); // Imprime "Hello, world!"

//? Hoisting: es un comportamiento de javaScript donde las declaraciones de variables y funciones son movidas automaticamente al comienzo de su contexto de ejecucion(el contexto actual de la funcion o del script) antes de que el codigo real sea ejecutado. Esto significa que puedes utilizar varialbes y funciones antes de declararlas en el codigo.

//* Hoisting de Funciones: las declaraciones de funciones en javaScript son completamente elevadas (hoisted) a la parte superior del contexto de ejecucion. Esto permite llamar a las funciones antes de su declaracion en el codigo.

// Llamada a la función antes de su declaración
greet();

function greet() {
  console.log("Hello, world!");
}

// Salida: "Hello, world!"

//* Hoisting de Variables: las declaraciones de variables con 'var' tambien son elevadas al inicio del contexto, pero solo la declaracion, no la asignacion. Esto puede llevar a comportamientos inesperados.

console.log(a); // Salida: undefined
var a = 5;
console.log(a); // Salida: 5

//* Hoisting con 'let' y 'const': las variables con 'let' y 'const' tambien son elevadas, pero no estan inicializadas. Intentar accedere a ellas antes de la declaracion resultara en un error de referencia(ReferenceError).

//console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 10;

//console.log(c); // ReferenceError: Cannot access 'c' before initialization
const c = 20;

//* Hoisting con Funciones expresadas y funciones de flecha: las funciones expresadas y las funciones flecha no son elevadas de la misma manera que las funciones declaradas. Solo la declaracion de la variable que contiene la funcion es elevada, no la definicion de la funcion.

// Función expresada
//console.log(sum); // Salida: undefined
var sum = function () {
  console.log("Sum function");
};
sum(); // Salida: "Sum function"

// Función flecha
console.log(multiply); // Salida: undefined
var multiply = () => {
  console.log("Multiply function");
};
multiply(); // Salida: "Multiply function"

//* Funcion Expresada: las funciones expresadas se definen asignando una funcion anonima a una variable. A diferencia de las funciones declaradas, las funciones expresadas no se elevan.

const sayHello1 = function () {
  console.log("Hola, mundo! --> Funcion expresada");
};

// Llamando a la función
sayHello1(); // Imprime "Hello, world!"

//* Funcion flecha: las funciones flecha son una forma mas conocida de escribir funciones en javaScript. Se definen utilizando la sintaxis '=>'.

const sayHello2 = () => {
  console.log("Hola, mundo! --> Funcion flecha");
};

// Llamando a la función
sayHello2(); // Imprime "Hello, world!"

//! Funciones sin parametros ni retorno:
console.log("Funciones sin parametros ni retorno");
//* Mostrar un mensaje: una funcion que simplemente imprime un mensaje en la consola.

function greet1() {
  console.log("Hola!!, Bienvenido a JavaScript! ");
}

greet1(); // Imprime "Hola!!, Bienvenido a JavaScript!"

//* Mostrar Hora actual

const showCurrentTime = () => {
  const now = new Date();
  console.log(`La hora actual es: ${now.toLocaleTimeString()}`);
};

showCurrentTime(); // Imprime la hora actual en formato local

//* Realizar una Operacion matematica

function addTwoNumbers() {
  const a = 5;
  const b = 3;
  console.log(`The sum is: ${a + b}`);
}

addTwoNumbers(); // Imprime "The sum is: 8"

//* Actualizar el contenido de una pagina web

// function updateContent() {
//   document.getElementById("content").innerText = "Content has been updated!";
// }

// // Llamando a la función
// updateContent();

//* Configurar un temporizador

function showAlert() {
  console.log("Esta es una alerta temporizada!");
  //   alert("Esta es una alerta temporizada!");
}

// Llamando a la función después de 3 segundos
setTimeout(showAlert, 3000);

//! Funciones con uno o varios parametros:
console.log("Funciones con uno o varios parametros");

//* Funcion con un parametro:
//* funcion que saluda a una persona
function greet2(name) {
  console.log(`Hello, ${name}!`);
}
// Llamando a la función con un parámetro
greet2("Alice"); // Imprime "Hello, Alice!"
greet2("Bob"); // Imprime "Hello, Bob!"

//* Funciones con varios parametros
//* funcion que suma dos numeros
function add(a, b) {
  return a + b;
}

// Llamando a la función con dos parámetros
console.log(add(3, 4)); // Imprime 7
console.log(add(10, 5)); // Imprime 15

//* Funcion que multiplica tres numeros
function multiply1(x, y, z) {
  return x * y * z;
}

// Llamando a la función con tres parámetros
console.log(multiply1(2, 3, 4)); // Imprime 24
console.log(multiply1(1, 5, 6)); // Imprime 30

//* Funcion con parametros predeterminados: los parametros predeterminados permiten asignar valores por defecto a los parametros en caso de que no pasen argumentos durante la llamada de la funcion.
//* Funcion con un parametro determinado
function greet3(name = "Guest") {
  console.log(`Hello, ${name}!`);
}

// Llamando a la función sin pasar un argumento
greet3(); // Imprime "Hello, Guest!"
// Llamando a la función con un argumento
greet3("Alice"); // Imprime "Hello, Alice!"

//* Funciones con un numero variable de parametros: puedes usar el objeto `arguments` o el operador de propagacion (`...`) para manejar un numero de variables de parametros.
//* Funcion que suma un numero variable de argumentos usando el operador de propagacion.
function sum1(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

// Llamando a la función con diferentes números de argumentos
console.log(sum1(1, 2, 3)); // Imprime 6
console.log(sum1(4, 5, 6, 7)); // Imprime 22

//* Funcion flecha con parametros: las funciones flecha ('=>') proporcionan una sintaxis mas consisa para definir funciones.
//* Funcion flecha que resta dos numeros.
const subtract = (a, b) => a - b;

// Llamando a la función con dos parámetros
console.log(subtract(10, 3)); // Imprime 7
console.log(subtract(5, 2)); // Imprime 3

//! Funciones con retorno:
console.log("Funciones con retorno");

//* Funcion que suma dos numeros
function add1(a, b) {
  return a + b;
}

let result = add1(3, 4); // Llamando a la función y almacenando el resultado
console.log(result); // Imprime 7

//* Funcion que verifica si un numero es par
function isEven(number) {
  return number % 2 === 0;
}

console.log(isEven(4)); // Imprime true
console.log(isEven(7)); // Imprime false

//* Funcion que devuelve el valor absoluto de un numero
function absoluteValue(num) {
  if (num < 0) {
    return -num;
  }
  return num;
}

console.log(absoluteValue(-5)); // Imprime 5
console.log(absoluteValue(3)); // Imprime 3

//* Funcion que devuelve el mayor de dos numeros
function max(a, b) {
  if (a > b) {
    return a;
  }
  return b;
}

console.log(max(10, 20)); // Imprime 20
console.log(max(50, 30)); // Imprime 50

//* Funcion que calcula el factorial de un numero
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(5)); // Imprime 120
console.log(factorial(3)); // Imprime 6

//* Funcion que devuelve una cadena en mayusculas
function toUpperCase(str) {
  return str.toUpperCase();
}

console.log(toUpperCase("hello")); // Imprime "HELLO"
console.log(toUpperCase("world")); // Imprime "WORLD"

//* Funcion que concatena dos cadenas
function concatenate(str1, str2) {
  return str1 + " " + str2;
}

console.log(concatenate("Hello", "World")); // Imprime "Hello World"
console.log(concatenate("Good", "Morning")); // Imprime "Good Morning"

//* Funcion flecha que multiplica dos numeros
const multiply2 = (a, b) => {
  return a * b;
};

console.log(multiply2(3, 4)); // Imprime 12
console.log(multiply2(5, 6)); // Imprime 30

//* Funcion flecha que devuelve el cuadrado de un numero
const square = (x) => x * x;

console.log(square(5)); // Imprime 25
console.log(square(8)); // Imprime 64

//* Funcion que retorna un objeto
function createPerson(name, age) {
  return {
    name: name,
    age: age,
  };
}

let person = createPerson("Alice", 25);
console.log(person); // Imprime { name: 'Alice', age: 25 }

//! Funciones dentro de funciones: en js puedes definir funciones dentro de otras funciones. Esto se conoce como funciones anidadas. Las funciones internas tienen acceso a las variables y parametros de las funciones externas, lo que permite un encapsulacion y modularidad mas efectivas.

console.log("Funciones dentro de funciones");
//* Funcion Anidada simple:
function outerFunction(x) {
  console.log("Outer function");

  function innerFunction(y) {
    console.log("Inner function");
    return x + y;
  }

  return innerFunction;
}

const inner = outerFunction(5);
console.log(inner(10)); // Imprime 15

//* Funcion que calcula el area y el perimetro de un rectangulo
function rectangleMetrics(length, width) {
  function calculateArea() {
    return length * width;
  }

  function calculatePerimeter() {
    return 2 * (length + width);
  }

  return {
    area: calculateArea(),
    perimeter: calculatePerimeter(),
  };
}

const metrics = rectangleMetrics(5, 3);
console.log(`Area: ${metrics.area}`); // Imprime "Area: 15"
console.log(`Perimeter: ${metrics.perimeter}`); // Imprime "Perimeter: 16"

//* Funcion de cierre (Closure): un cierre es una funcion interna que tiene acceso a las variables de la funcion externa, incluso despues de que la funcion externa haya finalizado su ejecucion.
function counter() {
  let count = 0;

  return function () {
    count++;
    return count;
  };
}

const increment = counter();
console.log(increment()); // Imprime 1
console.log(increment()); // Imprime 2
console.log(increment()); // Imprime 3

//* Funcion que genera otras funciones: en este ejemplo, la funcion externa "makeMultiplier" genera y devuelve una funcion interna que multiplica su argumento por un factor especifico.
function makeMultiplier(multiplier) {
  return function (x) {
    return x * multiplier;
  };
}

const double = makeMultiplier(2);
const triple = makeMultiplier(3);

console.log(double(5)); // Imprime 10
console.log(triple(5)); // Imprime 15

//* Funcion anudada con parametros: en este ejemplo, las funciones internas utilizan parametros para realizar calculos especificos.
function calculateHypotenuse(a, b) {
  function square(x) {
    return x * x;
  }

  return Math.sqrt(square(a) + square(b));
}

console.log(calculateHypotenuse(3, 4)); // Imprime 5
console.log(calculateHypotenuse(5, 12)); // Imprime 13

//* Funcion que filtra y mapea valores: en este ejemplo, la funcion externa "filterAndMap" tiene dos funciones internas para filtrar y mapear una lista de numeros.
function filterAndMap(arr) {
  function filterEvenNumbers(numbers) {
    return numbers.filter((num) => num % 2 === 0);
  }

  function squareNumbers(numbers) {
    return numbers.map((num) => num * num);
  }

  const evenNumbers = filterEvenNumbers(arr);
  return squareNumbers(evenNumbers);
}

const numbers = [1, 2, 3, 4, 5, 6];
console.log(filterAndMap(numbers)); // Imprime [4, 16, 36]

//*Las funciones anidadas en JavaScript permiten una mayor modularidad y encapsulación del código. Pueden ser utilizadas para crear cierres, generar otras funciones, y para organizar mejor la lógica interna de una función compleja. Al tener acceso a las variables de la función externa, las funciones internas pueden aprovechar el contexto y los datos del entorno donde fueron definidas.

//! Funciones ya creadas en el lenguaje
console.log("Funciones ya creadas en el lenguaje");

//* Funcion que formatea una fecha: vamos a utilizar las funciones incorporadas de js para trabajas con flechas ('Date') y anidarlas dentro de una funcion personalizada para formatear la fecha.
function formatDate(dateString) {
  function padZero(num) {
    return num < 10 ? "0" + num : num;
  }

  const date = new Date(dateString);
  const day = padZero(date.getDate());
  const month = padZero(date.getMonth() + 1); // Los meses comienzan en 0
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
}

console.log(formatDate("2024-07-03")); // Imprime "03/07/2024"
console.log(formatDate("1990-01-01")); // Imprime "01/01/1990"

//* Funcion que convierte una cadena a titulo: usaremos las funciones de cadena ('String') de js, como 'toLowerCase', 'toUpperCase' y 'split', anidadas dentro de una funcion personalizada para convertir una cadena en formato titulo (donde cada palabra comienza con una letra mayuscula).
function toTitleCase(str) {
  function capitalize(word) {
    return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
  }

  return str.split(" ").map(capitalize).join(" ");
}

console.log(toTitleCase("hello world")); // Imprime "Hello World"
console.log(toTitleCase("javaScript is FUN")); // Imprime "Javascript Is Fun"

//* Funcion que filtra numeros positivos y calcula la suma: usaremos las funciones de arreglo ('array') de js como 'filter' y 'reduce', anidadas dentro de una funcion personalizada para filtrar numeros positivos y calcular la suma.
function sumOfPositiveNumbers(arr) {
  function isPositive(num) {
    return num > 0;
  }

  function sum4(total, num) {
    return total + num;
  }

  const positiveNumbers = arr.filter(isPositive);
  return positiveNumbers.reduce(sum4, 0);
}

const numbers1 = [-1, 2, -3, 4, -5, 6];
console.log(sumOfPositiveNumbers(numbers1)); // Imprime 12

//* Funcion que genera una cadena aleatoria: usaremos la funcion 'Math.random' y otras funciones de cadena ('String'), anidadas dentro de una funcion personalizada para generar una cadena aleatoria de una longitud especifica.
function generateRandomString(length) {
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  function getRandomCharacter() {
    const randomIndex = Math.floor(Math.random() * characters.length);
    return characters.charAt(randomIndex);
  }

  let randomString = "";
  for (let i = 0; i < length; i++) {
    randomString += getRandomCharacter();
  }

  return randomString;
}

console.log(generateRandomString(10)); // Ejemplo: "A1b2C3d4E5"
console.log(generateRandomString(15)); // Ejemplo: "fGh1I2jK3L4mN5"

//* Funcion que encuentra el maximo valor de un arreglo: usaremos la funcion 'Math.max' y la funcion 'apply' anidadas dentro de una funcion personalizada para encontrar el valor maximo en un arreglo.
function findMax(arr) {
  function getMax() {
    return Math.max.apply(null, arr);
  }

  return getMax();
}

const values = [10, 20, 30, 5, 25];
console.log(findMax(values)); // Imprime 30

//! Variable global y local
console.log("Variable global y local");
//* las variables globales son aquellas que se definen fuera de cualquier funcion. Estas variables estan disponibles en cualquier partde del codigo.
// Variable global
let globalVar = "I'm a global variable";

function displayGlobalVar() {
  // Accediendo a la variable global dentro de una función
  console.log(globalVar);
}

displayGlobalVar(); // Imprime "I'm a global variable"

//* Variables locales: se definen dentro de una funcion y solo estan disponibles dentro de esa funcion. No se pueden acceder desde fuera de la funcion
function localVarFunction() {
  // Variable local
  let localVar = "I'm a local variable";
  console.log(localVar); // Imprime "I'm a local variable"
}

localVarFunction();

// Intentando acceder a la variable local fuera de la función
//console.log(localVar);
// Error: localVar is not defined

//!Extra
// Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//     - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//     - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//     - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//     - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
//   Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
//   Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

const extra = (strA, strB) => {
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(strA + strB);
    } else if (i % 3 === 0) {
      console.log(strA);
    } else if (i % 5 === 0) {
      console.log(strB);
    } else {
      console.log(i);
    }
  }
};

extra("Ejercicio", "Extra");
