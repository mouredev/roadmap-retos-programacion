#!/bin/bash

# ESTE PRINCIPIO ESTABLECE DOS COSAS:
# 1ª LOS MODULOS DE ALTO NIVEL NO PUEDEN DEPENDER DE LOS MODULOS DE BAJO NIVEL, LOS DOS DEBEN DEPENDER DE LAS ABSTRACCIONES
# 2ª LAS ABSTRACCIONES NO PUEDEN DEPENDER DE LOS DETALLES SINO LOS DETALLES DE LAS ABSTRACCIONES



echo -e "\n\n=======================================EJERCICIO=======================================\n\n"


#  * EJERCICIO:
#  * Explora el "Principio SOLID de Inversin de Dependencias (Dependency Inversion
#  * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
#  * de forma correcta e incorrecta.

# SIN DIP

# function dictionary_chek_word(){
#     local word=$1
#     local dictionary=("hola" "mundo" "correcto")
#     for dict_word in "${dictionary[@]}"; do
#         if [ "$word" == "$dict_word" ]; then
#             echo "La palabra $word está en el diccionario"
#             return
#         fi
#     done
#     echo "La palabra $word no está en el diccionario"    
# }
            
# function spell_correct(){
#     local text=$1
#     local words="($text)"
#     for word in "${words[@]}"; do
#         dictionary_chek_word "$word"
#     done        
# }



# CON DIP
    
function dictionary_check_word(){
    local word=$1
    local dictionary=("hola" "mundo" "correcto")
    for dict_word in "${dictionary[@]}"; do
        if [ "$word" == "$dict_word" ];then
            echo "La palabra $word está en el diccionario"
            return
        fi
    done
    echo "La palabra $word no está en el diccionario"
}

function online_service_check_word(){
    local word=$1
    local online_dictionary=("traductor" "online" "word")
    for dict_word in "${online_dictionary[@]}"; do
        if [ "$word" == "$dict_word" ];then
            echo "La palabra está en el diccionario online"
            return
        fi
    done
    echo "Lapalabra no está en el diccionario online"
}

function spell_correct(){
    local checker_function=$1
    local text=$2
    local words=("$text")
    for word in "${words[@]}"; do
        $checker_function "$word"
    done
}



echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un sistema de notificaciones.
#  * Requisitos:
#  * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones especÃ­ficas).
#  * 2. El sistema de notificaciones no puede depender de las implementaciones especÃ­ficas.
#  * Instrucciones:
#  * 1. Crea la interfaz o clase abstracta.
#  * 2. Desarrolla las implementaciones especÃ­ficas.
#  * 3. Crea el sistema de notificaciones usando el DIP.
#  * 4. Desarrolla un cÃ³digo que compruebe que se cumple el principio.


function send_email(){
    local message=$1
    echo "Enviando por email el mensaje: $message"
}

function send_PUSH(){
    local message=$1
    echo "Enviando por PUSH el mensaje: $message"
}

function send_SMS(){
    local message=$1
    echo -e "Enviando por SMS el mensaje: $message"
}

function send_notification(){
    local send_method=$1
    local message=$2
    $send_method "$message"
}
        
function notifier(){
    local message=$1
    echo "1. Email"
    echo "2. PUSH"
    echo "3. SMS"
    read -p "Elige una como quieres enviar el mensaje: " option
    
    case $option in
        1)
            send_notification send_email "$message" 
            ;;
        2)
            send_notification send_PUSH "$message"
            ;;
        3)
            send_notification send_SMS "$message"
            ;;
        *)
            echo "Opción no válida"   
            ;;
    esac
}
    

        
notifier "Felices vacaciones!!"

    
    
    


