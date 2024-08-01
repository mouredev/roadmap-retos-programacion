<?

//Sitio web Oficial: https://www.php.net

echo "Comentario de varias lineas";
/*
Comentario de varias lineas

*/
echo "Comentarios de una sola linea"; //Soy un comentario de una linea

echo "Comentario de una sola linea"; #Soy un comentario de una linea al estilo consola de Unix 

//Declaración de una variable y una constante
$nameDeVariable = "Variable pueden ser cualquier tipo de dato";
define('nameDeLaConstante', 'valor de la constante');
define('PI', 3.1416); 
echo "El valor de pi es:".PI;

//Declaraciones de los tipos de Datos primivitios
$integer = 10;
$float = 10.9;
$double = 1990.10;
$string = "Recien empiezo y apenas se usar github, si me pueden decir que fallo 
al subir la PR xfa";
$boolean = true;
$boolean = false;
$null = null;

//Array indexado
$numeros = array(1,2,4,5,6);
//Array asociativo
$datosUsuario = array(

    "nombre" => "juan",
    "edad" => 19

);

echo "Hola, mi proximo dolor de cabeza PHP";


?>