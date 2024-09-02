#!/bin/bash

#  * EJERCICIO:
#  * ¡Los JJOO de París 2024 han comenzado!
#  * Crea un programa que simule la celebración de los juegos.
#  * El programa debe permitir al usuario registrar eventos y participantes,
#  * realizar la simulación de los eventos asignando posiciones de manera aleatoria
#  * y generar un informe final. Todo ello por terminal.
#  * Requisitos:
#  * 1. Registrar eventos deportivos.
#  * 2. Registrar participantes por nombre y paÃ­s.
#  * 3. Simular eventos de manera aleatoria en base a los participantes (mÃ­nimo 3).
#  * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
#  * 5. Mostrar los ganadores por cada evento.
#  * 6. Mostrar el ranking de países según el número de medallas.
#  * Acciones:
#  * 1. Registro de eventos.
#  * 2. Registro de participantes.
#  * 3. Simulación de eventos.
#  * 4. Creación de informes.
#  * 5. Salir del programa.


declare -A events         
declare -A participants   
declare -A results        

function register_event() {
    local event_name="$1"
    if [[ -z "${events[$event_name]}" ]]; then
        events["$event_name"]=""  
        echo "Evento '$event_name' registrado."
    else
        echo "El evento '$event_name' ya está registrado."
    fi
}

function register_participant() {
    local name="$1"
    local country="$2"
    local event_name="$3"

    if [[ -n "${events[$event_name]+exist}" ]]; then
        participants["$name"]="$country"
        events["$event_name"]+="$name,"  
        echo "Participante '$name' de '$country' registrado en el evento '$event_name'."
    else
        echo "El evento '$event_name' no está registrado."
    fi
}

function simulate_events() {
    for event_name in "${!events[@]}"; do
        local participant_list=(${events[$event_name]//,/ })
        local participant_count=${#participant_list[@]}

        if (( participant_count >= 3 )); then
            # Mezcla aleatoria de participantes
            shuffled_participants=($(shuf -e "${participant_list[@]}"))

            # Almacenar los tres primeros como ganadores
            results[$event_name]="${shuffled_participants[0]},${shuffled_participants[1]},${shuffled_participants[2]}"
        else
            echo "No hay suficientes participantes en el evento '$event_name' para realizar una simulación."
        fi
    done
}

function generate_report() {
    for event_name in "${!results[@]}"; do
        echo "Evento: $event_name"
        local winners=(${results[$event_name]//,/ })
        local medals=("Gold" "Silver" "Bronze")

        for i in ${!winners[@]}; do
            local participant=${winners[$i]}
            local country=${participants[$participant]}
            echo "${medals[$i]}: $participant ($country)"
        done
        echo ""
    done
}

function show_menu() {
    while true; do
        echo -e "\nMenú:"
        echo -e "\t1. Registrar Evento"
        echo -e "\t2. Registrar Participante"
        echo -e "\t3. Simular Evento"
        echo -e "\t4. Generar Informe"
        echo -e "\t5. Salir"
        echo -e "\t6. Mostrar eventos y participantes guardados"

        read -p "Seleccione una opción del menú: " option

        case $option in
            1)
                read -p "Pon el nombre del nuevo evento: " event_name
                register_event "$event_name"
                ;;
            2)
                read -p "Escriba el nombre del participante: " name
                read -p "Escriba el país al que pertenece el nuevo participante: " country
                read -p "Escriba el nombre del evento en el que desea inscribirse: " event_name
                register_participant "$name" "$country" "$event_name"
                ;;
            3)
                simulate_events
                ;;
            4)
                generate_report
                ;;
            5)
                echo -e "\nEventos guardados:"
                for event_name in "${!events[@]}"; do
                    echo "$event_name"
                done

                echo -e "\nParticipantes guardados:"
                for name in "${!participants[@]}"; do
                    echo "$name (${participants[$name]})"
                done
                ;;
            6)
                echo "Saliendo del programa."
                break
                ;;
            *)
                echo "Opción incorrecta, por favor elija una opción entre la 1 y la 6."
                ;;
        esac
    done
}

show_menu
