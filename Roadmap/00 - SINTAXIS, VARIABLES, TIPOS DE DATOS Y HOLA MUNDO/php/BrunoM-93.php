<?php
# -SITIO WEB OFICIAL- 
  // PHP: Hypertext Preprocessor - https://www.php.net/


# -COMENTARIOS-

  //Esto es un comentario de una sola línea
  #Esto tambien es un comentario de una sola línea

  /*
  Esto es
  un comentario
  de varias
  líneas
  */

  /**
     * Los DocBlocks en PHP son comentarios de documentación especialmente formateados que se utilizan
     * para describir elementos del código, como funciones, clases, métodos, propiedades, y otros.
     * Estos comentarios están diseñados para ser interpretados por herramientas externas que generan documentación automáticamente,
     * como PHPDocumentor o Doxygen.
     *
     * @param string $nombre Nombre de la persona
     * @param int $edad Edad de la persona
     * @return string Saludo personalizado
  */
    function saludar($nombre, $edad) {
        // Implementación de la función
    }

# -VARIABLES-

  /* En PHP las variables se declaran con un signo de dólar seguido
     por el nombre de la variable, es sensible a minúsculas y mayúsculas.
     Un nombre de variable válido tiene que empezar con una letra o un
     carácter de subrayado (underscore), seguido de cualquier número de
     letras, números y caracteres de subrayado.
  */
  
  $nombre_variable = "valor de la variable";

# -CONSTANTES-

  /* Usamos constantes cuando necesitamos que el valor que almacenamos
     no se modifique aunque cometamos un error. Es decir, necesitamos
     que el valor almacenado permanezca idéntico, constante.
     A diferencia de las variables, es imposible definirles un valor
     mediante un operador de asignación (el signo igual), lo que facilita
     que “ni por error” alteremos su valor durante toda su vida útil,
     ya que siempre almacenarán el mismo valor.
  */
  
  // Hay dos formas de definir una constante en PHP
    const nom_const = "valor de la constante";
    define('nom_const2', "valor de la constate");

# -TIPOS DE DATOS PRIMITIVOS-

  /* PHP soporta varios tipos de datos primitivos entre ellos:
      *Escalares
          -boleanos (boolean)
          -enteros (integer)
          -punto flotante (float)
          -cadena (string)
      *Compuestos:
          -arreglos (array)
          -objetos (object)
      *Especiales:
          -null
  */
  
  $boolean = True; //o False
  $interger = 4; //Numeros entero
  $float = 4.5; //Numeros con coma decimal
  $string = "Hola Mundo!"; //Cadenas de caracteres con comillas dobles
  $string2 = 'Hola Mundo!'; //Cadenas de caracteres con comillas simples
  
  $array = array(1, 2, 3, 4); //Almacena varios datos en un mismo espacio de memoria.
  
  //Declaracion de una clase
  class Objeto {
      // Declaración de una propiedad
      public $nombre = 'un valor predeterminado';
      public $tipo = 'un valor';
  }
  
  //Creacion de un objeto de la clase previamente declarada
  $objeto = new Objeto();
  
  $var = null; //El tipo de dato especial NULL representa una variable sin valor.

# -IMPRESION POR TERMINAL-
  
  $lenguaje = 'PHP';

  // echo
  echo "¡Hola ".$lenguaje."!\n"; // Salida: ¡Hola PHP!

  // print
  print "¡Hola ".$lenguaje."!\n"; // Salida: ¡Hola PHP!

  // printf (formateo)
  printf("¡Hola %s!\n", $lenguaje); // Salida: ¡Hola PHP!

  // sprintf (parecido a printf, pero devuelve en una variable la cadena formateada)
  $cadena_formateada = sprintf("¡Hola %s!\n", $lenguaje);
  echo $cadena_formateada; // Salida: ¡Hola PHP!

?>