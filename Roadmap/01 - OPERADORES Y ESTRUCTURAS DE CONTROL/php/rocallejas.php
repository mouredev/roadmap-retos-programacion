<?php
# Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits.

    // Operadores aritméticos
        echo "**************** Operadores aritméticos ****************  <br>";
        $a = 16;
        $b = 8;

        // Suma
        $resultadoSuma = $a + $b;
        echo "Resultado de la suma de $a mas $b es: $resultadoSuma <br>";

        // Resta
        $resultadoResta = $a - $b;
        echo "Resultado de la resta de $a menos $b es: $resultadoResta <br>";

        // Multiplicación
        $resultadoMultiplicacion = $a * $b;
        echo "Resultado de la multiplicación de $a por $b es: $resultadoMultiplicacion <br>";

        // División
        $resultadoDivision = $a / $b;
        echo "Resultado de la división de $a entre $b es: $resultadoDivision <br>";

        // Módulo (resto de la división)
        $resultadoModulo = $a % $b;
        echo "Resultado de $a módulo de $b es: $resultadoModulo <br>";

    // Operadores de comparación
        echo "<br> **************** Operadores de comparación **************** <br>";
        $x = 16;
        $y = "16";

        // Igual ==
        $resultadoIgual = ($x == $y);
        echo "Resultado de la igualdad: " . ($resultadoIgual ? 'true' : 'false') . " <br>";

        // Comparación de identidad (valor y tipo) con ===
        $resultadoIdentico = ($x === $y);
        echo "Resultado de la identidad: " . ($resultadoIdentico ? 'true' : 'false') . " <br>";

        // Diferente !=
        $resultadoDiferente = ($x != $y);
        echo "Resultado de la diferencia: " . ($resultadoDiferente ? 'true' : 'false') . " <br>";

        // No idéntico !==
        $resultadoNoIdentico = ($x !== $y);
        echo "Resultado de la no identidad: " . ($resultadoNoIdentico ? 'true' : 'false') . " <br>";

        // Mayor que >
        $resultadoMayorQue = ($x > $y);
        echo "Resultado de mayor que: " . ($resultadoMayorQue ? 'true' : 'false') . " <br>";

        // Menor que <
        $resultadoMenorQue = ($x < $y);
        echo "Resultado de menor que: " . ($resultadoMenorQue ? 'true' : 'false') . " <br>";

        // Mayor o igual que >=
        $resultadoMayorIgual = ($a >= $b);
        echo "Resultado de mayor o igual que: " . ($resultadoMayorIgual ? 'true' : 'false') . " <br>";

        // Menor o igual que <=
        $resultadoMenorIgual = ($a <= $b);
        echo "Resultado de menor o igual que: " . ($resultadoMenorIgual ? 'true' : 'false') . " <br>";

    // Operadores lógicos
        echo "<br> **************** Operadores lógicos **************** <br>";

        $p = true;
        $q = false;

        // AND lógico (&&)
        $resultadoAnd = ($p && $q);
        echo "Resultado del AND lógico: " . ($resultadoAnd ? 'true' : 'false') . " <br>";

        // OR lógico (||)
        $resultadoOr = ($p || $q);
        echo "Resultado del OR lógico: " . ($resultadoOr ? 'true' : 'false') . " <br>";

        // NOT lógico (!)
        $resultadoNot = !$p;
        echo "Resultado del NOT lógico: " . ($resultadoNot ? 'true' : 'false') . " <br>";

    // Operadores de asignación
        echo "<br> **************** Operadores de asignación **************** <br>";

        $variable = 8;

        // Asignación simple
        $variable = 16;
        echo "Valor actual de la variable: $variable <br>";

        // Asignación con suma
        $variable += 3;
        echo "Valor después de la asignación con suma: $variable <br>";

        // Asignación con resta
        $variable -= 2;
        echo "Valor después de la asignación con resta: $variable <br>";

        // Asignación con multiplicación
        $variable *= 4;
        echo "Valor después de la asignación con multiplicación: $variable <br>";

        // Asignación con división
        $variable /= 2;
        echo "Valor después de la asignación con división: $variable <br>";

    // Operadores de pertenencia
        echo "<br> **************** Operadores de pertenencia **************** <br>";

        $array = array(1, 2, 3, 4, 5);

        // Verificar si un valor está en un array con in_array()
        $resultadoPertenencia = in_array(3, $array);
        echo "Resultado de la pertenencia en array: " . ($resultadoPertenencia ? 'true' : 'false') . " <br>";

    // Operadores de Bits
        echo "<br> **************** Operadores de Bits **************** <br>";
        /*
            Los operadores de bits son menos comunes en aplicaciones cotidianas,
            pero pueden ser útiles en situaciones específicas donde se trabaje directamente
            con representaciones binarias de datos
        */
        $numero1 = 5;   // Representación binaria: 0101
        $numero2 = 3;   // Representación binaria: 0011

        // Operador AND a nivel de bits &
        $resultadoAndBits = $numero1 & $numero2;
        echo "Resultado del AND a nivel de bits: $resultadoAndBits <br>";

        // Operador OR a nivel de bits |
        $resultadoOrBits = $numero1 | $numero2;
        echo "Resultado del OR a nivel de bits: $resultadoOrBits <br>";

        // Operador XOR a nivel de bits ^
        $resultadoXorBits = $numero1 ^ $numero2;
        echo "Resultado del XOR a nivel de bits: $resultadoXorBits <br>";

        // Desplazamiento a la izquierda <<
        $resultadoDesplazamientoIzquierda = $numero1 << 1;
        echo "Resultado del desplazamiento a la izquierda: $resultadoDesplazamientoIzquierda <br>";

        // Desplazamiento a la derecha >>
        $resultadoDesplazamientoDerecha = $numero1 >> 1;
        echo "Resultado del desplazamiento a la derecha: $resultadoDesplazamientoDerecha <br>";

# Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos
# de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones

    // Condicionales
        echo "<br> **************** Condicionales **************** <br>";

        // if, else y elseif
        echo "---- if, else y elseif ----  <br>";
        $edad = 35;

        if ($edad < 18) {
            echo "Eres menor de edad. <br>";
        } elseif ($edad >= 18 && $edad < 65) {
            echo "Eres adulto. <br>";
        } else {
            echo "Eres un adulto mayor. <br>";
        }

        // SWITCH
        echo "---- switch ----  <br>";

        $marca = "Toyota";

        switch ($marca) {
            case "Toyota":
                echo "Seleccionaste un vehículo de la marca Toyota <br>";
                break;
            case "Honda":
                echo "Seleccionaste un vehículo de la marca Honda <br>";
                break;
            case "Nissan":
                echo "Seleccionaste un vehículo de la marca Nissan <br>";
                break;
            default:
                echo "La marca seleccionada no es una marca japonesa conocida <br>";
                break;
        }

    // Iterativas
        echo "<br> **************** Iterativas **************** <br>";

        // Bucle FOR
        echo "Resultado del bucle FOR: ";
        for ($i = 1; $i <= 5; $i++) {
            echo $i . " ";
        }
        echo " <br>";

        // Bucle WHILE
        echo "Resultado del bucle WHILE: ";
        $num = 1;
        while ($num <= 5) {
            echo $num . " ";
            $num++;
        }
        echo " <br>";

        // Bucle DO-WHILE
        echo "Resultado del bucle DO-WHILE: ";
        $num = 1;
        do {
            echo $num . " ";
            $num++;
        } while ($num <= 5);
        echo " <br>";

        // Bucle FOREACH
        echo "Resultado del bucle FOREACH:  <br>";
        $colores = array("Rojo", "Verde", "Azul");

        foreach ($colores as $color) {
            echo "Color: $color <br>";
        }

    // Excepciones try, catch, finally
        echo "<br> **************** Excepciones try, catch, finally **************** <br>";
            function dividir($a, $b) {
                try {
                    if ($b == 0) {
                        throw new Exception("División por cero.");
                    }
                    $resultado = $a / $b;
                    echo "Resultado: " . $resultado;
                } catch (Exception $ex) {
                    echo "Error: " . $ex->getMessage();
                } finally {
                    echo " Fin de la operación.";
                }
            }
        echo "Resultado de dividir(10, 2): ";
        dividir(10, 2); // Salida: Resultado: 5 Fin de la operación.
        echo " <br>";

        echo "Resultado de dividir(10, 0): ";
        dividir(10, 0); // Salida: Error: División por cero. Fin de la operación.
        echo " <br>";

# Reto extra
    /*
        Crea un programa que imprima por pantalla todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
    */
    echo "<br> **************** Reto extra **************** <br>";

    echo "Números pares entre 10 y 55 (excluyendo el 16 y múltiplos de 3): ";
    echo "<ul>"; // Abre la lista
    for ($i = 10; $i <= 55; $i++) {
        // Verificar si el número es par
        $esPar = $i % 2 == 0;

        // Verificar si el número no es el 16
        $noEs16 = $i != 16;

        // Verificar si el número no es múltiplo de 3
        $noEsMultiploDe3 = $i % 3 != 0;

        // Comprobar todas las condiciones
        if ($esPar && $noEs16 && $noEsMultiploDe3) {
            echo "<li>$i</li>";
        }
    }
    echo "</ul>"; // Cierra la lista
?>