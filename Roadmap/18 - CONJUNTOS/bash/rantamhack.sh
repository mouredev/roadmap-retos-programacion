#!/bin/bash

# EJERCICIO:
# Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
# operaciones (debes utilizar una estructura que las soporte):
# - Inserta un elemento al final.
# - Inserta un elemento al principio.
# - Inserta varios elementos en bloque al final.
# - Inserta varios elementos en bloque en una posicion concreta.
# - Elimina un elemento en una posicion concreta.
# - Actualiza el valor de un elemento en una posicion concreta.
# - Comprueba si un elemento esta en un conjunto.
# - Elimina todo el contenido del conjunto.

group=(Miguel Ana Juan Rantamplan Helena Brais)

echo "Los elementos que conforman ahora mismo el conjunto group son: ${group[*]}"

echo -e "\n=====================\n"

group=("${group[@]}" Raul)
echo "Inserto un elemento al final del conjunto: ${group[*]}"

echo -e "\n=====================\n"

group=(Luis "${group[@]}")
echo "Inserto un elemento al principio del conjunto: ${group[*]}"

echo -e "\n=====================\n"

group=("${group[@]}" Jaime Isabel Rosa) 
echo "Inserto varios elementos en bloque al final del conjunto: ${group[*]}"

echo -e "\n=====================\n"

group=("${group[@]:0:2}" Fernando Cristina Jon "${group[@]:3}")  
echo "Inserto en bloque 3 elementos en la posicion 2 del conjunto: ${group[*]}"

echo -e "\n=====================\n"

unset 'group[4]'
echo "Elimino el elemento elegido (4 - Jon) del conjunto: ${group[*]}"

echo -e "\n=====================\n"

group[6]="Rantamhack"
echo "Actualizo el elemento elegido (6 - Rantamplan) del conjunto: ${group[*]}"
# El elemento a actualizar es el '6º' porque borrando el 4º con 'unset' lo elimina pero el hueco sigue existiendo

echo -e "\n=====================\n"

if [[ "${group[*]}" =~ "Jon" ]]; then
    echo "El elemento pertenece a 'group'"
else
    echo "El elemento no pertenece 'group'"
fi

echo -e "\n=====================\n"

unset group
echo  "${group[*]}"



# DIFICULTAD EXTRA (opcional):
# Muestra ejemplos de las siguientes operaciones con conjuntos:
# - Union.
# - Interseccion.
# - Diferencia.
# - Diferencia simetrica.


echo -e "\n\n=======================================DIFICULTAD EXTRA=======================================\n\n"

alumnos_ciencias=('Luis' 'Miguel' 'Fernando' 'Cristina' 'Ana' 'Juan')

alumnos_letras=('Helena' 'Brais' 'Ana' 'Juan' 'Raul' 'Jaime' 'Luis' 'Isabel' 'Miguel' 'Rosa')

total_alumnos=($(echo "${alumnos_ciencias[@]}" "${alumnos_letras[@]}" | tr ' ' '\n' | sort -u)) 

echo -e "El total de alumnos matriculados es: ${total_alumnos[*]}"

echo -e "\n=====================\n"

alumnos_mixtos=$(printf "%s\n" "${alumnos_ciencias[@]}" | grep -F -e "$(printf "%s\n" "${alumnos_letras[@]}")")  
echo -e "El total de alumnos matriculados en las dos ramas: ${alumnos_mixtos[*]}"

echo -e "\n=====================\n"

alumnos_solo_ciencias=($(comm -23 <(printf "%s\n" "${alumnos_ciencias[@]}" | sort) <(printf "%s\n" "${alumnos_letras[@]}" | sort)))

echo -e "Alumnos matriculados solo en ciencias: ${alumnos_solo_ciencias[*]}"

alumnos_solo_letras=($(comm -13 <(printf "%s\n" "${alumnos_ciencias[@]}" | sort) <(printf "%s\n" "${alumnos_letras[@]}" | sort)))

echo -e "\nAlumnos matriculados solo en letras: ${alumnos_solo_letras[*]}"

echo -e "\n=====================\n"

alumnos_una_matricula=($(comm -3 <(printf "%s\n" "${alumnos_ciencias[@]}" | sort) <(printf "%s\n" "${alumnos_letras[@]}" | sort)))

echo -e "Alumnos matriculados solo en una rama sin importar cual: ${alumnos_una_matricula[*]}"
