#!/bin/bash

echo -e "\n\n=======================================EJERCICIO=======================================\n\n"

# * EJERCICIO:
# * Explora el patron de diseño "singleton" y muestra como crearlo
# * con un ejemplo generico.

# * Bash no es un lenguaje orientado a objetos. Hay que simular el comportamiento de las clases

singleton_instance=""

function get_singleton_instance(){
    if [[ -z "$singleton_instance" ]]; then
        singleton_instance="instance_created"
    fi
}


instance1=$(get_singleton_instance)
instance2=$(get_singleton_instance)

echo -e "\nComprobando que las dos instancias son la misma instancia:\n"

if [[ "$instance1" == "$instance2" ]]; then
    echo "True"
else
    echo "False"
fi




echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"


# * DIFICULTAD EXTRA (opcional):
# * Utiliza el patron de diseño "singleton" para representar una clase que
# * haga referencia a la sesion de usuario de una aplicacion ficticia.
# * La sesion debe permitir asignar un usuario (id, username, nombre y email),
# * recuperar los datos del usuario y borrar los datos de la sesion.


session_id=""
session_username=""
session_name=""
session_email=""

function log_in() {
    if [[ -z "$session_id" ]];then
        session_id=$1
        session_username=$2
        session_name=$3
        session_email=$4
        echo -e "\n\nEl usuario $2 iniciado sesion"
    else
        echo -e "\nYa hay un usuario con sesion iniciada\n"
    fi
}

function logout() {
    if [[ -n "$session_id" ]]; then
        echo -e "\nEl usuario $session_username ha cerrado la sesion"
        session_id=""
        session_username=""
        session_name=""
        session_email=""
    else
        echo  -e "\nNo hay ninguna sesion iniciada\n"
    fi
}

function get_user() {
    if [[ -n $session_id ]]; then
        echo -e "\n\nUsuario actual:"
        echo -e "\tID: $session_id"
        echo -e "\tUSERNAME: $session_username"
        echo -e "\tNAME: $session_name"
        echo -e "\tEMAIL: $session_email"
    else
        echo -e "\nNo hay ninguna sesion abierta"
    fi
}


user1_id=1 
user1_username="Rantam"
user1_name="Alex"
user1_email="rantam@rantam.es"



user2_id=2
user2_username="Junior"
user2_name="Maria"
user2_email="maria@rantam.es"

log_in $user1_id $user1_username $user1_name $user1_email
get_user

log_in $user2_id $user2_username $user2_name $user2_email

logout

log_in $user2_id $user2_username $user2_name $user2_email
get_user

logout

