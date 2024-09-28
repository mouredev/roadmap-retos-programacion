// Acceso a caracteres específicos
let cadena = "Hola, mundo!";
console.log(cadena[0]);

// Subcadenas
let subcadena = cadena.substring(1, 5);
console.log(subcadena);

// Longitud de la cadena
let longitud = cadena.length;
console.log(longitud);

// Concatenación
let otraCadena = "¡Cómo estás?";
let concatenacion = cadena + " " + otraCadena;
console.log(concatenacion);

// Repetición
let repetida = cadena.repeat(3);
console.log(repetida);

// Recorrido
for (let letra of cadena) {
  console.log(letra);
}

// Conversión a mayúsculas y minúsculas
let mayusculas = cadena.toUpperCase();
let minusculas = cadena.toLowerCase();
console.log(mayusculas);
console.log(minusculas);

// Reemplazo
let nuevaCadena = cadena.replace("mundo", "amigo");
console.log(nuevaCadena);

// División
let palabras = cadena.split(" ");
console.log(palabras);

// Unión
let union = palabras.join(" ");
console.log(union);

// Interpolación
let nombre = "Juan";
let saludoPersonalizado = `Hola, ${nombre}!`;
console.log(saludoPersonalizado);

// Verificación
let contieneHola = cadena.includes("Hola");
console.log(contieneHola);

// Ejercicio extra
function esPalindromo(palabra) {
  palabra = palabra.toLowerCase().replace(/\s/g, "");
  return palabra === palabra.split("").reverse().join("");
}

function esAnagrama(palabra1, palabra2) {
  palabra1 = palabra1.toLowerCase().replace(/\s/g, "");
  palabra2 = palabra2.toLowerCase().replace(/\s/g, "");
  return (
    palabra1.split("").sort().join("") === palabra2.split("").sort().join("")
  );
}

function esIsograma(palabra) {
  palabra = palabra.toLowerCase().replace(/\s/g, "");
  return new Set(palabra).size === palabra.length;
}

function analizarPalabras(palabra1, palabra2) {
  if (esPalindromo(palabra1)) {
    console.log(`${palabra1} es un palíndromo.`);
  } else {
    console.log(`${palabra1} no es un palíndromo.`);
  }

  if (esAnagrama(palabra1, palabra2)) {
    console.log(`${palabra1} y ${palabra2} son anagramas.`);
  } else {
    console.log(`${palabra1} y ${palabra2} no son anagramas.`);
  }

  if (esIsograma(palabra1)) {
    console.log(`${palabra1} es un isograma.`);
  } else {
    console.log(`${palabra1} no es un isograma.`);
  }

  if (esPalindromo(palabra2)) {
    console.log(`${palabra2} es un palíndromo.`);
  } else {
    console.log(`${palabra2} no es un palíndromo.`);
  }

  if (esAnagrama(palabra1, palabra2)) {
    console.log(`${palabra1} y ${palabra2} son anagramas.`);
  } else {
    console.log(`${palabra1} y ${palabra2} no son anagramas.`);
  }

  if (esIsograma(palabra2)) {
    console.log(`${palabra2} es un isograma.`);
  } else {
    console.log(`${palabra2} no es un isograma.`);
  }
}

const palabra1 = "amor";
const palabra2 = "roma";

analizarPalabras(palabra1, palabra2);
