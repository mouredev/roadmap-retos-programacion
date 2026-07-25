<?php

// URL del sitio web oficial de PHP
// https://www.php.net/

// Diferentes formas de crear comentarios en PHP:

// 1. Comentario de una línea

/*
 * 2. Comentario
 * de varias
 * líneas
 */

/**
 * 3. Comentario de documentación (DocBlock)
 * Se usa para generar documentación automática del código
 */

// Creación de una variable
$miVariable = "Hola, PHP!";

// Creación de una constante
define("MI_CONSTANTE", 42);

// Variables representando tipos de datos en PHP
$miEntero = 10;
$miFlotante = 3.14;
$miBooleano = true;
$miCadena = "Esto es una cadena";
$miArray = array(1, 2, 3);
$miArrayAsociativo = ["clave" => "valor"];
$miNulo = null;

// Impresión del texto solicitado
echo "¡Hola, PHP!\n";

// Impresión de los valores de las variables (opcional, para verificación)
echo "miVariable: " . $miVariable . "\n";
echo "MI_CONSTANTE: " . MI_CONSTANTE . "\n";
echo "miEntero: " . $miEntero . "\n";
echo "miFlotante: " . $miFlotante . "\n";
echo "miBooleano: " . ($miBooleano ? "true" : "false") . "\n";
echo "miCadena: " . $miCadena . "\n";
echo "miArray: " . print_r($miArray, true) . "\n";
echo "miArrayAsociativo: " . print_r($miArrayAsociativo, true) . "\n";
echo "miNulo: " . var_export($miNulo, true) . "\n";

// Demostración de tipos de datos adicionales en PHP
$miObjeto = new stdClass();
$miObjeto->propiedad = "valor";
echo "miObjeto: " . print_r($miObjeto, true) . "\n";

$miCallable = function() { return "Soy una función anónima"; };
echo "miCallable: " . $miCallable() . "\n";

// Demostración de tipado fuerte (disponible desde PHP 7)
function sumaEntera(int $a, int $b): int {
    return $a + $b;
}
echo "Suma entera: " . sumaEntera(5, 3) . "\n";

?>