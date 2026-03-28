<?php
declare(strict_types=1);
/*
|--------------------------------------------------------------------------
| ESTRUCTURA DE CONTROL EN PHP
|--------------------------------------------------------------------------
*/

function condicionales(): void
{
    echo "=== CONDICIONALES ===" . "<br>";

    $edad = 20;

    // IF - ELSEIF - ELSE
    if ($edad >= 18) {
        echo "Mayor de edad" . "<br>";
    } elseif ($edad === 17) {
        echo "Casi mayor" . "<br>";
    } else {
        echo "Menor de edad" . "<br>";
    }

    // SWITCH
    $dia = 3;

    switch ($dia) {
        case 1:
            echo "Lunes" . "<br>";
            break;
        case 2:
            echo "Martes" . "<br>";
            break;
        default:
            echo "Otro dia" . "<br>";
    }

    // MATCH
    $nota = 15;
    $resultado = match (true) {
        $nota >= 18 => "Excelente",
        $nota >= 13 => "Aprobado",
        default => "Desaprobado",
    };
    echo $resultado . "<br>";
}

/*
|--------------------------------------------------------------------------
| ESTRUCTURA ITERATIVAS
|--------------------------------------------------------------------------
*/

function iterativas(): void
{
    echo "=== ITERATIVAS ===" . "<br>";

    //FOR
    for ($i = 0; $i < 3; $i++) {
        echo "FOR: $i" . "<br>";
    }

    //WHILE
    $i = 0;
    do {
        echo "DO-WHILE $i" . "<br>";
        $i++;
    } while ($i < 3);

    //FOREACH
    $nombres = ["Victor", "Ana", "Luis"];
    foreach ($nombres as $nombre) {
        echo "FOREACH: $nombre" . "<br>";
    }
}

/*
|--------------------------------------------------------------------------
| CONTROL DE FLUJO
|--------------------------------------------------------------------------
*/

function controlFlujo(): void
{
    echo "=== CONTROL DE FLUJO ===" . "<br>";
    for ($i = 1; $i <= 5; $i++) {
        if ($i === 3) {
            continue; //salta esta interacion
        }

        if ($i === 5) {
            break; //rompe el bucle
        }
        echo $i . "<br>";
    }
}

/*
|--------------------------------------------------------------------------
| MANEJO DE EXCEPCIONES
|--------------------------------------------------------------------------
*/
function excepciones(): void
{
    echo "=== EXCEPCIONES ===" . "<br>";

    try {
        $divisor = 0;
        if ($divisor === 0) {
            throw new Exception("No se puede dividir entre cero");
        }
        echo 10 / $divisor;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "<br>";
    } finally {
        echo "Bloque final ejecutado" . "<br>";
    }
}

/*
|--------------------------------------------------------------------------
| FUNCIONES Y OBJETOS
|--------------------------------------------------------------------------
*/

function funciones(): void
{
    echo "=== FUNCIONES ===" . "<br>";

    function sumar(int $a, int $b): int
    {
        return $a + $b;

    }
    echo sumar(5, 3) . "<br>";
}

class Persona
{
    public function saludar(): string
    {
        return "Hola desde un objeto";
    }
}

function objetos(): void
{
    echo "=== OBJETOS ===" . "<br>";
    $persona = new Persona();
    echo $persona->saludar() . "<br>";
}

/*
|--------------------------------------------------------------------------
| CRUD + ORDENACION
|--------------------------------------------------------------------------
*/
function crud(): void
{
    echo "=== CRUD Y ORDENACION ===" . "<br>";
    $usuarios = [
        ["id" => 1, "nombre" => "Javier", "edad" => 25],
        ["id" => 2, "nombre" => "Elizabeth", "edad" => 23],
    ];

    //INSERTAR
    $nuevoUsuario = ["id" => 3, "nombre" => "Jessica", "edad" => 30];
    $usuarios[] = $nuevoUsuario;

    echo "INSERTADO: " . "<br>";
    print_r($usuarios);

    //ACTUALIZAR
    foreach ($usuarios as &$usuario) {
        if ($usuario["id"] === 2) {
            $usuario["edad"] = 31;
        }
    }
    unset($usuario); //referencia

    echo "<br> ACTUALIZADO: " . "<br>";
    print_r($usuarios);

    //ELIMINAR
    foreach ($usuarios as $key => $usuario) {
        if ($usuario["id"] === 1) {
            unset($usuarios[$key]);
        }
    }

    //REINDEXAR ARRAY
    $usuarios = array_values($usuarios);

    echo "<br> ELIMINADO: " . "<br>";
    print_r($usuarios);

    //ORDENAR (por edad)
    usort($usuarios, function ($a, $b) {
        return $a["edad"] <=> $b["edad"];
    });

    echo "<br> ORDENADO POR EDAD: " . "<br>";
    print_r($usuarios);
}

/*
|--------------------------------------------------------------------------
| EJECUCION
|--------------------------------------------------------------------------
*/

condicionales();
iterativas();
controlFlujo();
excepciones();
funciones();
objetos();
crud();
?>