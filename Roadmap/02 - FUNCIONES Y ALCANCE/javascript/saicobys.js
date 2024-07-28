/* Ejemplos de funciones basicas */

/* Función sin parámetros y sin retorno: */
function saludar() {
  console.log("Hello!");
}

saludar();

/* Función con parámetros y sin retorno: */
function saludarConNombre(nombre) {
  console.log("Hello " + "!");
}

saludarConNombre("Juan");

/* Función con parámetros y retorno: */
function sumar(num1, num2) {
  return num1 + num2;
}

let resultado = sumar(9, 7);
console.log(resultado);

/* Función autoejecutable: */
(function () {
  console.log("Función autoejecutable");
})();

/* Función flecha */
const saludarFlecha = (nombre) => {
  console.log("Hello " + "!");
};

saludarFlecha("Maria");

/* Función constructora de objetos: */
function crearPersona(nombre, apellido, edad) {
  return {
    nombre: nombre,
    apellido: apellido,
    edad: edad,
    presentarse: function () {
      console.log(
        "Hola, mi nombres es " +
          this.nombre +
          " " +
          this.apellido +
          " y tengo " +
          this.edad +
          " años."
      );
    },
  };
}

let persona1 = crearPersona("Ana", "Moronta", 30);
persona1.presentarse();

/* funciones anidadas */
function saludarExterior(nombre) {
  console.log("Hola " + nombre + " desde la función exterior.");

  function saludarInterior() {
    console.log("Hola " + nombre + " desde función interior.");
  }
  saludarInterior();
}

saludarExterior("Pedro");

/* Funciones ya creadas en el lenguaje */

/* ALERTA */
alert("DOMINICANA ES EL MEJOR PAIS");

/* Función Math.random(): */

let numeroAleartorio = Math.random();
console.log(numeroAleartorio);

/* Funciones locales y globsales */

/* Función Local */
function saludarLocal(nombre) {
  let mensaje = "Hola " + nombre + "!";
  console.log(mensaje);
}

saludarLocal("Ana");
console.log(mensaje); // La variable 'mensaje' no es accesible fuera de la función.

/* Función global */

let nombreGlobal = "Pedro";

function saludarGlobal() {
  console.log("Hola " + nombreGlobal + " desde la función global!");
}

saludarGlobal(); // Imprime: Hola Pedro desde la función global!
console.log(nombreGlobal); // Imprime: Pedro
