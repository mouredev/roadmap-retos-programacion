// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23
#include <algorithm> // Libreria con un conjunto de algoritmos
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <iomanip> // Para setprecision
#include <ctime>   // Para manejo de fechas

/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
*/

// Definimos una estructura para representar a un estudiante
struct Student {
    std::string name;
    std::string birthdate;
    std::vector<double> grades;
};

// Función para calcular el promedio de una lista de calificaciones
double average(const std::vector<double>& grades) {
    if (grades.empty()) return 0.0;
    double sum = std::accumulate(grades.begin(), grades.end(), 0.0);
    return sum / grades.size();
}

// Función para convertir una fecha en formato string a time_t
time_t stringToDate(const std::string& date) {
    struct tm tm{};
    strptime(date.c_str(), "%Y-%m-%d", &tm);
    return mktime(&tm);
}

int main() {
    // Lista de estudiantes
    std::vector<Student> students = {
        {"Adán", "2004-06-28", {9.7, 10.0, 9.9}},
        {"Andy", "2006-07-17", {9.5, 9.0, 9.0}},
        {"Mauricer", "2004-03-15", {6.0, 7.5, 8.0}},
        {"David", "2005-06-30", {10.0, 9.5, 9.5}}
    };

    // Promedio de calificaciones
    std::cout << "Promedio de calificaciones:" << std::endl;
    for (const auto& student : students) {
        double avg = average(student.grades);
        std::cout << student.name << ": " << std::fixed << std::setprecision(2) << avg << std::endl;
    }
    
    // Mejores estudiantes
    std::cout << "\nMejores estudiantes (promedio >= 9):" << std::endl;
    for (const auto& student : students) {
        if (average(student.grades) >= 9.0) {
            std::cout << student.name << std::endl;
        }
    }

    // Ordenar estudiantes por fecha de nacimiento, de más joven a más viejo
    // Funcion de orden superior
    std::sort(students.begin(), students.end(), [](const Student& a, const Student& b) {
        return stringToDate(a.birthdate) > stringToDate(b.birthdate);
    });

    std::cout << "\nEstudiantes ordenados por nacimiento (de más joven a más viejo):" << std::endl;
    for (const auto& student : students) {
        std::cout << student.name << ": " << student.birthdate << std::endl;
    }

    // Mayor calificación entre todos los estudiantes
    double highest_grade = 0.0;
    for (const auto& student : students) {
        for (double grade : student.grades) {
            if (grade > highest_grade) {
                highest_grade = grade;
            }
        }
    }

    std::cout << "\nMayor calificación entre todos los estudiantes: " << highest_grade << std::endl;

    return 0;
}
