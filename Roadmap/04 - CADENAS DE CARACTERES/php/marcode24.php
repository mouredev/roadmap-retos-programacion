<?php
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
$cadena = 'Hola, mundo!';
echo 'Carácter en la posición 0: ' . $cadena[0] . PHP_EOL;

// Subcadenas
$subcadena = substr($cadena, 2, 4);
echo 'Subcadena: ' . $subcadena . PHP_EOL;

// Longitud de la cadena
echo 'Longitud de la cadena: ' . strlen($cadena) . PHP_EOL;

// Concatenación
$otraCadena = ' Qué tal?';
$cadenaConcatenada = $cadena . $otraCadena;
echo 'Cadena concatenada: ' . $cadenaConcatenada . PHP_EOL;

// Repetición
$cadenaRepetida = str_repeat($cadena, 3);
echo 'Cadena repetida 3 veces: ' . $cadenaRepetida . PHP_EOL;

// Recorrido
for ($i = 0; $i < strlen($cadena); $i++) {
  echo 'Carácter en posición ' . $i . ': ' . $cadena[$i] . PHP_EOL;
}

// Conversión a mayúsculas y minúsculas
$mayusculas = strtoupper($cadena);
$minusculas = strtolower($cadena);
echo 'Mayúsculas: ' . $mayusculas . PHP_EOL;
echo 'Minúsculas: ' . $minusculas . PHP_EOL;

// Reemplazo
$nuevaCadena = str_replace('mundo', 'amigo', $cadena);
echo 'Cadena con reemplazo: ' . $nuevaCadena . PHP_EOL;

// División
$palabras = explode(' ', $cadena);
echo 'Palabras divididas: ' . implode(', ', $palabras) . PHP_EOL;

// Unión
$union = implode('-', $palabras);
echo 'Palabras unidas con guiones: ' . $union . PHP_EOL;

// Interpolación
$nombre = 'Juan';
$edad = 30;
$mensaje = "Hola, me llamo $nombre y tengo $edad años.";
echo 'Mensaje interpolado: ' . $mensaje . PHP_EOL;

// Verificación
$contieneHola = strpos($cadena, 'Hola') !== false;
echo "¿La cadena contiene 'Hola'? " . ($contieneHola ? 'Sí' : 'No') . PHP_EOL;

// Programa que verifica palíndromos, anagramas e isogramas

function esPalindromo($palabra) {
  $palabraInvertida = strrev($palabra);
  return $palabra === $palabraInvertida;
}

function esAnagrama($palabra1, $palabra2) {
  $ordenPalabra1 = str_split($palabra1);
  $ordenPalabra2 = str_split($palabra2);
  sort($ordenPalabra1);
  sort($ordenPalabra2);
  return $ordenPalabra1 === $ordenPalabra2;
}

function esIsograma($palabra) {
  $caracteresUnicos = array_unique(str_split($palabra));
  return count(str_split($palabra)) === count($caracteresUnicos);
}

// Ejemplos
$palabra1 = 'oso';
$palabra2 = 'soso';
echo "\"$palabra1\" es palíndromo: " . (esPalindromo($palabra1) ? 'Sí' : 'No') . PHP_EOL;
echo "\"$palabra1\" es anagrama de \"$palabra2\": " . (esAnagrama($palabra1, $palabra2) ? 'Sí' : 'No') . PHP_EOL;
echo "\"$palabra1\" es isograma: " . (esIsograma($palabra1) ? 'Sí' : 'No') . PHP_EOL;

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>
