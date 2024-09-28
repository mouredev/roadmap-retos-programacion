#!/bin/bash


# * EJERCICIO:
# * Empleando tu lenguaje, explora la definiciÃ³n del tipo de dato
# * que sirva para definir enumeraciones (Enum).
# * Crea un Enum que represente los dÃ­as de la semana del lunes
# * al domingo, en ese orden. Con ese enumerado, crea una operaciÃ³n
# * que muestre el nombre del dÃ­a de la semana dependiendo del nÃºmero entero
# * utilizado (del 1 al 7).


echo -e "\n\n=======================================EJERCICIO=======================================\n\n"

# Bash no tiene un tipo de dato "enum". Bash es un lenguaje de scripting que no admite la definiciÃ³n 
# de tipos de datos enumerados como en otros lenguajes de programaciÃ³n. Hay que simularlo

declare -A week

week[MONDAY]='1'
week[TUESDAY]='2'
week[WEDNESDAY]='3'
week[THURSDAY]='4'
week[FRIDAY]='5'
week[SATURDAY]='6'
week[SUNDAY]='7'


for key in "${!week[@]}"; do
    if [[ "${week[$key]}" -eq '3' ]]; then
        echo "$key"
    fi
done


echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"

# * DIFICULTAD EXTRA (opcional):
# * Crea un pequeÃ±o sistema de gestiÃ³n del estado de pedidos.
# * Implementa una clase que defina un pedido con las siguientes caracterÃ­sticas:
# * - El pedido tiene un identificador y un estado.
# * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
# * - Implementa las funciones que sirvan para modificar el estado:
# * - Pedido enviado
# * - Pedido cancelado
# * - Pedido entregado
# *  (Establece una lÃ³gica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
# * - Implementa una funciÃ³n para mostrar un texto descriptivo segÃºn el estado actual.
# * - Crea diferentes pedidos y muestra cÃ³mo se interactÃºa con ellos. 



declare -A order_management

order_management[PENDING]=1
order_management[SENT]=2
order_management[DELIVERED]=3
order_management[CANCELED]=4        
    

function initialize_order {

    local order_id=$1
    declare -g "order_${order_id}_status"
    eval "order_${order_id}_status=${order_management[PENDING]}"
    echo -e "Order $order_id initialized with status PENDING\n"

}



function send_order {

    local order_id=$1
    local current_status_var="order_${order_id}_status"
    local current_status=${!current_status_var}

    if [[ $current_status == "${order_management[PENDING]}" ]]; then
        echo -e "The order with the id $1 has been received and is ready to be shipped\n"
        eval "$current_status_var=${order_management[SENT]}"
        echo -e "The order with the id $order_id has already been submitted\n"
    else
        #status=${order_management[CANCELED]}v
        #echo -e "The order with the id $1 has been cancelled\n"
        echo -e "The order with the id $order_id cannot be sent\n"
    fi

}
    
function delivered_order {

    local order_id=$1
    local current_status_var="order_${order_id}_status"
    local current_status=${!current_status_var}

    if [[ $current_status == "${order_management[SENT]}" ]]; then
        eval "$current_status_var=${order_management[DELIVERED]}"
        echo -e "The order with the id $1 has been delivered\n"
    else
        echo -e "The order with the id $order_id cannot be delivered\n"
    fi

}

function rejected_order {

    local order_id=$1
    local current_status_var="order_${order_id}_status"
    local current_status=${!current_status_var}

    if [[ $current_status == "${order_management[PENDING]}" ]] || [[ $current_status == "${order_management[SENT]}" ]]; then
        eval "$current_status_var=${order_management[CANCELED]}"
        echo -e "The order with the id $order_id has been cancelled\n"
    else            
        [[ $current_status == "${order_management[DELIVERED]}" ]]
        echo -e "The order with the id $order_id has been delivered and cannot be cancelled\n"
    fi

}

function show_status {

    local order_id=$1
    local current_status_var="order_${order_id}_status"
    local current_status=${!current_status_var}

    echo -e "The order with id $order_id is in status $current_status\n"
}


initialize_order 1
show_status 1

send_order 1
show_status 1

delivered_order 1
show_status 1

rejected_order 1
show_status 1

initialize_order 2
show_status 2
send_order 2
rejected_order 2
show_status 2

       

















