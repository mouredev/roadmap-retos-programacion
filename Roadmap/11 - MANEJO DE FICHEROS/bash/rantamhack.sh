#!/bin/bash

# * IMPORTANTE: Solo debes subir el fichero de codigo como parte del ejercicio.
# * 
# * EJERCICIO:
# * Desarrolla un programa capaz de crear un archivo que se llame como
# * tu usuario de GitHub y tenga la extension .txt.
# * Añade varias lineas en ese fichero:
# * - Tu nombre.
# * - Edad.
# * - Lenguaje de programacion favorito.
# * Imprime el contenido.
# * Borra el fichero.

function crear_archivo() {

    file="rantamhack.txt"
    f=("Me llamo Rantam" "Mi edad es de 25 años" "Mi lenguaje de programacion favorito es bash")
    printf "%s\n" "${f[@]}" > "$file"    
    echo -e "\nEl archivo rantamhack.txt ha sido creado\n"

}    
crear_archivo

function leer_archivo() {

    file="rantamhack.txt"
    cat $file
    
}
leer_archivo

function borrar_archivo() { 
    if [ -e "rantamhack.txt" ]; then
        rm rantamhack.txt
        echo -e "\nEl archivo 'rantamhack.txt' ha sido eliminado\n\n"
    else
        echo -e "\nEl archivo no existe\n"
    fi
}
        
borrar_archivo


# * DIFICULTAD EXTRA (opcional):
# * Desarrolla un programa de gestion de ventas que almacena sus datos en un 
# * archivo .txt.
# * - Cada producto se guarda en una linea del arhivo de la siguiente manera:
# *   [nombre_producto], [cantidad_vendida], [precio].
# * - Siguiendo ese formato, y mediante terminal, debe permitir aÃ±adir, consultar,
# *   actualizar, eliminar productos y salir.
# * - Tambien debe poseer opciones para calcular la venta total y por producto.
# * - La opcion salir borra el .txt.



store="sales.txt"

function add_product() {

    read -p "Nombre: " name 
    read -p "Cantidad vendida: " quantity
    read -p "Precio: " price

    echo  "$name, $quantity, $price" >> $store

}


function consult_product() {

    read -p "Nombre: " name

    while IFS= read -r line; do
        if [[ $(echo "$line" | cut -d ',' -f1) == "$name" ]]; then
            echo "$line"
            break            
        fi
    done < "$store"
}


function delete_product() {
    read -p "Nombre: " name
    while IFS= read -r line; do
        if [[ $(echo "$line" | cut -d',' -f1) != "$name" ]]; then
            sed -i "/^$name/d" $store
        fi
    done < $store 

}


function update_product() {

    delete_product
    add_product 

}


function read_file() {
    
    cat $store

}


function product_sales() {
    total=0
    read -p "Nombre: " name

    while IFS= read -r line; do
        if [[ $(echo "$line" | cut -d ',' -f1) == "$name" ]]; then
            quantity=$(echo "$line" | cut -d ',' -f2)
            price=$(echo "$line" | cut -d ',' -f3)
        fi
        
    done < $store

    total=$(echo "$quantity * $price" | bc) 
    echo -e "\nEl total de las ventas de $name es: $total\n"
}


function total_sales() {
    total=0
    while IFS= read -r line; do
        quantity=$(echo "$line" | cut -d ',' -f2)
        price=$(echo "$line" | cut -d ',' -f3)
        total=$(bc <<< "$total + $quantity * $price")
    done < $store

    echo -e "\nEl total de las ventas es: $total\n"

}

function exit() {

    echo -e "Borrando archivo sales.txt"
    rm "sales.txt"
    echo -e "[!] Saliendo del programa ... \n"

}


echo -e "\nBienvenido al menu de opciones\n"

    echo "1) AÃ±adir producto"
    echo "2) Consultar producto"
    echo "3) Eliminar producto"
    echo "4) Actualizar producto"
    echo "5) Consultar archivo de productos"
    echo "6) Calculadora de ventas por producto"
    echo "7) Calculadora de ventas totales"
    echo "8) Salir"

while true; do 

    read -p "Elige la opcion que quieres utilizar: " option

    case $option in

        [1]*) add_product; break;;
        [2]*) consult_product; break;;
        [3]*) delete_product; break;;
        [4]*) update_product; break;;
        [5]*) read_file; break;;
        [6]*) product_sales; break;;
        [7]*) total_sales; break;;
        [8]*) exit; break;;

    esac   

done
