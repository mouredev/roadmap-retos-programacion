
#!/bin/bash


echo -e "\n\n======================LISTAS - ARRAYS======================\n\n"


# ARRAYS- Se pueden declarar de varias formas. Asignado valores, mediante la palabra reservada "declare" con "-a"
# Pueden hacerse de de cualquier tipo de datos incluso mezclandolos
# Cuando un elemento tiene varios palabras para considerarlo como un solo elemento se pone entre comillas, dobles o simples

declare -a array_strings

array_strings=(Luis Mari­a Helena Pedro Ignacio 'Jose Maria' Zoe Candela)
echo ${array_strings[@]}
# Para acceder a un elemento de la lista
echo ${array_strings[2]}
# Para acceder al primer elemento se puede hacer de dos maneras
echo ${array_strings[0]}
echo ${array_strings}
# Para ver cuantos elementos tiene un array
echo ${#array_strings[@]}
# Para saber la longitud uno de los elemento
# En este caso es el tercer elemento (Helena) nos devolvera un[6]
echo ${#array_strings[2]}
# Los arrays pueden ser tanto de cadenas de texto, como de numeros como mixtos
array_numbers=(3 7 52 4.5 9 8 8 8 7 5)
echo ${array_numbers[@]}

array_mix=(3 7 'Jose Luis' Juan 92)
echo ${array_mix[@]}

# Insercion 
# Podemos añadir elementos al array por el principio
array_strings=(Isabel "${array_strings[@]}")
# Tambien por el final
array_strings=("${array_strings[@]}" Isabel)
# Incluso en la posicion que tu quieras
array_strings=("${array_strings[@]:0:2}" Isabel "${array_strings[@]:3}")

# Borrado
# Borrar un elemento
unset array_strings[1]
array_strings=(${array_strings[@]/Luis/})


echo -e "\n\n======================DICCIONARIOS======================\n\n"


# Diccionarios - Tambien llamados Arrays asociativos. Es un elemento definido por pares
# clave-valor. Para iniciarlos se usa la palabra clave "declare" con el parametro -A

declare -A evaluation
evaluation[Luis]='5'
evaluation[Maria]='7.5' 
evaluation[Helena]='9' 
evaluation[Pedro]='3.8'
evaluation[Ignacio]='2'

# Para imprimir todos los valores de un diccionario tenemos dos opciones
echo ${evaluation[@]}
echo ${evaluation[*]}

# Para imprimir todas las claves de un diccionario tambien tenemos dos opciones
echo ${!evaluation[@]}
echo ${!evaluation[*]}
# Para imprimir un elemento
echo ${evaluation[Luis]}
# Para imprimir varios elementos a la vez
echo ${evaluation[@]:1:2}
# Para ver cuantos elementos tiene un diccionario
echo ${#evaluation[@]}

# Insercion Se puede hacer en una linea o en varias como antes
evaluation+=([Lola]=7 [Manuel]=8)
echo ${!evaluation[@]}
echo ${evaluation[*]}

# Borrado  --para borrar todo el diccionario
unset evaluation
# Para borrar un elemento
unset evaluation['Luis']  
echo ${!evaluation[@]}


echo -e "\n\n======================DIFICULTAD EXTRA======================\n\n"

#!/bin/bash

declare -A agenda

agenda[Juan]='1111'
agenda[Luis]='2222'
agenda[Maria]='3333'
agenda[Helena]='4444'
agenda[Candela]='5555'
agenda[Miguel]='6666'
agenda[Jose]='7777'
agenda[Isabel]='8888'
agenda[Alberto]='99995'

echo ${agenda[@]}]    #Imprime los valores
echo ${#agenda[@]}    #Imprime el numero de componentes del diccionario
echo ${!agenda[@]}    #Imprime las keys

function insert_contact(){
    echo "Escribe el nombre del nuevo contacto: " && read -r name
    echo "Escribe el numero del contacto $name : " && read -r number

    if [ -v agenda[$name] ]; then
        echo -e "El contacto $name ya existe"
    else
        echo -e "El contacto $name no existe y se incorpora a la agenda"
        agenda[$name]="$number"
    fi
  echo ${!agenda[@]}
  echo ${agenda[@]}
}

function delete_contac(){
    echo "Escribe el nombre del contacto que quieres borrar: " && read -r name

    if [ -v agenda[$name] ]; then
        unset agenda[$name]
    else
        echo -e "El contacto $name no existe en la agenda"
    fi

    echo ${!agenda[@]}
    echo ${agenda[@]}
}

function find_contact(){
    echo "Escribe el nombre del contacto que quieres buscar: " && read -r name
    if [ -v agenda[$name] ]; then
        echo "El numero de $name es: " ${agenda[$name]}
    else
	echo "El contacto no estÃ¡ en la agenda"
    fi

    echo ${!agenda[@]}
    echo ${agenda[@]}
}

function update_contact(){
    echo "Escribe el nombre del contacto que deseas actualizar: " && read -r name
    echo "Escribe el nuevo numero del contacto $name: " && read -r new_number

    if [ -v agenda[$name] ]; then
        agenda[$name]="$new_number"
        echo  "El contacto $name se ha actualizado"
    else
        echo "El contacto $name no existe y no se puede actualizar
        si quieres añadirlo escoge la opcion adecuada"
    fi
    echo ${!agenda[@]}
    echo ${agenda[@]}
}


option=0

while [ $option -ne 5 ];do
    echo " "
    echo "Opciones de la agenda: "
    echo "1) Añadir contacto a la agenda"
    echo "2) Borrar un contacto de la agenda"
    echo "3) Buscar un contacto en la agenda"
    echo "4) Actualizar la agenda"
    echo "5) Salir de la agenda"
    echo 

    read -p "Elige la opcion de lo que deseas hacer: " option

    case $option in

        1) insert_contact;;
        2) delete_contac;;
        3) find_contact;;
        4) update_contact;;
        5) break
           echo "[+] Saliendo de la agenda ....";;
        *) echo "$option es una opcion no valida, por favor elige una valida";;
    esac 
done




