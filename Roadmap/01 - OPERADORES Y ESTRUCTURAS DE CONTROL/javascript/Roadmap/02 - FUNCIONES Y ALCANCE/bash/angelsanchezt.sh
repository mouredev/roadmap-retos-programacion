#!/bin/bash


# Ejemplo 1: Función sin parámetros ni retorno
function funcionSinParametrosNiRetorno() {
  echo "Esta es una función sin parámetros ni retorno."
}

funcionSinParametrosNiRetorno

# Ejemplo 2: Función con parámetros
function funcionConParametros() {
  echo "Esta función tiene $# parámetros: $@"
}

funcionConParametros "ANGEL" "JAVIER" "SANCHEZ"

# Ejemplo 3: Función con retorno
function funcionConRetorno() {
  resultado=$((2 + 2))
}

funcionConRetorno
echo $resultado

# Ejemplo 4: Función con variables locales y globales
variableGlobal="Soy global"

function funcionConVariables() {
  local variableLocal="Soy local"
  echo "Desde la función: $variableGlobal, $variableLocal"
}

# Ejemplo 5: Llamadas a funciones y variables
echo "Ejemplo 1:"
funcionSinParametrosNiRetorno

echo -e "\nEjemplo 2:"
funcionConParametros "Hola" "Mundo" "!"

echo -e "\nEjemplo 3:"
funcionConRetorno
echo "El resultado de la función con retorno es: $?"

echo -e "\nEjemplo 4:"
funcionConVariables
echo "Desde fuera de la función: $variableGlobal"

# Dificultad Extra: Función con múltiples condiciones y retorno de conteo
function funcionExtra() {
  parametro1=$1
  parametro2=$2
  
  for i in $(seq 1 100); do
    if [ $(($i % 3)) -eq 0 ] && [ $(($i % 5)) -eq 0 ]; then
        echo $i "Es" $parametro1 "y es "$parametro2
    elif [ $(($i % 3)) -eq 0 ]; then
        echo $i "Es" $parametro1 
    elif [ $(($i % 5)) -eq 0 ]; then
        echo $i "Es" $parametro2
    else
        let "contador +=1"
        echo $i
    fi
  done

  echo "Hay "$contador "números que no son" $parametro1 "ni" $parametro2

  return $contador
}

# Ejemplo 6: Llamada a función con múltiples condiciones y retorno de conteo
echo -e "\nDificultad Extra:"
funcionExtra "Multiplo 3" "Multiplo 5"
echo "Número de veces que se imprimió: $?"
