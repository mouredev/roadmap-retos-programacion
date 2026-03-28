<?php
/*
EJERCICIO
✅  Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
✅  Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
✅  Crea una variable (y una constante si el lenguaje lo soporta).
✅  Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
✅  Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

/*
https://www.php.net/manual/es/
*/

//comentario una linea
#comentario una linea
/*
Comentario varias lineas
*/

$variable = 50;
define("PI", 3.1416);

class Persona
{
    public $nombre;
    public $edad;
    public $peso;
    public $es_valido;

    public $comidas;
}

$persona1 = new Persona();

$persona1->nombre = "Victor";
$persona1->edad = 25;
$persona1->peso = 90.5;
$persona1->es_valido = true;
$persona1->comidas = ["lomito", "chaufa"];

echo "Hola que tal soy " . $persona1->nombre . " tengo la edad de " . $persona1->edad;
echo "!Hola , PHP";
?>