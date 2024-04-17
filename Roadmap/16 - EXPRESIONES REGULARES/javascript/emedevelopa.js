/*EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.*/

const texto = "Este es un texto de prueba que contiene todos estos números: 32, 45, 3, 25, 67 y además estos otros: 67, 8, 6, 14.";
const numRegex = /\d+/g;
const resultado = texto.match(numRegex);
console.log(resultado);

//EXTRA
/*Crea 3 expresiones regulares (a tu criterio) capaces de:
* - Validar un email.
* - Validar un número de teléfono.
* - Validar una url.*/

function mail (email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }
  
  console.log(mail("email@email.com"));

  function phone(number) {
    const regex = /^\d{9}$/;
    return regex.test(number.toString());
  }
  
  console.log(phone(611234321));

  function url (url) {
    const regex = /^(ftp|http|https):\/\/[^ "]+$/;
    return regex.test(url)
  }
  console.log(url("https://retosdeprogramacion.com/roadmap/"));
