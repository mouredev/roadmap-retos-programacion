<?php

/**********************************************/
/*                  IMPORTANTE                */
/* En php la división por cero no lanza una   */
/* excepción, sino que muestra un warning.    */
/* Para evitarlo se utiliza el manejador de   */
/* errores set_error_handler()                */
/**********************************************/

set_error_handler("warning_handler", E_WARNING);

function warning_handler($errno, $errstr) { 
    throw new \Exception($errstr, $errno);
}

try {
    $result = 10 / 0;
    echo $result;
} catch(Exception $e){
    echo $e->getMessage()."\n";
} finally { 
    echo "La ejecución ha finalizado\n";
}

restore_error_handler();

try {
    $array = [1, 2, 3];
    echo $array[3];
} catch (Error $error) {    
    echo 'Error: ' . $error->getMessage()."\n";
} finally { 
    echo "La ejecución ha finalizado\n";
}

class MyException extends Exception{
    public function __construct($message, $code = 0, Exception $previous = null) {
        parent::__construct($message, $code, $previous);
    }
    public function __toString() {
        return __CLASS__ . ": [{$this->code}]: {$this->message}\n";
    }
}

function ejercicioExtra ($nombre, $reto, $lenguaje){
    $resultado = "";
    try {
        if (!is_int($reto) || $reto < 0) {
            throw new InvalidArgumentException("El número debe ser un entero positivo");
        }

        if (!is_string($lenguaje) || empty($lenguaje)) {
            throw new InvalidArgumentException("El lenguaje debe ser una cadena no vacía");
        }

        if ($nombre == "Mouredev"){
            throw new MyException("El nombre no puede ser Mouredev");
        }

        $resultado = "Solución reto # $reto - $lenguaje del usuario $nombre\n";
    } catch (InvalidArgumentException $e) {
        $resultado = "Error: " . $e->getMessage()."\n";
    } catch (Exception $e) {
        $resultado = "Error: " . $e->getMessage()."\n";
    } catch (MyException $e) {
        $resultado = "Error: " . $e->getMessage()."\n";
    } finally {
        $resultado .= "La ejecución ha finalizado\n";
    }   
    return $resultado;
}

echo "\nEJERCICIO EXTRA\n";
echo ejercicioExtra("Miguelex", 10, "PHP") . "\n";
echo ejercicioExtra("", -5, "JavaScript") . "\n";
echo ejercicioExtra("Miguelex", 2, "") . "\n";
echo ejercicioExtra("Mouredev", 1, "Python") . "\n";
