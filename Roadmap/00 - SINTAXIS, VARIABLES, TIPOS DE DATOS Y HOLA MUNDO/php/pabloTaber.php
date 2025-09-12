<?php

/* --- Crea un comentario en el código y coloca la URL del sitio web 
    oficial dellenguaje de programación que has seleccionado. --- */ 

    //Sitio web oficial de php: https://www.php.net

/* --- Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...). --- */

    // Comentario de una linea.

    /* Comentario
        de varias
        lineas 
    */

// --- rea una variable (y una constante si el lenguaje lo soporta). --- 

    //variable
    $variable = "Esto es una variable.";

    //Constante
    define("CONSTANTE", "Esto es una constante");

 /* --- Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...). --- */   

    //Boolean
    $verdadero = true;
    $falso = false;

    //Integer
    $numeroEntero = 10;
    $numeroEnteroNegativo = -10;

    //Float
    $numeroReal = 1.5;

    //String
    $comillasDobles = "Estas comillas expanden el contenido de las variables. Ej: numeroEntero es igual a $numeroEntero";
    $comillasSimples = 'Estas comillas no expanden el contenido de las variables';

    //Array
        //Array Indexado.
        $arrayIndexado = array ("Hola", "a", "todos"); 
        $arrayIndexado2[0] = "Hola"; //Tambien se pueden asignar valores directamente, los 2 arrays son iguales.
        $arrayIndexado2[1] = "a";
        $arrayIndexado2[2] = "todos";

        //Array Asociativo.
        $arrayAsociativo = array ( "es" => "Hola", "gz" => "Ola", "pt" => "Olá");
        $arrayAsociativo2["es"] = "Hola"; //Tambien se pueden asignar valores directamente, los 2 arrays son iguales.
        $arrayAsociativo2["gz"] = "Ola";
        $arrayAsociativo2["pt"] = "Olá";
        
    //Object
    class Objeto {
        public $descripcion = "Soy un objeto";
    }

    $objeto = new Objeto();

    //Null
    $nulo = NULL;
    $tambienNulo; 

// --- * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" 

    $lenguaje = "PHP";
    echo "¡Hola, $lenguaje!";