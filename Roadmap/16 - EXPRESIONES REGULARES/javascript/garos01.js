// Texto de ejemplo
var texto =
  "Este es un texto con algunos números como 123 y 4567, pero también tiene palabras.";

// Expresión regular para encontrar números
var regex = /\d+/g;

// Extraer números del texto
var numeros = texto.match(regex);

// Mostrar los números encontrados
console.log("Números encontrados:", numeros);

// Ejercicio extra

// Función para validar un email
function validarEmail(email) {
  var regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regexEmail.test(email);
}

// Función para validar un número de teléfono
function validarTelefono(telefono) {
  var regexTelefono = /^\d{10}$/;
  return regexTelefono.test(telefono);
}

// Función para validar una URL
function validarURL(url) {
  var regexURL = /^(https?:\/\/)?([\w-]+\.)*[\w-]+(\/[\w-./?%&=]*)?$/;
  return regexURL.test(url);
}

// Ejemplos
var email = "ejemplo@dominio.com";
console.log("¿Email válido?", validarEmail(email));

var telefono = "1234567890";
console.log("¿Teléfono válido?", validarTelefono(telefono));

var url = "https://www.ejemplo.com";
console.log("¿URL válida?", validarURL(url));
