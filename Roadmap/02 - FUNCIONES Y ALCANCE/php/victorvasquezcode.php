<?php
declare(strict_types=1);

/*
|--------------------------------------------------------------------------
| UTILIDADES BÁSICAS
|--------------------------------------------------------------------------
*/

function saludar(): string
{
    return "Hola como estas";
}

function saludarPersona(string $nombre): string
{
    return "Hola como estas, $nombre";
}

function sumar(int $a, int $b): int
{
    return $a + $b;
}

function multiplicar(int $a, int $b): int
{
    return $a * $b;
}

function saludarDefecto(string $nombre = "Invitado"): string
{
    return "Hola, $nombre";
}

function mostrarArray(array $array): string
{
    return implode(" ", $array);
}

/*
|--------------------------------------------------------------------------
| VARIABLES (BUENA PRÁCTICA)
|--------------------------------------------------------------------------
*/

function ejemploVariables(): array
{
    $local = 50;
    return [
        "local" => $local
    ];
}

/*
|--------------------------------------------------------------------------
| MOTOR DE REGLAS (CORE SENIOR)
|--------------------------------------------------------------------------
*/

function procesarNumeros(array $reglas, int $limite = 100): array
{
    $resultado = [];
    $contadorNumeros = 0;

    for ($i = 1; $i <= $limite; $i++) {
        $texto = "";

        foreach ($reglas as $divisor => $valor) {

            if ($i % $divisor === 0) {

                // Permite string o función (nivel pro)
                if (is_callable($valor)) {
                    $texto .= $valor($i);
                } else {
                    $texto .= $valor;
                }
            }
        }

        if ($texto === "") {
            $resultado[] = $i;
            $contadorNumeros++;
        } else {
            $resultado[] = $texto;
        }
    }

    return [
        "resultado" => $resultado,
        "contador" => $contadorNumeros
    ];
}

/*
|--------------------------------------------------------------------------
| PRESENTACIÓN (SALIDA)
|--------------------------------------------------------------------------
*/

function imprimirResultados(): void
{
    echo saludar() . "<br>";
    echo saludarPersona("Victor") . "<br>";
    echo "Suma: " . sumar(10, 15) . "<br>";
    echo "Multiplicación: " . multiplicar(10, 15) . "<br>";
    echo saludarDefecto() . "<br>";
    echo mostrarArray([1, 2, 3, 4]) . "<br>";

    $vars = ejemploVariables();
    echo "Variable local: " . $vars["local"] . "<br>";

    // Motor dinámico
    $data = procesarNumeros([
        3 => "Hola",
        5 => "Mundo",

        // Nivel PRO: reglas dinámicas
        7 => fn($i) => "Siete($i)"
    ]);

    echo implode(" ", $data["resultado"]);
    echo "<br>Total números: " . $data["contador"];
}

/*
|--------------------------------------------------------------------------
| EJECUCIÓN
|--------------------------------------------------------------------------
*/

imprimirResultados();
?>