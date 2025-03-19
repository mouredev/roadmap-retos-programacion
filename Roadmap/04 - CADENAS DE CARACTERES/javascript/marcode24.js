/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

// Operaciones comunes con cadenas de caracteres

// Acceso a caracteres específicos
const cadena = 'Hola, mundo!';
console.log('Carácter en la posición 0:', cadena[0]);

// Subcadenas
const subcadena = cadena.substring(2, 6);
console.log('Subcadena:', subcadena);

// Longitud de la cadena
console.log('Longitud de la cadena:', cadena.length);

// Concatenación
const otraCadena = ' Qué tal?';
const cadenaConcatenada = cadena + otraCadena;
console.log('Cadena concatenada:', cadenaConcatenada);

// Repetición
const cadenaRepetida = cadena.repeat(3);
console.log('Cadena repetida 3 veces:', cadenaRepetida);

// Recorrido
for (let i = 0; i < cadena.length; i++) {
  console.log('Carácter en posición', i, ':', cadena[i]);
}

// Conversión a mayúsculas y minúsculas
const mayusculas = cadena.toUpperCase();
const minusculas = cadena.toLowerCase();
console.log('Mayúsculas:', mayusculas);
console.log('Minúsculas:', minusculas);

// Reemplazo
const nuevaCadena = cadena.replace('mundo', 'amigo');
console.log('Cadena con reemplazo:', nuevaCadena);

// División
const palabras = cadena.split(' ');
console.log('Palabras divididas:', palabras);

// Unión
const union = palabras.join('-');
console.log('Palabras unidas con guiones:', union);

// Interpolación
const nombre = 'Juan';
const edad = 30;
const mensaje = `Hola, me llamo ${nombre} y tengo ${edad} años.`;
console.log('Mensaje interpolado:', mensaje);

// Verificación
const contieneHola = cadena.includes('Hola');
console.log("¿La cadena contiene 'Hola'?", contieneHola);

// Programa que verifica palíndromos, anagramas e isogramas

function esPalindromo(palabra) {
  const palabraInvertida = palabra.split('').reverse().join('');
  return palabra === palabraInvertida;
}

function esAnagrama(palabra1, palabra2) {
  const ordenPalabra1 = palabra1.split('').sort().join('');
  const ordenPalabra2 = palabra2.split('').sort().join('');
  return ordenPalabra1 === ordenPalabra2;
}

function esIsograma(palabra) {
  const caracteresUnicos = new Set(palabra);
  return palabra.length === caracteresUnicos.size;
}

// Ejemplos
const palabra1 = 'oso';
const palabra2 = 'soso';
console.log(`"${palabra1}" es palíndromo:`, esPalindromo(palabra1));
console.log(
  `"${palabra1}" es anagrama de "${palabra2}":`,
  esAnagrama(palabra1, palabra2),
);
console.log(`"${palabra1}" es isograma:`, esIsograma(palabra1));

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
