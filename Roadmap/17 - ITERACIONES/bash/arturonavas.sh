#!/usr/bin/bash
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

 # mecanismo 1 || desde i hasta 10
for i in {1..10}
do
  echo $i
done


# mecanismo 2 || un for basico
for ((i=1; i<=10; i++))
do
  echo $i
done

# mecanismo 3 ||(while)
i=1
while [ $i -le 10 ]
do
  echo $i
  ((i++))
done

# mecanismo 4 || lo mismo que un while
i=1
until [ $i -gt 10 ]
do
  echo $i
  ((i++))
done
