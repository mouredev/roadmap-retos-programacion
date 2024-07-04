#!/bin/bash


# BASH NO ESTA ORIENTADO A OBJETOS Y NO TIENE CLASES, ESTE EJERCICIO ES UNA SIMULACION DE LAS CLASES

echo -e "\n\n=======================================EJERCICIO SIN SRP=======================================\n\n"

# * EJERCICIO:
# * Explora el "Principio SOLID de Responsabilidad Unica (Single Responsibility
# * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
# * de forma correcta e incorrecta.


# * Sin aplicar el principio "SRP"

students=()
subscriptions=()
payments=()


function mouredev_academy() {
    local user_id="$1"
    local name="$2"
    local surname="$3"
    local email="$4"

    read -p "Introduce tu nombre de usuario:  " nick
    read -p "introduce tu contraseña:  " passwd

    students+=("$user_id, $name, $surname, $email, $username, $password")
    echo -e "[+] El estudiante $username se ha añadido a la base de datos" 

    if [[ $nick == $username && $passwd == $password ]]; then
        echo -e "[*] Bienvenido a la academia $username"
    else
        echo -e "[!] Los datos introducidos no son correctos"
    fi  
}

function subs_type(){
    local monthly="$1"
    local quarterly="$2"
    local half_yearly="$3"
    local yearly="$4"
    subscriptions+=("$monthly, $quarterly, $half_yearly, $yearly")
    echo -e "[-] Los tipos de suscripcion se han aÃ±adido"
}
        
function payment() {
    local credit_card="$1"
    local debit_card="$2"
    local bizum="$3"
    local bank_transfer="$4"
    payments+=("$credit_card, $debit_card, $bizum, $bank_transfer")
    echo -e "[-] Los metodos de pago se han añadido" 
}


mouredev_academy "username" "password"
mouredev_academy 1 "Luis" "Ramos" "rantam@rantam.com" "fake" "126354"
subs_type "Monthly" "Quarterly" "Half_yearly" "Yearly"
payment "credit_card" "debit_card" "bizum" "bank_transfer"


echo -e "\n\n=======================================EJERCICIO CON SRP=======================================\n\n"



# * Aplicando el principio "SRP"

students=()
subscriptions=()
payments=()

function auth(){
    local username="$1"
    local password="$2"

    read -p "Introduce tu nombre de usuario:  " nick
    read -p "introduce tu contraseña:  " passwd

    echo -e "[-] Autenticando al usuario $nick"

    if [[ $nick == "$username" && $passwd == "$password" ]]; then
        echo -e "[*] Bienvenido a la academia $username"
    else
        echo -e "[!] Los datos introducidos no son correctos"
    fi  

}

function add_students(){
    local user_id="$1"
    local name="$2"
    local surname="$3"
    local email="$4"
    local username=$5

    students+=("$user_id, $name, $surname, $email, $username")

    for student in "${students[@]}";do
        echo -e "[+] La lista de estudiantes es $student"
    done
    
}

function add_subs(){
    local monthly="$1"
    local quarterly="$2"
    local half_yearly="$3"
    local yearly="$4"
    subscriptions+=("$monthly, $quarterly, $half_yearly, $yearly")
    echo -e "[-] Los tipos de suscripcion se han añadido"
}

function add_payment() {
    local credit_card="$1"
    local debit_card="$2"
    local bizum="$3"
    local bank_transfer="$4"
    payments+=("$credit_card, $debit_card, $bizum, $bank_transfer")
    echo -e "[-] Los metodos de pago se han añadido" 
}

function moure_academy(){
    local command="$1"
    shift
    
    case "$command" in
        auth)
            auth "$@"
            ;;
        add_students)
            add_students "$@"
            ;;
        add_subs)
            add_subs "$@"
            ;;
        add_payment)
            add_payment "$@"
            ;;
        *)
            echo -e "[!] Comando no reconocido"
            ;;
    esac
}

moure_academy add_students 1 "Rosa" "Lopez" "rosa@moureacademy.com" "rantam"
moure_academy add_students 2 "Mario" "Bros" "mario@moureacademy.com" "Ka_OS"
moure_academy auth "rantam" "123456"
moure_academy auth "Ka_Os" "654321"
moure_academy add_subs "Monthly" "Quarterly" "Half_yearly" "Yearly"
moure_academy add_payment "credit_card" "debit_card" "bizum" "bank_transfer"







