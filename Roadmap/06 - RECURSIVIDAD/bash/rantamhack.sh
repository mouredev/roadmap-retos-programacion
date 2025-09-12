#!/bin/bash


#* EJERCICIO:
#     * Entiende el concepto de recursividad creando una función recursiva que imprima
# * números del 100 al 0.
# *
# * DIFICULTAD EXTRA (opcional):
# * Utiliza el concepto de recursividad para:
# * - Calcular el factorial de un número concreto (la función recibe ese número).
# * - Calcular el valor de un elemento concreto (según su posición) en la #
# *   sucesión de Fibonacci (la función recibe la posición).

echo -e "\n\n=====================================EJERCICIO=====================================\n\n"

function recursive(){
    if [[ $1 -ge 0 ]]; then
        echo $1
        recursive $(( $1 -1 ))
    fi
}
recursive 100  

echo -e "\n\n=====================================DIFICULTAD EXTRA=====================================\n\n"

# Función factorial

function factorial(){

    if [[ $1 -eq 1 ]]; then
        echo 1
    else 
        value=$(factorial $(( $1 -1 )))
        result=$(( $1 * value ))
        echo $result
    fi
}
factorial 5
echo "El valor factorial de 5 es:" $result

# Función factorial aplicada a posicion de elementos  en fibonacci

read -p "Introduce un numero entero: " num
echo "El numero elegido es $num"

function fibonacci(){

    if [[ $1 -lt 2 ]]; then
        echo 1
    else
        value_position=$(( $(fibonacci $(( $1 -1 )))+$(fibonacci $(( $1 -2 ))) ))
        echo $value_position

    fi
}


fibonacci num
echo "El valor de la posicion $num en la sucesion de fibonacci es: $value_position"


n=$value_position

function factorial_fib(){
    factor=$(factorial_fib $(( n -1 )))
    result=$(( factor * n ))

}
factorial n
echo "El valor de la posición $num en la sucesion de fibonacci es: $value_position"
echo "El valor del factorial de $n es: $result"



 