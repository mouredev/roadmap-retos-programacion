#!/bin/bash

echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


# * EJERCICIO:
# * Explora el concepto de funciones de orden superior en tu lenguaje 
# * creando ejemplos simples (a tu elección) que muestren su funcionamiento.


function arithmetic() {
    square_root $1
    elevate_cube $2
}    

function square_root() {
    local num1=$1
    result=$(echo "scale=2; sqrt($num1)" | bc -l)
    echo -e "\nEl resultado de la raiz cuadrada de $num1 es $result\n"
}
function elevate_cube() {
    local num2=$1
    result=$(echo "scale=10; $num2 ^ 3" | bc -l)
    echo -e "El resultado de elevar al cubo $num2 es $result\n\n"
}

 arithmetic 25 10




echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"
 


# * DIFICULTAD EXTRA (opcional):
# * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
# * lista de calificaciones), utiliza funciones de orden superior para 
# * realizar las siguientes operaciones de procesamiento y análisis:
# * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
# *   y promedio de sus calificaciones.
# * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
# *   que tienen calificaciones con un 9 o mas de promedio.
# * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el mas joven.
# * - Mayor calificación: Obtiene la calificación mas alta de entre todas las
# *   de los alumnos.
# * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).



# Lista de estudiantes en formato JSON
students='[
    {"name":"Rantam", "born_date":"29-05-2000", "grades":[7.2, 9.0, 8.6]},
    {"name":"Helena", "born_date":"12-02-2005", "grades":[9.8, 9.2, 8.7]},
    {"name":"Silvia", "born_date":"10-07-2003", "grades":[8.5, 8.0, 8.4]},
    {"name":"Jose Luis", "born_date":"22-10-2003", "grades":[7.0, 6.5, 7.4]},
    {"name":"Fernando", "born_date":"17-07-1998", "grades":[5.0, 3.8, 4.6]},
    {"name":"Brais", "born_date":"11-06-2003", "grades":[8.0, 9.4, 9.7]}
]'

# Función para calcular el promedio
calculate_average() {
    local grades=("$@")
    local sum=0
    local count=${#grades[@]}
    for grade in "${grades[@]}"; do
        sum=$(echo "$sum + $grade" | bc)
    done
    echo "scale=2; $sum / $count" | bc
}

# Función para obtener la nota media de los estudiantes
get_average_grades() {
    echo "$students" | jq -r '.[] | [.name, (.grades | map(tostring) | join(" "))] | @tsv' |
    while IFS=$'\t' read -r name grades; do
        avg=$(calculate_average $grades)
        echo -e "$name\t$avg"
    done
}

# Función para obtener los mejores estudiantes
get_top_students() {
    get_average_grades | awk -F'\t' '$2 >= 9.0 { print $1, $2 }'
}

# Función para ordenar estudiantes desde el mas joven
sort_students_by_age() {
    echo "$students" | jq -r '.[] | [.name, .born_date] | @tsv' |
    while IFS=$'\t' read -r name born_date; do
        # Convertir la fecha de DD-MM-YYYY a YYYY-MM-DD para una ordenación correcta
        born_date_formatted=$(echo "$born_date" | awk -F'-' '{ printf "%04d-%02d-%02d", $3, $2, $1 }')
        echo -e "$name\t$born_date_formatted"
    done | sort -t$'\t' -k2,2r | awk -F'\t' '{ printf "%s\t%s\n", $1, $2 }'
}

# Función para obtener la calificación mas alta
get_highest_grade() {
    echo "$students" | jq -r '.[] | .grades[]' | sort -nr | head -n1
}

# Ejecución de las funciones
echo -e "\nPromedio calificaciones:\n"
get_average_grades

echo -e "\nMejores estudiantes:"
get_top_students

echo -e "\nEstudiantes ordenados desde el mas joven:"
sort_students_by_age

echo -e "\nMayor calificación:"
get_highest_grade

