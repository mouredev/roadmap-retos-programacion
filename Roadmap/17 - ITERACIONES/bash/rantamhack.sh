#!/bin/bash


# * EJERCICIO:
# * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
# * numeros del 1 al 10 mediante iteracion.


echo -e "\n\n=======================================EJERCICIO=======================================\n\n"

# Usando 'for'

for i in {1..10}; do
    echo "El valor de la iteracion en 'bucle for' para 'i' es: $i"
done

echo -e "\n=====================\n"
    
# Usando 'while break'    
    
n=1    
while true; do
    if [ $n -gt 10 ]; then
        break
    fi
    echo "El valor de la iteracion en bucle 'while' para 'n' es: $n"
    ((n++))
done
    
echo -e "\n=====================\n"

# Usando 'until'

n=10
until [ $n -lt 0 ]; do
    echo "El valor de la iteracion en bucle 'until' para 'n' es: $n"
    ((n--))

done
 


echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"



# DIFICULTAD EXTRA (opcional):
# Escribe el mayor numero de mecanismos que posea tu lenguaje
# para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?


# while continue

for i in {1..10}; do
    if [[ $i -eq 5 || $i -eq 6 ]];then
        continue
    fi
    echo "Mi posicion en el bucle for es: $i"
done

echo -e "\n=====================\n"

# Iterar Cadena de Texto

texto="rantamplan"
for (( i=0; i<${#texto}; i++ )); do
    echo "${texto:$i:1}"
done

echo -e "\n=====================\n"

# Iterar rango de 2 en 2

for i in {0..20..2}; do
    echo $i
done

echo -e "\n=====================\n"

# Iterar lista

lista=(1 2 3 4 5 6 7 8 9 10)
for i in "${lista[@]}"; do
    echo "Mi posicion en la lista es: $i"
done

echo -e "\n=====================\n"
    
# Iterar diccionario por clave

declare -A dict

dict[1]='a'
dict[2]='b'
dict[3]='c'
dict[4]='d'
dict[5]='e'

for key in "${!dict[@]}"; do
    echo "Estoy en la posicion de claves del diccionario: $key"
done

echo -e "\n=====================\n"

# Iterar diccionario por valor

for value in "${dict[@]}"; do
    echo "Estoy en la posicion de valores del diccionario: $value"
done
    
echo -e "\n=====================\n"

# Iterando lista al reves

for i in $(seq 10 -1 1); do
    echo "mi posiciÃ³n descendente es: $i"
done

echo -e "\n=====================\n"


# Iterando mediante recursividad

function recursive(){
    if [[ $1 -le 10 ]]; then    
        echo "Mi posicion en la funcion recursiva es: $1"
        recursive $(( $1 +1 ))
    fi
}

recursive 0
