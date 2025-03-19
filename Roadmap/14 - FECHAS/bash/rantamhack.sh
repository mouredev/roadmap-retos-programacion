#!/bin/bash

# * EJERCICIO:
# * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
# * - Una primera que represente la fecha (di­a, mes, año, hora, minuto, segundo) actual.
# * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
# * Calcula cuantos años han transcurrido entre ambas fechas.


echo -e "\n\n=======================================EJERCICIO=======================================\n\n"

now=$(date +"%Y-%m-%d  %H:%M:%S")
echo -e "\nLa fecha en el momento actual es: $now"

birth_date=$(date -d "1962-07-09 19:15:00" +"%Y-%m-%d %H:%M:%S")
echo -e "\nLa fecha de nacimiento de Rantam fue: $birth_date"

function edad(){
    current_year=$(date +"%Y")
    birth_year=$(date -d "$birth_date" +"%Y")
    age=$((current_year - birth_year))

    echo -e "\nLa edad actual de rantam es: $age"
}

edad


 

# * DIFICULTAD EXTRA (opcional):
# * Utilizando la fecha de tu cumpleaños, formateala y muestra su resultado de
# * 10 maneras diferentes. Por ejemplo:
# * - Dia, mes y año.
# * - Hora, minuto y segundo.
# * - Di­a del año.
# * - Dia de la semana.
# * - Nombre del mes.
# * (lo que se te ocurra...)


echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"


echo -e "\nLa fecha de nacimiento de Rantam fue: \n"

echo -e "\n\t 1.- Usando el formato por defecto de  ('AÑO-MES-DIA  HORA-MINUTO-SEGUNDO'): $birth_date"
echo -e "\n\t 2.- usando formato con textos: $(date -d "$birth_date" +"%a %b %d %T %Y")"
echo -e "\n\t 3.- Usando dia, mes y año: $(date -d "$birth_date" +"%d/%m/%Y")"
echo -e "\n\t 4.- Usando hora, minuto y segundo: $(date -d "$birth_date" +"%H:%M:%S")"
echo -e "\n\t 5.- Dia del año: $(date -d "$birth_date" +"%j")"
echo -e "\n\t 6.- Dia de la semana: $(date -d "$birth_date" +"%A")"
echo -e "\n\t 7.- Mes de nacimiento: $(date -d "$birth_date" +"%B")"
echo -e "\n\t 8.- Numero de semana del año: $(date -d "$birth_date" +"%U")"
echo -e "\n\t 9.- Dia de la semana, mes, dia,  numero de semana y año en texto: $(date -d "$birth_date" +"%A, %d de %B, semana %U, del año %Y")"
echo -e "\n\t10.- Hora de nacimiento en formato 12 horas: $(date -d "$birth_date" +"%I:%M:%S%p") PM"













