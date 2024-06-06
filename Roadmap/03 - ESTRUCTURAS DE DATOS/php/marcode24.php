<?php
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

// Arrays
$arrayEjemplo = [1, 2, 3, 4, 5];
echo 'Array original: ' . implode(', ', $arrayEjemplo) . PHP_EOL;

// Inserción
array_push($arrayEjemplo, 6);
echo 'Array después de la inserción: ' . implode(', ', $arrayEjemplo) . PHP_EOL;

// Borrado
array_pop($arrayEjemplo);
echo 'Array después del borrado: ' . implode(', ', $arrayEjemplo) . PHP_EOL;

// Actualización
$arrayEjemplo[0] = 10;
echo 'Array después de la actualización: ' . implode(', ', $arrayEjemplo) . PHP_EOL;

// Ordenación
$arrayOrdenado = $arrayEjemplo;
sort($arrayOrdenado);
echo 'Array ordenado: ' . implode(', ', $arrayOrdenado) . PHP_EOL;

// Objetos
$objetoEjemplo = ['nombre' => 'Juan', 'edad' => 25, 'ciudad' => 'Barcelona'];
echo 'Objeto original: ' . implode(', ', $objetoEjemplo) . PHP_EOL;

// Inserción/Actualización
$objetoEjemplo['profesion'] = 'Ingeniero';
echo 'Objeto después de la inserción/actualización: ' . implode(', ', $objetoEjemplo) . PHP_EOL;

// Borrado
unset($objetoEjemplo['edad']);
echo 'Objeto después del borrado: ' . implode(', ', $objetoEjemplo) . PHP_EOL;

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>
