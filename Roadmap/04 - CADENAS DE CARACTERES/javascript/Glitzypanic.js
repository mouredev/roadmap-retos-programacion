// CADENA DE CARACTERES
var cadena = "Hola Mundo"; // Comillas simples
var cadena2 = "Hola Mundo"; // Comillas dobles

var nombre = "Jose";
var cadena = `Hola ${nombre}`; // Comillas invertidas

var nombre = "Jose";
var apellido = "Perez";

var cadena1 = nombre + " " + apellido;
console.log(cadena1); // Jose Perez

// Metodos de las cadenas
var cadena = "Hola Mundo";
console.log(cadena.length); // 10
console.log(cadena.repeat(3)); // Hola MundoHola MundoHola Mundo
console.log(cadena.replace("Hola", "Hello")); // Hello Mundo
console.log(cadena.charAt[2]); // l

for (var i = 0; i < cadena.length; i++) {
  console.log(cadena[i]);
}

// Convertir a mayusculas y minusculas
console.log(cadena.toUpperCase()); // HOLA MUNDO
console.log(cadena.toLowerCase()); // hola mundo

console.log(cadena.indexOf("Mundo")); // 5
console.log(cadena.lastIndexOf("o")); // 7
console.log(cadena.includes("Mundo")); // true
console.log(cadena.substring(0, 4)); // Hola
console.log(cadena.slice(0, 4)); // Hola

var suma = 1 + 2;
console.log(`El resultado de la suma es ${suma}`); // El resultado de la suma es 3

// EJERCICIO
function comprobarPalabra1(word1, word2) {
  // Comprobamos si la palabra es un palindromo
  console.log(
    word1 +
      " es un palíndromo?: " +
      (word1 === word1.split("").reverse().join(""))
  );
  console.log(
    word2 +
      " es un palindromo?: " +
      (word2 === word2.split("").reverse().join(""))
  );

  // Comprobamos si las palabras son anagramas
  console.log(
    word1 +
      " y " +
      word2 +
      " son anagramas?: " +
      (word1.split("").sort().join("") === word2.split("").sort().join(""))
  );

  // Comprohbar si las palabras son isogramas
  console.log(
    word1 +
      " es un isograma?: " +
      (new Set(word1.split("")).size === word1.length)
  );
  console.log(
    word2 +
      " es un isograma?: " +
      (new Set(word2.split("")).size === word2.length)
  );
}

comprobarPalabra1("amor", "radar");
comprobarPalabra1("roma", "amor");
comprobarPalabra1("murcielago", "repetir");
