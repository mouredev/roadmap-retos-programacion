   <?php

   #----------------------------------------------------------------------------
   
   /* Crea un comentario en el código y coloca la URL del sitio web oficial del
   lenguaje de programación que has seleccionado. */

   # sitio web de php: https://www.php.net/
   
   /* Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...). */

   /* Comentarios
   de
   varias
   lineas */

   #  Esto es comentario de una sola linea estilo shell
   // Esto tambien es un comentario de una sola linea pero al estilo c++
   
   /*Crea una variable (y una constante si el lenguaje lo soporta).*/
   #Variable
   $var = 'Roberto';
   $Var = 'Juan';
   echo "$var, $Var" . "<br>";

   #Constante
   #define("PI", 3.1416);
   const PI = 3.1416;
   echo "El valor de pi de $var es " . " " . PI;

   /*Crea variables representando todos los tipos de datos primitivos
   del lenguaje (cadenas de texto, enteros, booleanos...).*/
   #numero (int)
   $edad = 25;
   #numero con decimal (float)
   $precio = 10.5;
   #String
   $nombre = "Victor";
   #Boolean
   $estado = true;
   #Array
   $colores = ["Morado", "Crema", "Celeste"];
   #NULL
   $variable_NULL = null;

   echo "<br> Hola que tal soy $nombre <br>";
   echo "Mi edad es $edad <br>";
   echo "Mis colores favoritos son: " . implode("; ", $colores) . "<br>";
   echo "Mi estado de animo es " . ($estado ? "Activo" : "Inactivo");

   /*Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/
   echo "<br>¡Hola , PHP!"
   ?>