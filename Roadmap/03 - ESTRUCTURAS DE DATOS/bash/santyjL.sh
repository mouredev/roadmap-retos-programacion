#!/bin/bash

# 03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

: "
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"

# Arrays
function print_array() {
    # Declarar un array
    declare -a array_strings=("hola" "bash" "python" "javascript" "c++")
    echo -e "\nArray inicial: ${array_strings[@]}"

    # Añadir elementos al array
    array_strings+=("java" "c#")
    echo -e "\nArray tras añadir elementos: ${array_strings[@]}"

    # Añadir un elemento al principio del array
    array_strings=("Go" "${array_strings[@]}")
    echo -e "\nArray tras añadir un elemento al principio: ${array_strings[@]}"

    # Insertar un elemento en una posición específica
    array_strings=(${array_strings[@]:0:4} "Rust" ${array_strings[@]:5})
    echo -e "\nArray tras insertar 'Rust': ${array_strings[@]}"

    # Mostrar un elemento específico del array
    echo -e "\nPrimer elemento-segundo valor: ${array_strings[1]}"

    # Mostrar el número de elementos en el array
    echo -e "\nNúmero de elementos en el array: ${#array_strings[@]}"

    # Actualizar un elemento del array
    array_strings[2]="bash2"
    echo -e "\nArray tras actualizar un elemento: ${array_strings[@]}"

    # Eliminar un valor del array
    unset array_strings[2]
    echo -e "\nArray tras eliminar un elemento: ${array_strings[@]}"

    # Reindexar el array tras eliminar un elemento
    array_strings=("${array_strings[@]}")
    echo -e "\nArray tras reindexar: ${array_strings[@]}"
}

# Diccionarios
function print_dictionary() {
    # Declarar un diccionario
    declare -A evaluation
    evaluation[Luis]='5'
    evaluation[Maria]='7.5'
    evaluation[Helena]='9'
    evaluation[Pedro]='3.8'
    evaluation[Ignacio]='2'

    # Mostrar todos los valores del diccionario
    echo -e "\nDiccionario: ${evaluation[@]}"

    # Mostrar todas las claves del diccionario
    echo -e "\nClaves del diccionario: ${!evaluation[@]}"

    # Mostrar un valor específico
    echo -e "\nNota de Maria: ${evaluation[Maria]}"

    # Actualizar un valor
    evaluation[Pedro]='6.5'
    echo -e "\nDiccionario tras actualizar la nota de Pedro: ${evaluation[@]}"

    # Eliminar un elemento del diccionario
    unset evaluation[Ignacio]
    echo -e "\nDiccionario tras eliminar a Ignacio: ${evaluation[@]}"
}

# Llamar a las funciones
print_array
print_dictionary

echo -e "\n======================Extra======================\n"

# Agenda de contactos (pendiente de implementación)

declare -A contacto

function inserción() {
    nombre=$1
    numero=$2

    contacto["$nombre"]="$numero"
    echo "se ha agregado a ${nombre}  a la lista de contactos"
}

function busqueda() {
    nombre=$1

    for usuario in "${!contacto[@]}"; do
        if [ "$usuario" == "$nombre" ]; then
            echo "Contacto encontrado: $nombre - ${contacto[$nombre]}"
            return 1
        fi
    done

    echo "Contacto no encontrado: $nombre"
    return 0
}

function actualización() {
    nombre=$1
    nuevo_numero=$2

    busqueda $nombre
    if [ $? -eq 1 ]; then
        contacto["$nombre"]="$nuevo_numero"
        echo "Número de teléfono de $nombre actualizado a $nuevo_numero"
        return
    fi

    echo "el contacto que desea cambiar no existe"

}

function eliminación() {
    nombre=$1

    busqueda $nombre
    if [ $? -eq 1 ]; then
        unset contacto["$nombre"]
        echo "Contacto $nombre eliminado."
    else
        echo "Contacto no encontrado: $nombre"
    fi
}

while [[ 1 -eq 1 ]]; do
    echo " "
    echo "Opciones de la agenda: "
    echo "0) revisar contactos"
    echo "1) Añadir contacto a la agenda"
    echo "2) Borrar un contacto de la agenda"
    echo "3) Buscar un contacto en la agenda"
    echo "4) Actualizar la agenda"
    echo "5) Salir de la agenda"
    echo

    read -p "Elige la opción de lo que deseas hacer: " opcion

    if [ "$opcion" == "0" ]; then
        echo "Contactos en la agenda:"
        if [[ ${#contacto[@]} > 0 ]]; then
            for usuario in "${!contacto[@]}"; do
                echo "$usuario - ${contacto[$usuario]}"
            done
        fi

    elif [ "$opcion" == "1" ]; then
        read -p "Introduce el nombre del contacto: " nombre
        read -p "Introduce el número del contacto: " numero
        if [[ "$numero" =~ ^[0-9]{1,11}$ ]]; then
            inserción "$nombre" "$numero"
        else
            echo "El número debe ser numérico y tener como máximo 11 dígitos."
        fi

    elif [ "$opcion" == "2" ]; then
        read -p "Introduce el nombre del contacto a eliminar: " nombre
        eliminación "$nombre"

    elif [ "$opcion" == "3" ]; then
        read -p "Introduce el nombre del contacto a buscar: " nombre
        busqueda "$nombre"

    elif [ "$opcion" == "4" ]; then
        read -p "Introduce el nombre del contacto a actualizar: " nombre
        read -p "Introduce el nuevo número del contacto: " nuevo_numero
        if [[ "$nuevo_numero" =~ ^[0-9]{1,11}$ ]]; then
            actualización "$nombre" "$nuevo_numero"
        else
            echo "El número debe ser numérico y tener como máximo 11 dígitos."
        fi

    elif [ "$opcion" == "5" ]; then
        echo "Saliendo de la agenda..."
        break

    else
        echo "Opción no válida. Por favor, elige una opción entre 1 y 5."
    fi
done