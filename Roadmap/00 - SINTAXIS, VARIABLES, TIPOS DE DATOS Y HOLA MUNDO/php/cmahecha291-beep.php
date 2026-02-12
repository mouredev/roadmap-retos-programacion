<?php
    //WEB OFICIAL PHP
        // https://www.php.net
    //TIPOS DE COMENTARIOS EN PHP :
        // Comentario de una sola linea " // " es utilizando dos barras o slash.
        # Comentario de una sola linea " # " este se genera utilisando un numeral.
        /* 
            Comentario multilinea " / * * / " se genera utilizando una barra al inicio con un asterisco y se cierra 
            al final con un asterisco y una barra, y sirve para hacer que todo el texto o codigo que este dentro de 
            dichos simbolos no se tomara en cuenta a la hora de ejecutar el codigo.
        */
    //DECLARACION DE VARIABLES
        /*
            Para declara variables en el leguaje de programacion PHP se utiliza el simbolo "$" segudo del nombre de
            la variable, luego en el signo " = " con el cual se le asigna un valor a dicha variable y por ultimo se finaliza 
            con un punto y coma " ; ", ejemplo : $myfloat = 19,9; oh $name = value; , como php es un lenguje de tipado 
            dinamico no es necesario asignar directamente el tipo de valor a ingresar, si es una cadena de texto seria 
            " $mystring = "Christian"; " con comillas dobles para identificar que es una cadena de texto.
        */
            $my_integer = 17;
            $my_float = 17,5;
            $my_string = "Christian";
            $my_array = array(1, 2, 3);
            $my_boolean = true;
            $my_boolean = false;
        //  Constantes en PHP
            /*
                Una variable se caracteriaza por que no cambia su contenido despues de asignarlo, en php a diferencia de las 
                las variables no es necesario declararlas con el signo " $ " y dichas constantes se utilizan para definir 
                informacion fija. 
             */
            public const pi = 3.1415926535;
            define("MI_CONSTANTE", 17);
        // Imprimir en  PHP
            /*
                Para imprimir en PHP debemos escribir echo, luego dentro de comillas ponemos en texto y terminamos con punto y coma,
                ejemplo : echo "Hola soy PHP";
             */
            echo " Hola soy PHP ! ";
            /* 
                Imprimir textoy variables al tiempo
                    Para imprimir un texto y una variable al tiempo debemos escibir echo, luego enttre comillar el texto y para concatenar
                    utilizamnos un punto " . ", luego el nombre de la variable, ejemplo: echo "Soy una cadena de texto: " . $mysting; 
                    " Siempre que llamemos una variable la tendremos que llamar con el signo $".
            */
            echo " Soy una cadena de texto: " . $my_string;
    
        // OPERADORES EN PHP
            // Operadores Aritmeticos
                $a = 10;
                $b = 5;
                echo " La suma de a + b es: " . ($a + $b);
                echo " La resta de a - b es: " . ($a - $b);
                echo " La multiplicacion de a * b es: " . ($a * $b);
                echo " La division de a / b es: " . ($a / $b);
                echo " El modulo de a % b es: " . ($a % $b);
        

    
 
?>