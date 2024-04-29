<?php

try {
    // Intenta dividir 10 por 0
    $resultado = 10 / 0;
} catch (DivisionByZeroError $e) {
    // Captura la excepción y muestra el mensaje de error
    echo "Se produjo un error: " . $e->getMessage() . "\n";
}

// Función para manejar las advertencias como excepciones
function manejarAdvertenciaComoExcepcion($errno, $errstr) {
    throw new ErrorException($errstr, 0, $errno);
}

// Configurar el controlador de errores personalizado
set_error_handler("manejarAdvertenciaComoExcepcion");

try {
    // Intenta acceder a un índice no existente en un array
    $array = array(1, 2, 3);
    $elemento = $array[5];
} catch (ErrorException $e) {
    // Captura la excepción y muestra el mensaje de error
    echo "Se produjo un error: " . $e->getMessage() . "\n";
}


//Dificultad extra

// Define una excepción personalizada
class MiExcepcionPersonalizada extends Exception {
    public function errorMessage() {
        // Mensaje personalizado
        return "Error personalizado: " . $this->getMessage() . "\n";
    }
}

// Función que procesa parámetros y puede lanzar excepciones
function procesarParametros($parametro) {
    if ($parametro == 0) {
        throw new InvalidArgumentException("El parámetro no puede ser cero.");
    } elseif ($parametro < 0) {
        throw new RuntimeException("El parámetro no puede ser negativo.");
    } elseif ($parametro > 100) {
        throw new MiExcepcionPersonalizada("El parámetro excede el límite permitido.");
    }

    return "Procesamiento exitoso con el parámetro: $parametro\n";
}

// Llama a la función y captura todas las excepciones
try {
    echo procesarParametros(50) . "\n"; // Llamada exitosa
} catch (Exception $e) {
    echo "Error capturado: " . $e->getMessage() . "\n";
} 
try {
    echo procesarParametros(0) . "\n";  // Lanzará una excepción de tipo InvalidArgumentException
} catch (InvalidArgumentException $e) {
    echo "Error capturado: " . $e->getMessage() . "\n";
}
try{
    echo procesarParametros(-5) . "\n"; // Lanzará una excepción de tipo RuntimeException
} catch (RuntimeException $e) {
    echo "Error capturado: " . $e->getMessage() . "\n";
}
try{
    echo procesarParametros(150) . "\n"; //Lanzará una excepción de tipo MiExcepcionPersonalizada
    echo "No se han producido errores.\n";
} catch (MiExcepcionPersonalizada $e) {
    echo "Error capturado: " . $e->errorMessage() . "\n";
}
finally {
    echo "La ejecución ha finalizado.\n";
}
