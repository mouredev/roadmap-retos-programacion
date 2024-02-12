//Ejemplos de operaciones de cadenas

//1.Acceso a caracteres específicos:
let cadena = 'Hola, Mundo!';
console.log(cadena[0]); // Muestra 'H'
//2.Subcadenas
let subcadena = cadena.substring(0, 4);
console.log(subcadena); // Muestra 'Hola'
//3.Longitud
console.log(cadena.length); // Muestra 12
//4.Concatenación
let otraCadena = 'Adios, Mundo';
let concatenada = cadena + ' ' + otraCadena;
console.log(concatenada); // Muestra 'Hola, Mundo! ¡Qué tal!'
//5.Repetición
let repetida = cadena.repeat(2);
console.log(repetida); // Muestra 'Hola, Mundo! Hola, Mundo!'
//6.Recorrido
for (let i = 0; i < cadena.length; i++) {
  console.log(cadena[i]);
}
//7.Conversión a mayúsculas y minúsculas:
console.log(cadena.toUpperCase()); // Muestra 'HOLA, MUNDO!'
console.log(cadena.toLowerCase()); // Muestra 'hola, mundo!'
//8.Reemplazo
let nuevaCadena = cadena.replace('Mundo', 'Universo'); //Remplaza Mundo pór Universo
console.log(nuevaCadena); // Muestra 'Hola, Universo!'
//9.División
let palabras = cadena.split(', '); //Separa palabras
console.log(palabras); // Muestra ['Hola', 'Mundo!']
//10.Unión
let arregloPalabras = ['Hola', 'Mundo!'];
let nuevaCadenaUnion = arregloPalabras.join(', ');
console.log(nuevaCadena); // Muestra 'Hola, Mundo!'
//11.Interpolación
let nombre = 'Juan';
let saludo = `Hola, ${nombre}!`;
console.log(saludo); // Muestra 'Hola, Juan!'
//12.Verificación
let contieneMundo = cadena.includes('Mundo'); //Muy  utilizada
console.log(contieneMundo); // Muestra true
//13.Invertir
let cadenaInvertida = cadena.split('').reverse().join('');
console.log(cadenaInvertida);
// DIFICULTAD EXTRA (opcional):

//Palíndromos
function Palindromo(cadena) {
  let cadenaInvertida = cadena.split('').reverse().join('');
  if (cadena === cadenaInvertida) {
    return console.log('Es palindromo');
  }
  return console.log('No es palindromo');
}

Palindromo('oso');

//Anagramas
function Anagramas(palabraUno, palabrasDos) {
  // Eliminar espacios y convertir a minúsculas para ignorar diferencias de caso y espacios
  let palabra1Normalizada = palabraUno.toLowerCase().replace(/\s/g, '');
  let palabra2Normalizada = palabrasDos.toLowerCase().replace(/\s/g, '');
  // Verificar si ambas cadenas tienen la misma longitud
  if (palabra1Normalizada.length !== palabra2Normalizada.length) {
    return false;
  }
  // Convertir las cadenas a arrays, ordenar los arrays y compararlos
  let array1 = palabra1Normalizada.split('').sort();
  let array2 = palabra2Normalizada.split('').sort();
  if (array1.join('') === array2.join('')) {
    return console.log('Es anagrama');
  }
  return console.log('No es anagrama');
}

Anagramas('roma', 'amor');

//Isogramas
function Isograma(cadena) {
  // Eliminar espacios y convertir a minúsculas para ignorar diferencias de caso y espacios
  let cadenaNormalizada = cadena.toLowerCase().replace(/\s/g, '');

  // Crear un conjunto para almacenar las letras únicas
  let letrasUnicas = new Set();

  // Iterar sobre cada letra de la cadena
  for (let letra of cadenaNormalizada) {
    // Verificar si la letra ya está en el conjunto
    if (letrasUnicas.has(letra)) {
      return console.log('No es isograma'); // La letra se repite, no es un isograma
    } else {
      letrasUnicas.add(letra); // Agregar la letra al conjunto
    }
  }

  return console.log('El isograma');
}

Isograma('murciélago');
Isograma('Hoy es un buen día');
