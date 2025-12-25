<?php 
    /* Un operador es algo que toma uno o más valores (o expresiones) y que devuelve otro valor.
    */

    // operadores aritméticos
    $num1 = 4;
    $num2 = 2;
   
    $sum = $num1 + $num2; #suma
    $subtraction = $num1 - $num2; #resta
    $multiplication = $num1 * $num2; #multiplicación
    $division = $num1 / $num2; #división
    $modulo = $num1 % $num2; #módulo
    $exponentiation = $num2 ** $num1; //exponenciación

    echo $sum."<br>";
    echo $subtraction . "<br>";
    echo $multiplication . "<br>";
    echo $division . "<br>";
    echo $modulo . "<br>";
    echo $exponentiation . "<br>";

    //operadores de asignación - sirve para asignar un valor a una variable

    #asignación simple (=)
    $num1 = 10;
    $num2 = 5;
    echo $num1;
    echo "<br>";
    echo $num2;

    #asignación y suma (+=)
    $num1 += $num2;
    echo $num1;
    echo "<br>";

    #asignación y resta (-=);
    $num1 -= $num2;
    echo $num1;
    echo "<br>";

    #asignación y multiplicación (*=)
    $num1 *= $num2;
    echo $num1;
    echo "<br>";

    #asignación y división (/=)
    $num1 /= $num2;
    echo $num1;

    #asignación y módulo (%=)
    $num1 %= $num2;

    // operadores de comparación
    $num1 = 4;
    $num2 = 2;

    echo $num1 == $num2; //igual (compara valor)
    echo $num1 === $num2; // idéntico (compara valor y tipo)
    echo $num1 != $num2; //diferente de 
    echo $num1 <> $num2; //no igual
    echo $num1 !== $num2; // diferente de (compara valor y tipo)
    echo $num1 > $num2; //mayor que
    echo $num1 < $num2; //menor que
    echo $num1 >= $num2; //mayor o igual que
    echo $num1 <= $num2; //mayor que
    //operador spaceship (me devuelve -1, 0 o 1 dependiendo de si el primer número es menor, igual o mayor que el segundo.)
    echo $num1 <=> $num2; 
    echo "<br>";

    // operadores de incremento/decremento
    $num1 = 0;
    echo $num1++; //pre-incremento
    echo ++$num1; //post-incremento
    echo --$num1; //pre-decremento
    echo $num1--; //post-decremento
    echo "<br>";

    // operadores lógicos
    $expression1 = 18 > 9;
    $expression2 = 50 > 15;
    
    echo $expression1 && $expression2; //and
    echo $expression1 || $expression2; //or
    echo $expression1 xor $expression2; //xor
    echo !$expression2;
    echo "<br>";

    //operadores de cadena
    $string1 = "Esto es una cadena";
    $string2 = "Esto es otra cadena";

    echo $string1 . $string2; //concatenación
    echo $string1 .= $string2; //asignación con concatenación

    echo "<br>";
    //operadores de matrices
    $array1 = ["uno" => 1,"dos" => 2, "tres" => 3];
    $array2 = ["cuatro" => 4,"cinco" => 5,"seis" =>  6];

    $array3 = $array1 + $array2; // unión (concatena o une dos arrays);
    print_r($array3);

    var_dump($array1 == $array2); //igual
    var_dump($array1 === $array2); //identidad (compara valor y tipo)
    var_dump($array1 != $array2); //diferente de
    var_dump($array1 !== $array2); //diferente de (compara valor y tipo)
    var_dump($array1 <> $array2); //diferente de
    echo "<br>";
    
    //operadores de asignación condicional
    /**Se usan para asignar un valor a algo dependiendo si se cumple una condición o no. */

    $number = null;
    echo $number > 10 ? "el número $number es mayor a diez" : "el número $number es menor o igual a diez"; //operador ternario
    echo "<br>";

    //null coalescing
    /**Este operador asigna un valor dependiendo si el primer operando es null o no.
     * si la primera expresión es null, asigna la segunda expresión o el segundo valor.
     * si el primer valor o el primer operando contiene un valor y no es null, entonces asignará la primera expresión.
     */
    echo $number ?? "No existe ningún número";
    echo "<br>";

    /** Estructuras de control */
    //condicionales

    $a = 20;
    $b = 25;

    if($a > $b){
        echo "$a es más grande que $b";
    } elseif($a === $b) {
        echo  "$a es igual a $b";
    } else {
        echo "$a es menor a $b";
    }

    echo "<br>";

    //estructuras repetitivas(ciclo)
    $i = 0;
    while($i <= 10):
        echo $i++."<br>";
    endwhile;

    $elements = [1, 2, 3, 4, 5];
    $i = 0;
    do{
        echo "Elemento #".$elements[$i]."<br>"; 
        $i++;
    }while($i < count($elements));

    $total = 0;
    $numbers = [1, 2, 3, 4, 5];

    echo "Elementos: ";
    for($i = 0; $i < count($numbers); $i++){
        echo "$numbers[$i] ";
        $total += $numbers[$i];
    }

    echo "<br>La suma total de los elementos es: $total <br>";

    $languagesPeople = [
        "Ana" => ["Español", "Francés"], 
        "José" => ["Italiano", "Inglés"], 
        "Mateo" => ["Español", "Inglés"]
    ];

    //mostrado los idiomas de cada persona con foreach anidado
    foreach($languagesPeople as $namePerson => $languages){
        echo "Los idiomas que habla $namePerson son ";
        foreach($languages as $language){
            echo "$language ";
        }
        echo "<br>";
    }

    echo "====<br>";

    //mostrando los idiomas con desestructuración de array
    foreach($languagesPeople as $namePerson => [$language1, $language2]){
        echo "Los idiomas que habla $namePerson son $language1 y $language2 <br>";
    }

    /**
     * break
     * la sentencia break permite salir de una estructura for, while, do-while, foreach y switch;
     */

    for ($i=0; $i < 10; $i++) { 
        if($i === 5){
            echo "STOP";
            break;
        }

        echo "$i ";
    }

    echo "<br>";

    /**
     * break acepta como argumento un valor numérico que indica cuántas estructuras 
     * anidadas quiero interrumpir o romper. por defecto el valor es 1, y sólo 
     * termina la estructura de la que se encuentra dentro;
     */

    for ($i=0; $i < 10; $i++) { 
        for ($j=0; $j < 10; $j++) { 
           if($j === 5 && $i === 5){
                echo "[ $i ] [ $j ] <br>";
                echo "Se rompen/interrumpen los dos ciclos anidados";
                break 2;
           } else if($j === 5){
                echo "[ $i ] [ $j ] <br>";
                break;
           }
        }
    }

    echo "<br>";

    /**
     * continue 
     * -salta a la siguiente iteración de un bucle.
     * -evita las instrucciones de código de la iteración actual y me lleva a la condición del bucle, si se cumple,
     * ejecuta la siguiente iteración.
     */

    $i = 0;
    $countries = ["Mexico", "Italy", "Mozambique", "Costa Rica", "Germany", "Egypt", "New Zealand"];
    const LETTER_TO_COMPARE = "m";

    while($i < count($countries)){
        if(str_contains(strtolower($countries[$i]), LETTER_TO_COMPARE)){
            $i++;
            continue;
        }

        echo $countries[$i]."<br>";
        $i++;
    }

    /**
     * Estructura switch
     */

    /**
    * "La lista de comandos de un case puede estar vacía, en cuyo caso PHP utilizará la lista de comandos del caso siguiente."
    */

    foreach ($countries as $country) {
        switch (strtolower($country)) {
            case "mexico":
            case "costa rica":
                echo "$country es de América <br>";
                break;
            case "italy":
            case "germany":
                echo "$country es de Europa <br>";
                break;
            case "mozambique":
            case "egypt":
                echo "$country es de África <br>";
                break;
            default:
                echo "$country es de otro continente <br>";
                break;
        }
    }

    #Excepciones
    //validar que el usuario sólo ingrese números, que no se pueda dividir entre 0, y que ingrese un signo de opración válida (+ - * /)

    function calculateOperation($number1, $number2, $operation){
        define("OPERATIONS", ["+", "-", "*", "/"]);
        $signoDivision = OPERATIONS[3];

        if(!is_numeric($number1) || !is_numeric($number2)){
            return "Se tienen que ingresar números";
        }

        if(!in_array($operation, OPERATIONS)){
            return "Mandaste una operación inválida";
        }

        if($operation === $signoDivision && ($number1 === 0 || $number2 === 0)){
            return "No se puede dividir entre 0";
        }

        switch($operation){
            case "+":
                return $number1 + $number2;
                break;   
            case "-":
                return $number1 - $number2;
                break;
            case "*":
                return $number1 * $number2;
                break;
            case "/":
                return $number1 / $number2;
                break;
        }
    }

    const NUMBER1 = 20;
    CONST NUMBER2 = 4;
    const OPERATION = "/";

    try {
        //en try pongo el código donde puede puede haber una excepción (o un error)
        $result = calculateOperation(NUMBER1, NUMBER2, OPERATION);

        if(is_string($result)){
            throw new Exception($result);
        }

        echo NUMBER1.OPERATION.NUMBER2."=".$result;
    } catch (Exception $e) {
        //en caso de que lance una excepción, entra a este bloque 'catch' 
        echo $e->getMessage();
    } finally {
        // este código se ejecuta, se lance o no una excepción.
        echo "<br>resultado obtenido";
    }

    echo "<br><br>";
    /* -- Dificultad extra -- */
    const INITIAL_NUMBER = 10;
    const LIMIT_NUMBER = 55;
    const NUMBER_WITHOUT_PRINT = 16;

    for($i = INITIAL_NUMBER; $i <= LIMIT_NUMBER; $i++){
        if($i % 2 === 0 && $i !== NUMBER_WITHOUT_PRINT && $i % 3 !== 0){
            echo "$i ";
        }
    }
?>