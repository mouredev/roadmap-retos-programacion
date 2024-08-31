#!/bin/bash

# * EJERCICIO:
# * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# * asincrona una funcion que tardara en finalizar un numero concreto de
# * segundos parametrizables. Tambien debes poder asignarle un nombre.
# * La funcion imprime su nombre, cuando empieza, el tiempo que durara
# * su ejecucion y cuando finaliza.

function task_D(){
    echo -e "[+] La tarea $1 comienza a ejecutarse....\n"
    sleep 5
    echo -e "[!] La tarea $1 ha finalizado\n"
}    
task_D "Tarea D"




# * DIFICULTAD EXTRA (opcional):
# * Utilizando el concepto de asincronia y la funcion anterior, crea
# * el siguiente programa que ejecuta en este orden:
# * - Una funcion C que dura 3 segundos.
# * - Una funcion B que dura 2 segundos.
# * - Una funcion A que dura 1 segundo.
# * - Una funcion D que dura 1 segundo.
# * - Las funciones C, B y A se ejecutan en paralelo.
# * - La funcion D comienza su ejecucion cuando las 3 anteriores han
# *   finalizado.


function task_C(){
    echo -e "[+] La tarea $1 comienza a ejecutarse....\n"
    sleep 3
    echo -e "[!] La tarea $1 ha finalizado\n"
}

function task_B(){
    echo -e "[+] La tarea $1 comienza a ejecutarse....\n"
    sleep 2
    echo -e "[!] La tarea $1 ha finalizado\n"
}

function task_A(){
    echo -e "[+] La tarea $1 comienza a ejecutarse....\n"
    sleep 1
    echo -e "[!] La tarea $1 ha finalizado\n"
}

function main(){
   
   echo -e "[+] La 'Tarea D' Espera a que las demas terminen de ejecutarse....\n"
   
   task_C "Tarea C" &
   task_B "Tarea B" &
   task_A "Tarea A" &
   wait
   task_D "Tarea D" 

}  

main
