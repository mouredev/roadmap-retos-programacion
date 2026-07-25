#!/bin/bash

# Función genérica que ejecuta tareas asincrónicamente con nombre y duración
function run_task() {
    local name="$1"
    local duration="$2"
    
    if [[ -z "$name" || -z "$duration" ]]; then
        echo -e "[!] Error: Debes proporcionar un nombre y una duración para la tarea.\n"
        return 1
    fi

    echo -e "[+] La tarea '$name' comienza a ejecutarse y durará ${duration} segundos...\n"
    sleep "$duration"
    echo -e "[!] La tarea '$name' ha finalizado.\n"
}

# Función principal para ejecutar las tareas en el orden especificado
function main() {
    echo -e "[+] Ejecutando las tareas en paralelo...\n"

    # Ejecutar tareas C, B y A en paralelo
    run_task "Tarea C" 3 &
    run_task "Tarea B" 2 &
    run_task "Tarea A" 1 &

    # Esperar a que todas las tareas en paralelo finalicen
    wait

    echo -e "[+] Todas las tareas C, B y A han terminado. Iniciando la tarea D...\n"
    
    # Ejecutar la tarea D después de que las demás terminen
    run_task "Tarea D" 1
}

# Ejecutar la función principal
main
