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

 <?php

/* 
 * OPERACIONES
 */

// 1. Declaración de una cadena
$cadena = "Hola Mundo";

// 2. Acceso a caracteres específicos
echo "2. Acceso a caracteres:<br>";
echo "   El primer carácter es: " . $cadena[0] . "<br>";    // 'H'
echo "   El cuarto carácter es: " . $cadena[3] . "<br>";    // 'a'
echo '<br>';

// 3. Subcadenas (substr)
echo "3. Subcadenas:<br>";
echo "   Subcadena desde el índice 5: " . substr($cadena, 5) . "<br>";      // "Mundo"
echo "   Subcadena de longitud 3 desde el índice 5: " . substr($cadena, 5, 3) . "<br>"; // "Mun"
echo '<br>';

// 4. Longitud de la cadena (strlen)
echo "4. Longitud:<br>";
echo "   La longitud de '$cadena' es: " . strlen($cadena) . "<br>";
echo '<br>';

// 5. Concatenación (operador .)
echo "5. Concatenación:<br>";
$otraCadena = " desde PHP";
$concatenada = $cadena . $otraCadena;
echo "   Cadena concatenada: $concatenada<br>";
echo '<br>';

// 6. Repetición de cadenas (str_repeat)
echo "6. Repetición:<br>";
$repetida = str_repeat($cadena, 2);
echo "   Repetir '$cadena' 2 veces: $repetida<br>";
echo '<br>';

// 7. Recorrer cada carácter (str_split + bucle)
echo "7. Recorrido de la cadena carácter a carácter:<br>";
$arrayCaracteres = str_split($cadena);
foreach ($arrayCaracteres as $char) {
    echo "   $char<br>";
}
echo '<br>';

// 8. Conversión a mayúsculas y minúsculas (strtoupper, strtolower)
echo "8. Cambios de mayúsculas/minúsculas:<br>";
echo "   En mayúsculas: " . strtoupper($cadena) . "<br>"; // "HOLA MUNDO"
echo "   En minúsculas: " . strtolower($cadena) . "<br>"; // "hola mundo"
echo '<br>';

// 9. Reemplazo de subcadenas (str_replace)
echo "9. Reemplazo:<br>";
$reemplazada = str_replace("Mundo", "ChatGPT", $cadena);
echo "   Reemplazar 'Mundo' por 'ChatGPT': $reemplazada<br>";
echo '<br>';

// 10. División de cadenas (explode)
echo "10. División (explode):<br>";
$partes = explode(" ", $cadena); // ["Hola", "Mundo"]
echo "   Después de explode(' ', '$cadena'): <br>";
print_r($partes);
echo '<br>';

// 11. Unión de elementos de un array en una cadena (implode)
echo "11. Unión (implode):<br>";
$unida = implode("-", $partes); // "Hola-Mundo"
echo "   Unir con '-': $unida<br>";
echo '<br>';

// 12. Interpolación de variables
echo "12. Interpolación:<br>";
$nombre = "Carlos";
echo "   Usando comillas dobles, se puede interpolar: \"Hola, $nombre\"<br>";
echo '<br>';

// 13. Verificación de la existencia de subcadena (strpos o str_contains en PHP8+)
echo "13. Verificación de subcadena:<br>";
if (strpos($cadena, "Mundo") !== false) {
    echo "   'Mundo' se encuentra dentro de '$cadena'.<br>";
} else {
    echo "   'Mundo' NO se encuentra dentro de '$cadena'.<br>";
}
echo '<br>';

/*
 *  🔥 PROGRAMA PARA PALÍNDROMOS, ANAGRAMAS E ISOGRAMAS
 * 
 * Este programa analiza dos palabras y realiza comprobaciones 
 * para descubrir si son:
 *   - Palíndromos
 *   - Anagramas
 *   - Isogramas
 */

// Puedes cambiar estas dos palabras para hacer pruebas.
$palabra1 = "Murcielago";
$palabra2 = "Guacamole";

/**
 * isPalindrome
 * Comprueba si una palabra es palíndroma (se lee igual al derecho y al revés).
 */
function isPalindrome($word) {
    // Convertimos a minúsculas y quitamos espacios en blanco
    $procesada = strtolower(preg_replace("/\s+/", "", $word));
    // Comparamos con su inversa
    return $procesada === strrev($procesada);
}

/**
 * isAnagram
 * Comprueba si dos palabras son anagramas (contienen las mismas letras en distinto orden).
 */
function isAnagram($word1, $word2) {
    // Convertimos a minúsculas y quitamos espacios
    $procesada1 = strtolower(preg_replace("/\s+/", "", $word1));
    $procesada2 = strtolower(preg_replace("/\s+/", "", $word2));

    // Creamos arrays de caracteres y los ordenamos
    $array1 = str_split($procesada1);
    sort($array1);
    $array2 = str_split($procesada2);
    sort($array2);

    // Comparamos el resultado
    return implode("", $array1) === implode("", $array2);
}

/**
 * isIsogram
 * Comprueba si una palabra es isograma (no repite ninguna letra).
 */
function isIsogram($word) {
    // Convertimos a minúsculas y quitamos espacios
    $procesada = strtolower(preg_replace("/\s+/", "", $word));
    // Dividimos en caracteres
    $letras = str_split($procesada);
    // Si el número de letras es el mismo que el número de letras únicas, es isograma
    return count($letras) === count(array_unique($letras));
}

echo "-------------------------------------<br>";
echo "   COMPROBACIONES ESPECIALES<br>";
echo "<br>";
echo "Palabra 1: $palabra1<br>";
echo "Palabra 2: $palabra2<br><br>";

// Palíndromos
echo "¿Palabra 1 es palíndromo? " . (isPalindrome($palabra1) ? "Sí<br>" : "No<br>");
echo "¿Palabra 2 es palíndromo? " . (isPalindrome($palabra2) ? "Sí<br>" : "No<br>");

// Anagramas
echo "¿Son anagramas? " . (isAnagram($palabra1, $palabra2) ? "Sí<br>" : "No<br>");

// Isogramas
echo "¿Palabra 1 es isograma? " . (isIsogram($palabra1) ? "Sí<br>" : "No<br>");
echo "¿Palabra 2 es isograma? " . (isIsogram($palabra2) ? "Sí<br>" : "No<br>");

?>
