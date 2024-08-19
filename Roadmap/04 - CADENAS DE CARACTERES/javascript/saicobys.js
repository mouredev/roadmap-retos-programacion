/* Operaciones basicas con string */

let saludo = "Hola, mundo!";

// Acceso a caracteres especificos
console.log(saludo[0]);
console.log(saludo.charAt(4));

// Subcadenas
console.log(saludo.slice(0, 4));
console.log(saludo.substring(5, 11));

// Longitud
console.log(saludo.length);

// Concatenacion
let nombre = "Juan";
console.log(saludo + " " + nombre);

// Repeticion
console.log("ja".repeat(3));

// Recorrido
for (let letra of saludo) {
  console.log(letra);
}

// Conversion a mayusculas y minusculas
console.log(saludo.toLocaleUpperCase());
console.log(saludo.toLowerCase());

// Reemplazo
console.log(saludo.replace("mundo", "JavaScript"));

// Division
let palabras = saludo.split(" ");
console.log(palabras);

// Union
console.log(palabras.join("-"));

// Interpolacion
let edad = 30;
console.log(`Hola, ${nombre}! Tienes ${edad} años.`);

// Verificación
console.log(saludo.startsWith("Hola"));
console.log(saludo.endsWith("!"));
console.log(saludo.includes("mundo"));

/* Desafío Extra */

function analizarPalabras(palabra1, palabra2) {
  palabra1 = palabra1.toLowerCase().replace(/[^a-z]/g, "");
  palabra2 = palabra2.toLowerCase().replace(/[^a-z]/g, "");

  // Palíndromo
  const esPalindromo = palabra1 === palabra1.split("").reverse().join("");

  // Anagrama
  const esAnagrama =
    palabra1.split("").sort().join("") === palabra2.split("").sort().join("");

  // Isograma (cada letra aparece solo una vez)
  const esIsograma = new Set(palabra1).size === palabra1.length;

  console.log(`Palíndromo: ${esPalindromo}`);
  console.log(`Anagrama: ${esAnagrama}`);
  console.log(`Isograma: ${esIsograma}`);
}

analizarPalabras("Amor", "Roma"); // Palíndromo y Anagrama
analizarPalabras("Ojo", "ojo"); // Palíndromo e Isograma
analizarPalabras("Hola", "Chau"); // Ninguna
