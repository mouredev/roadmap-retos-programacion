#!/bin/bash

# * EJERCICIO:
# * Explora el concepto de callback en tu lenguaje creando un ejemplo
# * simple (a tu eleccion) que muestre su funcionamiento.


echo -e "\n\n=======================================CONSIDERACIONES=======================================\n\n"


echo -e "\n\tEn bash no existe un return al uso por lo que hay que simularlo para"
echo -e "\n\tllamar a una funcion desde otra, para esto lo que hacemos es que el"
echo -e "\n\tvalor de la funcion a llamar lo igualamos a una variable y llamamos a esta\n"


echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


read -p "Elige un primer numero: " base
read -p "Elige un segundo numero: " altura

# Vamos a hacer el AREA DE UN TRIANGULO dividida en 2 funciones para que una llame a la otra
operation_one () {
    first_result=$(( $base * $altura ))
    echo $first_result
}

result=$(operation_one)

# Funcion area
value_area () {
    area=$(echo "scale=2; $1 / 2" | bc)
    echo -e "El valor del area de este triangulo es: $area"
}

value_area "$result"




# * DIFICULTAD EXTRA (opcional):
# * Crea un simulador de pedidos de un restaurante utilizando callbacks.
# * Estará formado por una función que procesa pedidos.
# * Debe aceptar el nombre del plato, una callback de confirmacion, una
# * de listo y otra de entrega.
# * - Debe imprimir un confirmación cuando empiece el procesamiento.
# * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
# *   procesos.
# * - Debe invocar a cada callback siguiendo un orden de procesado.
# * - Debe notificar que el plato está listo o ha sido entregado.

echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"



menu=("4Quesos" "Margarita" "Tropical" "Carbonara" "Campesina" "Barbacoa")

exit_program=false

read -p "Que Pizza de la carta te apetece tomar?: " order

function place_order() {

    local order=$1
    local callback=$2

    for pizza in "${menu[@]}"; do
        if [[ "$pizza" == "$order" ]]; then
            echo -e "\nHa elegido pizza $order, enviamos el pedido a cocina"
            waiting_time=$(($RANDOM % 10 + 1))
            sleep $waiting_time
            $callback "$order" #"order_in_process order_delivered"
            return 0
        fi
    done

    echo -e "\nLa pizza elegida no esta en la carta." 
    echo -e "\n[!] Saliendo del programa .....\n"
    exit_program=true 
}

function order_received() {

    local order=$1
    #local callback=$2

    if ! $exit_program; then
        echo -e "\nSu pedido de pizza $order ha llegado a cocina y esta en espera"
        waiting_time=$(($RANDOM % 10 + 1))
        sleep $waiting_time
        #$callback "$order" "order_delivered"
        order_in_process "$order"
    fi    
} 

function order_in_process() {

    local order=$1

    echo -e "\nSu pizza $order esta siendo procesada"
    waiting_time=$(($RANDOM % 10 + 1))
    sleep $waiting_time
    order_delivered "$order"
}

function order_delivered() {

    local order=$1

    echo -e "\nSu pizza $order esta preparada para entregar"
    waiting_time=$(($RANDOM % 10 + 1))
    sleep $waiting_time
    echo -e "\nSu pizza $order ha sido entregada"
}


place_order "$order" "order_received"

