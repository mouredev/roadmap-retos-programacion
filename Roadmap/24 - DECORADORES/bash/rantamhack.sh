#!/bin/bash


# Bash no tiene soporte para decoradores por lo que hay que simularlos
# en base a funciones y variable globales


echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


# * EJERCICIO:
# * Explora el concepto de "decorador" y muestra como crearlo
# * con un ejemplo generico.


function decorator() {
    local function="$1"
    shift
    echo -e "\nEste texto se imprime antes de realizar un calculo "
    "$function" "$@"
    echo -e "Este texto se imprime despues de realizar el calculo\n"
}


function sum() {
    local num1=$1
    local num2=$2
    echo "El resultado de la suma es $(($1 + $2))"
}    
  
function subtract() {
    local num1=$1
    local num2=$2
    echo "El resultado de la resta es $(($1 - $2))"
}
 
function pow() {
    local base=$1
    local exponente=$2
    echo -e "El resultado de elevar la base $1 a la potencia $2 es: $(($1**$2))"
}



decorator sum 10 5
decorator subtract 10 6
decorator pow 5 3


echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"



# * DIFICULTAD EXTRA (opcional):
# * Crea un decorador que sea capaz de contabilizar cuantas veces
# * se ha llamado a una funcion y aplicalo a una funcion de tu eleccion.

declare -A COUNTER


function decorator_counter() {
    local function="$1"
    shift
    
    COUNTER["$function"]=$(( ${COUNTER["$function"]} +1 ))
    if [ ${COUNTER["$function"]} == 1 ]; then
         echo "La funcion ha sido llamada ${COUNTER["$function"]} vez"
    else
        echo "La funcion ha sido llamada ${COUNTER["$function"]} veces"
    fi
    "$function" "$@"
}

function multiply() {
    local a="$1"
    local b="$2"
    echo $(($1 * $2))
}

function multiply_decorated() {
    decorator_counter multiply "$@"
}


multiply_decorated 5 3
multiply_decorated 7 2
multiply_decorated 15 17
multiply_decorated 24 42


