// Expresiones Regulares

const texto = "Hoy es 19 de Marzo del 2025"

const regex = /\d+/g;

const numeros = texto.match(regex)

console.log(numeros)


// Validar Email

const email = "usuario@example.com";

const regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

console.log(regexEmail.test(email));


// Validar numero de telefono

const telefono = "+1-800-555-5555";

const regexTelefono = /^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/;

console.log(regexTelefono.test(telefono));


// Validar una url

const url = "https://www.example.com/path";

const regexURL = /^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?$/;

console.log(regexURL.test(url));