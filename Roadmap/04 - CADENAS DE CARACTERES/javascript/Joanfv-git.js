//Operaciones de cadenas de caracteres
//Concatenar
let cadena1 = "Hola";
let cadena2 = "Mundo";
let concatenacion = cadena1 + " " + cadena2;
console.log(concatenacion);
//Longitud
console.log(concatenacion.length);
//Mayusculas
console.log(concatenacion.toUpperCase());
//Minusculas
console.log(concatenacion.toLowerCase());
//Extraer una parte de la cadena
console.log(concatenacion.substring(0, 4));
//Dividir una cadena en un array
console.log(concatenacion.split(" "));
//Reemplazar parte de una cadena
console.log(concatenacion.replace("Mundo", "World"));
//Buscar una cadena en otra
console.log(concatenacion.includes("Hola"));
//Comparar cadenas
let cadena3 = "Hola Mundo";
console.log(concatenacion === cadena3);
//Extraer un caracter
console.log(concatenacion.charAt(0));
//Buscar la posición de un caracter
console.log(concatenacion.indexOf("M"));
//Comparar cadenas sin importar mayúsculas o minúsculas
console.log(concatenacion.toUpperCase() === cadena3.toUpperCase());
//Eliminar espacios en blanco al principio y al final
let cadena4 = " Hola Mundo ";
console.log(cadena4.trim());
//Extraer una parte de la cadena
console.log(concatenacion.slice(0, 4));
//Extraer una parte de la cadena y reemplazarla
console.log(concatenacion.slice(0, 4).replace("H", "J"));

//Ejercicio extra
let primeraPalabra = prompt("Introduce una palabra");
let segundaPalabra = prompt("Introduce una palabra");

//Comprobar si son palindromas
if (primeraPalabra === segundaPalabra.split("").reverse().join("")) {
  console.log("Las palabras son palindromas");
} else {
  console.log("Las palabras no son palindromas");
}
//Comprobar si son anagramas
if (
  primeraPalabra.split("").sort().join("") ===
  segundaPalabra.split("").sort().join("")
) {
  console.log("Las palabras son anagramas");
} else {
  console.log("Las palabras no son anagramas");
}

//Comprobar si son isogramas
