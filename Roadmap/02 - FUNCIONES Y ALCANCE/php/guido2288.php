<?php
  /* Funciones con uno o varios parámetros  */

  function saludo ($name){
    echo "Hola $name"+"\n"; 
  }

  function sumar ($a , $b){
    echo "$a + $b" +"\n";
  }

  /* Funciones Sin parámetros ni retorno */

  function sinParametro(){
    echo "Buen día!" +"\n";
  }

  /* Funciones con retorno */
  function multiplica ($a , $b){
    $respuesta = $a * $b;
    return $respuesta;
  }

  /* Funciones dentro de funciones */
  function aritmetica ($a , $b){
    return sumar($a , $b);
  }

  /* Utiliza algún ejemplo de funciones ya creadas en el lenguaje. */

  // array_shift "Quita un elemento del principio del array"
  
  $stack = array("naranja", "plátano", "manzana", "frambuesa");

  $sinNaranja = array_shift($stack);

  print_r($stack);


  /* Pon a prueba el concepto de variable LOCAL y GLOBAL. */
  function ambitoVariables(){
    global $variableGlobal;
    $variableLocal = "Variable local";
    echo $variableLocal."\n";
    echo $variableGlobal."\n";
  }

  /* DIFICULTAD EXTRA (opcional) */

  function extra($varA , $varB){

    $count = 0;

    for ($i=1; $i < 100; $i++) { 
        if($i % 3 == 0 && $i % 5 != 0) echo "$varA <br>";

        if($i % 5 == 0 && $i % 3 != 0) echo "$varB <br>";

        if($i % 3 == 0 && $i % 5 == 0) echo "$varA  $varB <br>";

        if($i % 3 != 0 && $i % 5 != 0) {
            echo "$i <br>";
            $count ++;
        };
    }

    echo "El total es: $count";

}

extra("Manzana", "Banana");

?>