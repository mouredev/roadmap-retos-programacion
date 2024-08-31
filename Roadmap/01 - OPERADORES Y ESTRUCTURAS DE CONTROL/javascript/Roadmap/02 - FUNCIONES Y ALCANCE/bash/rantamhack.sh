#!/bin/bash

echo "==================== FUNCION SIN RETORNO NI ARGUMENTOS ===================="

function hola_mundo(){
    echo "Hola mundo!!"
}
hola_mundo
echo "===4================= FUNCION CON UN ARGUMETO SIN RETORNO ===================="

function hola_lenguaje(){
    echo "Hola mundo!! mi lenguaje de programación favorito es $1"
}
hola_lenguaje "Bash"

echo "==================== FUNCION CON DOS ARGUMENTOS SIN RETORNO ===================="

function presentacion(){
    echo "Hola mundo!! soy $1 y mi lenguaje de programación favorito es $2"
}
presentacion "rantamplan" "Bash" 

echo "==================== FUNCION CON DOS ARGUMETOS CON RETORNO ===================="

function publicacion(){

    edad=$(( 2024-$1 ))
    echo "El lenguaje $2 se publicó en el año $1"
    if [ $edad -ge 18 ]; then
        echo "El lenguaje $2 es mayor de edad, tiene $edad años" 
        return 0

# Se puede usar tanto return como exit para indicar el codigo de estado de salida    

    else
        echo "El lenguaje $2 es aún muy reciente, tiene $edad años"
        exit 1    
    fi
}
publicacion 1989 "Bash"

echo "==================== FUNCION DENTRO DE OTRA FUNCION ===================="
# Función dentro de func
function potencia(){
        result=$(( $1**$2 ))
        echo "El resultado del numero" $1 "elevado a la potencia" $2 es $result 
        function interior(){
            final=$(( "$result" * "$1" ))
            echo "El resultado de las funciones es" $final
    }
    interior 2
     
}
potencia 10 3

echo "==================== FUNCION PROPIA DE BASH ===================="

function num_aleatorio(){
    echo "Crear un numero aleatorio menor que 100"
    echo -e "El número que ha salido es:" $(( $RANDOM % 100 ))
}
num_aleatorio

echo "==================== VARIABLES GLOBALES Y LOCALES ===================="
# En Bash de entrada todas las variable son globales pues se pueden leer desde cualquier lugar 
# de un script esten dentro o fuera de una función
# Para que una variable sea considerada local se debe declarar dentro de una función y con la
# palabra local delante del nombre

var1="A"  # Variable global

function variables(){
    local var2="B"  # Variable local
    echo "El valor de la variable var1 es:"$var1 "y el de var2 es: "$var2
}
variables
echo "El valor de la variable var1 es:"$var1 "y el de var2 es: "$var2
# En ésta impresión no aparece el valor de $var2 porque no la reconoce al estar fuera de la función


echo "==================== EJERCICIO EXTRA ===================="

text1="multiplo de 3"
text2="multiplo de 5"

function num_impress(){
    contador=0
    for i in $(seq 1 100); do
        if [ $(($i % 3)) -eq 0 ] && [ $(($i % 5)) -eq 0 ]; then
            echo $i "Es" $text1 "y es "$text2
        elif [ $(($i % 3)) -eq 0 ]; then
            echo $i "Es" $text1 
        elif [ $(($i % 5)) -eq 0 ]; then
            echo $i "Es" $text2
        else
            let "contador +=1"
            echo $i
        fi
    done
    echo "Hay "$contador "números que no son" $text1 "ni" $text2
}
num_impress text1 text2