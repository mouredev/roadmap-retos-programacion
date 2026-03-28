<?php

declare(strict_types=1);

/*
|--------------------------------------------------------------------------
| OPERADORES
|--------------------------------------------------------------------------
*/

function operadores(): void
{
    echo "=== ARITMETICOS ===" . PHP_EOL;
    $a = 10;
    $b = 5;

    echo $a + $b . PHP_EOL;
    echo $a - $b . PHP_EOL;
    echo $a * $b . PHP_EOL;
    echo $a / $b . PHP_EOL;
    echo $a % $b . PHP_EOL;

    echo PHP_EOL . "=== COMPARACION ===" . PHP_EOL;
    var_dump($a == "10");
    var_dump($a === "10");

    echo PHP_EOL . "=== LOGICOS ===" . PHP_EOL;
    $edad = 20;
    $tieneDNI = true;

    var_dump($edad > 18 && $tieneDNI);
    var_dump($edad > 18 || false);
    var_dump(!$tieneDNI);

    echo PHP_EOL . "=== TERNARIO ===" . PHP_EOL;
    echo ($edad >= 18) ? "Mayor" : "Menor";
}

/*
|--------------------------------------------------------------------------
| ESTRUCTURAS DE CONTROL
|--------------------------------------------------------------------------
*/

function estructuras(): void
{
    echo PHP_EOL . "=== IF ===" . PHP_EOL;

    $edad = 20;

    if ($edad >= 18) {
        echo "Mayor";
    } elseif ($edad == 17) {
        echo "Casi";
    } else {
        echo "Menor";
    }

    echo PHP_EOL . "=== SWITCH ===" . PHP_EOL;

    $dia = 3;

    switch ($dia) {
        case 3:
            echo "Miercoles";
            break;
        default:
            echo "Otro";
    }

    echo PHP_EOL . "=== FOR ===" . PHP_EOL;

    for ($i = 0; $i < 5; $i++) {
        echo $i . " ";
    }

    echo PHP_EOL . "=== FOREACH ===" . PHP_EOL;

    $usuarios = ["Victor", "Ana"];

    foreach ($usuarios as $u) {
        echo $u . " ";
    }

    echo PHP_EOL . "=== MATCH ===" . PHP_EOL;

    $nota = 15;

    echo match (true) {
        $nota >= 18 => "Excelente",
        $nota >= 13 => "Aprobado",
        default => "Desaprobado"
    };
}

/*
|--------------------------------------------------------------------------
| EJERCICIO FINAL
|--------------------------------------------------------------------------
*/

function numerosFiltrados(): string
{
    $resultado = [];

    for ($i = 10; $i <= 55; $i++) {

        if (
            $i % 2 === 0 &&
            $i !== 16 &&
            $i % 3 !== 0
        ) {
            $resultado[] = $i;
        }
    }

    return implode(" ", $resultado);
}

/*
|--------------------------------------------------------------------------
| EJECUCION
|--------------------------------------------------------------------------
*/

operadores();
estructuras();

echo PHP_EOL . "=== EJERCICIO ===" . PHP_EOL;
echo numerosFiltrados();