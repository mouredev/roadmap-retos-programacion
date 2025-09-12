#!/bin/bash

# Utilizando tu lenguaje, explora el concepto de expresiones regulares,
# creando una que sea capaz de encontrar y extraer todos los numeros
# de un texto.

echo -e "\n\n=======================================EJERCICIO=======================================\n\n"

string="Mariano 1234"
regex="\d+"
numbers=$(grep -oP "$regex" <<< "$string")
echo -e "\n[+] Los numeros que hay en la cadena de texto son: $numbers"


echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"


# Crea 3 expresiones regulares (a tu criterio) capaces de:
#   - Validar un email.
#   - Validar un numero de telefono.
#   - Validar una url.


function check_email(){
    read -p "[+] Introduce un email: " email
    verify_email="^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9_+-]+\.[a-zA-Z]{2,}$"
    
    if [[ $email =~ $verify_email ]]; then
        echo -e "\n[+] El email introducido es correcto\n"
    else
        echo -e "\n[!] El email introducido no es correcto\n"
    fi
}


function check_number(){
    read -p "[+] Introduce un un numero de telefono: " number_phone
    verify_phone="^[+[0-9]{1,3}]?[0-9]{4,9}$"
    
    if [[ $number_phone =~ $verify_phone ]]; then
        echo -e "\n[+] El numero introducido es correcto\n"
    else
        echo -e "\n[!] El numero introducido es incorrecto\n"
    fi
}

function check_url(){
    read -p "[+] Introduce una direccion url: " url
    verify_url="((https?://(www\.)?)|www\.)\w{3,}\.[a-z]{2,}"

    if [[ $url =~ $verify_url ]]; then
        echo -e "\n[+] La direccion url introdudida es correcta\n"
    else
        echo -e "\n[!] La direccion url introducida no es corrrecta\n"
    fi
}


check_email
check_number
check_url
