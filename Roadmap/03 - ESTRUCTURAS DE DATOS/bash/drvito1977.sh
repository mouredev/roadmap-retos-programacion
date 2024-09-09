#!/bin/bash

# Ejemplos de estructuras en Bash

# Arrays
# Definición de un array con elementos iniciales
array=(1 2 3 4 5)
# Imprimir todos los elementos del array
echo "Array original: ${array[@]}"
# Añadir un nuevo elemento al final del array
array+=(6) # Inserción
# Imprimir el array después de la inserción
echo "Array después de inserción: ${array[@]}"
# Eliminar el tercer elemento del array (índice 2)
unset array[2] # Borrado
# Imprimir el array después del borrado
echo "Array después de borrado: ${array[@]}"
# Actualizar el segundo elemento del array (índice 1) a 10
array[1]=10 # Actualización
# Imprimir el array después de la actualización
echo "Array después de actualización: ${array[@]}"
# Ordenar el array y guardarlo en una nueva variable
sorted_array=($(for i in "${array[@]}"; do echo $i; done | sort)) # Ordenación
# Imprimir el array ordenado
echo "Array ordenado: ${sorted_array[@]}"

# Arrays asociativos
# Declarar un array asociativo
declare -A assoc_array
# Inicializar el array asociativo con pares clave-valor
assoc_array=([key1]=value1 [key2]=value2)
# Imprimir todos los valores del array asociativo
echo "Array asociativo original: ${assoc_array[@]}"
# Añadir un nuevo par clave-valor al array asociativo
assoc_array[key3]=value3 # Inserción
# Imprimir el array asociativo después de la inserción
echo "Array asociativo después de inserción: ${assoc_array[@]}"
# Eliminar un par clave-valor del array asociativo usando la clave
unset assoc_array[key1] # Borrado
# Imprimir el array asociativo después del borrado
echo "Array asociativo después de borrado: ${assoc_array[@]}"
# Actualizar el valor asociado a una clave existente
assoc_array[key2]=new_value # Actualización
# Imprimir el array asociativo después de la actualización
echo "Array asociativo después de actualización: ${assoc_array[@]}"

# Strings (cadenas de texto)
# Definir una cadena de texto
string="Hola Mundo"
# Imprimir la cadena original
echo "String original: $string"
# Añadir un carácter al final de la cadena
string+="!" # Inserción
# Imprimir la cadena después de la inserción
echo "String después de inserción: $string"
# Eliminar parte de la cadena (mantener solo los primeros 4 caracteres)
string=${string:0:4} # Borrado
# Imprimir la cadena después del borrado
echo "String después de borrado: $string"
# Actualizar la cadena completa
string="Hola Bash" # Actualización
# Imprimir la cadena después de la actualización
echo "String después de actualización: $string"

# Numbers (números)
# Definir un número
num=5
# Imprimir el número original
echo "Número original: $num"
# Incrementar el número en 5
((num+=5)) # Inserción (suma)
# Imprimir el número después de la inserción
echo "Número después de inserción: $num"
# Decrementar el número en 3
((num-=3)) # Borrado (resta)
# Imprimir el número después del borrado
echo "Número después de borrado: $num"
# Actualizar el número a 10
num=10 # Actualización
# Imprimir el número después de la actualización
echo "Número después de actualización: $num"

# Agenda de contactos
declare -A agenda

# Declarar un array asociativo para la agenda de contactos
declare -A agenda

# Función para insertar un contacto
function insertar_contacto {
    # Pedir al usuario que ingrese el nombre del contacto
    read -p "Nombre: " nombre
    # Pedir al usuario que ingrese el número de teléfono del contacto
    read -p "Número de teléfono: " telefono
    # Validar que el número de teléfono sea numérico y tenga hasta 11 dígitos
    if ! echo "$telefono" | grep -qE "^[0-9]{1,11}$"; then
        # Si el número no es válido, mostrar un mensaje y salir de la función
        echo "Número de teléfono inválido."
        return
    fi
    # Añadir el contacto a la agenda
    agenda[$nombre]=$telefono
    # Confirmar que el contacto ha sido añadido
    echo "Contacto añadido."
}

# Función para buscar un contacto
function buscar_contacto {
    # Pedir al usuario que ingrese el nombre del contacto a buscar
    read -p "Nombre: " nombre
    # Verificar si el contacto existe en la agenda
    if [[ -z ${agenda[$nombre]} ]]; then
        # Si no existe, mostrar un mensaje
        echo "Contacto no encontrado."
    else
        # Si existe, mostrar el número de teléfono del contacto
        echo "Teléfono de $nombre: ${agenda[$nombre]}"
    fi
}

# Función para actualizar un contacto
function actualizar_contacto {
    # Pedir al usuario que ingrese el nombre del contacto a actualizar
    read -p "Nombre: " nombre
    # Verificar si el contacto existe en la agenda
    if [[ -z ${agenda[$nombre]} ]]; then
        # Si no existe, mostrar un mensaje y salir de la función
        echo "Contacto no encontrado."
        return
    fi
    # Pedir al usuario que ingrese el nuevo número de teléfono
    read -p "Nuevo número de teléfono: " telefono
    # Validar que el nuevo número de teléfono sea numérico y tenga hasta 11 dígitos
    if ! echo "$telefono" | grep -qE "^[0-9]{1,11}$"; then
        # Si el número no es válido, mostrar un mensaje y salir de la función
        echo "Número de teléfono inválido."
        return
    fi
    # Actualizar el contacto en la agenda
    agenda[$nombre]=$telefono
    # Confirmar que el contacto ha sido actualizado
    echo "Contacto actualizado."
}

# Función para eliminar un contacto
function eliminar_contacto {
    # Pedir al usuario que ingrese el nombre del contacto a eliminar
    read -p "Nombre: " nombre
    # Verificar si el contacto existe en la agenda
    if [[ -z ${agenda[$nombre]} ]]; then
        # Si no existe, mostrar un mensaje y salir de la función
        echo "Contacto no encontrado."
        return
    fi
    # Eliminar el contacto de la agenda
    unset agenda[$nombre]
    # Confirmar que el contacto ha sido eliminado
    echo "Contacto eliminado."
}

# Función para mostrar el menú de opciones
function mostrar_menu {
    # Mostrar las opciones disponibles al usuario
    echo "1. Insertar contacto"
    echo "2. Buscar contacto"
    echo "3. Actualizar contacto"
    echo "4. Eliminar contacto"
    echo "5. Salir"
}

# Bucle principal para mostrar el menú y ejecutar las opciones seleccionadas
while true; do
    # Mostrar el menú de opciones
    mostrar_menu
    # Pedir al usuario que seleccione una opción
    read -p "Seleccione una opción: " opcion
    # Ejecutar la acción correspondiente a la opción seleccionada
    case $opcion in
        1) insertar_contacto ;;  # Llamar a la función para insertar un contacto
        2) buscar_contacto ;;    # Llamar a la función para buscar un contacto
        3) actualizar_contacto ;; # Llamar a la función para actualizar un contacto
        4) eliminar_contacto ;;  # Llamar a la función para eliminar un contacto
        5) break ;;              # Salir del bucle y terminar el programa
        *) echo "Opción inválida." ;; # Mostrar un mensaje si la opción no es válida
    esac
done