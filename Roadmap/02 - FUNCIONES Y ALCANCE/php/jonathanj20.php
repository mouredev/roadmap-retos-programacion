<?php 
    /*
        -Una función es código que se va a ejecutar cuando se llame.
        -Una función es una tarea especifica por hacer.
    */ 

    //sin parámetros ni retorno
    function jump(){
        echo "I'm jumping <br>";
    }

    jump();  

    //con uno o varios parametros
    function greet($name){
        echo "Hi, I'm $name <br>";
    }

    greet("Jose");

    // con retorno - arrow function
    $sum = fn($num1, $num2) => $num1 + $num2;
    echo $sum(4, 2)."<br>";

    //creación de función dentro de otra función

    function firstFunction(){
        function secondFunction(){
            echo "I'm second function <br>";
        }
    }

    firstFunction();
    secondFunction();

    // funciones ya creadas en el lenguaje
    echo strlen("Hi, I'm a string")."<br>";
    echo str_replace("o", "s", "Hola amigos, soy yo")."<br>";

    // variables locales y globales
    $myVariable = 2; //variable global
    function myFunction(){
        // echo $myVariable; no puedo acceder a $myVariable ya que sólo está disponible en un ámbito global (fuera de la función).
        
        //si quisiera acceder a una variable global, tendría que usar el array asociativo GLOBALS.
        echo $GLOBALS["myVariable"]."<br>";

        //también puedo acceder a variables globales definiendolas como globales con la palabra reservada global, deben de tener el mismo nombre.
        global $myVariable;

        echo $myVariable."<br>";

        //variable local

        //esta variable sólo está disponible dentro de esta función myFunction(), por lo que si intento acceder a ella fuera de la función ocurrirá un error.
        $variable_local = "Hola";
    }

    myFunction();

    /*
    * DIFICULTAD EXTRA (opcional):
    * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    *
    * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
    * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
    */

    function printStrings($string1, $string2){
        $counter = 0;

        for($i = 1; $i <= 100; $i++){
            if($i % 3 === 0 && $i % 5 === 0){
                echo $string1.$string2."<br>";
            } else if($i % 3 === 0){
                echo "$string1 <br>";
            } else if($i % 5 === 0){
                echo "$string2 <br>";
            } else {
                echo "$i <br>";
                $counter++;
            }
        }

        return $counter;
    }


    echo "Número de veces que se ha impreso un número: ".printStrings("Hello", "world");

?>