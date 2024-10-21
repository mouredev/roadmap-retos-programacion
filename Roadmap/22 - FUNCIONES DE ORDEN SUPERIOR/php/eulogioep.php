<?php

// Clase Estudiante para manejar la información de cada alumno
class Estudiante {
    private string $nombre;
    private DateTime $fechaNacimiento;
    private array $calificaciones;

    public function __construct(string $nombre, string $fechaNacimiento, array $calificaciones) {
        $this->nombre = $nombre;
        $this->fechaNacimiento = new DateTime($fechaNacimiento);
        // Validamos que las calificaciones estén entre 0 y 10
        $this->calificaciones = array_filter($calificaciones, function($calif) {
            return $calif >= 0 && $calif <= 10;
        });
    }

    public function getNombre(): string {
        return $this->nombre;
    }

    public function getFechaNacimiento(): DateTime {
        return $this->fechaNacimiento;
    }

    public function getCalificaciones(): array {
        return $this->calificaciones;
    }
}

// Creamos una lista de estudiantes de ejemplo
$estudiantes = [
    new Estudiante(
        "Ana García",
        "2000-05-15",
        [9.5, 8.7, 9.2, 9.8]
    ),
    new Estudiante(
        "Carlos Pérez",
        "1999-03-20",
        [7.5, 8.0, 6.5, 7.8]
    ),
    new Estudiante(
        "María López",
        "2001-08-10",
        [9.0, 9.5, 9.3, 9.7]
    )
];

// Funciones auxiliares
function calcularPromedio(array $calificaciones): float {
    return array_sum($calificaciones) / count($calificaciones);
}

// 1. Obtener lista de estudiantes con sus promedios
function obtenerPromedios(array $estudiantes): array {
    return array_map(function($estudiante) {
        return [
            'nombre' => $estudiante->getNombre(),
            'promedio' => calcularPromedio($estudiante->getCalificaciones())
        ];
    }, $estudiantes);
}

// 2. Obtener mejores estudiantes (promedio >= 9)
function obtenerMejoresEstudiantes(array $estudiantes): array {
    return array_map(
        fn($estudiante) => $estudiante->getNombre(),
        array_filter($estudiantes, function($estudiante) {
            return calcularPromedio($estudiante->getCalificaciones()) >= 9;
        })
    );
}

// 3. Obtener lista ordenada por fecha de nacimiento (más joven primero)
function ordenarPorEdad(array $estudiantes): array {
    $estudiantesCopia = $estudiantes;
    usort($estudiantesCopia, function($a, $b) {
        return $b->getFechaNacimiento() <=> $a->getFechaNacimiento();
    });
    
    return array_map(function($estudiante) {
        return [
            'nombre' => $estudiante->getNombre(),
            'fechaNacimiento' => $estudiante->getFechaNacimiento()->format('Y-m-d')
        ];
    }, $estudiantesCopia);
}

// 4. Obtener la calificación más alta de todos los estudiantes
function obtenerMayorCalificacion(array $estudiantes): float {
    $todasLasCalificaciones = array_merge(...array_map(
        fn($estudiante) => $estudiante->getCalificaciones(),
        $estudiantes
    ));
    return max($todasLasCalificaciones);
}

// Mostrar resultados
echo "1. Promedios de calificaciones:\n";
print_r(obtenerPromedios($estudiantes));

echo "\n2. Mejores estudiantes (promedio >= 9):\n";
print_r(obtenerMejoresEstudiantes($estudiantes));

echo "\n3. Estudiantes ordenados por edad (más joven primero):\n";
print_r(ordenarPorEdad($estudiantes));

echo "\n4. Mayor calificación de todos los estudiantes:\n";
echo obtenerMayorCalificacion($estudiantes) . "\n";

// Ejemplos adicionales de funciones de orden superior en PHP
echo "\nEjemplos adicionales de funciones de orden superior:\n";

// Ejemplo 1: función que retorna otra función (closure)
function multiplicadorPor($factor) {
    return function($numero) use ($factor) {
        return $numero * $factor;
    };
}
$multiplicarPor2 = multiplicadorPor(2);
echo "Multiplicar 4 por 2: " . $multiplicarPor2(4) . "\n"; // Output: 8

// Ejemplo 2: función que recibe otra función como parámetro
function aplicarOperacion(array $numeros, callable $operacion): array {
    return array_map($operacion, $numeros);
}
$duplicar = fn($numero) => $numero * 2;
echo "Duplicar números [1,2,3]: ";
print_r(aplicarOperacion([1,2,3], $duplicar));

// Ejemplo 3: composición de funciones
function componerFunciones(callable $f, callable $g): callable {
    return function($x) use ($f, $g) {
        return $f($g($x));
    };
}
$sumar1 = fn($x) => $x + 1;
$duplicarYSumar1 = componerFunciones($sumar1, $duplicar);
echo "Duplicar 5 y sumar 1: " . $duplicarYSumar1(5) . "\n"; // Output: 11

?>