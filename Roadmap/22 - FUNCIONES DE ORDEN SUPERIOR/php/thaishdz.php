<?php
/*
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones),✔️ utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones. ✔️
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio. ✔️
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven. ✔️
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.✔️
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).✔️
 */

/*
********** Este es un json que consideré como entrada externa **********

{
    "dataStudents" : [
        {
            "name": "Thais",
            "birthday": "10-09-1993",
            "grades": {
                "Math" : 4.5,
                "Biology" : 6,
                "Physics": 8,
                "Philosophy" : 9,
                "History": 8
            }
        },
        {
            "name": "Cristina",
            "birthday": "30-08-1991",
            "grades": {
                "Math" : 7,
                "Biology" : 5,
                "Physics": 7,
                "Philosophy" : 10,
                "History": 8
            } 
        },
        {
            "name": "Iván",
            "birthday": "01-07-1993",
            "grades": {
                "Math" : 10,
                "Biology" : 10,
                "Physics": 10,
                "Philosophy" : 7.5,
                "History": 8
            } 
        },
        {
            "name": "Paula",
            "birthday": "20-01-1995",
            "grades": {
                "Math" : 3,
                "Biology" : 5,
                "Physics": 7,
                "Philosophy" : 5.5,
                "History": 1
            } 
        },
        {
            "name": "Betancort",
            "birthday": "18-02-1991",
            "grades": {
                "Math" : 3.4,
                "Biology" : 9.2,
                "Physics": 2.5,
                "Philosophy" : 5,
                "History": 8
            } 
        },
        {
            "name": "Jerico",
            "birthday": "07-06-1980",
            "grades": {
                "Math" : 10,
                "Biology" : 9.2,
                "Physics": 10,
                "Philosophy" : 9.3,
                "History": 8
            } 
        }
    ]
}
************************************************************************

*/


$jsonDataStudents = file_get_contents("students.json"); // Al estar el json en otro path, hago esto
$dataset = json_decode($jsonDataStudents, true); // lo convierto a un array asociativo


function calculateAverageGrade(array $student)
{
   $grades = $student["grades"];
   $average = array_sum($grades) / count($grades);

   return [
      "name"      => $student["name"],
      "average"   => $average
   ];
}


function isTopStudent(array $student)
{
   return $student["average"] >= 9;
}

function sortStudentsByBirthdateDesc(array $students) : array 
{
   usort($students, function ($studentA, $studentB) {
      $birthA = DateTime::createFromFormat('d-m-Y', $studentA["birthday"]);
      $birthB = DateTime::createFromFormat('d-m-Y', $studentB["birthday"]);

      return $birthB <=> $birthA; // Ordenar desde el más joven al más viejo
   });
   
   return $students;
}

/* 
* Aquí entendí que solo debía devolver la nota más alta de todas
* porque consideré que en otro apartado ya estaba obteniendo 
* al alumnado con las mejores calificaciones
* así que me pareció volver a repetir lo mismo es por eso que solo devuelvo un valor
* En el caso de que hayan 2 estudiantes con la misma nota no pasaría nada 
* porque sería la nota más alta igualmente 😛
*/
function getHighestGrade(array $studentData): float 
{
   $grades = array_column($studentData, 'average');
   return max($grades);
}


// Las llamaditas a cada apartado del ejercicio
$averageStudentGrades = array_map('calculateAverageGrade', $dataset["dataStudents"]);
$bestStudents = array_filter($averageStudentGrades, 'isTopStudent');
$sortedStudentsByBirth = sortStudentsByBirthdateDesc($dataset["dataStudents"]);
$highestGrade = getHighestGrade($averageStudentGrades);
