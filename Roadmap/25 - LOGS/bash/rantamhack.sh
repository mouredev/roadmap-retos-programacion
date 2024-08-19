#!/bin/bash

# * EJERCICIO:
# * Explora el concepto de "logging" en tu lenguaje. Configuralo y muestra
# * un ejemplo con cada nivel de "severidad" disponible.


echo -e "\n\n=======================================EJERCICIO=======================================\n\n"



# * Emergency: El sistema esta inutilizable
# * Alert :    Se debe de actuar inmediatemente
# * Critical:  El sistema esta en condiciones criticas
# * Error:     Se ha producido un error 
# * Warning:   Aviso en condiciones de peligro
# * Notice:    Aviso normal pero condiciones notables
# * Info:      Aviso de informacion, mensajes informatiovs
# * Debug:     Depuracion, mensajes de bajo nive


log_message() {
    local log_level=$1
    local log_message=$2
    local log_date=$(date '+%Y-%m-%d %H:%M:%S')
    

    case $log_level in
        DEBUG)
            echo "$log_date - DEBUG - $log_message"
            ;;
        INFO)
            echo "$log_date - INFO - $log_message"
            ;;
        NOTICE)
            echo "$log_date - NOTICE - $log_message"
            ;;
        WARNING)
            echo "$log_date - WARNING - $log_message"
            ;;
        ERROR)
            echo "$log_date - ERROR - $log_message"
            ;;
        CRITICAL)
            echo "$log_date - CRITICAL - $log_message"
            ;;
        ALERT)
            echo "$log_date - ALERT - $log_message"
            ;;
        EMERGENCY)
            echo "$log_date - EMERGENCY - $log_message"
            ;;
        *)
            echo "$log_date - UNKNOWN - $log_message"
            ;;
    esac
}


log_message "DEBUG" "[+] Entramos a la funcion"
log_message "INFO" "[+] La conexion con el servidor fue exitosa"
log_message "NOTICE" "[+] Es importante que revises el archivo syslog"
log_message "WARNING" "[!] Queda poco espacio en disco"
log_message "ERROR" "[!] Bloque de sangria previsto"
log_message "CRITICAL" "[!] Hay un error critico. Saliendo de la aplicacion ...."
log_message "ALERT" "[!] Se debe de actuar inmediatemente"
log_message "EMERGENCY" "[!] El sistema esta inutilizable"

# Los logs se pueden generar con el comando 'logger' y se pueden ver en el archivo de logs dependiendo de la distribucion (syslog, rsyslog,...)
# Este script se ha hecho para que aparezcan en la salida por terminal cuando se ejecuta
# con el comando 'logger' sustituimos en el case, tampoco necesitamos la variable 'log_date' ya que el archivo de logs proporciona la fecha y hora. QuedarÃ­a asi:

        
#   logger -p user.debug "$log_message"
#   logger -p user.info "$log_message"
#   logger -p user.notice "$log_message"
#   logger -p user.warn "$log_message"
#   logger -p user.err "$log_message"
#   logger -p user.crit "$log_message"
#   logger -p user.alert "$log_message"
#   logger -p user.emerg "$log_message"




echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"


# * DIFICULTAD EXTRA (opcional):
# * Crea un programa ficticio de gestion de tareas que permita añadir, eliminar
# * y listar dichas tareas.
# * - Añadir: recibe nombre y descripcion.
# * - Eliminar: por nombre de la tarea.
# * Implementa diferentes mensajes de log que muestren informacion segun la 
# * tarea ejecutada (a tu eleccion).
# * Utiliza el log para visualizar el tiempo de ejecucion de cada tarea. 


function time_spent() {
    local star_time=$(date +%s.%N)    
    "$@"
    local end_time=$(date +%s.%N)
    local elapsed_time=$(echo "$end_time - $star_time" | bc)
    local formatted_time=$(LC_NUMERIC=C printf "%.4f" "$elapsed_time")
    echo -e "La funcion $1 ha tardado $formatted_time en ejecutarse\n"
}


declare -a list_task=()

function add_task() {
    local task="$1"
    local description="$2"
    local now=$(date '+%Y-%m-%d %H:%M:%S')
    logger -p user.debug "[*] Comienza la funcion para 'añadir tareas'"
    echo -e "[$now] (user.debug) [*] Comienza la funcion para 'añadir tareas'"
    sleep 1
    for t in "${list_task[@]}"; do
        if [[ "$t" == "$task" ]]; then
            logger -p user.warn "[!] La tarea ya esta en la lista"
            echo -e "[$now](user.warn) [!] La tarea ya esta en la lista"
            return
        fi
    done
    list_task+=("$task")
    sleep 1
    logger -p user.info "[+] Se agrega nueva tarea $task - $description"
    echo -e "[$now](user.info) [+] Se agrega nueva tarea $task - $description"
    logger -p user.debug "[*] Finaliza la funcion 'añadir tareas'"
    echo -e "[$now](user.debug) [*] Finaliza la funcion 'añadir tareas'"
}
    
    
function del_task() {
    local task="$1"
    local description="$2"
    local now=$(date '+%Y-%m-%d %H:%M:%S')
    logger -p user.debug "[*] Comienza la funcion para 'borrar tareas'"
    echo -e "[$now](user.debug) [*] Comienza la funcion para 'borrar tareas'"
    sleep 1
    local new_list=()
    local task_found=0
    for t in "${list_task[@]}"; do
        if [[ "$t" == "$task" ]]; then
            task_found=1
        else
            new_list+=("$t")
        fi
    done
    if [[ $task_found -eq 1 ]]; then
        list_task=("${new_list[@]}")
        logger -p user.info "[-] Se elimino la tarea: $task - $description"
        echo -e "[$now](user.info) [-] Se elimino la tarea: $task - $description"
    else
        logger -p user.warn "[!] La tarea a eliminar $task - $description no existe"
        echo -e "[$now](user.warn) [!] La tarea a eliminar $task - $description no existe"
    fi
    sleep 1
    logger -p user.debug "[*] Finaliza la funcion 'eliminar tareas'"
    echo -e "[$now](user.debug) [*] Finaliza la funcion 'eliminar tareas'"
}
   
           
function list_tasks() {
    local now=$(date '+%Y-%m-%d %H:%M:%S')
    logger -p user.debug "[*] Comienza la funcion para 'listar tareas'"
    echo -e "[$now](user.debug) [*] Comienza la funcion para 'listar tareas'"
    sleep 3
    for t in "${list_task[@]}"; do
        echo -e "[$now](user.info) [+] La lista de tareas programadas: $t"
        logger -p user.info "[+] La lista de tareas programadas: $t"
    done
    logger -p user.debug "[*] Finaliza la funcion 'listar tareas'" 
    echo -e "[$now}(user.debug) [*] Finaliza la funcion 'listar tareas'"    
            
}            
    

function decorator() {
    time_spent "$@"
}



decorator add_task "task1" "recepcionar pedidos"
decorator add_task "task2" "preparar pedidos"
decorator add_task "task3" "enviar pedidos"
decorator add_task "task2" "preparar pedidos"

decorator list_tasks

decorator del_task "task4" "ordenar pedidos"
decorator del_task "task3" "enviar pedidos"

decorator list_tasks 
