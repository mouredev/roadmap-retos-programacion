#!/bin/bash
# Esta línea indica que el script debe ser interpretado por Bash

# Función sin parámetros ni retorno
function sin_parametros_ni_retorno {
  # Imprime un mensaje indicando que esta función no tiene parámetros ni retorno
  echo "Función sin parámetros ni retorno"
}

# Función con un parámetro
function con_un_parametro {
  # $1 es el primer parámetro pasado a la función
  echo "Función con un parámetro: $1"
}

# Función con varios parámetros
function con_varios_parametros {
  # $1, $2, y $3 son los primeros tres parámetros pasados a la función
  echo "Función con varios parámetros: $1, $2, $3"
}

# Llamada a la función sin parámetros ni retorno
sin_parametros_ni_retorno

# Llamada a la función con un parámetro
con_un_parametro "Hola"

# Llamada a la función con varios parámetros
con_varios_parametros "Uno" "Dos" "Tres"

# Definición de la función 'fa' anidada
function fa {
	# Imprime un mensaje indicando que se está llamando a la función 'fa'
	echo "Llamando a la función anidada, fa"
	
	# Definición de la función interna 'fu' dentro de 'fa'
	function fu {
		# Imprime un mensaje indicando que se está llamando a la función 'fu'
		echo "Llamando a la función interna, fu"
	}
	
	# Llama a la función interna 'fu' dentro de la función 'fa'
	fu
}

# Llama a la función 'fa'
fa

# Calcula el factorial de 'n' usando un bucle while
function factorial {
  local n=$1
  local result=1
  while [ $n -gt 1 ]; do
    result=$((result * n))
    ((n--))
  done
  # Devuelve el resultado del factorial
  echo $result
}
factorial 5 # Llama a la función 'factorial' con el argumento 5

# Función que recibe dos parámetros de tipo cadena de texto y retorna un número
function imprimir_numeros {
  local cadena1=$1
  local cadena2=$2
  local contador=0

  for ((i=1; i<=100; i++)); do
    if ((i % 3 == 0 && i % 5 == 0)); then
      echo "${cadena1}${cadena2}"
    elif ((i % 3 == 0)); then
      echo "$cadena1"
    elif ((i % 5 == 0)); then
      echo "$cadena2"
    else
      echo "$i"
      ((contador++))
    fi
  done

  # Retorna el número de veces que se ha impreso el número en lugar de los textos
  return $contador
}

# Llamada a la función 'imprimir_numeros' con los parámetros "Fizz" y "Buzz"
imprimir_numeros "Fizz" "Buzz"
# Captura el valor de retorno de la función
contador=$?
echo "El número de veces que se ha impreso el número en lugar de los textos es: $contador"

