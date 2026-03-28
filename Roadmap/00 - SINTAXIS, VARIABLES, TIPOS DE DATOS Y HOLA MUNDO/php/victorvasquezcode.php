<?php

declare(strict_types=1);

/*
|--------------------------------------------------------------------------
| URL OFICIAL
|--------------------------------------------------------------------------
| https://www.php.net
*/

/*
|--------------------------------------------------------------------------
| TIPOS DE COMENTARIOS
|--------------------------------------------------------------------------
*/

// Comentario de una línea

# Comentario estilo Unix

/*
    Comentario de múltiples líneas
*/

/*
|--------------------------------------------------------------------------
| VARIABLES Y TIPOS
|--------------------------------------------------------------------------
*/

$nombre = "Victor";        // string
$precio = 19.5;            // float
$esValido = true;          // bool
$variableVacia = null;     // null
$colores = ["Rojo", "Verde", "Azul"]; // array

const APELLIDO = "Vasquez";

/*
|--------------------------------------------------------------------------
| CLASE (TIPADO FUERTE)
|--------------------------------------------------------------------------
*/

class Persona
{
    public string $ciudad;
    public string $nombreCompleto;
    public int $edad;

    public function __construct(string $ciudad, string $nombreCompleto, int $edad)
    {
        $this->ciudad = $ciudad;
        $this->nombreCompleto = $nombreCompleto;
        $this->edad = $edad;
    }

    public function caminar(): string
    {
        return "Estoy caminando en {$this->ciudad}, mi nombre es {$this->nombreCompleto} y tengo {$this->edad} años";
    }
}

/*
|--------------------------------------------------------------------------
| INSTANCIA
|--------------------------------------------------------------------------
*/

$usuario = new Persona("Trujillo", "Victor Javier Vasquez Trauco", 25);

/*
|--------------------------------------------------------------------------
| SALIDA
|--------------------------------------------------------------------------
*/

echo $usuario->caminar() . PHP_EOL;

echo "Hola que tal soy $nombre " . APELLIDO . " y tengo {$usuario->edad} años" . PHP_EOL;

echo "¡Hola, PHP!" . PHP_EOL;