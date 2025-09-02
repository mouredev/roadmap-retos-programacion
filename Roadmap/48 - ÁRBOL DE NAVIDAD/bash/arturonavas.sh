#!/bin/bash
: '
/*
 * EJERCICIO:
 * ¡Ha comenzado diciembre! Es hora de montar nuestro
 * árbol de Navidad...
 *
 * Desarrolla un programa que cree un árbol de Navidad
 * con una altura dinámica definida por el usuario por terminal.
 *
 * Ejemplo de árbol de altura 5 (el tronco siempre será igual):
 *
 *     *
 *    ***
 *   *****
 *  *******
 * *********
 *    |||
 *    |||
 *
 * El usuario podrá seleccionar las siguientes acciones:
 * 
 * - Añadir o eliminar la estrella en la copa del árbol (@)
 * - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
 * - Añadir o eliminar luces de tres en tres (+) aleatoriamente
 * - Apagar (*) o encender (+) las luces (conservando su posición)
 * - Una luz y una bola no pueden estar en el mismo sitio
 *
 * Sólo puedes añadir una estrella, y tantas luces o bolas
 * como tengan cabida en el árbol. El programa debe notificar
 * cada una de las acciones (o por el contrario, cuando no
 * se pueda realizar alguna).
 */
'
# variables basicas (son booleanas)
altura=0
estrella=0
bola=0
luz=0
luz_on=1

dibujar() {
    clear
    echo ":::::. arbol de navidad .:::::"
    echo
    echo
    
    # parte de arriba | hojasd
    for ((i=1; i<=$altura; i++)); do
        espacios=$((altura - i+1)) #para que no este pegado al borde
        printf "%${espacios}s"
        
    # no se como agregar aleatoriamente los simbolos al arbol

        for ((j=1; j<=2*i-1; j++)); do
            if ((i == 1)) && ((estrella == 1)); then
                echo -n "@"
            elif ((bola == 1)) && ((j % 2 == 0)); then
                echo -n "o"
            elif ((luz == 1)) && ((j % 3 == 0)); then
                ((luz_on)) && echo -n "+" || echo -n "-"
            else
                echo -n "*"
            fi
        done
        echo
    done
    
    # tronco
    printf "%$((altura - 1))s"
        echo "|||"
    printf "%$((altura - 1))s"
        echo "|||"
}

menu() {
    echo
    echo "1. poner o quitar estrella (@)"
    echo "2. poner o quitar bolas (o)"
    echo "3. poner o quitar luces (+)"
    echo "4. prender o apagar luces"
    echo "5. salir"
}

main() {
    read -p "altura del arbol: " altura
    
    while true; do
        dibujar
        menu
        read -p "opcion: " op

# este operador ""variable ^=1" hace la funcion de un switch enciende y apaga (1 o 0) al activarse
        
        case $op in
            1) ((estrella ^=1)) ;;
            2) ((bola ^=1)) ;;
            3) ((luz ^=1)) ;;
            4) ((luz_on ^=1)) ;;
            5) exit ;;
            *) echo "error opcion no valida x_x" ;;
        esac
    done
}

main