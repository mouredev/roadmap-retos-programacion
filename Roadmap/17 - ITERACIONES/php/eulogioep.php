<?php
/**
 * Demostración de diferentes mecanismos de iteración en PHP
 * 
 * PHP ofrece múltiples formas de realizar iteraciones, cada una
 * con sus propias características y casos de uso específicos.
 */

echo "=== Demostración de Mecanismos de Iteración en PHP ===\n\n";

// 1. Bucle for tradicional
echo "1. Usando bucle for tradicional:\n";
/*
 * El bucle for es uno de los más comunes y versátiles.
 * Sintaxis: for (inicialización; condición; incremento)
 */
for ($i = 1; $i <= 10; $i++) {
    echo $i . " ";
}
echo "\n\n";

// 2. Bucle while
echo "2. Usando bucle while:\n";
/*
 * El bucle while se ejecuta mientras una condición sea verdadera.
 * Es útil cuando no sabemos exactamente cuántas iteraciones necesitamos.
 */
$contador = 1;
while ($contador <= 10) {
    echo $contador . " ";
    $contador++;
}
echo "\n\n";

// 3. Bucle do-while
echo "3. Usando bucle do-while:\n";
/*
 * Similar al while, pero garantiza que el código se ejecute al menos una vez
 * ya que la condición se evalúa al final de cada iteración.
 */
$num = 1;
do {
    echo $num . " ";
    $num++;
} while ($num <= 10);
echo "\n\n";

// EXTRA: Más mecanismos de iteración

// 4. foreach con array
echo "4. Usando foreach con array:\n";
/*
 * foreach es especialmente útil para iterar sobre arrays y objetos.
 * Es muy legible y evita tener que manejar índices manualmente.
 */
$numeros = range(1, 10);
foreach ($numeros as $numero) {
    echo $numero . " ";
}
echo "\n\n";

// 5. array_map
echo "5. Usando array_map:\n";
/*
 * array_map aplica una función a cada elemento de un array.
 * Es útil para transformar datos de forma funcional.
 */
$resultado = array_map(function($n) {
    echo $n . " ";
    return $n;
}, range(1, 10));
echo "\n\n";

// 6. array_walk
echo "6. Usando array_walk:\n";
/*
 * array_walk es similar a array_map, pero modifica el array original
 * y permite pasar parámetros adicionales a la función de callback.
 */
array_walk($numeros, function($valor) {
    echo $valor . " ";
});
echo "\n\n";

// 7. Iterator
echo "7. Usando Iterator:\n";
/*
 * PHP proporciona varias clases de iterador para manejar colecciones
 * de manera más orientada a objetos.
 */
$arrayIterator = new ArrayIterator($numeros);
while ($arrayIterator->valid()) {
    echo $arrayIterator->current() . " ";
    $arrayIterator->next();
}
echo "\n\n";

// 8. Generator
echo "8. Usando Generator:\n";
/*
 * Los generadores permiten crear iteradores de forma simple y eficiente
 * sin necesidad de implementar la interfaz completa de Iterator.
 */
function generarNumeros() {
    for ($i = 1; $i <= 10; $i++) {
        yield $i;
    }
}

foreach (generarNumeros() as $numero) {
    echo $numero . " ";
}
echo "\n\n";

// 9. array_reduce
echo "9. Usando array_reduce:\n";
/*
 * Aunque array_reduce se usa principalmente para reducir un array a un solo valor,
 * también puede usarse para iterar realizando una acción en cada paso.
 */
array_reduce($numeros, function($carry, $item) {
    echo $item . " ";
    return $carry;
});
echo "\n\n";

// 10. SPL DirectoryIterator (ejemplo con números)
echo "10. Usando SPL DirectoryIterator (simulado con números):\n";
/*
 * PHP proporciona iteradores especializados para diferentes propósitos.
 * Aquí simulamos uno similar a DirectoryIterator pero con números.
 */
class NumberIterator implements Iterator {
    private $position = 0;
    private $array = [];

    public function __construct() {
        $this->array = range(1, 10);
    }

    public function rewind() {
        $this->position = 0;
    }

    public function current() {
        return $this->array[$this->position];
    }

    public function key() {
        return $this->position;
    }

    public function next() {
        ++$this->position;
    }

    public function valid() {
        return isset($this->array[$this->position]);
    }
}

$numberIterator = new NumberIterator();
foreach ($numberIterator as $number) {
    echo $number . " ";
}
echo "\n\n";

echo "=== Fin de la demostración ===\n";
?>