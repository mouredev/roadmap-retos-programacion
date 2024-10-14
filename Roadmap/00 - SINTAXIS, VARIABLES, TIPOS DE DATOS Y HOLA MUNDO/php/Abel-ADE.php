<?php

// Página Web Oficial: https://www.php.net/manual/es/index.php

//Tipos de comentarios en PHP:

    // Comentario de una sola línea
    # Otro Comentario de una línea
    /*  Comentario 
        multilínea 
    */

    /**
     * Comentario multilínea 
     * que se utiliza 
     * para generar documentación del programa
     */

//Declaración y asignación de variables
$variableCamelCase = 'Hola, Mundo!';

//Declaración y asignación de constantes
const MI_CONSTANTE = 12; //Se define en tiempo de compilación
define('OTRA_CONSTANTE', 50); //Se define en tiempo de ejecución

//Mostrar el contenido
print $variableCamelCase;
print MI_CONSTANTE;
print OTRA_CONSTANTE;

//Tipos de datos primitivos en PHP
$miEntero = 100;
$miDecimal = 20.50;
$miBooleano = true;
$miTexto = 'Soy un texto';
$miNulo = null;

//Imprime por terminal el texto: 'Hola, PHP!'
print 'Hola, PHP!';
