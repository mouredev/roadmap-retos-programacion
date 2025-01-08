#!/bin/bash

# Operadores Ariméticos
echo "Operadores Ariméticos"
a=5
b=2
echo "Suma ($a + $b): $((a + b))"
echo "Resta ($a - $b): $((a - b))"
echo "Multiplicación ($a * $b): $((a * b))"
echo "División ($a / $b): $((a / b))"
echo "Módulo ($a % $b): $((a % b))"

a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

# Operadores de Comparación
echo "\nOperadores de Comparación:"
echo "Igualdad ($a == $b) es: $((a == b))"
echo "Desigualdad ($a != $b) es: $((a != b))"
echo "Menor que: ($a < $b) es: $((a < b))"
echo "Mayor que: ($a > $b) es: $((a < b))"
echo "Mayor o igual que: ($a >= $b) es $((a >= b))"
echo "Menor o igual que: ($a <= $b) es $((a <= b))"

# Lógicos
echo "\nOperadores Lógicos:"
echo "AND &&: ($a != $b) && ($a > $b) es $(( a != b && a > b))"
echo "OR ||: ($a != $b) || ($a > $b) es $(( a != b || a > b))"
echo "NOT !: !($a != $b) es $(( ! (a != b) ))"

# Operadores de asignación
echo "\nOperadores de asignación"
a=10
echo "Antes de la asignación: $a"
a=$((a + 5))
echo "Después de la asignación: $a"

# aproximación de pi
echo "scale=7; 355 / 113" | bc -l
echo "4 ^ 2" | bc -l
echo "scale=2; sqrt(4)" | bc -l
echo "scale=3; (1.23 / 0.32) + (5 * 2)" | bc -l

# Estructuras de Control
echo "\nEstructuras de Control:"

# Condicionales
echo "\nCondicionales"
if [ $a -gt 15 ]; then
    echo "$a es mayor que 15"
else
    echo "$a es menor o igual que 15"
fi

str1="Hola"
str2="Hola"

if [ "$str1" = "$str2" ]; then
    echo "Equal"
else
    echo "No equals"
fi

# Iterativas
echo -e "\nEstructuras Iterativas:"
echo "Números del 10 al 55 (pares y no múltiplos de 3):"
for ((i=10; i<=55; i++)); do
    if [ $((i % 2)) -eq 0 ] && [ $((i % 3)) -ne 0 ]; then
        echo $i
    fi
done


set -e

command1 && command2 && command3
echo "All commands completed successfully"

echo "EXTRA"
echo "Números entre 10 y 55 (incluidos), pares, y no múltiplos de 3 ni 16:"

for ((i=10; i<=55; i++)); do
    if [ $((i % 2)) -eq 0 ] && [ $((i % 3)) -ne 0 ] && [ $i -ne 16 ]; then
        echo $i
    fi
done
