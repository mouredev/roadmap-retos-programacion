<?php

    // Ejemplo de funcion de orden superior con array map

    $numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    $squares = array_map(function($n) {
        return $n * $n;
    }, $numbers);

    foreach ($squares as $key => $values){
        echo "El cuadrado de ". $numbers[$key] . " es ". $values . "\n"; 
    }

    // Ejercicio extra

    echo "\n\nEJERCICIO EXTRA \n\n";

    $students = [
        ['name' => 'Ana', 'birthdate' => '2000-06-15', 'grades' => [8.5, 9.2, 7.3]],
        ['name' => 'Luis', 'birthdate' => '2002-12-03', 'grades' => [9.0, 8.7, 9.5]],
        ['name' => 'María', 'birthdate' => '2001-01-25', 'grades' => [6.5, 7.8, 8.2]],
        ['name' => 'Carlos', 'birthdate' => '2003-08-20', 'grades' => [9.1, 9.3, 9.4]],
        ['name' => 'Eva', 'birthdate' => '2000-03-11', 'grades' => [8.8, 9.0, 8.9]],
        ['name' => 'Fran', 'birthdate' => '1975-09-03', 'grades' => [2.5, 7.0]],
        ['name' => 'Daniel', 'birthdate' => '2010-07-02', 'grades' => [1, 1.5, 9.5, 9.8, 7.8, 3.6]],
    ];
    

    function calculateAverage($grades) {
        return array_sum($grades) / count($grades);
    }
        
    $averageGrades = array_map(function($student) {
        return [
            'name' => $student['name'],
            'average' => calculateAverage($student['grades'])
        ];
    }, $students);
    
    
    $topStudents = array_filter($averageGrades, function($student) {
        return $student['average'] >= 9;
    });
    
    usort($students, function($a, $b) {
        return strtotime($b['birthdate']) - strtotime($a['birthdate']);
    });
    
    
    $allGrades = array_merge(...array_column($students, 'grades'));
    $highestGrade = max($allGrades);
    
    echo "Promedio de calificaciones por estudiante:\n";
    foreach ($averageGrades as $student) {
        echo "{$student['name']}: {$student['average']}\n";
    }
    
    echo "\nMejores estudiantes (promedio >= 9):\n";
    foreach ($topStudents as $student) {
        echo "{$student['name']}: {$student['average']}\n";
    }
    
    echo "\nEstudiantes ordenados del más joven al más viejo:\n";
    foreach ($students as $student) {
        echo "{$student['name']} (Nacimiento: {$student['birthdate']})\n";
    }
    
    echo "\nLa calificación más alta entre todos los estudiantes es: $highestGrade\n";



    

