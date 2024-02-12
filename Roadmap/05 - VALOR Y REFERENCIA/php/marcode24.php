<?php
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

// Ejemplo de asignación por valor para tipos primitivos
$num1 = 10;
$num2 = $num1; // Asignación por valor
$num2 = 20;

echo $num1 . PHP_EOL; // Salida: 10 (valor original no cambia)
echo $num2 . PHP_EOL; // Salida: 20

// Ejemplo de asignación por referencia para objetos
$obj1 = ['nombre' => 'Juan'];
$obj2 = &$obj1; // Asignación por referencia
$obj2['nombre'] = 'Carlos';

echo $obj1['nombre'] . PHP_EOL; // Salida: Carlos (el valor original cambia)
echo $obj2['nombre'] . PHP_EOL; // Salida: Carlos

// Ejemplo de función que recibe parámetros por valor
function duplicar($numero) {
  $numero *= 2;
  return $numero;
}

$original = 5;
$resultado = duplicar($original);

echo $original . PHP_EOL; // Salida: 5 (el valor original no cambia)
echo $resultado . PHP_EOL; // Salida: 10

// Ejemplo de función que recibe parámetros por referencia (array)
function cambiarNombre(&$persona) {
  $persona['nombre'] = 'Pedro';
}

$personaOriginal = ['nombre' => 'Juan'];
cambiarNombre($personaOriginal);

echo $personaOriginal['nombre'] . PHP_EOL; // Salida: Pedro (el valor original cambia)

echo str_repeat(PHP_EOL, 2) . str_repeat('*', 50) . PHP_EOL;

// Función que intercambia valores por valor
function intercambiarValoresPorValor($a, $b) {
  $temp = $a;
  $a = $b;
  $b = $temp;
  return [$a, $b];
}

// Función que intercambia valores por referencia
function intercambiarValoresPorReferencia($obj) {
  $copia = $obj; // No es necesario crear una copia ya que en PHP los arrays se pasan por referencia por defecto
  $temp = $copia['valor1'];
  $copia['valor1'] = $copia['valor2'];
  $copia['valor2'] = $temp;
  return $copia; // Devolver la copia del array modificado
}

// Ejemplos
$valorA = 3;
$valorB = 7;

[$nuevoValorA, $nuevoValorB] = intercambiarValoresPorValor($valorA, $valorB);
echo $valorA . ' ' . $valorB . PHP_EOL; // Salida: 3 7
echo $nuevoValorA . ' ' . $nuevoValorB . PHP_EOL; // Salida: 7 3

$valores = ['valor1' => 10, 'valor2' => 5];

$nuevosValores = intercambiarValoresPorReferencia($valores);
echo $valores['valor1'] . ' ' . $valores['valor2'] . PHP_EOL; // Salida: 10 5
echo $nuevosValores['valor1'] . ' ' . $nuevosValores['valor2'] . PHP_EOL; // Salida: 5 10

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>
