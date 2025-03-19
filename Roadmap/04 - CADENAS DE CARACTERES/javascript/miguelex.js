// Operaciones básicas sobre cadenas de texto
const texto = "Hola, mundo!";

// Interpolación de cadenas (uso de plantillas de cadena)
const nombre = "Migue";
const lenguaje = "PHP";
const mensaje = `Hola, me llamo ${nombre} y trabajo con ${lenguaje} años.`;
console.log(mensaje);

// Longitud de la cadena
const longitud = texto.length;
console.log(`La longitud de la cadena ${texto} es ${longitud} caracteres`);

// Obtener el carácter en una posición específica
const primerCaracter = texto[0];
console.log(`El primer carácter de ${texto} es ${primerCaracter}`);

// Concatenar dos cadenas
const nuevaCadena = texto + " TypeScript";
console.log(`La nueva cadena de unir ${texto} con TypeScript es ${nuevaCadena}`);

// Convertir la cadena a minúsculas
const minusculas = texto.toLowerCase();
console.log(`${texto} en minúsculas es ${minusculas}`);

// Convertir la cadena a mayúsculas
const mayusculas = texto.toUpperCase();
console.log(`${texto} en mayúsculas es ${mayusculas}`);

// Obtener una subcadena
const subcadena = texto.substring(0, 4);
console.log(`La subcadena de ${texto} entre las posiciones 0 y 4 es ${subcadena}`);

// Reemplazar parte de la cadena
const reemplazada = texto.replace("Hola", "Saludos");
console.log(`Vamos a reemplazar Hola por Saludos: ${reemplazada}`);

// Operaciones adicionales sobre cadenas de texto
const textoConEspacios = "   Hola,      mundo!   ";

// Eliminar espacios en blanco al principio y al final
const sinEspaciosExtremos = textoConEspacios.trim();
console.log(`Cadena sin espacios al principio y al final: ${sinEspaciosExtremos}`);

// Eliminar todos los espacios en blanco
const sinEspacios = textoConEspacios.replace(/\s/g, "");
console.log(`Cadena sin espacios: ${sinEspacios}`);

// Unión de dos cadenas
const cadena1 = "Moure";
const cadena2 = "Dev";
const unionCadenas = cadena1.concat(" ", cadena2);
console.log(`La unión de las cadenas ${cadena1} y ${cadena2} es ${unionCadenas}`);

// Intersección de dos cadenas (caracteres comunes)
const interseccionCadenas = [...new Set(cadena1)].filter(char => cadena2.includes(char)).join("");
console.log(`Intersección de las cadenas ${cadena1} y ${cadena2} es ${interseccionCadenas}`);

// Acceso a caracteres específicos (por posición)
const tercerCaracter = texto.charAt(2);
console.log(`El tercer carácter de ${texto} es ${tercerCaracter}`);

// Repetición de una cadena
const cadenaRepetida = "Hola ".repeat(3);
console.log(`Cadena Hola repetida 3 veces queda ${cadenaRepetida}`);

// Recorrido de una cadena (usando un bucle)
for (let i = 0; i < texto.length; i++) {
  console.log(`Carácter en posición ${i}: ${texto[i]}`);
}

// Conversión a título (primera letra en mayúscula)
const titulo = texto.toLowerCase().replace(/\b\w/g, (char) => char.toUpperCase());
console.log(`La cadena ${texto} como título ${titulo}`);

// División de una cadena en un array de substrings
const palabras = texto.split(" ");
console.log(`Palabras en la cadena ${texto} son ${palabras}`);

// Verificación de si una cadena comienza o termina con ciertos caracteres
const comienzaCon = texto.startsWith("Hola");
console.log(`¿La cadena ${texto} comienza con "Hola"? ${comienzaCon}`);

const terminaCon = texto.endsWith("mundo!");
console.log(`¿La cadena ${texto}termina con "mundo!"? ${terminaCon}`);

// Verificar si una cadena es palíndromo
function esPalindromo(cadena) {
  const sinEspacios = cadena.replace(/\s/g, "").toLowerCase();
  const invertida = sinEspacios.split("").reverse().join("");
  return sinEspacios === invertida;
}

// Verificar si una cadena es un anagrama
function esAnagrama(cadena1, cadena2) {
  const limpiarCadena = (cadena) => cadena.replace(/\s/g, "").toLowerCase();
  const limpiaCadena1 = limpiarCadena(cadena1);
  const limpiaCadena2 = limpiarCadena(cadena2);

  const ordenada1 = limpiaCadena1.split("").sort().join("");
  const ordenada2 = limpiaCadena2.split("").sort().join("");

  return ordenada1 === ordenada2;
}

// Verificar si una cadena es un isograma
function esIsograma(cadena) {
  const caracteres = new Set();

  for (const char of cadena) {
    const caracter = char.toLowerCase();
    if (caracteres.has(caracter)) {
      return false;
    }
    caracteres.add(caracter);
  }

  return true;
}

// Ejemplos de uso de las funciones adicionales
console.log(`¿Es "${texto}" un palíndromo? ${esPalindromo(texto)}`);
console.log(`¿Es Ana un palíndromo? ${esPalindromo("Ana")}`);
console.log(`¿Es "listen" un anagrama de "silent"? ${esAnagrama("listen", "silent")}`);
console.log(`¿Es "programming" un isograma? ${esIsograma("programming")}`);
