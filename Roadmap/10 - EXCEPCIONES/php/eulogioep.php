<?php

// Parte 1: Manejo básico de excepciones

// Ejemplo 1: División por cero
try {
    // Intentamos dividir por cero para forzar una excepción
    $resultado = 10 / 0;
} catch (DivisionByZeroError $e) {
    echo "Error aritmético: " . $e->getMessage() . "\n";
}

// Ejemplo 2: Acceso a índice no existente
try {
    // Intentamos acceder a un índice no existente de un array
    $array = ["Elemento"];
    $elemento = $array[5];
} catch (OutOfBoundsException $e) {
    echo "Error de acceso: " . $e->getMessage() . "\n";
}

// Parte 2: Función con múltiples excepciones (DIFICULTAD EXTRA)

// Definimos nuestra excepción personalizada
class MiExcepcionPersonalizada extends Exception {}

// Función que puede lanzar 3 tipos diferentes de excepciones
function procesarParametro($parametro) {
    if (!is_numeric($parametro)) {
        throw new InvalidArgumentException("El parámetro debe ser un número");
    }
    if ($parametro < 0) {
        throw new RangeException("El parámetro no puede ser negativo");
    }
    if ($parametro == 0) {
        throw new DivisionByZeroError("No se puede dividir por cero");
    }
    if ($parametro > 10) {
        throw new MiExcepcionPersonalizada("El parámetro es demasiado grande");
    }

    // Si no hay errores, realizamos alguna operación
    $resultado = 100 / $parametro;
    echo "Resultado: $resultado\n";
}

// Función para probar procesarParametro
function probarProcesarParametro($valor) {
    try {
        procesarParametro($valor);
        echo "No se ha producido ningún error.\n";
    } catch (Exception $e) {
        echo "Tipo de error: " . get_class($e) . "\n";
        echo "Mensaje: " . $e->getMessage() . "\n";
    } finally {
        echo "La ejecución ha finalizado.\n";
    }
    echo "---\n";
}

// Probamos con diferentes valores
probarProcesarParametro("no es un número");
probarProcesarParametro(-1);
probarProcesarParametro(0);
probarProcesarParametro(5);
probarProcesarParametro(15);

?>