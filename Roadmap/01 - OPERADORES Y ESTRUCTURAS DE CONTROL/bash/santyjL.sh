#!/bin/bash

: "
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"

# Operadores Aritméticos
a=10
b=3

echo "Operadores Aritméticos:"

echo "Suma: $((a+b))"
echo "Resta: $((a-b))"
echo "Multiplicación: $((a*b))"
echo "División: $((a/b))"
echo "Módulo: $((a%b))"
echo "Exponenciación: $((a**b))"
echo -e "\n################################################################\n"

# Operadores de Comparación
echo "Operadores de Comparación:"
echo "Mayor que: $((a>b))"
echo "Mayor o igual que: $((a>=b))"
echo "Menor que: $((a<b))"
echo "Menor o igual que: $((a<=b))"
echo "Igual a: $((a==b))"
echo "Distinto de: $((a!=b))"
echo -e "\n################################################################\n"

# Operadores Lógicos
echo "Operadores Lógicos:"

echo "AND: $((a+b==13 && a>b))" #Devuelve 1 si ambas condiciones son verdaderas si no 0
echo "OR: $((a+b==13 || a<b))" # #Devuelve 1 si al menos una de las condiciones es verdadera si no 0
echo "NOT: $((!(a==b)))" #Devuelve 0 si es verdadero y 1 si es falso
echo -e "\n################################################################\n"
# Operadores de Asignación

echo "Operadores de Asignación:"

variable=15
echo "asignación: $variable"
echo "Suma y Asignación: $((variable+=5))"
echo "Resta y Asignación: $((variable-=3))"
echo "Multiplicación y Asignación: $((variable*=2))"
echo "División y Asignación: $((variable/=2))"
echo "Módulo y Asignación: $((variable%=4))"
echo -e "\n################################################################\n"

# Operadores de bits
echo "Operadores de bits:"
echo "AND: $((a & b))" # AND bit a bit
echo "OR: $((a | b))" # OR bit a bit
echo "XOR: $((a ^ b))" # XOR bit a bit

echo -e "\n################################################################\n"

# Estructuras de Control
echo "Estructuras de Control:"

## Condicionales Enteros
echo "Condicionales Enteros:"

valor_1=5*4
valor_2=4*8

echo -e "\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"

echo "primer valor: $((valor_1))"
echo "segundo valor: $((valor_2))"

if [[ $((valor_1)) > $((valor_2)) ]]; then
    echo "$((valor_1)) es mayor que $((valor_2))"
else
    echo "$((valor_1)) no es mayor que $((valor_2))"
fi  # Para cerrar los condiciones se usa fi

if [[ $((valor_1)) -le $((valor_2)) ]]; then        #el <= || >= son excepciones a la regla de usar [[]] para comparar
    echo "$((valor_1)) es menor o igual que $((valor_2))"
else
    echo "$((valor_1)) no es menor o igual que $((valor_2))"
fi

## Condicionales de cadenas

cadena_1="Hola"
cadena_2="Mundo"
echo -e "\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"

echo "primer texto: $cadena_1"
echo "segundo texto: $cadena_2"

if [[ "$cadena_1" == "$cadena_2" ]]; then    #se usa [[]] cuando se usan signos/operadores de comparación
    echo "Las cadenas son iguales"
else
    echo "Las cadenas son diferentes"
fi

if [[ "$cadena_1" > "$cadena_2" ]]; then
    echo "$cadena_1 es alfabéticamente mayor que $cadena_2"

elif [[ "$cadena_1" < "$cadena_2" ]]; then
    echo "$cadena_1 es alfabéticamente menor que $cadena_2"

else
    echo "$cadena_1 no es ni mayor ni menor alfabéticamente que $cadena_2"
fi

echo -e "\n################################################################\n"

# Iterativas, bucles

echo "Estructuras Iterativas:"
## Bucle for

for ((i=0; i<10; i++)); do
    echo "esta es la iteracion número: $i"
done

for i in {1..4}; do
    echo "esta es la iteracion número: $i"
done

for ((i=10; i<31; i+=5)); do # no cuenta el ultimo numero
    echo "el valor de i es: $i y ademas se va sumando 5 por iteracion"
done

echo -e "\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
# Bucle while

contador=0

while [[ contador < 10 ]]; do
    echo "contador: $contador"
    contador+=1
done

echo -e "\n#######################################################################\n"

# Ejercio EXTRA
echo "Ejercicio Extra:"

for ((numero=10; numero<=55; numero++)); do
    if [[ $numero == 10 || $numero == 16 || $((numero % 3)) == 0 || $((numero % 2)) != 0 ]]; then
        continue

    else
        echo "El número $numero es par y no es ni el 16 ni múltiplo de 3"
    fi
done
