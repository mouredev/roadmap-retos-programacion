#!/bin/bash

: "
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 * - Análisis de longitud
 * - Comparación de caracteres
 */
"

string1="hola"
string2="mundo"

# Acceso a caracteres específicos
echo "Primer carácter de string1: ${string1:0:1}"  # Primer carácter
echo "Último carácter de string2: ${string2: -1}"  # Último carácter

# longitud
echo "Longitud de string1: ${#string1}"  # Longitud de string1
echo "Longitud de string2: ${#string2}"  # Longitud de string2

# Concatenacion
echo "Concatenación: $string1 - $string2"  # Concatenación de dos cadenas

# Repeticion
repeated_string=""
for i in {1..3}; do
	repeated_string+="$string1"
done
echo "Repetición de string1: $repeated_string"

# recorrido
for (( i=0; i<${#string1}; i++ )); do
	echo "Carácter en posición $i de string1: ${string1:i:1}"
done

# conversión a mayúsculas
echo "String1 en mayúsculas: ${string1^^}"

# conversión a minúsculas
echo "String1 en minúsculas: ${string1,,}"

# Reemplazo
echo "Reemplazo de 'ho' por 'o' en string1: ${string1/ho/O}"  # Reemplaza la primera ocurrencia

# División
IFS=',' read -r -a words <<< "$string1, $string2, esto, esta, separando, por, comas"  # Divide en palabras
echo "División de string1 y string2 en palabras: ${words[@]}"  # siempre reemplazo los lugares con espacios

# Unión
union_string="$string1$string2"
echo "Unión de string1 y string2: $union_string"

# Interpolación
echo "Interpolación: $string1 y $string2 son cadenas de caracteres."

# Verificación
if [[ $string1 == *"hola"* ]]; then
  	echo "string1 contiene 'hola'"
else
  	echo "string1 no contiene 'hola'"
fi

function es_poligroma(){
    local palabra_input=$1
    local palabra_invertida=$(echo "$palabra_input" | rev)

    if [[ "$palabra_input" == "$palabra_invertida" ]]; then
        echo "La palabra ${palabra_input} es poligroma"
    else
        echo "La palabra ${palabra_input} no es poligroma"
    fi
}

function es_anagrama(){
	local palabra1=$1
	local palabra2=$2

	if [[ ${#palabra1} -ne ${#palabra2} ]]; then
		echo "Las palabras no son anagramas, ya que tienen diferente longitud"
		return 0
	fi


	for (( i=0; i<${#palabra1}; i++ )); do
		caracter=${palabra1:i:1}
		if [[ ! $palabra2 =~ $caracter ]]; then
			echo "Las palabras no son anagramas"
			return 0
		fi
	done

	echo "Las palabras son anagramas"

}

function es_isograma(){

	local palabra_input=$1
	local palabra_nueva=""

	for (( i=0; i<${#palabra_input}; i++ )); do
		if [[ $palabra_nueva == *"${palabra_input:i:1}"* ]]; then
			echo "La palabra ${palabra_input} no es isograma"
			return 0
		fi
		palabra_nueva+="${palabra_input:i:1}"
	done

	echo "La palabra ${palabra_input} es isograma"
}

function analisis_final() {
	local palabra1=$1
	local palabra2=$2

	echo -e "\nAnálisis de longitud:"
	echo "Longitud de '$palabra1': ${#palabra1}"
	echo "Longitud de '$palabra2': ${#palabra2}"

	echo "Comparación de caracteres:"
	if [[ "$palabra1" == "$palabra2" ]]; then
		echo "Las palabras son iguales."
	else
		echo "Las palabras son diferentes."
	fi

	echo "Verificando si son palíndromos:"
	es_poligroma "$palabra1"
	es_poligroma "$palabra2"

	echo "Verificando si son anagramas:"
	es_anagrama "$palabra1" "$palabra2"

	echo "Verificando si son isogramas:"
	es_isograma "$palabra1"
	es_isograma "$palabra2"
}

# Llamada a la función principal
analisis_final "uva" "oso"



