<?php
// WEB OFICIAL
// Sitio web oficial de PHP: https://www.php.net/

// COMENTARIOS
// En PHP tenemos 3 tipos de comentarios:

// - Comentarios de una sola línea (// Comentario): Se utilizan para explicar partes concretas del código.
// Esto es un comentario de una línea.

// - Comentarios de varias líneas (/* Comentario */): Estos comentarios permiten explicar bloques extensos de código.
/*
 * Esto es un ejemplo de
 * un comentario
 * de varias líneas. */

// - Comentarios de documentación (/** Comentario */): Sirven para generar documentación.
/**
 * Este tipo de comentarios son los que usaremos cuando queramos
 * explicar el funcionamiento de, por ejemplo, una función
 * o una clase de PHP.
 * Generan documentación de forma automática, también llamada
 * PHPDoc y suelen ir acompañados de etiquetas que mejoran
 * su comprensión:
 * - @param: Nos sirve para determinar el tipo de variable que
 *           recibe la función.
 * - @return: En este caso lo que nos informará del tipo de
 *            retorno o resultado que produce la función. */

// VARIABLES Y CONSTANTES
/* - Variables: Para declarar una variable en PHP utilizamos
                el nombre que le queramos dar a la variable
                precedido por el símbolo del dólar ($).
                Podemos dejar una variable sin inicializar o
                darle el valor null. */
$miVariable = 12;
$miVariableSinInicializar = null;

/* - Constantes: En PHP tenemos dos formas de declarar una constante,
                 la primera de ellas es la palabra const seguido del
                 nombre de nuestra constante y su valor.
                 También las podemos declarar con el método define(),
                 que recibe 2 parámetros: un string con el nombre de la
                 constante y un valor.
                 Por convención, las constantes deben declararse con mayúsculas. */
const MI_CONSTANTE = 33;
define('MI_OTRA_CONSTANTE', 40);

// DATOS PRIMITIVOS
// En PHP tenemos los siguientes tipos de datos primitivos:
$miInteger = 12; // Integer: Almacena números enteros.
$miFloat = 12.64; // Float: Almacena números con decimales.
$miBoolean = true; // Boolean: Sirve para valores lógicos (true o false).
$miNull = null; // Null: Almacena un dato nulo -sin valor-.
$miString = 'Esto es una cadena'; // String: Sirve para cadenas de texto o caracteres únicos.
$miArray = array('a', 'b', 'c'); // Array: Sirve para almacenar varios datos en un mismo lugar.

// IMPRESIÓN
echo '¡Hola, PHP!';