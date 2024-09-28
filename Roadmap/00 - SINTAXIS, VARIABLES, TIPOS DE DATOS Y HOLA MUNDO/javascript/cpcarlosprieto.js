// URL del sitio web oficial de JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript
// Representación de comentarios en JavaScript:

// Comentario de una línea
let comentarioDeUnaLinea = "Este es un comentario de una línea";

/*
  Comentario
  de
  varias
  líneas
*/
let comentarioDeVariasLineas = `
  Este es un comentario de varias líneas.
  Puede abarcar varias líneas utilizando el formato de plantilla.
`;

// Crear una variable y una constante:
let miVariable = "Hola, soy una variable";
const MI_CONSTANTE = "¡Soy una constante!";

// Variables de diferentes tipos de datos primitivos:
let cadenaDeTexto = "Hola, soy una cadena de texto";
let numeroEntero = 42;
let booleano = true;

// Imprimir por terminal:
console.log("¡Hola, JavaScript!");

// Operaciones matemáticas:
let resultadoSuma = numeroEntero + 8; // Suma
let resultadoMultiplicacion = numeroEntero * 2; // Multiplicación

// Concatenación de cadenas:
let saludoPersonalizado = "Hola, " + "mundo" + "!";

// Estructuras de control - if statement:
if (booleano) {
  console.log("La variable booleano es verdadera");
} else {
  console.log("La variable booleano es falsa");
}

// Bucle for:
for (let i = 0; i < 3; i++) {
  console.log("Iteración #" + (i + 1));
}

// Funciones:
function saludar(nombre) {
  return "¡Hola, " + nombre + "!";
}

let mensajeSaludo = saludar("Brais Moure - @mouredev");
console.log(mensajeSaludo);
