#!/bin/bash

echo -e "\n\n===============================OPERACIONES CON STRINGS===============================\n\n"

# Concatenacion
a="Hello"
b=" World"
c=$a$b
echo $c

# Multiplicar una cadena
a="Hello World"
for i in $(seq 1 5);do
    echo $a
done

# Iterar en una cadena de texto
a="Hello World"
for i in $a;do
    echo $i
done

# Convertir una cadena de texto a mayusculas
string="¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
echo ${string^^}

# Convertir una cadena de texto a minusculas
string="¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
echo ${string,,}

# cortar una cadena por el final
string="¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
echo ${string: -9}

# cortar una cadena por el principio
string="¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
echo ${string: 12}

# cortar una cadena por el principio y por el final
string="¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
echo ${string: 12:-9}

# Reemplazar texto
string="¡Es cierto! siempre he sido nervioso, muy nervioso, terriblemente nervioso." 
echo ${string/s/z}   # Cambia solo la primera letra
echo ${string//s/z}  # Cambia todas las letras coincidentes

# Contando los caracteres que tiene la cadena
string="¡Es cierto! siempre he sido nervioso, muy nervioso, terriblemente nervioso." 
echo ${#string}

# Interpolar
string="'¡Es cierto! siempre he sido nervioso, muy nervioso, terriblemente nervioso'" 
author="Edgar Allan Poe"
echo "El texto $string es el comienzo de una novela de $author"

echo -e "\n\n===============================DIFICULTAD EXTRA===============================\n\n"

read -p "Introduce la palabra que quieres comprobar: " var

function palindromo(){
    var=${var,,}
    var=${var//" "/""}
    if [[ $(rev <<< "$var") == "$var" ]]; then
        echo "$var es un palindromo"
    else
        echo "$var no es un palindromo"
    fi
}

palindromo 