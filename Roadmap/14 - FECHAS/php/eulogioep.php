<?php
/**
 * Ejercicio de manejo de fechas en PHP
 * Este script demuestra diferentes operaciones y formatos con fechas
 */

// PARTE 1: Crear variables de fecha y calcular años transcurridos

// Creamos la fecha actual
$fechaActual = new DateTime();

// Creamos una fecha de nacimiento (ejemplo)
$fechaNacimiento = new DateTime('1990-05-15 14:30:00');

// Calculamos la diferencia entre las fechas
$diferencia = $fechaActual->diff($fechaNacimiento);

echo "Fecha actual: " . $fechaActual->format('Y-m-d H:i:s') . "\n";
echo "Fecha de nacimiento: " . $fechaNacimiento->format('Y-m-d H:i:s') . "\n";
echo "Años transcurridos: " . $diferencia->y . "\n\n";

// PARTE 2: DIFICULTAD EXTRA - Formatear la fecha de 10 maneras diferentes

echo "DIFERENTES FORMATOS DE FECHA:\n";

// 1. Día, mes y año
echo "1. Día, mes y año: " . $fechaNacimiento->format('d/m/Y') . "\n";

// 2. Hora, minuto y segundo
echo "2. Hora, minuto y segundo: " . $fechaNacimiento->format('H:i:s') . "\n";

// 3. Día del año
echo "3. Día del año: " . $fechaNacimiento->format('z') . " (comenzando desde 0)\n";

// 4. Día de la semana
$diasSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
echo "4. Día de la semana: " . $diasSemana[$fechaNacimiento->format('w')] . "\n";

// 5. Nombre del mes
$meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 
          'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
echo "5. Nombre del mes: " . $meses[$fechaNacimiento->format('n') - 1] . "\n";

// 6. Formato largo personalizado
setlocale(LC_TIME, 'es_ES.UTF-8');
echo "6. Formato largo: " . strftime('%A, %d de %B de %Y', $fechaNacimiento->getTimestamp()) . "\n";

// 7. Formato ISO 8601
echo "7. Formato ISO 8601: " . $fechaNacimiento->format('c') . "\n";

// 8. Semana del año
echo "8. Semana del año: " . $fechaNacimiento->format('W') . "\n";

// 9. Trimestre del año
$trimestre = ceil($fechaNacimiento->format('n') / 3);
echo "9. Trimestre del año: " . $trimestre . "\n";

// 10. Timestamp Unix
echo "10. Timestamp Unix: " . $fechaNacimiento->getTimestamp() . "\n";

// Funciones auxiliares de ejemplo
function obtenerEdad($fechaNacimiento) {
    $hoy = new DateTime();
    $edad = $hoy->diff($fechaNacimiento);
    return $edad->y;
}

function esBisiesto($año) {
    return date('L', strtotime("$año-01-01")) == 1;
}

// Ejemplo de uso de funciones auxiliares
echo "\nFUNCIONES AUXILIARES:\n";
echo "Edad calculada: " . obtenerEdad($fechaNacimiento) . " años\n";
echo "¿El año de nacimiento es bisiesto? " . 
     (esBisiesto($fechaNacimiento->format('Y')) ? "Sí" : "No") . "\n";
?>