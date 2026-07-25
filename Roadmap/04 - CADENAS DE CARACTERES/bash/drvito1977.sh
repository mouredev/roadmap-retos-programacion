#!/bin/bash

# Función para mostrar ejemplos de operaciones con cadenas de caracteres
function ejemplos_cadenas {
  cadena="Hola Mundo"

  # Acceso a caracteres específicos
  primer_caracter=${cadena:0:1} # Obtiene el primer carácter de la cadena
  ultimo_caracter=${cadena: -1} # Obtiene el último carácter de la cadena
  echo "Primer carácter: $primer_caracter"
  echo "Último carácter: $ultimo_caracter"

  # Subcadenas
  subcadena=${cadena:0:4} # Obtiene una subcadena desde el inicio hasta el cuarto carácter
  echo "Subcadena: $subcadena"

  # Longitud de la cadena
  longitud=${#cadena} # Calcula la longitud de la cadena
  echo "Longitud de la cadena: $longitud"

  # Concatenación
  concatenada="${cadena}!" # Concatenación de la cadena con un signo de exclamación
  echo "Concatenación: $concatenada"

  # Repetición (simulación)
  repetida=$(printf "%.0sHa" {1..3}) # Repite "Ha" tres veces
  echo "Repetición: $repetida"

  # Recorrido de la cadena
  echo "Recorrido de la cadena:"
  for (( i=0; i<${#cadena}; i++ )); do
    echo "${cadena:$i:1}" # Imprime cada carácter de la cadena en una nueva línea
  done

  # Conversión a mayúsculas y minúsculas
  mayusculas=${cadena^^} # Convierte la cadena a mayúsculas
  minusculas=${cadena,,} # Convierte la cadena a minúsculas
  echo "Mayúsculas: $mayusculas"
  echo "Minúsculas: $minusculas"

  # Reemplazo
  reemplazo=${cadena/Mundo/Bash} # Reemplaza "Mundo" por "Bash" en la cadena
  echo "Reemplazo: $reemplazo"

  # División
  IFS=' ' read -r -a palabras <<< "$cadena" # Divide la cadena en palabras usando el espacio como delimitador
  echo "División en palabras: ${palabras[@]}"

  # Unión
  unidas=$(IFS=,; echo "${palabras[*]}") # Une las palabras con una coma como separador
  echo "Unión de palabras: $unidas"

  # Interpolación
  interpolacion="La cadena es: $cadena" # Interpolación de la cadena en otra cadena
  echo "Interpolación: $interpolacion"

  # Verificación
  if [[ $cadena == *"Mundo"* ]]; then
    echo "La cadena contiene 'Mundo'" # Verifica si la cadena contiene la palabra "Mundo"
  fi
}

# Función para comprobar si una palabra es un palíndromo
function es_palindromo {
  palabra=$1
  invertida=$(echo $palabra | rev) # Invierte la palabra
  if [[ $palabra == $invertida ]]; then
    echo "$palabra es un palíndromo" # Comprueba si la palabra es igual a su versión invertida
  else
    echo "$palabra no es un palíndromo"
  fi
}

# Función para comprobar si dos palabras son anagramas
function son_anagramas {
  palabra1=$(echo $1 | grep -o . | sort | tr -d "\n") # Ordena las letras de la primera palabra
  palabra2=$(echo $2 | grep -o . | sort | tr -d "\n") # Ordena las letras de la segunda palabra
  if [[ $palabra1 == $palabra2 ]]; then
    echo "$1 y $2 son anagramas" # Comprueba si las palabras ordenadas son iguales
  else
    echo "$1 y $2 no son anagramas"
  fi
}

# Función para comprobar si una palabra es un isograma
function es_isograma {
  palabra=$1
  letras=$(echo $palabra | grep -o . | sort | uniq -d) # Busca letras duplicadas
  if [[ -z $letras ]]; then
    echo "$palabra es un isograma" # Comprueba si no hay letras duplicadas
  else
    echo "$palabra no es un isograma"
  fi
}

# Llamada a la función de ejemplos de cadenas
ejemplos_cadenas

# Comprobaciones de palabras
palabra1="radar"
palabra2="dormir"
palabra3="amor"
palabra4="roma"
palabra5="isograma"

echo
es_palindromo $palabra1
es_palindromo $palabra2

echo
son_anagramas $palabra3 $palabra4

echo
es_isograma $palabra5