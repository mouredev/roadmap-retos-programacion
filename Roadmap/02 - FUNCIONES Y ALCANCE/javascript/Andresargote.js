// Funciones en JavaScript

// Las funciones son bloques de código, que nos permiten ejecutar una tarea especfica cuando son llamadas.

// Las funciones en JavaScript pueden ser declaradas, expresadas, de flecha, anónimas, de método, constructoras, generadoras y asíncronas.

// Funciones declaradas (Function declarations)

// Las funciones declaradas son funciones que se definen con la palabra clave function, seguida de un nombre, una lista de parámetros entre paréntesis y un bloque de código entre llaves.

function saludar() {
  console.log('Hola! Soy una función declarada');
}

saludar(); // Hola! Soy una función declarada

// Funciones expresadas (Function expressions)

// Las funciones expresadas son funciones que se definen y se asignan a una variable.

const despedirse = function () {
  console.log('Adiós! Soy una función expresada');
};

despedirse(); // Adiós! Soy una función expresada

// Funciones de flecha (Arrow functions)

// Las funciones de flecha son una forma más corta de escribir funciones anónimas, tienen una sintaxis más simple y no cambian el valor de this cuando se utilizan.

const sumar = (a, b) => {
  return a + b;
};

console.log(sumar(3, 5));

// Funciones anónimas (Anonymous functions)

// Las funciones anónimas son funciones que no tienen nombre y se utilizan generalmente como argumentos de otras funciones.

setTimeout(function () {
  console.log('Hola después de 1 segundo');
}, 1000);

// Funciones de método (Method functions)

// Las funciones de método son funciones que se definen dentro de un objeto.

const objeto = {
  saludar() {
    console.log('Hola desde un método');
  },
};

objeto.saludar(); // Hola desde un método

// Funciones constructoras (Constructor functions)

// Las funciones constructoras son funciones que se utilizan para crear objetos.

function Persona(nombre) {
  this.nombre = nombre;
}

const persona = new Persona('Andrés');

console.log(persona.nombre); // Andrés

// Funciones generadoras (Generator functions)

// Las funciones generadoras son funciones que nos permiten pausar y reanudar la ejecución de una función, como por ejemplo, en un bucle for, es utilizado para iterar sobre una secuencia de valores.

function* generador() {
  yield 1;
  yield 2;
  yield 3;
}
const iterador = generador();
console.log(iterador.next().value); // 1
console.log(iterador.next().value); // 2
console.log(iterador.next().value); // 3

// Funciones asíncronas (Async functions)

// Las funciones asíncronas son funciones que nos permiten trabajar con código asíncrono de una forma más sencilla y legible.

async function obtenerDatos() {
  const respuesta = await fetch('https://jsonplaceholder.typicode.com/posts');
  const datos = await respuesta.json();
  console.log(datos);
}
obtenerDatos();

// Variable local y global

// Las variables declaradas dentro de una función son locales y solo pueden ser accedidas dentro de la función.

function mostrarMensaje() {
  var mensaje = 'Hola desde una función';
  console.log(mensaje);
}

mostrarMensaje(); // Hola desde una función
console.log(mensaje); // mensaje is not defined the variable is local

// Las variables declaradas fuera de una función son globales y pueden ser accedidas desde cualquier parte del código.

var mensaje = 'Hola desde una variable global';

function mostrarMensaje2() {
  console.log(mensaje);
}

mostrarMensaje2(); // Hola desde una variable global
console.log(mensaje); // Hola desde una variable global

// Funciones anidadas

// Las funciones anidadas son funciones que se definen dentro de otra función.

function funcionExterior() {
  console.log('Soy la función exterior');

  function funcionInterior() {
    console.log('Soy la función interior');
  }

  funcionInterior();
}

funcionExterior();

// Extra: parámetros y argumentos, los parámetros son los nombres de los valores que se pasan a una función, y los argumentos son los valores reales que se le pasan a la función.

function printNumbersOrStringChain(stringOne, stringTwo) {
  let printNumberCounter = 0;
  for (let i = 1; i <= 100; i++) {
    let output = '';
    if (i % 3 === 0) {
      output += stringOne;
    }
    if (i % 5 === 0) {
      output += stringTwo;
    }
    if (output === '') {
      printNumberCounter++;
    } else {
      console.log(output);
    }
  }

  return printNumberCounter;
}

console.log(printNumbersOrStringChain('Hello', 'World'));
