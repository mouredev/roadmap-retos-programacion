<?php

# Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

    // https://www.php.net

# Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

    // Este es un ejemplo de comentario de una sola línea

    # Esta es otra forma de crear un comentario de una sola línea, aunque no es lo común

    /*
        Este es un comentario
        que abarca varias líneas
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

# Crea una variable (y una constante si el lenguaje lo soporta).

    // Variable
    $miVariable = "Asignamos un texto como valor de la variable";

    // Constantes
    // Usando la función define()
    define("MI_CONSTANTE", "Hola mundo.");
    // Usando la palabra reservada 'const' fuera de la definición de una clase a partir PHP 5.3.0
    const OTRA_CONSTANTE = 'Hola Mundo';

# Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    # PHP maneja ocho (8) tipos de datos primitivos:
    // Tipo entero
    $entero = 16;

    // Tipo punto flotante (número decimal)
    $flotante = 3.14;

    // Tipo cadena de texto
    $cadena = "¡Hola, PHP!";

    // Tipo booleano
    $verdadero = true;
    $falso = false;

    // Tipo arreglo (array)
    $arreglo = array(1, 2, 3, "cuatro", 5.5); // Es común tener arreglos con elementos de diferentes tipos de datos
    $arregloIndexado = array("Manzana", "Banana", "Cereza");
    $arregloAsociativo = array("nombre" => "John Doe", "edad" => 30, "ciudad" => "Raccoon City");
    $arregloMultidimensional = array(
        array("Manzana", "Banana", "Cereza"),
        array("Rojo", "Amarillo", "Rojo"),
        array("Dulce", "Dulce", "Ácido")
    );
    $arregloLista = ["Elemento 1", "Elemento 2", "Elemento 3"]; // Arreglo con Sintaxis Corta (PHP 5.4+)
    $arregloCorto = ["nombre" => "María", "edad" => 25, "ciudad" => "Barcelona"]; // Arreglo Asociativo con Sintaxis Corta (PHP 5.4+)

    // Tipo objeto (a partir de una clase definida)
    class MiClase {
        public $propiedad;

        public function __construct($valor) {
            $this->propiedad = $valor;
        }
    }

    $objeto = new MiClase("Valor del objeto");

    // Tipo recurso (utilizado para manejar recursos externos, como archivos)
    $archivo = fopen("archivo.txt", "r");

    // Tipo nulo
    $nulo = null;

# Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    // Forma 1: echo
    echo $cadena; // Salida: ¡Hola, PHP!

    // Forma 2: print
    print $cadena; // Salida: ¡Hola, PHP!

    // Forma 3: printf (formateo)
    printf("Mensaje: %s", $cadena); // Salida: Mensaje: ¡Hola, PHP!

    // Forma 4: sprintf (similar a printf, pero devuelve la cadena formateada en lugar de imprimirla)
    $mensaje_formateado = sprintf("Saludo: %s", $cadena);
    echo $mensaje_formateado; // Salida: Saludo: ¡Hola, PHP!

?>