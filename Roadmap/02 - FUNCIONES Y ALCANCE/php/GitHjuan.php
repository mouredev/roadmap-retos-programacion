EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 <?php 

 echo "FUNCIONES" . '<br/>'; 

//---------------------Funcion simple
function funcion(){
	echo "Mi funcion" . "\n";
}
echo funcion();

echo "<br/>";

//--------------------Funcion con parametro

function funcion_con_parametro($name){
	echo "Mi nombre es " . $name . "\n";
}

echo funcion_con_parametro("Ryan");

echo "<br/>";

// Funcion con parametros por defecto
echo "===== Funcion con parametros por defecto ========";
echo "<br/>";
function funct_default($param1 = "Name", $param2 = "Lastname"){
	echo "Mi Nombre y Apellido es: " . $param1 . "\n" . $param2;
}

funct_default();
echo "<br/>";

//-------------------Funcion con parametros
echo "===== Funcion con parametros ========";
echo "<br/>";
function funt_parametros($name, $lastname){
	echo "Mi nombre y Apellido es: " . $name ."\n" . $lastname . "<br/>";
}
echo funt_parametros("Ryan", "Rainol");

//-----------------Funcion con parametros y retorno
echo "===== Funcion con parametros y retorno ========";
echo "<br/>";
function funct_return($num1, $num2){
	return $num1 + $num2;
}
$suma = funct_return(20, 12);
echo "El resultado de la suma es: " . $suma;

//-----------------Funcion dentro de otra funcion
echo "===== Funcion dentro de otra funcion ========";
echo "<br/>";
function funcion1(){
	function funcion2(){
		echo "Esta es una funcion dentro de otra funcion";
	}
	funcion2();
}

funcion1();
echo "<br/>";
//-----------------Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
echo "===== Funcion ya creadas en el lenguaje ========";
echo "<br/>";
//para consultar el tipo de dato
$funcion = "Valor de la funcion";
$funcion2 = 100; 
 var_dump($funcion);
echo "<br/>";
//imprimir valor de una variable
print_r($funcion);
echo "<br/>";

/* DIFICULTAD EXTRA (opcional) */
echo "===== DIFICULTAD EXTRA ========";
echo "<br/>";
// Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

function extra($text_1, $text_2){
	for($i = 1 ; $i <= 100 ; $i++){
		if($i % 3 === 0 && $i % 5 === 0){
			echo $text_1 . ' ' . $text_2 . "<br/>";
			}else if($i % 3 === 0){
			echo $text_1 . "<br/>";
			}else if($i % 5 === 0){
			echo $text_2 . "<br/>";
			}else{
			echo $i . "<br/>";
				}
			}
		
		}
	extra("Fizz", "Buzz");
