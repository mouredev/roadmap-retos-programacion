#!/bin/bash

# Script de validación utilizando expresiones regulares

string="Pepe tiene el número 1234 y 5678"
regex="[0-9]+"
numbers=$(grep -oE "$regex" <<< "$string")
echo -e "[+] Los números encontrados en la cadena de texto son: $numbers"

echo -e "\n\n================================ DIFICULTAD EXTRA ================================\n"

# Función para solicitar la entrada de usuario
solicitar_entrada() {
    local mensaje="$1"
    local variable="$2"
    read -p "$mensaje" "$variable"
}

# Función para validar un correo electrónico
validar_email() {
    solicitar_entrada "[+] Introduce un email: " email
    regex_email="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if [[ $email =~ $regex_email ]]; then
        echo -e "[+] El email introducido es válido.\n"
    else
        echo -e "[!] El email introducido no es válido.\n"
    fi
}

# Función para validar un número de teléfono
validar_telefono() {
    solicitar_entrada "[+] Introduce un número de teléfono: " telefono
    regex_telefono="^\+?[0-9]{1,3}?[-. ]?\(?[0-9]{1,4}?\)?[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,9}$"
    
    if [[ $telefono =~ $regex_telefono ]]; then
        echo -e "[+] El número de teléfono introducido es válido.\n"
    else
        echo -e "[!] El número de teléfono introducido no es válido.\n"
    fi
}

# Función para validar una URL
validar_url() {
    solicitar_entrada "[+] Introduce una dirección URL: " url
    regex_url="^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
    
    if [[ $url =~ $regex_url ]]; then
        echo -e "[+] La dirección URL introducida es válida.\n"
    else
        echo -e "[!] La dirección URL introducida no es válida.\n"
    fi
}

# Ejecución de las validaciones
validar_email
validar_telefono
validar_url
