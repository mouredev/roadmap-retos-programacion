#!/usr/bin/env bash
# #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

declare -A events
declare -A participants
declare -A medals_gold
declare -A medals_silver
declare -A medals_bronze
declare -a event_list

register_event() {
    read -r -p "Nombre del evento: " event_name
    if [[ -v events["$event_name"] ]]; then
        echo "El evento '$event_name' ya existe."
    else
        events["$event_name"]=1
        event_list+=("$event_name")
        echo "Evento '$event_name' registrado."
    fi
}

register_participant() {
    if [[ ${#event_list[@]} -eq 0 ]]; then
        echo "No hay eventos registrados. Registra un evento primero."
        return
    fi
    echo "Eventos disponibles:"
    for e in "${event_list[@]}"; do echo "  - $e"; done
    read -r -p "Evento para el participante: " event_name
    if [[ ! -v events["$event_name"] ]]; then
        echo "Evento no encontrado."
        return
    fi
    read -r -p "Nombre del participante: " pname
    read -r -p "País del participante: " country
    key="${event_name}|${pname}"
    participants["$key"]="$country"
    echo "Participante '$pname ($country)' registrado en '$event_name'."
}

simulate_events() {
    if [[ ${#event_list[@]} -eq 0 ]]; then
        echo "No hay eventos para simular."
        return
    fi
    for event in "${event_list[@]}"; do
        echo ""
        echo "=== Simulando: $event ==="
        local event_parts=()
        for key in "${!participants[@]}"; do
            if [[ "$key" == "${event}|"* ]]; then
                event_parts+=("${key#*|}")
            fi
        done
        local count=${#event_parts[@]}
        if [[ $count -lt 3 ]]; then
            echo "  El evento '$event' necesita al menos 3 participantes (tiene $count). Saltando."
            continue
        fi
        for ((i=count-1; i>0; i--)); do
            j=$((RANDOM % (i+1)))
            tmp="${event_parts[$i]}"
            event_parts[$i]="${event_parts[$j]}"
            event_parts[$j]="$tmp"
        done
        gold_name="${event_parts[0]}"
        silver_name="${event_parts[1]}"
        bronze_name="${event_parts[2]}"
        gold_country="${participants[${event}|${gold_name}]}"
        silver_country="${participants[${event}|${silver_name}]}"
        bronze_country="${participants[${event}|${bronze_name}]}"
        echo "  🥇 Oro:    $gold_name ($gold_country)"
        echo "  🥈 Plata:  $silver_name ($silver_country)"
        echo "  🥉 Bronce: $bronze_name ($bronze_country)"
        medals_gold["$gold_country"]=$(( ${medals_gold["$gold_country"]:-0} + 1 ))
        medals_silver["$silver_country"]=$(( ${medals_silver["$silver_country"]:-0} + 1 ))
        medals_bronze["$bronze_country"]=$(( ${medals_bronze["$bronze_country"]:-0} + 1 ))
    done
}

show_report() {
    echo ""
    echo "=============================="
    echo "   INFORME FINAL - JJOO 2024  "
    echo "=============================="
    declare -A all_countries
    for c in "${!medals_gold[@]}"; do all_countries["$c"]=1; done
    for c in "${!medals_silver[@]}"; do all_countries["$c"]=1; done
    for c in "${!medals_bronze[@]}"; do all_countries["$c"]=1; done
    if [[ ${#all_countries[@]} -eq 0 ]]; then
        echo "No se han simulado eventos aún."
        return
    fi
    declare -a sorted_countries
    for c in "${!all_countries[@]}"; do
        g=${medals_gold["$c"]:-0}
        s=${medals_silver["$c"]:-0}
        b=${medals_bronze["$c"]:-0}
        sorted_countries+=("$g $s $b $c")
    done
    IFS=$'\n' sorted=($(sort -rn <<<"${sorted_countries[*]}")); unset IFS
    printf "%-5s %-25s %-6s %-6s %-6s %-6s\n" "Pos." "País" "Oro" "Plata" "Bronce" "Total"
    echo "------------------------------------------------------------"
    pos=1
    for entry in "${sorted[@]}"; do
        read -r g s b c <<< "$entry"
        total=$((g + s + b))
        printf "%-5s %-25s %-6s %-6s %-6s %-6s\n" "$pos." "$c" "$g" "$s" "$b" "$total"
        ((pos++))
    done
}

while true; do
    echo ""
    echo "====== SIMULADOR JJOO PARÍS 2024 ======"
    echo "1. Registrar evento"
    echo "2. Registrar participante"
    echo "3. Simular eventos"
    echo "4. Ver informe"
    echo "5. Salir"
    read -r -p "Selecciona una opción: " choice
    case $choice in
        1) register_event ;;
        2) register_participant ;;
        3) simulate_events ;;
        4) show_report ;;
        5) echo "¡Hasta luego!"; break ;;
        *) echo "Opción no válida." ;;
    esac
done
