<?php

function dividir($dividendo, $divisor) {
    if ($divisor == 0) {
        throw new Exception("División por cero");
    }
    return $dividendo / $divisor;
}

function procesarParams($p1, $p2) {
    try {
        if (!is_int($p1) || !is_int($p2)) {
            throw new InvalidArgumentException("Los parámetros no son números");
        } elseif ($p1 == 0 || $p2 == 0) {
            throw new InvalidArgumentException("Los números son cero");
        } elseif ($p1 < 0 || $p2 < 0) {
            throw new InvalidArgumentException("Alguno de los números es negativo");
        } else {
            echo $p1 + $p2 . "\n";
            echo "No se ha producido ningún error\n";
        }
    } catch (Exception $ex) {
        echo "Se ha producido un error: " . $ex->getMessage() . "\n";
    } finally {
        echo "La ejecución ha finalizado\n";
    }
}

try {
    $resultado = dividir(10, 0);
    echo "El resultado es: " . $resultado . "\n";
} catch (Exception $ex) {
    echo "Error: " . $ex->getMessage() . "\n";
} finally {
    echo "Finalizando programa...\n";
}

//Dificultad adicional:
procesarParams(1, 0); // Error parametro cero
procesarParams(-7, 7); // Error numero negativo
procesarParams(1, 1); // Suma normal sin error

?>