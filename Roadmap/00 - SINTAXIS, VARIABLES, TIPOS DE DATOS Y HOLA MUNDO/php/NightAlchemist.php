<?php 

// https://www.php.net/

// one line comment
# one line comment too

/* 
Multi-line comment
Multi-line comment
*/

//variables
$var_example = "";
$var2 = 2;

//contantes
define("CONST1", "No cambio");
const MYCONST = "Const2";
define("array", [
    1,
    3,
    "good"
]);

//tipos de datos primitivos

$string = "Esto es una línea de texto";
$integer = 15;
$float = 1.5;
$boolean = true;
$var_array = ["my", 568, false, "Jimmyyyy"];

//El siguiente es el tipo de dato objeto, creamos antes una clase
class Car {
    public $color;
    public $model;
    public function __construct($color, $model) {
      $this->color = $color;
      $this->model = $model;
    }
    public function message() {
      return "My car is a " . $this->color . " " . $this->model . "!";
    }
  }
  
  $myCar = new Car("red", "Volvo"); # <= Este es el objeto, instanciado desde la clase
//fin del objeto

echo "Hola PHP!";

?>