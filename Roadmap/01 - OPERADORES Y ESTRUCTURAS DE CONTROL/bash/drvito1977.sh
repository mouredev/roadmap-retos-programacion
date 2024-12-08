#!/bin/bash

# Sección de operadores (ejemplo básico)
a=10 # Asignación de valor a la variable a
b=5 # Asignación de valor a la variable b

suma=$((a+b))
resta=$((a-b))
multiplicacion=$((a*b)) 
division=$((a/b))
modulo=$((a%b))
mayor=$((a>b))
menor=$((a<b))
igual=$((a==b))
diferente=$((a!=b))
and_logico=$((a && b))
or_logico=$((a || b))
not_logico=$((!a))

# Imprimir resultados de los operadores
echo "Suma: $suma"
echo "Resta: $resta"
echo "Multiplicación: $multiplicacion"
echo "División: $division"
echo "Módulo: $modulo"
echo "Mayor: $mayor"
echo "Menor: $menor"
echo "Igual: $igual"
echo "Diferente: $diferente"
echo "AND lógico: $and_logico"
echo "OR lógico: $or_logico"
echo "NOT lógico: $not_logico"

# Sección de estructuras de control y operadores de comparación

if [ $a -gt 5 ]; then #Comparación de la variable a 
                      #con el operador de mayor que -gt
  echo "$a es mayor que 5"
else
  echo "$a es menor o igual que 5"
fi

if [ $b -eq  5 ]; then #Comparación de la variable b 
                       #con el operador de igualdad -eq
  echo "$b es igual a 5"
else
  echo "$b no es igual a 5"
fi

if [ ! $a -eq 5 ]; then #Comparación de la variable a
                       #con el operador de negación "!" de igualdad -eq  
  echo "$a no es igual a 5"
else
  echo "$a es igual a 5"
fi

# Ejemplo de case con la variable b
b=2
case $b in
  1)
    echo "$b es 1" # Caso 1  
    ;;
  2)
    echo "$b es 2" # Caso 2
    ;;
  *)
    echo "$b no es ni 1 ni 2" # Caso por defecto
    ;;
esac

#while [ $c -eq 10 ]; do # Bucle mientras c sea igual a 10

# Bucle while con una variable c
c=10

primera_vez=true # Variable para saber si es la primera vez que se ejecuta el bucle
while [ $c -ge 1 ]; do # Bucle mientras c sea mayor o igual a 1
  if [ $primera_vez = true ]; then
    echo "El contador empieza en $c"
    primera_vez=false
  else
    echo "El contador continua con $c"
  fi
  ((c--)) # Decremento de la variable
done
echo "El contador termina en $c"

# Bucle for con una secuencia de números
for i in {1..5}; do # Bucle de 1 a 5
  echo "Iteración $i del bucle for"
done

#Ejercicio opcional
for ((i=10; i<=55; i++)); do # Bucle de 10 a 55
  if (( i % 2 == 0 )) && (( i != 16 )) && (( i % 3 != 0 )); then # Condiciones para que el número sea par, 
                                                                  #!/usr/bin/env bash
                                                                  # -*- coding: utf-8 -*-no sea 16 y no sea divisible por 3
    echo $i
  fi
done
