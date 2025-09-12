<?php
# Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
# Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

    /**
     * Sin utilizar parámetros ni retorno.
     */
    function greeting() {
        echo "¡Hola, PHP!<br>";
    }

    // Llamada a la función
    greeting();

    /**
     * Función que saluda utilizando un parámetro.
     *
     * @param string $nombre Nombre para saludar.
     */
    function saludar($nombre) {
        echo "¡Hola, $nombre!<br>";
    }

    // Llamada a la función con un parámetro
    saludar("John");

    /**
     * Función que realiza operaciones matemáticas con dos parámetros.
     *
     * @param int $a Primer número.
     * @param int $b Segundo número.
     *
     */
    function operations($a, $b) {
        $suma = $a + $b;
        $producto = $a * $b;

        echo "La suma de $a y $b es: $suma<br>";
        echo "El producto de $a y $b es: $producto<br>";
    }

    // Llamada a la función con varios parámetros
    operations(5, 3);

    /**
     * Función que calcula el cuadrado de un número (Tiene un valor de retorno).
     *
     * @param float $numero Número para calcular su cuadrado.
     *
     * @return float Cuadrado del número.
     */
    function calcularCuadrado($numero) {
        $cuadrado = $numero * $numero;
        return $cuadrado;
    }

    // Llamada a la función y asignación del valor de retorno a una variable
    $resultadoCuadrado = calcularCuadrado(7.5);

    // Impresión del resultado
    echo "El cuadrado de 7.5 es: $resultadoCuadrado";

    /**
     * Función que calcula el cuadrado y el cubo de un número.
     * Esta función recibe parametros por referencia
     * Estas funciones son utiles cuando esperamos recibir más de un valor de retorno
     *
     * @param float $numero Número para calcular su cuadrado y cubo.
     * @param float $cuadrado Referencia para almacenar el cuadrado del número.
     * @param float $cubo Referencia para almacenar el cubo del número.
     */
    function calcularCuadradoYCubo($numero, &$cuadrado, &$cubo) {
        $cuadrado = $numero * $numero;
        $cubo = $numero * $numero * $numero;
    }

    // Uso de la función con parámetros por referencia
    $numero = 4.5;
    $cuadradoResultado = 0;
    $cuboResultado = 0;

    calcularCuadradoYCubo($numero, $cuadradoResultado, $cuboResultado);

    // Impresión de los resultados
    echo "El cuadrado de $numero es: $cuadradoResultado<br>";
    echo "El cubo de $numero es: $cuboResultado";


# Comprueba si puedes crear funciones dentro de funciones.

    function funcionExterna($parametroExterno) {
        // Definición de la función interna
        function funcionInterna($parametroInterno) {
            return $parametroInterno * 2;
        }

        // Llamada a la función interna
        $resultado = funcionInterna($parametroExterno);

        return $resultado;
    }

    // Llamada a la función externa
    $valorExterno = 5;
    $resultadoFinal = funcionExterna($valorExterno);

    echo "El resultado final es: $resultadoFinal";

# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    // Muestra toda la información, por defecto INFO_ALL
    phpinfo();

    // Muestra solamente la información de los módulos.
    // phpinfo(8) hace exactamente lo mismo.
    phpinfo(INFO_MODULES);

    // Función que convierte una cadena de texto a mayúsculas
    $str = "Mary Had A Little Lamb and She LOVED It So";
    $str = strtoupper($str);
    echo $str; // muestra: MARY HAD A LITTLE LAMB AND SHE LOVED IT SO

# Pon a prueba el concepto de variable LOCAL y GLOBAL
    // Variable global
    $variableGlobal = 10;

    function localGlobal() {
        // Variable local
        $variableLocal = 5;

        // Acceder a la variable global dentro de la función
        global $variableGlobal;

        echo "Variable local dentro de la función: $variableLocal<br>";
        echo "Variable global dentro de la función: $variableGlobal<br>";

        // Modificar la variable global desde la función
        $variableGlobal = 20;
    }

    // Llamada a la función
    localGlobal();

    // Acceder a la variable global fuera de la función
    echo "Variable global fuera de la función: $variableGlobal";

# Reto Extra
    /**
     * Imprime números del 1 al 100 siguiendo ciertas reglas y cuenta cuántas veces se imprime un número
     * y no un texto pasado por parámetro.
     *
     * @param string $texto1 Cadena de texto a imprimir si el número es múltiplo de 3.
     * @param string $texto2 Cadena de texto a imprimir si el número es múltiplo de 5.
     *
     * @return int Número de veces que se ha impreso un número en lugar de un texto.
     */
    function retoExtra($texto1, $texto2) {
        $contador = 0;

        for ($i = 1; $i <= 100; $i++) {
            if ($i % 3 == 0 && $i % 5 == 0) {
                echo $texto1 . $texto2 . "<br>";
            } elseif ($i % 3 == 0) {
                echo $texto1 . "<br>";
            } elseif ($i % 5 == 0) {
                echo $texto2 . "<br>";
            } else {
                echo $i . "<br>";
                $contador++;
            }
        }

        return $contador;
    }

    // Ejemplo de uso
    $vecesImpreso = retoExtra("Fizz", "Buzz");
    echo "La función ha impreso $vecesImpreso el número en lugar de los textos.";
?>