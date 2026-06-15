<?php

// Operadores aritméticos.
$a = 10;
$b = 5;
echo "Valores usados para las operaciones a: ". $a . " y b: " . $b . "\n"; 
echo "Suma(a+b): " . ($a + $b) . "\n";
echo "Resta(a-b): " . ($a - $b) . "\n";
echo "Multiplicación(a*b): " . ($a * $b) . "\n";
echo "Dividir(a/b): " . ($a / $b) . "\n";
echo "Exponenciación: " . ($a** $b) . "\n";
echo "Módulo, devuelve el resto de la división entera de a entre b: \n"  . ($a % $b) . "\n";

// if else if
echo "\nEstructuras de control\n";
echo "Usando if else if\n";
$a = 5;
$b = 10;

if ($a > $b) {
    echo "El valor de a es mayor que el valor de b\n";
} else if ($b > $a){
    echo "El valor de b es mayor que el valor de a\n";
} else if ( $b = $a){
    echo "El valor de a y el valor de b son iguales\n";
}

//switch
echo "\nUsando switch\n";

$codigoError = 200;

switch ($codigoError) {
    case 200:
        echo "Éxito";
        break;
    case 404:
        echo "Error";
        break;
    default:
        echo "Código desconocido";
}

//match (php8+)
echo "\n\nUsando match (sólo disponible a partir de php8+)\n";
$status = 2 - 2 ; 

$mensaje = match ($status) {
    0 => "Inactivo",
    1 => "Activo", 
    default => "Estado desconocido",
};
echo $mensaje . "\n";

// Estructuras Iteractivas(Bucles)
// While
echo "\nBucle While:\n";
$contador = 1;
while ($contador <= 3) {
    echo "Vuelta: " . $contador . "\n";
    $contador += 1; //Incremento
};

// do while
echo "\nBucle do-While\n";
$numero = 10;
do {
    echo"\nEste código se ejecuta una vez, mientras la operación ".$numero. " por 2, no supere 150";
    $numero = $numero*2;
}while ($numero < 150);

// for
echo "\n\nBuble for\n\n";
for ( $i = 0; $i <= 10; $i = $i + 2){
    echo "Número par " . $i. "\n";
}

// foreach

echo "\n\nBucle foreach\n\n";
$precios = [10,20,30];
$total = 0;

foreach ($precios as $precio){
    $total = $total + $precio;
    echo "Viendo el bucle en acción. ".$total. "\n";
}
echo "El total es: ". $total . "\n";

// Excepciones try,catch,finally

echo "\n\nEstructuras de Excepciones\n\n";
$divisor = 15 - 15;

try{
    if($divisor === 0) {
        throw new Exception("Error matemático: División por cero.");
    }else{
        $resultado = 100 / $divisor;
        echo $resultado;
    }
    
}catch (Exception $e){
    echo "Se detecto un problema: ". $e->getMessage();
}finally {    
    echo "\nOperación finalizada."; // Esta línea se ejecuta siempre, falle o no falle
}

// Estructura de alteración de flujo

echo "\n\nEstructura de alteración de flujo\n\n";

for ($i = 1; $i <= 5; $i++) {
    if( $i === 2){
        continue; // Se salta el 2
    }
    if ($i === 4) {
        break; // detiene el bucle por completo al llegar a 4
    }
    echo "Número: " . $i . "\n"; // Imprime solo el 1 y el 3
}

echo "\n\nDIFICULTAD EXTRA\n\n";



for ( $i = 10; $i <= 55; $i++){
    // Verificamos si es par
    if ( $i % 2 !== 0){
        continue;
    }
    
    // Verificamos que no sea el número 16

    if ($i === 16){
        continue;
    }

    // verificamos que no sea multiplos de 3
    if($i % 3 === 0){
        continue;
    }

    // Si pasa todos los filtro , se imprime.
    // echo $i . PHP_EOL;
    echo $i. "\n";
}
// Explicación de los filtros utilizados:
// $i % 2 !== 0: Descarta los números impares (el residuo de la división entre 2 no es 0).
// $i === 16: Excluye específicamente el número 16 de la lista.
// $i % 3 === 0: Detecta y descarta los múltiplos de 3 (como el 12, 18, 24, 30, 36, 42, 48, 54) porque su residuo es 0.
// PHP_EOL: Es una constante nativa de PHP que aplica un salto de línea limpio según el sistema operativo en el que ejecutes la consola.

