// ** EJERCICIO

const texto = '32T0 32 UN4 PRU3B4';
const regex = /\d+/g;
const result = texto.match(regex);
result // Array(6) [ '32', '0', '32', '4', '3', '4']

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------------------

const regexEmail = /^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$/
const regexTelefono = /^[0-9]{9}$/
const regexUrl = /^(https?:\/\/|ftp:\/\/)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$/