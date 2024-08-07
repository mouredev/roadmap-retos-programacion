/*
  Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
*/

// Funciones declaradas (Function declarations)
function saludar() {
  console.log("Hola!");
}
saludar();

// Funciones expresadas (Function expressions)
const saludarExpresada = function () {
  console.log("Hola desde una función expresada!");
};
saludarExpresada();

// Funciones de flecha (Arrow functions)
const saludarFlecha = () => {
  console.log("Hola desde una función de flecha!");
};
saludarFlecha();

// Funciones anónimas (Anonymous functions)
setTimeout(function () {
  console.log("Hola después de 1 segundo");
}, 1000);

// Funciones de método (Method functions)
const objeto = {
  saludar() {
    console.log("Hola desde un método!");
  }
};
objeto.saludar();

// Funciones constructoras (Constructor functions)
function Persona(nombre) {
  this.nombre = nombre;
}
const persona = new Persona("7R0N1X");
console.log(persona.nombre);

// Funciones generadoras (Generator functions)
function* generador() {
  yield 1;
  yield 2;
  yield 3;
}
const iterador = generador();
console.log(iterador.next().value);
console.log(iterador.next().value);
console.log(iterador.next().value);

// Funciones asíncronas (Async functions)
async function obtenerDatos() {
  const respuesta = await fetch('https://valorant-api.com/v1/agents');
  const datos = await respuesta.json();
  console.log(datos);
}
obtenerDatos();

// Variable local y global
var global = 20
function func() {
  var local = 10
  console.log(local, global)
}

func()

// Funciones anidadas
function outerFunction() {
  console.log("Soy la función exterior");

  function innerFunction() {
    console.log("Soy la función interior");
  }

  // Llamando a la función interior dentro de la función exterior
  innerFunction();
}

// Llamando a la función exterior
outerFunction();

/*
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/

function imprimirNumeros(texto1, texto2) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0) {
      console.log(texto1);
    }
    if (i % 5 === 0) {
      console.log(texto2);
    }
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(texto1 + texto2);
    } else {
      console.log(i);
      contador++;
    }
  }
}

imprimirNumeros("Hola", "Mundo")
