#!/usr/bin/bash
: '
/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */
'

# variables de fecha
now=$(date '+%Y-%m-%d %H:%M:%S')
birth='2004-11-20 12:00:00'

#los datos son falsos!!!!

# calculo de edad en años exactos
current_year=$(date '+%Y')
current_md=$(date '+%m%d')
birth_year=2004
birth_md=$(date -d "$birth" '+%m%d')

age=$(( current_year - birth_year - 1))


echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
echo "fecha actual:            $now"
echo "fecha nacimiento:        $birth"
echo "años transcurridos:      $age"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

# dificultad extra: 10 formatos distintos de la fecha de nacimiento
echo "formato 1 (dd-mm-yyyy):          $(date -d "$birth" '+%d-%m-%Y')"
echo "formato 2 (hh:MM:ss):            $(date -d "$birth" '+%H:%M:%S')"
echo "formato 3 (dia del ano):         $(date -d "$birth" '+%j')"
echo "formato 4 (dia de la semana):    $(date -d "$birth" '+%A')"
echo "formato 5 (nomrbe del mes):      $(date -d "$birth" '+%B')"
echo "formato 6 (mes abreviado):       $(date -d "$birth" '+%b')"
echo "formato 7 (numero dia semana):   $(date -d "$birth" '+%u')"
echo "formato 8 (numero semana ano):   $(date -d "$birth" '+%V')"
echo "formato 9 (iso completo):        $(date -d "$birth" '+%Y-%m-%dT%H:%M:%S%z')"
echo "formato 10 (rfc):                $(date -d "$birth" '+%a, %d %b %Y %H:%M:%S %z')"
echo "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"