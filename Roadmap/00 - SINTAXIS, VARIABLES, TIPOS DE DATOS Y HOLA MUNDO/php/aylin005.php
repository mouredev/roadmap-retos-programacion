<?php

//=================================================================================
/* - Crea un comentario en el código y coloca la URL del sitio web oficial del
        lenguaje de programación que has seleccionado. */

/* PHP sitio web oficial: https://www.php.net/
 DOCUMENTACIÓN (ES) https://www.php.net/manual/es/
 DOCUMENTACIÓN (EN) https://www.php.net/manual/en/ */


//=================================================================================
 /* - Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...). */

// PHP soporta comentarios tipo C, C++ y Shell Unix (También llamado estilo Perl) Ejemplos:

// Esto es un comentario de una linea, estilo C++
/* Esto es un comentario
    de varias lineas */
# Esto es un comentario de una sola linea, estilo shell

//=================================================================================
 /* - Crea una variable (y una constante si el lenguaje lo soporta).
    - Crea variables representando todos los tipos de datos primitivos
        del lenguaje (cadenas de texto, enteros, booleanos...). */

    // CONSTANTES =================================================================
        //Una constante es un identificador para un valor simple.
        //Ese valor no puede ser cambiado durante la ejecucion del script. Son case-sensitive
        //como las Superglobals, su entorno es global.

        //Se pueden definir con define() o const

        define("FOO", "algo");

        //const solo acepta valores escalares (bool, int, float, string) y arrays constantes.
        //con constant() se puede obtener el valor de una constante
        //Nota: NO se definen con $

        const CONSTANT = "Hello World";

    //VARIABLES ======================================================
        //Se representan con un $ seguida del nombre de la variable, son case sensitive.
        // (i) $this <-- variable escpecial que no puede ser asignada

        $var = 'Bob';
        $Var = 'Joe';
        echo "$var, $Var"; //imprime: 'Bob Joe'

        //Asignar por referencia con &
        $foo = 'Bob';
        $bar = &$foo;
        $bar = "Mi nombre es $bar";
        echo $bar . PHP_EOL;
        echo $foo . PHP_EOL;  //imprime: Mi nombre es Bob Mi nombre es Bob

        // (+) isset() <-- para saber si la variable ha sido inicializada
        // (+) unset() <-- para destruir una varaiable

        // (+) global keyword <-- para traer una variable del entorno global al local
        global $foo, $bar;

        // (+) variables static <--existen solo en el entorno local pero no pierde su valor cuando el programa sale de ese entorno
        function test()
        {
            static $a = 0;
            echo $a . PHP_EOL;
            $a++;
        }

        // (+) variables variables <-- toma el valor de la variable y lo trata como el nombre de la variable
        $a = 'hello';
        $$a = 'world';
        var_dump($hello); // Imprime: string(5) "world"

        // TIPOS /////////////////////////////////////////////////////
        
        //(escalares)
        $boolean = True;
        $int = 1234;
        $float = 1.234;
        $string = 'hola';

        $array1 = [
            "foo" => "bar", 
            "bar" => "foo"
        ];
        $array2 = array(
            "foo" => "bar", 
            "bar" => "foo"
            );
        
        $objeto = new stdClass();

        $null = null;
        
        $resource = fopen('php://stdout', 'w'); //tipo recurso
        // (+) fopen() <-- abre un archivo o URL

        //callabe <-- referencia a funcion o metodo que pasa a otra funcion como argumento
        function foo(callable $callback) {
            $callback();
        }


    // SUPERGLOBALS ================================================
        // variables predefinidas que estan disponibles en todos los scopes.
            // nota: AA = Associative Arrays <-- arreglos clave-valor;  A = Array

        $GLOBALS["var"]; // <-- AA contiene la referencia a variables globales definidas en el script
        // Nota: Trae solo una copia, y de una copia de la gloabal no se puede cambiar el valor original

        $_SERVER['HTTP_USER_AGENT']; // <-- A Contiene informacion obtenida del servidor 
        // como headers, paths, y locaciones de scripts

        $_GET['name']; // <-- AA contiene las variables pasadas al script desde los Query Params
        // ej. de " http://example.com/?name=Hannes." name = 'Hannes'

        $_POST['name']; // <-- AA contiene variables pasadas al script desde un POST
        // Solo cuando se usa 'application/x-www-form-urlencoded or multipart/form-data' Como el HTTP Content-Type
        
        $_REQUEST['name']; // <-- AA contiene por default los contenidos de  $_GET, $_POST y $_COOKIE

        $_FILES['file.txt']; // <-- AA contiene los elementos subidos al script por un metodo POST
        
        $_COOKIE['name']; // <-- AA contiene las variables pasadas al script por HTTP Cookies

        $_SESSION['newsession']; // <-- AA Contiene variables de sesion disponibles en el script

        $_ENV['name']; // <-- AA Contiene variables pasadas al script por el metodo del entorno.
        //Son importadas al namespace global de PHP desde el entorno en el que se ejecuta el interprete PHP


//=================================================================================
//Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!

echo "¡Hola, PHP!";


